// compile.js — 构建三份提交 PPTX（各 10 页）
const pptxgen = require("pptxgenjs");
const Hp = require("./helpers");

const DECKS = [
  {
    mod: require("./deck_b12"),
    theme: { primary: "1F2933", secondary: "4A5568", accent: "E8630A", light: "C9D2DA", bg: "F4F5F7" },
    out: "../../submissions/初赛提交_B12_安灯中枢.pptx", name: "B12 安灯中枢"
  },
  {
    mod: require("./deck_b31"),
    theme: { primary: "16324F", secondary: "2D4A6B", accent: "2563EB", light: "A8C4E8", bg: "F5F7FA" },
    out: "../../submissions/初赛提交_B31_齐途.pptx", name: "B31 齐途"
  },
  {
    mod: require("./deck_b21"),
    theme: { primary: "1E3A2F", secondary: "3C5A4C", accent: "1F9D55", light: "A9D6BC", bg: "F4F8F5" },
    out: "../../submissions/初赛提交_B21_气脉助手.pptx", name: "B21 气脉助手"
  }
];

(async () => {
  for (const d of DECKS) {
    const pres = new pptxgen();
    pres.layout = "LAYOUT_16x9";
    d.mod.build(pres, d.theme, Hp);
    await pres.writeFile({ fileName: d.out });
    console.log("OK", d.name, "->", d.out);
  }
})();
