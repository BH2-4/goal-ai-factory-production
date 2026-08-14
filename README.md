# Goal AI Factory Production

GOAI 世界人工智能开源大赛 · 无界应用（Boundless Agents）赛道 · **AI+工业制造** 方向参赛项目仓库。

> 仓库名保留用户命名的 "Goal"（赛事官方缩写实为 GOAI，Global Open-source AI Challenge）。

## 赛事关键信息（详见 docs/research/）

- 初赛提交截止：**2026-08-16 23:59:59（北京时间）**；初赛必交：作品简介 ≤500 字 + 方案 PPT/PDF
- 复赛（9.3 截止）：可运行 Demo + 代码仓库 + 合规说明，四项全必交
- 评审权重：行业场景价值 25 / Agent 能力与任务闭环 25 / 产品体验与 Demo 完成度 20 / 技术实现深度 15 / 安全合规可追溯 10 / 开放复用 5
- 工业制造个性化评审：多源信息融合、流程闭环、解释性、可操作性、安全生产边界
- 官方手册 PDF：`docs/research/GOAI无界应用参赛手册_官方.pdf`

## 目录结构

```
docs/
  DECISIONS.md      # 决策日志（含依据，逐条可溯源）
  research/         # 调研成果归档（赛事调研 → 方向池 → 评估筛选 → 合并 → MVP 库 → 评分标准）
prds/               # 9 份 MVP PRD（产出中）
```

## 项目三大主线（P1/P2/P3）

| 项目 | 视角 | 主推 MVP |
|---|---|---|
| P2 装备售后全旅程闭环 After-Sales Copilot | 装备厂商 | M2-A 报修-修复-沉淀主链、M2-B 批次故障哨兵、M2-C 设备档案自动建立 |
| P3 计划协同副驾 Planning Copilot | 中小厂计划域 | M3-A 齐套+插单冲突解释、M3-C 供应商风险哨兵、M3-B 缺料请购联动 |
| P1 厂内异常闭环中枢 Factory Ops Copilot | 工厂运营 | M1-A 质量根因链、M1-B Andon 值守循环、M1-E 沉淀飞轮 |

## 核心设计哲学（贯穿所有 Agent）

**微循环自主、宏流程门禁**：Agent 在极小闭环内自主完成（发现-分析-起草-准备）；
大流水线的关键节点设人工门禁，终点（放行/召回/停线/采纳计划等重大决策）必须人工确认。

## 提交规范

频繁提交，conventional commits：`docs:` 调研文档 / `prd:` 产品文档 / `feat:` 代码 / `fix:` 修正 / `chore:` 杂项。
