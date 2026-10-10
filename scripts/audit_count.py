#!/usr/bin/env python3
"""Count what a UI's source holds outside its tokens, for `design-settle`'s audit.

The audit's first subagent runs this once (`skills/design-settle/references/audit.md`) and
copies what it prints. Counted by hand, two audits of one app read the same rows two ways:
the files a token change touches came out as 793 and as 616. A script counts them one way.

It reads the files git tracks or does not ignore, line by line, and writes nothing but the
`places.md` it is told to write. A styling file - one that defines custom properties, or a
Tailwind config - is where values are defined, so nothing in it is counted.

Three rows more, because an audit handed the script still wrote a scan of its own for each:
the tokens nothing reads, the sizes and weights of the icons, and the lengths of the labels.

Usage: python3 audit_count.py <repo root> [--scope PATH ...] [--src PATH ...]
                              [--styles PATH ...] [--out DIR]
"""
import argparse
import json
import re
import statistics
import subprocess
import sys
from collections import Counter
from pathlib import Path

SOURCE = (".tsx", ".jsx", ".ts", ".js", ".mjs", ".vue", ".svelte", ".astro", ".html", ".blade.php")
CSS = (".css", ".scss", ".less")
# Build output, vendored code and this skill's own folders: never an app's source.
SKIP_DIRS = {"node_modules", "vendor", "dist", "build", "out", "coverage", "storage", "public",
             ".next", ".nuxt", ".svelte-kit", ".git", ".design-audit", "design-canvas"}
MAX_BYTES = 1_500_000
MINIFIED_LINE = 2_000

HEX = re.compile(r"(?<![\w&#/])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?![\w-])")
PALETTE = ("slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|"
           "blue|indigo|violet|purple|fuchsia|pink|rose")
KINDS = [
    ("hex", [HEX]),
    ("colour functions", [re.compile(r"\b(?:rgba?|hsla?)\(\s*\d[^)]*\)")]),
    ("font sizes", [re.compile(r"(?<![\w-])text-\[\d[^\]\s]*\]"),
                    re.compile(r"\bfont-size\s*:\s*\d[\w.%]*"),
                    re.compile(r"\bfontSize\s*:\s*['\"]?\d[\w.%]*")]),
    ("spacings", [re.compile(r"(?<![\w-])-?(?:p[xytrblse]?|m[xytrblse]?|gap(?:-[xy])?|space-[xy]|"
                             r"inset(?:-[xy])?|top|right|bottom|left)-\[\d[^\]\s]*\]"),
                  # `margin: 0` is a reset, not a value outside the scale.
                  re.compile(r"\b(?:padding|margin|gap)(?:-[a-z]+|[A-Z][A-Za-z]*)*\s*:\s*['\"]?"
                             r"-?(?:[1-9]|0?\.\d)[\w.%]*")]),
]
RAMP = ("numbered ramp classes", [re.compile(
    r"(?<![\w-])(?:bg|text|border(?:-[trblxyse])?|ring(?:-offset)?|fill|stroke|from|via|to|divide|"
    r"outline|decoration|placeholder|caret|accent|shadow)-(?:" + PALETTE + r")-(?:50|[1-9]00|950)(?![\w-])")])
IMPORT = re.compile(r"(?:\bfrom\s+|\brequire\(\s*|\bimport\s*\(?\s*|@import\s+)['\"]([^'\"./][^'\"]*)['\"]")
ICONS = re.compile(r"lucide|heroicons|react-icons|phosphor|tabler|feather|fontawesome|iconify|ionicons|"
                   r"bootstrap-icons|remixicon|material-icons|@mui/icons|react-icons|/icons?$|-icons?$")
TOKEN_DEF = re.compile(r"^\s*--[\w-]+\s*:", re.M)
FONT_FAMILY = re.compile(r"font-family\s*:\s*([^;{}]+)")
FONT_LINK = re.compile(r"<link[^>]+href=[\"']([^\"']*font[^\"']*)[\"']", re.I)

# Token health: what a styling file defines, block by block, and what reads it.
COMMENT = re.compile(r"/\*.*?\*/", re.S)
BLOCK = re.compile(r"([^{}]*)\{([^{}]*)\}")
VAR_READ = re.compile(r"var\(\s*--([\w-]+)")
WORD = re.compile(r"(?<![\w-])[a-z][a-z0-9]*(?:-[a-z0-9]+)+(?![\w-])")
# Tailwind 4 names a token by its namespace: `--color-brand` is read by a class ending in `-brand`.
NAMESPACE = re.compile(r"^(?:color|text|font|radius|spacing|shadow|ease|animate|breakpoint|container)-")
COLOUR = re.compile(r"(?:#[0-9a-f]{3,8}|(?:rgba?|hsla?|oklch|oklab|lab|lch|hwb|color)\(.+\)|"
                    r"[\d.]+(?:deg)?[ ,]+[\d.]+%[ ,]+[\d.]+%(?:\s*/\s*[\d.]+%?)?)$", re.I)
