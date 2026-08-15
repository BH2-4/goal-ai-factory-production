// helpers.js — 三副提交 PPT 共用的布局引擎（16:9, 10"×5.625"）
const FONT = "Microsoft YaHei";
const W = 10, H = 5.625;

function badge(slide, pres, theme, n) {
  slide.addShape(pres.shapes.OVAL, { x: 9.3, y: 5.1, w: 0.34, h: 0.34, fill: { color: theme.accent } });
  slide.addText(String(n), { x: 9.3, y: 5.1, w: 0.34, h: 0.34, fontSize: 10, fontFace: FONT, color: "FFFFFF", bold: true, align: "center", valign: "middle" });
}

function header(slide, pres, theme, title, sub) {
  slide.background = { color: theme.bg };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0.55, y: 0.42, w: 0.09, h: 0.62, fill: { color: theme.accent } });
  slide.addText(title, { x: 0.78, y: 0.34, w: 8.4, h: 0.52, fontSize: 21, fontFace: FONT, color: theme.primary, bold: true });
  if (sub) slide.addText(sub, { x: 0.78, y: 0.84, w: 8.4, h: 0.3, fontSize: 11, fontFace: FONT, color: theme.secondary });
}

function cover(pres, theme, meta) {
  const slide = pres.addSlide();
  slide.background = { color: theme.primary };
  slide.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: W, h: 0.12, fill: { color: theme.accent } });
  slide.addText(meta.kicker, { x: 0.7, y: 0.85, w: 8.6, h: 0.35, fontSize: 13, fontFace: FONT, color: theme.light, bold: true, charSpacing: 2 });
  slide.addText(meta.title, { x: 0.7, y: 1.35, w: 8.6, h: 1.0, fontSize: 40, fontFace: FONT, color: "FFFFFF", bold: true });
  slide.addText(meta.subtitle, { x: 0.7, y: 2.35, w: 8.6, h: 0.5, fontSize: 18, fontFace: FONT, color: theme.light });
  slide.addShape(pres.shapes.LINE, { x: 0.72, y: 3.05, w: 2.2, h: 0, line: { color: theme.accent, width: 2.5 } });
  slide.addText(meta.oneline, { x: 0.7, y: 3.25, w: 8.0, h: 0.75, fontSize: 13, fontFace: FONT, color: "E8ECF0", lineSpacing: 20 });
  const tags = meta.tags.map((t, i) => ({ text: (i ? "    " : "") + "◆ " + t, options: { fontSize: 11.5, fontFace: FONT, color: theme.light, bold: true } }));
  slide.addText(tags, { x: 0.7, y: 4.35, w: 8.6, h: 0.4, align: "left", valign: "middle" });
  slide.addText(meta.footer, { x: 0.7, y: 5.05, w: 8.6, h: 0.3, fontSize: 10, fontFace: FONT, color: theme.light });
  return slide;
}

function statCards(slide, pres, theme, stats, y, opt) {
  const gap = 0.25, cw = (W - 1.4 - gap * (stats.length - 1)) / stats.length;
  stats.forEach((s, i) => {
    const x = 0.7 + i * (cw + gap);
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: cw, h: opt && opt.h || 1.5, fill: { color: "FFFFFF" }, line: { color: theme.light, width: 1 }, rectRadius: 0.06 });
    slide.addShape(pres.shapes.RECTANGLE, { x, y, w: cw, h: 0.07, fill: { color: theme.accent } });
    slide.addText(s.num, { x, y: y + 0.18, w: cw, h: 0.62, fontSize: 30, fontFace: FONT, color: theme.accent, bold: true, align: "center" });
    slide.addText(s.label, { x: x + 0.15, y: y + 0.82, w: cw - 0.3, h: 0.55, fontSize: 11, fontFace: FONT, color: theme.secondary, align: "center", valign: "top", lineSpacing: 14 });
  });
}

