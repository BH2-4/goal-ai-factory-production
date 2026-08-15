// deck_b12.js — 安灯中枢 AndonCop（10 页提交版）
module.exports.build = function (pres, theme, Hp) {
  const { badge, header, cover, statCards, flowRow, panel, dutyTable, milestones } = Hp;

  cover(pres, theme, {
    kicker: "GOAI 世界人工智能开源大赛 · 无界应用赛道 · AI+工业制造",
    title: "安灯中枢 AndonCop",
    subtitle: "车间异常响应值守智能体",
    oneline: "把设备报警、质量超标、缺料预警从“现场吼人 + 微信群”，变成自动分诊、按技能派单、超时升级、结案归档的闭环。",
    tags: ["自动分诊派单", "SLA 超时升级", "结案即沉淀"],
    footer: "参赛作品 · 方案汇报"
  });

  let s = pres.addSlide(); header(s, pres, theme, "01 场景与痛点", "机加车间的异常，靠吼来传递");
  statCards(s, pres, theme, [
    { num: "≥30min", label: "异常平均响应时长\n（假设口径，交付前访谈校准）" },
    { num: "≥30%", label: "同类异常复发率\n（复盘缺失所致）" },
    { num: "0", label: "结构化处理记录\n（散落在微信群）" }
  ], 1.35);
  panel(s, pres, theme, { x: 0.7, y: 3.15, w: 8.6, h: 1.9, title: "现状链条", lines: [
    "异常发生后：班组长现场喊人 + 微信群 @人，谁看到谁没看到不可知",
    "超时无兜底：没有升级机制，事拖着就没人管",
    "处理完即蒸发：无结构化记录，月度复盘无数据，同类问题反复发生"
  ], fs: 12, ls: 20 });
  badge(s, pres, theme, 2);

  s = pres.addSlide(); header(s, pres, theme, "02 用户与全旅程", "三个角色，一条闭环");
  panel(s, pres, theme, { x: 0.7, y: 1.25, w: 2.7, h: 1.5, title: "班组长", lines: ["哨位屏值守", "异常第一响应人"], fs: 11 });
  panel(s, pres, theme, { x: 3.65, y: 1.25, w: 2.7, h: 1.5, title: "维修工程师", lines: ["移动端接单", "处置与记录填报"], fs: 11, accent: theme.secondary });
  panel(s, pres, theme, { x: 6.6, y: 1.25, w: 2.7, h: 1.5, title: "车间主任", lines: ["复盘端看板", "Pareto 与复发趋势"], fs: 11, accent: theme.light });
  flowRow(s, pres, theme, ["异常流入", "分诊定级", "按技派单", "处置", { t: "结案确认 ◉", gate: true }, "案例归档", "复发预警"], 3.25, { fs: 10.5, h: 0.8 });
  s.addText("◉ = 宏门禁：停线建议与结案确认由主管人工拍板；橙色框为人工环节", { x: 0.7, y: 4.35, w: 8.6, h: 0.3, fontSize: 10.5, fontFace: Hp.FONT, color: theme.secondary, italic: true });
  badge(s, pres, theme, 3);

  s = pres.addSlide(); header(s, pres, theme, "03 产品方案", "值守调度台 · 三端形态");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 4.2, h: 3.55, title: "核心机制", lines: [
    "事件引擎：统一接入遥测越限 / 质检超标 / 缺料预警 / 人工拍照上报",
    "分诊：规则优先（故障码、产线、时段），AI 仅辅助分类定级 P1-P3",
    "派单：技能矩阵 × 班次 × 当前负荷，自动推荐人选与备份",
    "SLA 升级链：P1 15min / P2 30min / P3 4h（可配置），超时逐级上报",
    "升级凭证：超时时长、同类历史均值、当班负载数据打包，主管一眼可判"
  ], fs: 11.5, ls: 19 });
  panel(s, pres, theme, { x: 5.15, y: 1.3, w: 4.15, h: 1.68, title: "知识闭环（越用越快）", lines: ["结案自动归档为结构化案例", "同型事件再现 → 匹配 Top-3 历史预案推送", "首次 40 分钟 → 再次 5 分钟"], fs: 11, accent: theme.secondary });
  panel(s, pres, theme, { x: 5.15, y: 3.17, w: 4.15, h: 1.68, title: "三端形态", lines: ["班组长哨位屏：事件流与处置台", "工程师移动端：接单 / 填报 / 预案查看", "主任复盘端：Pareto / 复发趋势"], fs: 11, accent: theme.light });
  badge(s, pres, theme, 4);

  s = pres.addSlide(); header(s, pres, theme, "04 AI 设计：谁在哪个环节干活", "规则管确定性，AI 管语言，人管拍板");
  dutyTable(s, pres, theme, [
    ["环节", "机制", "AI 是否参与"],
    ["事件值守 / 触发", "事件引擎（规则）", "无（不监视）"],
    ["分诊分类定级", "规则优先 + 阈值表", "辅助分类（生成）"],
    ["派单", "技能矩阵匹配", "无"],
    ["SLA 超时升级", "时钟 + 规则", "无（凭证撰写=生成）"],
    ["结案归档", "模板抽取", "案例整理（生成）"],
    ["复发预警", "聚集度统计", "归因叙述（生成）"],
    ["停线 / 结案确认", "人工门禁", "无"]
  ], 1.35);
  s.addText("设计原则：持续盯的事交给便宜的规则；判断的事交给昂贵的人；AI 只做中间的调度与文书。", { x: 0.7, y: 4.6, w: 8.6, h: 0.4, fontSize: 11.5, fontFace: Hp.FONT, color: theme.primary, bold: true });
  badge(s, pres, theme, 5);

  s = pres.addSlide(); header(s, pres, theme, "05 技术路线", "公开数据打底，事件驱动架构");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 4.2, h: 3.55, title: "技术栈", lines: [
    "事件源：UCI AI4I 2020 公开数据集（1 万条合成、5 类故障模式）映射设备告警流；支持人工拍照上报",
    "事件引擎：规则 DSL（分诊阈值、SLA 配置）",
    "检索：案例向量匹配（Top-3 预案）",
    "生成：升级凭证 / 案例卡 / 归因叙述（大模型，输出附数据引用）"
  ], fs: 11.5, ls: 19 });
  panel(s, pres, theme, { x: 5.15, y: 1.3, w: 4.15, h: 3.55, title: "照片多模态（辅助信号）", lines: [
    "现场照片辅助分诊判断（跑冒滴漏 / 显示面板）",
    "定位为辅助信号，不作唯一依据",
    "降级路径：纯文字事件照样跑通全链",
    "演示即证据：事件回放模式可复算"
  ], fs: 11.5, ls: 19, accent: theme.secondary });
  badge(s, pres, theme, 6);

  s = pres.addSlide(); header(s, pres, theme, "06 数据与合规", "公开 + 模拟，全披露");
  panel(s, pres, theme, { x: 0.7, y: 1.3, w: 8.6, h: 1.8, title: "数据口径", lines: [
    "AI4I 公开数据集（UCI）驱动设备事件；排班 / 技能矩阵 / 复发剧本为自建模拟，字段与生成逻辑披露",
    "不使用任何真实企业数据；案例只记“事”，不记“人”（无人员绩效评价）"
  ], fs: 12, ls: 20 });
  panel(s, pres, theme, { x: 0.7, y: 3.35, w: 8.6, h: 1.55, title: "边界声明", lines: [
    "仅作辅助参考，不控制真实设备，不替代现场安全生产决策与专业判断（官方手册 9.3、FAQ Q13）",
    "停线、重启等动作仅生成建议并要求人工确认"
  ], fs: 12, ls: 20, accent: "E8630A" });
  badge(s, pres, theme, 7);

  s = pres.addSlide(); header(s, pres, theme, "07 评测与验证", "三个可判卷指标");
  statCards(s, pres, theme, [
    { num: "≥85%", label: "分诊准确率\n（500 条标注事件集）" },
    { num: "0", label: "SLA 升级遗漏\n（程序断言判卷）" },
    { num: "≥75%", label: "复发 Top-3 命中率\n（预置案例库+复发剧本）" }
  ], 1.35);
  panel(s, pres, theme, { x: 0.7, y: 3.15, w: 8.6, h: 1.7, title: "演示即验证", lines: [
    "事件回放模式：灌入事件流，全链可复算",
    "对比演示：同一故障首次 40 分钟 vs 再次 5 分钟（知识闭环的价值）"
  ], fs: 12, ls: 20 });
  badge(s, pres, theme, 8);

  s = pres.addSlide(); header(s, pres, theme, "08 排期与开放", "从材料到三端");
  milestones(s, pres, theme, [
    { date: "初赛 8.16", txt: "方案材料\n（简介+本 PPT）" },
    { date: "复赛 9.3", txt: "事件回放一条链可运行\n（AI4I 驱动，分诊→归档）" },
    { date: "决赛 9.22", txt: "三端齐展示：实时注入\n+照片分诊+复发对比" }
  ], 1.45);
  panel(s, pres, theme, { x: 0.7, y: 3.4, w: 8.6, h: 1.6, title: "开源与复用", lines: [
    "异常事件统一 schema ｜ SLA 升级策略 DSL ｜ 案例库模板 ｜ 事件流模拟器（含复发剧本）",
    "可迁移至各类离散制造车间；冷启动支持存量纸质记录导入"
  ], fs: 11.5, ls: 19 });
  badge(s, pres, theme, 9);

  s = pres.addSlide(); s.background = { color: theme.primary };
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: Hp.W, h: 0.12, fill: { color: theme.accent } });
  s.addText("安灯中枢 AndonCop", { x: 0.7, y: 1.7, w: 8.6, h: 0.8, fontSize: 30, fontFace: Hp.FONT, color: "FFFFFF", bold: true });
  s.addText("把车间靠吼的异常，交给一个不下班的调度员。", { x: 0.7, y: 2.55, w: 8.6, h: 0.5, fontSize: 16, fontFace: Hp.FONT, color: theme.light });
  s.addText([
    { text: "AI 管调度与文书，规则管值守，人管拍板。", options: { fontSize: 13, fontFace: Hp.FONT, color: "E8ECF0", breakLine: true } },
    { text: "每次结案都在积累车间知识——第一次 40 分钟，第二次 5 分钟。", options: { fontSize: 13, fontFace: Hp.FONT, color: "E8ECF0" } }
  ], { x: 0.7, y: 3.3, w: 8.6, h: 0.9, lineSpacing: 22 });
  s.addText("GOAI 世界人工智能开源大赛 · 无界应用 · AI+工业制造", { x: 0.7, y: 4.9, w: 8.6, h: 0.3, fontSize: 10, fontFace: Hp.FONT, color: theme.light });
};