# Icons: the names a file imports from an icon package, then each element of that name.
ICON_IMPORT = re.compile(r"\bimport\s+(?:type\s+)?(\w+)?\s*,?\s*(?:\{([^}]*)\})?\s*from\s*['\"]([^'\"]+)['\"]")
ICON_SIZE = re.compile(r"(?<![\w-])(?:size|h)-(\d+(?:\.\d+)?|\[[^\]]+\])(?![\w-])|\bsize=\{?['\"]?([\d.]+)")
ICON_WEIGHT = re.compile(r"\b(?:strokeWidth|stroke-width|weight)=\{?['\"]?([\w.]+)")
# Labels: a string a page shows - a translation call's argument, text closed by a tag, a label attribute.
I18N = re.compile(r"(?<!\w)(?:\$?t|__|trans)\(\s*(['\"`])((?:(?!\1).)+)\1")
MARKUP_TEXT = re.compile(r">\s*([^<>{}\n]*[^\W\d_][^<>{}\n]*?)\s*</")
LABEL_ATTR = re.compile(r"\b(?:label|title|placeholder|aria-label|alt|tooltip|description|helperText|caption)"
                        r"=(['\"])((?:(?!\1).)+)\1")
# `sales.empty_title` is a translation key: its text is in a locale file, and its length is not the label's.
KEY = re.compile(r"(?:[\w-]+(?:[.:][\w-]+)+|[a-z0-9]+(?:_[a-z0-9]+)+)$")


def listed(root: Path) -> list[str]:
    """Every path git tracks or does not ignore; every file under the root where git has none."""
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-co", "--exclude-standard", "-z"],
                             capture_output=True, timeout=120)
        if out.returncode == 0 and out.stdout:
            return [p for p in out.stdout.decode("utf-8", "replace").split("\0") if p]
    except (OSError, subprocess.SubprocessError):
        pass
    return [p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()]


def under(path: str, roots: list[str]) -> bool:
    return any(path == r or path.startswith(r.rstrip("/") + "/") for r in roots)


def package(spec: str) -> str:
    parts = spec.split("/")
    return "/".join(parts[:2]) if spec.startswith("@") else parts[0]


def number(n: int) -> str:
    return f"{n:,}"


def some(items: list[str], cap: int = 12) -> str:
    return " · ".join(items[:cap]) + (f" · and {len(items) - cap} more" if len(items) > cap else "")


