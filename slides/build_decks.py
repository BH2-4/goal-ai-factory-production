#!/usr/bin/env python3
"""从 9 份 PRD 生成 9 份自包含翻页 HTML deck。
主题：endfield=终末地工业HUD / zzz=绝区零涩谷朋克，按项目气质分配。
统一 12 屏页序（映射 PRD §1-§12 + 审核记录页），键盘/按钮翻页，print CSS 支持 PDF 导出。
用法：python3 slides/build_decks.py
"""
import re, pathlib, html as H

ROOT = pathlib.Path(__file__).resolve().parents[1]
PRD_DIR, OUT = ROOT / 'prds', ROOT / 'slides'
OUT.mkdir(exist_ok=True)

DECKS = [
    dict(key='M2A', prd='PRD_M2A_报修修复沉淀主链.md', theme='endfield', proj='P2',
         code='ENF-01', title='气脉助手 AirFix', sub='报修-修复-沉淀主链',
         anchor='S01 · 空压机厂商售后远程支持', score='86.4', rank='作品层 5/9 · 第二梯队'),
    dict(key='M2B', prd='PRD_M2B_批次故障哨兵.md', theme='endfield', proj='P2',
         code='ENF-02', title='气脉哨兵 AirSentinel', sub='批次故障哨兵 ★旗舰',
         anchor='S04 · 空压机机队批次故障监测', score='91.2', rank='作品层 1/9 · 第一梯队'),
    dict(key='M2C', prd='PRD_M2C_设备档案自动建立.md', theme='endfield', proj='P2',
         code='ENF-03', title='气脉建档 AirDoc', sub='设备档案自动建立',
         anchor='S07 · 装机验收档案数字化', score='83.0', rank='作品层 8/9 · 模块库'),
    dict(key='M3A', prd='PRD_M3A_齐套核算与插单冲突解释.md', theme='endfield', proj='P3',
         code='ENF-04', title='齐途 QiPlan', sub='齐套核算+插单冲突解释 ★主推',
         anchor='S10 · 机械/汽配二级供应商', score='89.7', rank='作品层 3/9 · 第一梯队'),
    dict(key='M1B', prd='PRD_M1B_Andon值守循环.md', theme='endfield', proj='P1',
         code='ENF-05', title='安灯中枢 AndonCop', sub='Andon 值守循环',
         anchor='S22 · 机加车间设备+质量混合', score='89.9', rank='作品层 2/9 · 第一备选'),
    # ZZZ 四份（M1A/M3C/M3B/M1E）已改由 build_zzz_decks.py 以编辑部式美术重新生成，此处不再生成
]

