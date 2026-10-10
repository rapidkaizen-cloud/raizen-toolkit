function (mode) {
  // audit_measure.js - what the open page renders, for design-settle's audit walk
  // (skills/design-settle/references/audit-walk.md). Not a script to load: one function,
  // pasted as `const M = <this file>` inside an evaluate call, kept in window.name, and
  // called once per route and theme mode, so two walks measure the same things.
  // mode: none = contrast pairs and components · 'pairs' = pairs only · 'focus' = the
  // focus ring of the first field and button · 'selftest' = the colour arithmetic.
  const cache = new Map();
  let ctx = null;
  const parse = c => {
    if (!c) return null;
    if (cache.has(c)) return cache.get(c);
    let out = null;
    const m = c.match(/^rgba?\(([^)]+)\)$/);
    if (m) { const p = m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); out = { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; }
    else if (typeof document !== 'undefined') {
      // oklch(), lab(), color(): the browser paints it, the pixel says what it is in sRGB.
      ctx = ctx || document.createElement('canvas').getContext('2d', { willReadFrequently: true });
      ctx.clearRect(0, 0, 1, 1); ctx.fillStyle = '#000'; ctx.fillStyle = c; ctx.fillRect(0, 0, 1, 1);
      const d = ctx.getImageData(0, 0, 1, 1).data; out = { r: d[0], g: d[1], b: d[2], a: d[3] / 255 };
    }
    cache.set(c, out); return out;
  };
  const over = (f, b) => ({ r: f.r * f.a + b.r * (1 - f.a), g: f.g * f.a + b.g * (1 - f.a), b: f.b * f.a + b.b * (1 - f.a), a: 1 });
  const lum = c => { const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c.r) + 0.7152 * f(c.g) + 0.0722 * f(c.b); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return Math.round((Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05) * 100) / 100; };
  const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  // WCAG large text: 24px, or 18.66px bold.
  const floorOf = (px, weight) => (px >= 24 || (px >= 18.66 && weight >= 700)) ? 3 : 4.5;
  if (mode === 'selftest') {
    const k = { r: 0, g: 0, b: 0, a: 1 }, w = { r: 255, g: 255, b: 255, a: 1 };
    const ok = ratio(k, w) === 21 && ratio(parse('rgb(119, 119, 119)'), w) === 4.48 && hex(over({ ...k, a: 0.5 }, w)) === '#808080'
      && floorOf(24, 400) === 3 && floorOf(18.66, 700) === 3 && floorOf(18, 700) === 4.5 && parse('rgba(1, 2, 3, 0.5)').a === 0.5;
    if (!ok) throw new Error('audit_measure: colour arithmetic is off');
    return 'ok';
  }
  const cs = e => getComputedStyle(e);
  const SKIP = '.phpdebugbar, [class*=phpdebugbar], nextjs-portal, vite-error-overlay, .tsqd-parent-container, [aria-hidden=true], script, style, noscript, template';
  const vis = e => { const r = e.getBoundingClientRect(), s = cs(e); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' && !e.closest(SKIP); };
  const q = sel => [...document.querySelectorAll(sel)].filter(vis);
  const px = v => Math.round(parseFloat(v) * 10) / 10;
  if (mode === 'focus') {
    const ring = e => { if (!e) return 'none on this page'; e.focus({ preventScroll: true }); const s = cs(e); const out = `outline ${s.outlineStyle === 'none' ? 'none' : s.outlineWidth + ' ' + s.outlineColor + ' offset ' + s.outlineOffset} · shadow ${s.boxShadow}`; e.blur(); return out; };
    return { field: ring(q('input:not([type=hidden]):not([disabled]), textarea:not([disabled])')[0]), button: ring(q('button:not([disabled])')[0]) };
  }
  // The colour behind an element; null where a gradient or an image sits under it.
  const bgOf = e => { const layers = []; for (let n = e; n && n.nodeType === 1; n = n.parentElement) { const s = cs(n); if (s.backgroundImage !== 'none') return null; const c = parse(s.backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } } let base = { r: 255, g: 255, b: 255, a: 1 }; for (let i = layers.length - 1; i >= 0; i--) base = over(layers[i], base); return base; };
  const opacity = e => { let o = 1; for (let n = e; n && n.nodeType === 1; n = n.parentElement) o *= parseFloat(cs(n).opacity); return o; };
  const pairs = { text: {}, nontext: {} }; let unreadable = 0;
  const add = (kind, label, colour, behind, floor, sample, disabled) => {
    const c = parse(colour); if (!c || c.a === 0) return;
    const bg = bgOf(behind); if (!bg) { unreadable++; return; }
    const fg = over({ ...c, a: c.a * opacity(behind) }, bg), key = `${label}${hex(fg)} on ${hex(bg)} floor ${floor}`;
    (pairs[kind][key] = pairs[kind][key] || { n: 0, r: ratio(fg, bg), floor, sample, disabled }).n++;
  };
  q('body *').forEach(e => {
    const s = cs(e), tag = e.tagName;
    const own = [...e.childNodes].filter(n => n.nodeType === 3 && n.textContent.trim()).map(n => n.textContent.trim()).join(' ');
    const off = !!e.closest('[disabled], [aria-disabled=true]');
    if (own) add('text', '', s.color, e, floorOf(parseFloat(s.fontSize), +s.fontWeight), own.slice(0, 20), off);
    if ((tag === 'INPUT' || tag === 'TEXTAREA') && e.placeholder) add('text', 'placeholder ', getComputedStyle(e, '::placeholder').color, e, 4.5, e.placeholder.slice(0, 20), off);
    if (tag.toLowerCase() === 'svg' && e.parentElement) add('nontext', 'icon ', s.color, e.parentElement, 3, '', off);
    if (['INPUT', 'TEXTAREA', 'SELECT', 'BUTTON'].includes(tag) && parseFloat(s.borderTopWidth) > 0 && e.parentElement) add('nontext', `border ${tag.toLowerCase()} `, s.borderTopColor, e.parentElement, 3, '', off);
  });
  const lines = (m, cap) => { const all = Object.entries(m).map(([k, v]) => ({ k, ...v, under: v.r < v.floor && !v.disabled })).sort((a, b) => b.under - a.under || b.n - a.n); return { shown: all.slice(0, cap).map(v => `${v.under ? 'UNDER ' : ''}${v.k} = ${v.r} x${v.n}${v.disabled ? ' (disabled)' : ''}${v.sample ? ' · ' + v.sample : ''}`), more: Math.max(0, all.length - cap), under: all.filter(v => v.under).length, distinct: all.length }; };
  const out = { url: location.pathname, theme: document.documentElement.className.trim() || 'no class on <html>', text: lines(pairs.text, 45), nontext: lines(pairs.nontext, 20), onGradientOrImage: unreadable };
  if (mode === 'pairs') return out;
  const group = (els, fn, cap) => { const m = {}; els.forEach(e => { const k = fn(e, cs(e), e.getBoundingClientRect()); m[k] = (m[k] || 0) + 1; }); return Object.entries(m).sort((a, b) => b[1] - a[1]).slice(0, cap).map(([k, n]) => `${k} x${n}`); };
  const pad = s => `${px(s.paddingTop)}/${px(s.paddingRight)}/${px(s.paddingBottom)}/${px(s.paddingLeft)}`;
  out.components = {
    buttons: group(q('button, [role=button], a[class*=btn], a[class*=button]'), (e, s, b) => `h${px(b.height)} pad ${pad(s)} r${s.borderTopLeftRadius} fs${s.fontSize}/${s.fontWeight} bd${s.borderTopWidth}`, 6),
    inputs: group(q('input:not([type=checkbox]):not([type=radio]):not([type=hidden]), textarea, select, [role=combobox]'), (e, s, b) => `${e.tagName.toLowerCase()} h${px(b.height)} pad ${pad(s)} r${s.borderTopLeftRadius} fs${s.fontSize} bd${s.borderTopWidth}`, 5),
    cards: group(q('main *, [class*=card], [data-slot=card]').filter(e => { const s = cs(e), b = e.getBoundingClientRect(); return parseFloat(s.borderTopLeftRadius) >= 4 && (parseFloat(s.borderTopWidth) > 0 || s.boxShadow !== 'none') && parse(s.backgroundColor)?.a > 0 && b.width > 200 && b.height > 60; }), (e, s) => `pad ${pad(s)} r${s.borderTopLeftRadius} bd${s.borderTopWidth} shadow ${s.boxShadow === 'none' ? 'none' : 'yes'}`, 4),
    tableHead: group(q('th'), (e, s, b) => `h${px(b.height)} pad ${pad(s)} fs${s.fontSize}/${s.fontWeight} ${s.textTransform}`, 3),
    tableRow: group(q('tbody td'), (e, s, b) => `h${px(b.height)} pad ${pad(s)} fs${s.fontSize}`, 3),
    badges: group(q('[class*=badge], [data-slot=badge]'), (e, s, b) => `h${px(b.height)} pad ${pad(s)} r${s.borderTopLeftRadius} fs${s.fontSize}/${s.fontWeight}`, 4),
    dialogs: group(q('[role=dialog], [role=alertdialog], dialog[open]'), (e, s) => `pad ${pad(s)} r${s.borderTopLeftRadius}`, 3),
    toasts: group(q('[data-sonner-toast], [class*=Toastify__toast], [class*=toast][role=status], [class*=toast][role=alert]'), (e, s) => `pad ${pad(s)} r${s.borderTopLeftRadius}`, 3),
    icons: group(q('svg'), (e, s, b) => `${Math.round(b.width)}x${Math.round(b.height)} stroke ${e.getAttribute('stroke-width') || s.strokeWidth}`, 6),
    headings: group(q('h1, h2, h3'), (e, s) => `${e.tagName.toLowerCase()} ${s.fontSize}/${s.fontWeight}`, 6),
    header: group(q('header').slice(0, 1), (e, s, b) => `h${px(b.height)} pad ${pad(s)} border-bottom ${s.borderBottomWidth}`, 1),
  };
  return out;
}