def tally(counter: Counter) -> str:
    return some([f"{key} ×{number(n)}" for key, n in counter.most_common()])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--scope", nargs="*", default=[], help="paths the run redraws, relative to the root")
    ap.add_argument("--src", nargs="*", default=[], help="count only under these paths")
    ap.add_argument("--styles", nargs="*", default=[], help="styling files, where this script guessed wrong")
    ap.add_argument("--out", help="folder to write places.md into")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    root = Path(args.root).resolve()
    norm = lambda paths: [Path(p).as_posix().strip("/") for p in paths]
    scope, src, styles_given = norm(args.scope), norm(args.src), norm(args.styles)

    deps, data = {}, {}
    manifest = root / "package.json"
    if manifest.is_file():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8", errors="replace"))
            deps = {**data.get("devDependencies", {}), **data.get("dependencies", {})}
        except ValueError:
            pass
    tailwind = "tailwindcss" in deps or any(root.glob("tailwind.config.*"))
    kinds = KINDS + ([RAMP] if tailwind else [])

    paths = [p for p in listed(root)
             if p.lower().endswith(SOURCE + CSS) and not p.lower().endswith((".min.js", ".min.css", ".d.ts"))
             and not SKIP_DIRS.intersection(p.split("/")[:-1]) and (not src or under(p, src))]
    by_ext, skipped, styling = Counter(), 0, []
    hits = {k: Counter() for k, _ in kinds}            # kind -> file -> occurrences
    places, imports, fonts, links = [], Counter(), Counter(), set()
    blocks, read, mapped, words = [], set(), set(), set()   # token blocks, and what reads a token
    sizes, scope_sizes, weights, icon_files, labels = Counter(), Counter(), Counter(), set(), {}
    for rel in sorted(paths):
        file = root / rel
        try:
            if file.stat().st_size > MAX_BYTES:
                skipped += 1
                continue
            text = file.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.split("\n")
        if any(len(line) > MINIFIED_LINE for line in lines[:5]):
            skipped += 1
            continue
        by_ext[rel[rel.rindex("."):]] += 1
        for name in {package(s) for s in IMPORT.findall(text)}:
            imports[name] += 1
        css = rel.lower().endswith(CSS)
        is_styling = (under(rel, styles_given) if styles_given
                      else Path(rel).name.startswith("tailwind.config.") or (css and len(TOKEN_DEF.findall(text)) >= 3))
        if css:
            fonts.update(" ".join(f.split()) for f in FONT_FAMILY.findall(text))
        links.update(FONT_LINK.findall(text))
        if is_styling:
            styling.append(rel)
            if not css:
                mapped.update(VAR_READ.findall(text))       # a config maps a token under a key of its own
            for selector, body in BLOCK.findall(COMMENT.sub("", text)) if css else ():
                found = {}
                for declaration in body.split(";"):
                    prop, _, value = declaration.partition(":")
                    if prop.strip().startswith("--"):
                        found[prop.strip()[2:]] = " ".join(value.split())
                        mapped.update(VAR_READ.findall(value))
                    else:
                        read.update(VAR_READ.findall(declaration))
                        if "@apply" in declaration:
                            words.update(WORD.findall(declaration))
                if found:
                    blocks.append((" ".join(selector.rsplit(";", 1)[-1].split()) or rel, found))
            continue
        read.update(VAR_READ.findall(text))
        if not css:
            if tailwind:
                words.update(WORD.findall(text))
            names = {name.split(" as ")[-1].replace("type ", "").strip()
                     for default, named, spec in ICON_IMPORT.findall(text)
                     if package(spec) in deps and ICONS.search(package(spec))
                     for name in [default, *named.split(",")]}
            for name in filter(None, names):
                # An attribute holding `>` cuts the element short: its size then reads `none set`.
                for element in re.finditer(r"<" + re.escape(name) + r"\b([^>]*)>", text):
                    size = ICON_SIZE.search(element.group(1))
                    step = "none set" if not size else size.group(1) or size.group(2) + "px"
                    sizes[step] += 1
                    if under(rel, scope):
                        scope_sizes[step] += 1
                    weights.update(ICON_WEIGHT.findall(element.group(1)))
                    icon_files.add(rel)
            if not scope or under(rel, scope):
                labels[rel] = [" ".join(s.split()) for s in [m[1] for m in I18N.findall(text)]
                               + MARKUP_TEXT.findall(text) + [m[1] for m in LABEL_ATTR.findall(text)]]
        for no, line in enumerate(lines, 1):
            for kind, patterns in kinds:
                found = [m.group(0) for p in patterns for m in p.finditer(line)
                         # In a stylesheet `#abc {` is a selector: a colour follows a colon.
                         if not (css and p is HEX and ":" not in line[:m.start()])]
                if found:
                    hits[kind][rel] += len(found)
                    places.append(f"{rel}:{no} · {' '.join(found)[:120]} · Stray raw values — {kind}")

    affected = {f for c in hits.values() for f in c}
    def row(pick) -> str:
        return " · ".join(f"{k} {number(sum(n for f, n in hits[k].items() if pick(f)))} in "
                          f"{number(sum(1 for f in hits[k] if pick(f)))} files" for k, _ in kinds)

    print(f"AUDIT COUNT — {root}")
    print("Files read          : " + number(sum(by_ext.values())) + " source files ("
          + " · ".join(f"{e} {number(n)}" for e, n in by_ext.most_common()) + f") · {skipped} skipped as minified or too large")
    print("Styling files       : " + (" · ".join(styling) or "none found") + " — values defined there are not counted")
    tokens = sorted({name for _, found in blocks for name in found if not name.startswith("tw-")})
    if tokens:
        # `bg-sidebar-primary` reads `primary` too: a miss here leans to read, never to a finding.
        tails = {"-".join(word.split("-")[i:]) for word in words for i in range(1, word.count("-") + 1)}
        unread = [t for t in tokens if t not in read and t not in tails and NAMESPACE.sub("", t) not in tails]
        never, through = [t for t in unread if t not in mapped], [t for t in unread if t in mapped]
        same = []
        for selector, found in blocks:
            values = Counter(value.lower() for value in found.values() if COLOUR.match(value))
            groups = [n for n in values.values() if n > 1]
            if groups:
                same.append(f"`{selector}` {len(groups)} groups holding {sum(groups)} of {sum(values.values())} colours")
        print(f"Token health        : {number(len(tokens))} tokens defined · never read {len(never)}"
              + (f" ({some(never)})" if never else "")
              + f" · read only where a config or another token maps it {len(through)}"
              + (f" ({some(through)}) — never read where source holds no class of the key that maps it" if through else "")
              + " · one colour under several names — " + (some(same, 4) or "none")
              + ("" if tailwind else " · a read is a var() only — no Tailwind in this repo"))
    else:
        print("Token health        : not counted — no styling file defines a custom property")
    print("Stray raw values    : whole app — " + row(lambda f: True))
    if scope:
        print("                      scope     — " + row(lambda f: under(f, scope)))
    if not tailwind:
        print("                      numbered ramp classes not counted — no Tailwind in this repo")
    print(f"Components affected : {number(len(affected))} files hold at least one of the values above"
          + (f" · scope {number(sum(1 for f in affected if under(f, scope)))}" if scope else ""))
    if args.out:
        out = Path(args.out)
        out.mkdir(parents=True, exist_ok=True)
        head = ("# places.md\n\nOne line per place: file and line · what is there · the audit row it falls under. "
                "Written by `audit_count.py` over the whole app.\n\n")
        (out / "places.md").write_text(head + "\n".join(places) + "\n", encoding="utf-8", newline="\n")
        print(f"places.md           : {number(len(places))} lines written to {(out / 'places.md').as_posix()}")
    if deps:
        used = sorted(((n, d) for d, n in imports.items() if d in deps), reverse=True)
        print("Imports             : " + " · ".join(f"{d} {n}" for n, d in used[:25])
              + (f" · and {len(used) - 25} more" if len(used) > 25 else "") + "  (package, files importing it)")
        icons = [f"{d} {n}" for n, d in used if ICONS.search(d)]
        print("Icon families       : " + (" · ".join(icons) or "none imported"))
        if sizes:
            print(f"Icon sizes          : {number(sum(sizes.values()))} icon elements in {number(len(icon_files))} files · "
                  f"{len(sizes) - ('none set' in sizes)} sizes — {tally(sizes)} · weights set — {tally(weights) or 'none'}"
                  "  (a bare number is a step of the class scale)")
            if scope:
                print("                      scope     — " + (tally(scope_sizes) or "no icon element"))
        elif icons:
            print("Icon sizes          : not counted — no element of an imported icon found")
        config = " ".join(p.read_text(encoding="utf-8", errors="replace") for p in root.iterdir()
                          if p.is_file() and ".config." in p.name)
        scripts = json.dumps(data.get("scripts", {}))
        never = sorted(d for d in deps if d not in imports and d not in config and d.split("/")[-1] not in scripts
                       and not d.startswith("@types/"))
        print("Never imported      : " + (" · ".join(never) or "none")
              + "  (in package.json; no source file, root config file or script names them)")
    if fonts:
        print("Font families named : " + " | ".join(f for f, _ in fonts.most_common(6)))
    if links:
        print("Fonts loaded by link: " + " ".join(sorted(links)))
    texts = {f: [s for s in found if not KEY.match(s)] for f, found in labels.items()}
    flat = [s for found in texts.values() for s in found]
    keys = sum(map(len, labels.values())) - len(flat)
    left_out = f" · {number(keys)} translation keys left out — their text is in the locale files" if keys else ""
    if flat:
        longest = max(flat, key=lambda s: len(s.split()))
        repeats = sorted(((sum(1 for n in c.values() if n > 1), sum(n for n in c.values() if n > 1), f)
                          for f, c in ((f, Counter(found)) for f, found in texts.items())), reverse=True)
        print(f"Repeated labels     : {number(len(flat))} strings in {number(sum(1 for v in texts.values() if v))} files"
              f"{' of the scope' if scope else ''} · longest {len(longest.split())} words (\"{longest[:80]}\")"
              f" · median {statistics.median(len(s.split()) for s in flat):g} · repeating within a file — "
              + (some([f"{'/'.join(f.split('/')[-2:])} {n} labels in {shown} places"
                       for n, shown, f in repeats if n], 8) or "none") + left_out
              + "  (a translation call's argument, text closed by a tag, a label attribute)")
    elif labels:
        print(f"Repeated labels     : not counted — no label found as a string in {number(len(labels))} files" + left_out)
    if not paths:
        print("NOT COVERED — no web source file found; count this stack by your own commands")
    return 0


if __name__ == "__main__":
    sys.exit(main())
