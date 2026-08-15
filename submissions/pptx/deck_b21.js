// deck_b21.js — 气脉助手 AirFix（10 页提交版）
module.exports.build = function (pres, theme, Hp) {
  const { badge, header, cover, statCards, flowRow, panel, dutyTable, milestones } = Hp;

  cover(pres, theme, {
    kicker: "GOAI 世界人工智能开源大赛 · 无界应用赛道 · AI+工业制造",
    title: "气脉助手 AirFix",
    subtitle: "空压机售后报修修复沉淀智能体",
    oneline: "客户拍照报修，系统带出档案、多轮问诊翻译症状、给出带依据的诊断，查备件、起草工单——修完自动沉淀案例，下次同型报修答案已在库里。",
    tags: ["证据化诊断", "设备档案·保内判定", "批次线索（纯规则）"],
    footer: "参赛作品 · 方案汇报"
  });

  let s = pres.addSlide(); header(s, pres, theme, "01 场景与痛点", "报修电话的另一端，总在等专家");
  statCards(s, pres, theme, [
    { num: "≥24h", label: "报修响应时长\n（假设口径，交付前校准）" },
    { num: "30-40%", label: "专家差旅占售后成本\n（行业常识口径）" },
    { num: "修完即蒸发", label: "维修知识随人流失\n（同故障重复诊断）" }
  ], 1.35);
  panel(s, pres, theme, { x: 0.7, y: 3.15, w: 8.6, h: 1.9, title: "售后现状", lines: [
    "客户说外行话（“机器响得厉害、出气变少”），客服不懂技术，工程师在出差",
    "诊断知识在老师傅脑中与纸质手册里；备件库存靠翻表格",
    "批次性故障靠客户投诉倒逼才发现，缺乏数据支撑"
  ], fs: 12, ls: 20 });
  badge(s, pres, theme, 2);

  s = pres.addSlide(); header(s, pres, theme, "02 用户与全旅程", "双端形态，一条全链");
  panel(s, pres, theme, { x: 0.7, y: 1.25, w: 4.2, h: 1.5, title: "客户设备管理员", lines: ["报修端：拍照 / 语音 / 故障码", "看进度与维修指导"], fs: 11 });
  panel(s, pres, theme, { x: 5.15, y: 1.25, w: 4.15, h: 1.5, title: "厂商售后工程师", lines: ["工作台：接单、确认诊断", "处置填报与案例审核"], fs: 11, accent: theme.secondary });
  flowRow(s, pres, theme, ["拍照报修", "档案带出", "多轮问诊", "证据化诊断", "备件+工单", "指导维修", { t: "确认沉淀 ◉", gate: true }], 3.25, { fs: 10, h: 0.8 });
  s.addText("◉ = 宏门禁：诊断确认＝工程师；高压电气/压力容器作业＝转持证人员；案例入库＝存档审核", { x: 0.7, y: 4.35, w: 8.6, h: 0.3, fontSize: 10.5, fontFace: Hp.FONT, color: theme.secondary, italic: true });
  badge(s, pres, theme, 3);

  s = pres.addSlide(); header(s, pres, theme, "03 产品方案", "售后服务台 · 从接单到知识资产");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 4.2, h: 3.55, title: "核心机制", lines: [
    "设备档案：报修即带出装机信息、保养计划、保修状态——保内保外规则自动判定",
    "问诊：状态机约束的多轮对话，最多三轮澄清，信息不足转人工坐席",
    "诊断 Top-3：每条附诊断依据（手册段落坐标 / 相似维修工单 / 照片标注）+ 待确认项 + 置信度",
    "备件与工单：BOM 匹配、库存查询、派单建议；缺货附请购提醒卡"
  ], fs: 11, ls: 18 });
  panel(s, pres, theme, { x: 5.15, y: 1.3, w: 4.15, h: 1.68, title: "知识沉淀（越用越准）", lines: ["结案自动归档维修案例（五要素）", "同型报修再现 → 直接命中历史方案", "同型热度 30 天计数（纯规则）"], fs: 11, accent: theme.secondary });
  panel(s, pres, theme, { x: 5.15, y: 3.17, w: 4.15, h: 1.68, title: "批次线索报告", lines: ["热度超阈 → 一键生成批次线索", "影响面清单供厂商研判", "是否深查与通报：厂商拍板"], fs: 11, accent: theme.light });
  badge(s, pres, theme, 4);

  s = pres.addSlide(); header(s, pres, theme, "04 AI 设计：诊断必须可溯", "检索给依据，规则管统计，人管确认");
  dutyTable(s, pres, theme, [
    ["环节", "机制", "AI 是否参与"],
    ["档案带出 / 保内判定", "规则", "无"],
    ["多轮问诊", "状态机 + 大模型", "对话（翻译症状）"],
    ["知识检索", "手册 RAG + 工单 CBR", "检索（附引用）"],
    ["备件 / 工单起草", "模板填充", "起草"],
    ["同型热度统计", "30 天计数规则", "无（报告一键生成）"],
    ["诊断确认 / 高危作业", "人工门禁", "无"]
  ], 1.35);
  s.addText("诊断输出 = 建议 + 待确认项 + 依据引用；无依据时明说“手册未覆盖”，不编造。", { x: 0.7, y: 4.6, w: 8.6, h: 0.4, fontSize: 11.5, fontFace: Hp.FONT, color: theme.primary, bold: true });
  badge(s, pres, theme, 5);

  s = pres.addSlide(); header(s, pres, theme, "05 技术路线", "双端 + 检索增强 + 证据卡");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 4.2, h: 3.55, title: "技术栈", lines: [
    "双端：客户报修端（Web/小程序形态）+ 工程师工作台",
    "知识层：手册 RAG（引用到段落坐标）+ 维修工单相似检索",
    "诊断证据卡：结论 × 依据列表 × 待确认项 × 置信度分级",
    "照片：部件与状态识别，辅助信号（降级路径：纯文字问诊）"
  ], fs: 11.5, ls: 19 });
  panel(s, pres, theme, { x: 5.15, y: 1.3, w: 4.15, h: 3.55, title: "诊断卡的样子", lines: [
    "疑似：进气阀积碳（置信度 高）",
    "依据：手册 §4.2（第 12 页）｜相似工单 #0741（同类机型 3 例）｜照片标注：阀体温度异常",
    "待确认项：运行时长是否超 8000h",
    "建议措施：更换阀组件（库存 2 件）",
    "——工程师确认后生效"
  ], fs: 11.5, ls: 19, accent: theme.secondary });
  badge(s, pres, theme, 6);

  s = pres.addSlide(); header(s, pres, theme, "06 数据与合规", "自建数据，版权干净");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 8.6, h: 1.8, title: "数据口径", lines: [
    "自建 2-3 本模拟设备手册（规避版权）+ 200 条模拟维修工单（预埋 2 组批次热度剧本），生成逻辑披露",
    "不使用真实厂商与客户数据；照片素材自行拍摄或公开图"
  ], fs: 12, ls: 20 });
  panel(s, pres, theme, { x: 0.7, y: 3.35, w: 8.6, h: 1.55, title: "边界声明", lines: [
    "诊断是“建议 + 待确认项”，确认者是工程师；高压电气、压力容器作业强制提示转持证人员（官方手册 9.3、FAQ Q13）",
    "批次深查与客户通报由厂商管理层决定；系统不监视，来单才动"
  ], fs: 12, ls: 20, accent: "E8630A" });
  badge(s, pres, theme, 7);

  s = pres.addSlide(); header(s, pres, theme, "07 评测与验证", "三个可判卷指标");
  statCards(s, pres, theme, [
    { num: "≥70%", label: "Top-3 诊断命中率\n（预置 ground truth 工单集）" },
    { num: "≥90%", label: "备件建议准确率\n（BOM 匹配判卷）" },
    { num: "2/2", label: "批次线索检出\n（误报 ≤1 次/月）" }
  ], 1.35);
  panel(s, pres, theme, { x: 0.7, y: 3.15, w: 8.6, h: 1.7, title: "演示即验证", lines: [
    "全旅程演示：拍照报修 → 三轮问诊 → 证据卡 → 工单 → 结案沉淀 → 同型报修直接命中",
    "失败分支也是演示内容：信息缺失 → 澄清；检索未命中 → 转人工"
  ], fs: 12, ls: 20 });
  badge(s, pres, theme, 8);

  s = pres.addSlide(); header(s, pres, theme, "08 排期与开放", "从双端原型到完整旅程");
  milestones(s, pres, theme, [
    { date: "初赛 8.16", txt: "方案材料\n（简介+本 PPT）" },
    { date: "复赛 9.3", txt: "报修→沉淀一条链可运行\n（双端，证据卡完整）" },
    { date: "决赛 9.22", txt: "完整旅程 + 失败分支\n+ 批次线索彩蛋" }
  ], 1.45);
  panel(s, pres, theme, { x: 0.7, y: 3.4, w: 8.6, h: 1.6, title: "开源与复用", lines: [
    "售后知识库规范（手册/案例/备件三库）｜ 问诊流程 DSL ｜ 诊断证据卡模板 ｜ 同型热度规则 ｜ 模拟手册与工单生成器",
    "可迁移至其他装备行业：换手册，不换引擎"
  ], fs: 11.5, ls: 19 });
  badge(s, pres, theme, 9);

  s = pres.addSlide(); s.background = { color: theme.primary };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: Hp.W, h: 0.12, fill: { color: theme.accent } });
  s.addText("气脉助手 AirFix", { x: 0.7, y: 1.7, w: 8.6, h: 0.8, fontSize: 30, fontFace: Hp.FONT, color: "FFFFFF", bold: true });
  s.addText("终点是工单与案例，不是一句话回答。", { x: 0.7, y: 2.55, w: 8.6, h: 0.5, fontSize: 16, fontFace: Hp.FONT, color: theme.light });
  s.addText([
    { text: "诊断带依据，高危转持证，批次线索人拍板。", options: { fontSize: 13, fontFace: Hp.FONT, color: "E8ECF0", breakLine: true } },
    { text: "每次维修都变成厂商的知识资产——同样的报修再打进来，答案已经在库里等着。", options: { fontSize: 13, fontFace: Hp.FONT, color: "E8ECF0" } }
  ], { x: 0.7, y: 3.3, w: 8.6, h: 0.9, lineSpacing: 22 });
  s.addText("GOAI 世界人工智能开源大赛 · 无界应用 · AI+工业制造", { x: 0.7, y: 4.9, w: 8.6, h: 0.3, fontSize: 10, fontFace: Hp.FONT, color: theme.light });
};