CSS = """
:root{--w:1280px;--h:720px}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:"PingFang SC","Microsoft YaHei",system-ui,sans-serif;background:#08090c;overflow:hidden;
     display:flex;align-items:center;justify-content:center}
.mono{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace}
.deck{width:var(--w);height:var(--h);position:relative;box-shadow:0 30px 90px rgba(0,0,0,.6)}
.slide{position:absolute;inset:0;padding:56px 72px 64px;display:none;flex-direction:column;overflow:hidden}
.slide.active{display:flex}
/* ---------- 主题：终末地 工业HUD ---------- */
body[data-theme=endfield]{--bg:#E9ECEE;--panel:#F8F9FA;--ink:#16181D;--muted:#5B6472;--line:#C6CCD2;
 --amber:#E8630A;--steel:#3D5A6C;--signal:var(--pc);--chip:#16181D;--chiptx:#F5F7F8}
body[data-theme=endfield] .deck{background:
 radial-gradient(1100px 500px at 85% -10%,rgba(62,90,108,.10),transparent 60%),
 repeating-linear-gradient(0deg,transparent 0 47px,rgba(22,24,29,.045) 47px 48px),
 repeating-linear-gradient(90deg,transparent 0 47px,rgba(22,24,29,.045) 47px 48px),var(--bg);
 color:var(--ink)}
body[data-theme=endfield] .contour{position:absolute;inset:0;opacity:.5;pointer-events:none}
body[data-theme=endfield] .hazbar{position:absolute;left:0;right:0;top:0;height:8px;
 background:repeating-linear-gradient(-45deg,var(--ink) 0 14px,var(--amber) 14px 28px)}
body[data-theme=endfield] .brk{border:2px solid var(--ink);position:relative;background:var(--panel)}
body[data-theme=endfield] .brk::before,body[data-theme=endfield] .brk::after{content:"";position:absolute;width:14px;height:14px;border:3px solid var(--amber)}
body[data-theme=endfield] .brk::before{left:-3px;top:-3px;border-right:none;border-bottom:none}
body[data-theme=endfield] .brk::after{right:-3px;bottom:-3px;border-left:none;border-top:none}
body[data-theme=endfield] .code{color:var(--amber);letter-spacing:.14em}
body[data-theme=endfield] .chip{background:var(--chip);color:var(--chiptx)}
body[data-theme=endfield] h1{font-size:56px;letter-spacing:.02em}
body[data-theme=endfield] h2{font-size:34px;border-left:10px solid var(--signal);padding-left:16px;margin-bottom:22px}
body[data-theme=endfield] .card{background:var(--panel);border:1.5px solid var(--line);border-top:4px solid var(--signal)}
body[data-theme=endfield] .tag{border:1.5px solid var(--ink);color:var(--ink);background:transparent}
/* ---------- 主题：绝区零 涩谷朋克 ---------- */
body[data-theme=zzz]{--bg:#0F1014;--panel:#17181F;--ink:#F5F7FA;--muted:#9BA1AC;--line:#2A2C36;
 --amber:#FFB020;--signal:var(--neon)}
body[data-theme=zzz] .deck{background:
 radial-gradient(900px 420px at 90% 0%,color-mix(in srgb,var(--neon) 12%,transparent),transparent 60%),
 repeating-linear-gradient(45deg,transparent 0 26px,rgba(245,247,250,.03) 26px 52px),var(--bg);color:var(--ink)}
body[data-theme=zzz] .dots{position:absolute;inset:auto 0 0 0;height:200px;pointer-events:none;opacity:.5;
 background-image:radial-gradient(color-mix(in srgb,var(--neon) 55%,transparent) 1.6px,transparent 1.6px);background-size:18px 18px;
 -webkit-mask-image:linear-gradient(180deg,transparent,#000 70%)}
body[data-theme=zzz] .hazbar{position:absolute;left:0;right:0;top:0;height:10px;background:repeating-linear-gradient(-45deg,var(--neon) 0 16px,#0F1014 16px 32px)}
body[data-theme=zzz] .brk{border:3px solid var(--ink);background:var(--panel);box-shadow:8px 8px 0 color-mix(in srgb,var(--neon) 65%,#000)}
body[data-theme=zzz] .code{color:var(--neon);letter-spacing:.22em;text-shadow:0 0 14px color-mix(in srgb,var(--neon) 55%,transparent)}
body[data-theme=zzz] .chip{background:var(--neon);color:#0F1014;transform:rotate(-1.2deg);font-weight:700}
body[data-theme=zzz] h1{font-size:58px;transform:rotate(-.6deg);text-shadow:4px 4px 0 color-mix(in srgb,var(--neon) 70%,#000)}
body[data-theme=zzz] h2{font-size:36px;margin-bottom:22px;display:inline-block;background:var(--ink);color:#0F1014;padding:2px 18px;transform:rotate(-.5deg)}
body[data-theme=zzz] .card{background:var(--panel);border:2px solid var(--line);border-left:6px solid var(--neon)}
body[data-theme=zzz] .tag{border:2px solid var(--neon);color:var(--neon);background:rgba(0,0,0,.25)}
/* ---------- 通用组件 ---------- */
.footer{position:absolute;left:72px;right:72px;bottom:20px;display:flex;justify-content:space-between;
 font-size:13px;color:var(--muted);border-top:1px solid var(--line);padding-top:8px}
.pager{position:absolute;right:24px;bottom:52px;display:flex;gap:8px;z-index:5}
.pager button{width:44px;height:36px;font-size:18px;cursor:pointer;border:2px solid var(--muted);
 background:transparent;color:inherit;border-radius:4px}
.pager button:hover{border-color:var(--signal);color:var(--signal)}
h1{font-weight:800;line-height:1.15}h2{font-weight:800}
.chip{display:inline-block;padding:4px 14px;font-size:14px;margin-right:10px;border-radius:3px}
.tag{display:inline-block;padding:2px 10px;font-size:13px;margin:2px 6px 2px 0;border-radius:3px}
.card{padding:18px 20px;border-radius:4px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.card h3{font-size:19px;margin-bottom:10px}
.card li{margin:6px 0 6px 18px;font-size:15.5px;line-height:1.55}
.md{font-size:16.5px;line-height:1.75}
.md p{margin:8px 0}.md li{margin:6px 0 6px 20px}
.md table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}
.md th,.md td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
.md th{background:color-mix(in srgb,var(--signal) 16%,transparent);font-weight:700}
.md strong{color:var(--signal)}
.quote{border-left:5px solid var(--signal);background:color-mix(in srgb,var(--signal) 8%,transparent);
 padding:12px 16px;margin:10px 0;font-size:15.5px;border-radius:0 4px 4px 0}
.kpi{font-size:15px}.kpi b{font-size:26px;color:var(--signal)}
.cover{justify-content:center;gap:26px}
.cover .sub{font-size:26px;color:var(--muted);font-weight:600}
.cover .meta{display:flex;gap:0;flex-wrap:wrap;margin-top:8px}
.pipeline{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;align-items:stretch}
.step{border:1.5px solid var(--line);border-radius:4px;padding:10px 8px;font-size:13.5px;line-height:1.4;
 background:color-mix(in srgb,var(--signal) 6%,transparent);min-height:118px}
.step b{display:block;color:var(--signal);margin-bottom:6px;font-size:14px}
.gate{color:var(--amber);font-weight:700}
.loop{color:var(--signal);font-weight:700}
/* 打印导出 PDF */
@media print{
 body{background:#fff;display:block;overflow:visible}
 .deck{width:1280px;height:auto;box-shadow:none}
 .slide{display:flex;position:relative;inset:auto;width:1280px;height:720px;page-break-after:always}
 .pager{display:none}
}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')];let cur=0;
const show=i=>{cur=Math.max(0,Math.min(slides.length-1,i));
 slides.forEach((s,k)=>s.classList.toggle('active',k===cur));
 document.getElementById('pg').textContent=String(cur+1).padStart(2,'0')+' / '+String(slides.length).padStart(2,'0');};
document.addEventListener('keydown',e=>{
 if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();show(cur+1)}
 if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(cur-1)}
 if(e.key==='Home')show(0); if(e.key==='End')show(slides.length-1);});
"""