function flowRow(slide, pres, theme, steps, y, opt) {
  opt = opt || {};
  const n = steps.length, gap = 0.34, cw = (W - 1.4 - gap * (n - 1)) / n, hh = opt.h || 0.78;
  steps.forEach((s, i) => {
    const x = 0.7 + i * (cw + gap);
    const gate = s.gate;
    slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x, y, w: cw, h: hh,
      fill: { color: gate ? "FFF6EC" : "FFFFFF" },
      line: { color: gate ? "E8630A" : theme.light, width: gate ? 1.6 : 1 }, rectRadius: 0.05
    });
    slide.addText(s.t || s, { x: x + 0.04, y: y + 0.06, w: cw - 0.08, h: hh - 0.12, fontSize: opt.fs || 11, fontFace: FONT, color: theme.primary, bold: true, align: "center", valign: "middle", lineSpacing: 13 });
    if (i < n - 1) slide.addText("→", { x: x + cw - 0.02, y: y + hh / 2 - 0.17, w: gap + 0.04, h: 0.34, fontSize: 14, fontFace: FONT, color: theme.accent, bold: true, align: "center", valign: "middle" });
  });
}

function panel(slide, pres, theme, o) {
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: o.x, y: o.y, w: o.w, h: o.h, fill: { color: "FFFFFF" }, line: { color: theme.light, width: 1 }, rectRadius: 0.06 });
  slide.addShape(pres.shapes.RECTANGLE, { x: o.x, y: o.y, w: o.w, h: 0.06, fill: { color: o.accent || theme.accent } });
  slide.addText(o.title, { x: o.x + 0.18, y: o.y + 0.14, w: o.w - 0.36, h: 0.34, fontSize: 13, fontFace: FONT, color: theme.primary, bold: true });
  if (o.lines) {
    const runs = o.lines.map(l => ({ text: l, options: { bullet: true, fontSize: o.fs || 11, fontFace: FONT, color: theme.secondary, lineSpacing: o.ls || 16 } }));
    slide.addText(runs, { x: o.x + 0.22, y: o.y + 0.52, w: o.w - 0.42, h: o.h - 0.66, valign: "top", align: "left" });
  }
}

function dutyTable(slide, pres, theme, rows, y) {
  const head = rows[0].map(t => ({ text: t, options: { bold: true, color: "FFFFFF", fill: { color: theme.primary }, fontSize: 11.5, fontFace: FONT, align: "center", valign: "middle" } }));
  const body = rows.slice(1).map(r => r.map((t, ci) => ({
    text: t, options: {
      fontSize: 10.5, fontFace: FONT, color: ci === 0 ? theme.primary : theme.secondary,
      bold: ci === 0, align: ci === 0 ? "center" : "left", valign: "middle",
      fill: { color: "FFFFFF" }
    }
  })));
  slide.addTable([head, ...body], { x: 0.7, y, w: 8.6, colW: [2.0, 3.3, 3.3], border: { pt: 0.75, color: theme.light }, rowH: 0.34, valign: "middle" });
}

function milestones(slide, pres, theme, ms, y) {
  slide.addShape(pres.shapes.LINE, { x: 1.1, y: y + 0.5, w: 7.8, h: 0, line: { color: theme.light, width: 1.5 } });
  const n = ms.length, cw = 7.8 / n;
  ms.forEach((m, i) => {
    const cx = 1.1 + i * cw + cw / 2;
    slide.addShape(pres.shapes.OVAL, { x: cx - 0.09, y: y + 0.41, w: 0.18, h: 0.18, fill: { color: theme.accent } });
    slide.addText(m.date, { x: cx - cw / 2, y: y + 0.02, w: cw, h: 0.3, fontSize: 12.5, fontFace: FONT, color: theme.accent, bold: true, align: "center" });
    slide.addText(m.txt, { x: cx - cw / 2 + 0.1, y: y + 0.68, w: cw - 0.2, h: 0.85, fontSize: 10.5, fontFace: FONT, color: theme.secondary, align: "center", valign: "top", lineSpacing: 14 });
  });
}

module.exports = { FONT, W, H, badge, header, cover, statCards, flowRow, panel, dutyTable, milestones };
