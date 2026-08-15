// deck_b31.js — 齐途 QiPlan（10 页提交版）
module.exports.build = function (pres, theme, Hp) {
  const { badge, header, cover, statCards, flowRow, panel, dutyTable, milestones } = Hp;

  cover(pres, theme, {
    kicker: "GOAI 世界人工智能开源大赛 · 无界应用赛道 · AI+工业制造",
    title: "齐途 QiPlan",
    subtitle: "机加厂齐套核算与插单冲突解释智能体",
    oneline: "求解器负责算数、大模型负责说话：齐套核算、可行排产、被延订单的冲突解释与动作包，插单全链 30 秒。",
    tags: ["插单冲突解释", "LLM 零数值契约", "动作包交付"],
    footer: "参赛作品 · 方案汇报"
  });

  let s = pres.addSlide(); header(s, pres, theme, "01 场景与痛点", "插单的答案，不该靠电话和 Excel");
  statCards(s, pres, theme, [
    { num: "≥2h", label: "一次插单评估耗时\n（Excel 核对+电话确认，假设口径）" },
    { num: "T-1~2天", label: "缺料暴露时点\n（投产前才发现）" },
    { num: "说不清", label: "被延订单原因\n（销售与产线互相埋怨）" }
  ], 1.35);
  panel(s, pres, theme, { x: 0.7, y: 3.15, w: 8.6, h: 1.9, title: "计划员的日常", lines: [
    "销售接急单 → 计划员翻 BOM 表、问仓库、问车间，两小时后才敢回“能不能做、几号交”",
    "开工前 1-2 天发现料不够，赶工、紧急采购、违约金三重代价叠加",
    "被延的订单没有解释，信任在销售与车间之间流失"
  ], fs: 12, ls: 20 });
  badge(s, pres, theme, 2);

  s = pres.addSlide(); header(s, pres, theme, "02 用户与全旅程", "四个角色，一条解释链");
  panel(s, pres, theme, { x: 0.7, y: 1.25, w: 2.7, h: 1.5, title: "计划员", lines: ["控制台主用户", "方案采纳者"], fs: 11 });
  panel(s, pres, theme, { x: 3.65, y: 1.25, w: 2.7, h: 1.5, title: "销售", lines: ["CTP 问答端", "交期承诺方"], fs: 11, accent: theme.secondary });
  panel(s, pres, theme, { x: 6.6, y: 1.25, w: 2.7, h: 1.5, title: "物控 / 采购", lines: ["缺口与请购包", "比价与下单"], fs: 11, accent: theme.light });
  flowRow(s, pres, theme, ["插单/变化", "齐套核算", "约束求解", "冲突解释", "动作包", { t: "计划签字 ◉", gate: true }], 3.25, { fs: 10.5, h: 0.8 });
  s.addText("◉ = 宏门禁：计划采纳、交期承诺、替代料启用、供应商选择与下单，均由人签字", { x: 0.7, y: 4.35, w: 8.6, h: 0.3, fontSize: 10.5, fontFace: Hp.FONT, color: theme.secondary, italic: true });
  badge(s, pres, theme, 3);

  s = pres.addSlide(); header(s, pres, theme, "03 产品方案", "计划控制台 + 销售问答端");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 4.2, h: 3.55, title: "计划员控制台", lines: [
    "齐套看板：三层 BOM 展开 × 库存 × 在途（含供应商风险加权）",
    "插单 30 秒：可行排产 + 被延订单 + 逐单归因",
    "冲突解释：缺哪个料 / 哪台机满载 / 哪批在途有风险，每条可点开约束日志",
    "假设区：若明晨到货 200 件 → 计划 B（条件化推演）",
    "偏好库：手动调整三次的模式，提示转为显式规则（人确认）"
  ], fs: 11, ls: 18 });
  panel(s, pres, theme, { x: 5.15, y: 1.3, w: 4.15, h: 1.68, title: "销售 CTP 问答端", lines: ["自然语言问单：能不能接、几号交", "澄清品项/数量/交期/优先级", "输出条件化承诺草案（若料到→D 日）"], fs: 11, accent: theme.secondary });
  panel(s, pres, theme, { x: 5.15, y: 3.17, w: 4.15, h: 1.68, title: "动作包（交付物）", lines: ["工单建议 + 请购单 + 比价矩阵", "交期承诺草案（条件化）", "不是一张表，是一组可执行动作"], fs: 11, accent: theme.light });
  badge(s, pres, theme, 4);

  s = pres.addSlide(); header(s, pres, theme, "04 AI 设计：数字与语言的契约", "大模型零数值计算，写进产品契约");
  dutyTable(s, pres, theme, [
    ["环节", "机制", "AI 是否参与"],
    ["齐套核算", "纯程序（BOM×库存×在途）", "无（100% 可判卷）"],
    ["排产求解", "OR-Tools 约束求解", "无"],
    ["在途风险评分", "规则（历史准时率+物流事件）", "无（不监视）"],
    ["约束澄清 / 冲突解释", "大模型引用约束日志", "生成（不改数）"],
    ["假设区 / CTP 问答", "大模型 + 求解器", "对话（数字来自程序）"],
    ["采纳 / 承诺 / 下单", "人工门禁", "无"]
  ], 1.35);
  s.addText("界面数字全部标注程序来源，可点开核对——“大模型算错数”这一质疑在契约层被排除。", { x: 0.7, y: 4.6, w: 8.6, h: 0.4, fontSize: 11.5, fontFace: Hp.FONT, color: theme.primary, bold: true });
  badge(s, pres, theme, 5);

  s = pres.addSlide(); header(s, pres, theme, "05 技术路线", "确定性归程序，解释性归模型");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 4.2, h: 3.55, title: "技术栈", lines: [
    "齐套引擎：MRP 逻辑纯程序实现，单元测试判卷",
    "求解器：OR-Tools flexible job-shop，输出可行解与约束违反日志",
    "约束日志：解释的唯一事实来源（哪条约束 / 谁占用 / 何时释放）",
    "生成层：冲突解释、假设标注、CTP 对话（仅引用日志与程序输出）"
  ], fs: 11.5, ls: 19 });
  panel(s, pres, theme, { x: 5.15, y: 1.3, w: 4.15, h: 3.55, title: "解释的样子", lines: [
    "“订单 A 被推至下周三：",
    "① 缺 X 材料 200 件（在途 300，风险分 0.7）",
    "② Y 机床本周满载（周四释放）",
    "替代方案：调序（换 Z 单）或催料（加急在途）",
    "假设区：若明晨 X 到货 → A 可回排至周五”",
    "——每一条都能点开日志核对"
  ], fs: 11.5, ls: 19, accent: theme.secondary });
  badge(s, pres, theme, 6);

  s = pres.addSlide(); header(s, pres, theme, "06 数据与合规", "模拟生成器开源，可复算");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 8.6, h: 1.8, title: "数据口径", lines: [
    "自建模拟生成器：BOM 三层 × 库存 × 在途（含风险分）× 订单 30-50 张 × 产能日历，字段与剧本全披露",
    "不接真实 ERP，不使用任何企业真实数据"
  ], fs: 12, ls: 20 });
  panel(s, pres, theme, { x: 0.7, y: 3.35, w: 8.6, h: 1.55, title: "边界声明", lines: [
    "纯计划建议系统，不替代计划员专业判断（官方手册 9.3）；不写入真实 ERP",
    "计划采纳、交期承诺、替代料启用、下单均为人工门禁"
  ], fs: 12, ls: 20, accent: "E8630A" });
  badge(s, pres, theme, 7);

  s = pres.addSlide(); header(s, pres, theme, "07 评测与验证", "三个硬指标");
  statCards(s, pres, theme, [
    { num: "100%", label: "齐套核算准确率\n（程序自动判卷）" },
    { num: "0", label: "排产硬约束违反\n（求解器保证）" },
    { num: "≤30s", label: "插单全链响应\n（重算+求解+解释）" }
  ], 1.35);
  panel(s, pres, theme, { x: 0.7, y: 3.15, w: 8.6, h: 1.7, title: "演示即验证", lines: [
    "现场插单：30 秒出方案 + 逐单解释 + 动作包；评委可自拟订单现场重跑",
    "对照实验：同一数据集下，延期订单数较 FIFO 基线下降 ≥15%"
  ], fs: 12, ls: 20 });
  badge(s, pres, theme, 8);

  s = pres.addSlide(); header(s, pres, theme, "08 排期与开放", "从控制台到问答端");
  milestones(s, pres, theme, [
    { date: "初赛 8.16", txt: "方案材料\n（简介+本 PPT）" },
    { date: "复赛 9.3", txt: "齐套+插单解释+请购包\n一条链可运行（含 CTP 端）" },
    { date: "决赛 9.22", txt: "交互推演：批量急单 /\n假设区现场改条件重排" }
  ], 1.45);
  panel(s, pres, theme, { x: 0.7, y: 3.4, w: 8.6, h: 1.6, title: "开源与复用", lines: [
    "制造模拟数据生成器 ｜ 齐套核算引擎 ｜ 约束日志规范 ｜ 冲突解释模板 ｜ CTP 问答端组件",
    "中小机械/汽配厂可直接复用；与排产/ERP 系统松耦合集成"
  ], fs: 11.5, ls: 19 });
  badge(s, pres, theme, 9);

  s = pres.addSlide(); s.background = { color: theme.primary };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: Hp.W, h: 0.12, fill: { color: theme.accent } });
  s.addText("齐途 QiPlan", { x: 0.7, y: 1.7, w: 8.6, h: 0.8, fontSize: 30, fontFace: Hp.FONT, color: "FFFFFF", bold: true });
  s.addText("求解器算数，大模型说话，计划员签字。", { x: 0.7, y: 2.55, w: 8.6, h: 0.5, fontSize: 16, fontFace: Hp.FONT, color: theme.light });
  s.addText([
    { text: "数字可复算，解释可点开，交付是动作包。", options: { fontSize: 13, fontFace: Hp.FONT, color: "E8ECF0", breakLine: true } },
    { text: "插单从两小时变成三十秒——省下的不是工时，是销售与车间之间的信任。", options: { fontSize: 13, fontFace: Hp.FONT, color: "E8ECF0" } }
  ], { x: 0.7, y: 3.3, w: 8.6, h: 0.9, lineSpacing: 22 });
  s.addText("GOAI 世界人工智能开源大赛 · 无界应用 · AI+工业制造", { x: 0.7, y: 4.9, w: 8.6, h: 0.3, fontSize: 10, fontFace: Hp.FONT, color: theme.light });
};