CONTOUR = ('<svg class="contour" viewBox="0 0 1280 720" preserveAspectRatio="none">'
 '<g fill="none" stroke="#3D5A6C" stroke-opacity=".13">'
 '<path d="M-40 620 Q 300 480 640 560 T 1340 520"/><path d="M-40 660 Q 320 530 660 600 T 1340 570"/>'
 '<path d="M-40 700 Q 340 580 700 640 T 1340 620"/><path d="M900 -40 Q 1050 200 980 420 T 1120 760"/>'
 '<path d="M960 -40 Q 1120 210 1040 430 T 1180 760"/></g></svg>')

def esc(t): return H.escape(t, quote=False)

def inline(t):
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<span class="mono">\1</span>', t)
    return t

def md_html(text):
    lines = text.strip().splitlines(); out = []; i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells); i += 1
            head, body = rows[0], rows[2:]
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>')
            for r in body:
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            out.append('</tbody></table>'); continue
        if re.match(r'^\s*[-●]\s+', l):
            out.append('<ul>')
            while i < len(lines) and re.match(r'^\s*[-●]\s+', lines[i]):
                out.append(f'<li>{inline(re.sub(r"^\s*[-●]\s+","",lines[i]))}</li>'); i += 1
            out.append('</ul>'); continue
        if l.startswith('> '):
            out.append(f'<div class="quote">{inline(l[2:])}</div>'); i += 1; continue
        if l.strip():
            out.append(f'<p>{inline(l)}</p>')
        i += 1
    return '\n'.join(out)

def sections(md):
    parts = re.split(r'^## (\d+)\.', md, flags=re.M)
    secs = {}
    for j in range(1, len(parts), 2):
        secs[int(parts[j])] = parts[j+1].strip()
    return secs

STEPS = ['任务输入', '意图理解', '任务规划', '能力调用', '结果交付', '验证反馈', '安全边界']

def slide(no, total, prd_ref, inner, cls=''):
    return (f'<section class="slide {cls}" id="s{no}">{inner}'
            f'<div class="footer"><span>对应 PRD {prd_ref}</span><span class="mono" id="pg0"></span></div></section>')

def build(d):
    md = (PRD_DIR / d['prd']).read_text(encoding='utf-8')
    s = sections(md)
    pc = '#1F9D55' if d['proj'] == 'P2' else ('#2563EB' if d['proj'] == 'P3' else '#EA580C')
    neon = d.get('neon', pc)
    N = 12

    cover = (f'<div class="code mono">{d["code"]} // GOAI · 无界应用 · AI+工业制造</div>'
             f'<h1>{esc(d["title"])}</h1><div class="sub">{esc(d["sub"])}</div>'
             f'<div class="meta"><span class="chip">{d["proj"]} · {d["key"]}</span>'
             f'<span class="chip">作品层 {d["score"]} 分</span><span class="chip">{esc(d["rank"])}</span></div>'
             f'<div class="brk" style="padding:14px 20px;max-width:900px">锚定场景：{esc(d["anchor"])}</div>'
             f'<div style="margin-top:6px"><span class="tag">微循环自主</span><span class="tag">宏流程门禁</span>'
             f'<span class="tag">辅助建议系统 · 不替代专业决策</span></div>')

    def md_slide(content, ref, title):
        return f'<h2>{title}</h2><div class="md" style="overflow:auto">{md_html(content)}</div>'

    agents = s[4]
    pipe_steps = ''.join(f'<div class="step"><b>{i+1}. {t}</b></div>' for i, t in enumerate(STEPS))
    review = ('<h2>审核记录（供你填写）</h2><div class="grid3">'
              '<div class="card"><h3>✓ 亮点</h3><p style="color:var(--muted)">叙事/设计上最打动你的点…</p></div>'
              '<div class="card"><h3>△ 顾虑</h3><p style="color:var(--muted)">可信度/工作量/合规疑虑…</p></div>'
              '<div class="card"><h3>? 疑问</h3><p style="color:var(--muted)">待我补充说明的问题…</p></div></div>'
              '<div class="quote" style="margin-top:22px">审核结论：☐ 转正式 PPT　☐ 修改后再审　☐ 冻结为模块</div>')

    slides = [
        slide(1, N, '封面', cover, 'cover'),
        slide(2, N, '§1 场景锚定', md_slide(s[1], None, '01 场景锚定')),
        slide(3, N, '§3 用户与痛点', md_slide(s[3], None, '02 目标用户与痛点')),
        slide(4, N, '§2 产品定位', md_slide(s[2], None, '03 产品定位')),
        slide(5, N, '§4 Agent 编排', f'<h2>04 Agent 编排 · 微循环与宏门禁</h2><div class="md" style="overflow:auto">{md_html(agents)}</div>'),
        slide(6, N, '§5 闭环 7 步（手册 8.2）', f'<h2>05 任务闭环 7 步映射</h2><div class="pipeline">{pipe_steps}</div>'
              f'<div class="md" style="margin-top:18px">{md_html(s[5])}</div>'),
        slide(7, N, '§6 数据策略 ＋ §7 评测指标', f'<h2>06 数据策略 ＆ 评测指标</h2><div class="grid2">'
              f'<div class="card md" style="overflow:auto">{md_html(s[6])}</div>'
              f'<div class="card md" style="overflow:auto">{md_html(s[7])}</div></div>'),
        slide(8, N, '§8 安全合规', md_slide(s[8], None, '07 安全合规口径')),
        slide(9, N, '§9 三档排期', md_slide(s[9], None, '08 三档赛事排期')),
        slide(10, N, '§10 开源复用 ＋ §11 风险', f'<h2>09 开源复用物 ＆ 风险对策</h2><div class="grid2">'
              f'<div class="card md" style="overflow:auto">{md_html(s[10])}</div>'
              f'<div class="card md" style="overflow:auto">{md_html(s[11])}</div></div>'),
        slide(11, N, '§12 参赛简介', f'<h2>10 参赛简介（≤500 字 · 八要素）</h2>'
              f'<div class="brk" style="padding:26px 32px;overflow:auto;max-height:440px" class="md"><div class="md">{md_html(s[12])}</div></div>'),
        slide(12, N, '审核页', review),
    ]
    body_attr = f'data-theme="{d["theme"]}" style="--pc:{pc};--neon:{neon}"'
    deco = CONTOUR if d['theme'] == 'endfield' else '<div class="dots"></div>'
    doc = (f'<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{esc(d["title"])} · {d["key"]} 审核稿</title><style>{CSS}</style></head>'
           f'<body {body_attr}><div class="deck"><div class="hazbar"></div>{deco}'
           + '\n'.join(slides) +
           f'<div class="pager"><button onclick="show(cur-1)">◀</button><button onclick="show(cur+1)">▶</button></div>'
           f'<div class="footer" style="z-index:4"><span>{d["code"]} · {d["key"]} 审核稿</span>'
           f'<span class="mono" id="pg">01 / {N}</span></div></div>'
           f'<script>{JS}</script></body></html>')
    f = OUT / f'deck_{d["key"]}.html'
    f.write_text(doc, encoding='utf-8')
    return f

if __name__ == '__main__':
    for d in DECKS:
        f = build(d)
        n = f.read_text(encoding='utf-8').count('class="slide')
        print(f'OK {f.name}  slides={n}')
