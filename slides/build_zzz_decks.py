#!/usr/bin/env python3
"""绝区零风格 deck 生成器 v2 —— 以用户提供的 pitch.html 为美术参考。
核心：纸感+墨色+四色点缀、明暗页节奏、叙事式标题、eyebrow/footer-mark、
big-number、专属可视化组件、演讲者备注(N)、reveal 交错入场、进度条、clamp() 流式字号。
12 屏仍映射 PRD §1-§12 + 审核页，与终末地组保持横向可比。
用法：python3 slides/build_zzz_decks.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'slides'; OUT.mkdir(exist_ok=True)

# ---------- 主题：仅保留 M3C（其余三份已改由 build_endfield_decks.py 生成终末地版） ----------
DECKS = {
 'M3C': dict(acc='#d7ff3f', deep='#91bd00', code='ZZ-07', brand='SUPPLY SENTINEL DESK',
   name='供脉哨兵 SupplySentinel', sub='供应商风险哨兵 · 情报播报台 · 非官方审核稿',
   h1='断供从来不是突然的，<span class="accent">只是没人盯着信号</span>',
   lede='四源信号值守哨兵：交期、物流、退货、集中度，聚合成评分与分级预警，并把替代方案先备好——换不换供应商，人拍板。',
   marks=['四源值守','分级预警','备好再问']),
}

CSS = """
:root{--ink:#171816;--muted:#676a64;--line:#cfd3ca;--paper:#f4f5f1;--white:#fff;
 --acid:#d7ff3f;--acid-deep:#91bd00;--coral:#f05a40;--cyan:#1eaeb7;--yellow:#ffcc4a;
 --acc:#1eaeb7;--deep:#137378;
 --title-size:clamp(1.9rem,6.6vh,4.4rem);--h2-size:clamp(1.5rem,4.8vh,3.1rem);
 --h3-size:clamp(.95rem,2.6vh,1.45rem);--body-size:clamp(.8rem,2.05vh,1.22rem);
 --small-size:clamp(.66rem,1.6vh,.92rem);--pad-y:clamp(1rem,4.6vh,3.6rem);
 --pad-x:clamp(1rem,5%,5.2rem);--gap:clamp(.7rem,2.8vh,2rem);
 font-family:"Avenir Next","PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif}
*{box-sizing:border-box}html,body{height:100%;overflow-x:hidden}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth;background:var(--paper)}
body{margin:0;color:var(--ink);letter-spacing:0}
button{font:inherit}
.slide{width:100vw;height:100vh;height:100dvh;overflow:hidden;scroll-snap-align:start;
 display:flex;flex-direction:column;position:relative;isolation:isolate;border-bottom:1px solid var(--line);
 background-color:var(--paper);background-image:linear-gradient(rgba(23,24,22,.035) 1px,transparent 1px),
 linear-gradient(90deg,rgba(23,24,22,.028) 1px,transparent 1px);background-size:64px 64px}
.slide--dark{color:#f7f8f3;background-color:#1c1f1b;
 background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),
 linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px)}
.slide--white{background-color:var(--white)}
.slide-content{flex:1;width:min(100%,1600px);max-height:100%;margin:0 auto;overflow:hidden;
 padding:var(--pad-y) var(--pad-x);display:flex;flex-direction:column;justify-content:center;gap:var(--gap)}
.eyebrow{margin:0 0 .35rem;color:var(--muted);font-size:var(--small-size);font-weight:800;text-transform:uppercase;letter-spacing:.08em}
.slide--dark .eyebrow{color:#aeb4aa}
h1{max-width:16ch;margin:0;font-size:var(--title-size);line-height:1.05;font-weight:900}
h2{max-width:22ch;margin:0;font-size:var(--h2-size);line-height:1.1;font-weight:900}
h3{margin:0 0 .35rem;font-size:var(--h3-size);line-height:1.2}
p{margin:0;font-size:var(--body-size);line-height:1.55}
.lede{max-width:38ch;color:var(--muted);font-size:clamp(.95rem,2.5vh,1.45rem)}
.slide--dark .lede{color:#c7ccc2}
.accent{color:var(--acc)}
.slide--dark .accent{color:var(--acc)}
.slide--dark .lede .accent,.slide--dark h1 .accent{color:var(--acc)}
.brand{display:flex;align-items:center;gap:clamp(.65rem,1.5vh,1rem)}
.brand .mono-badge{display:grid;place-items:center;width:clamp(42px,8vh,64px);height:clamp(42px,8vh,64px);
 border:2px solid currentColor;border-radius:6px;font-weight:900;font-size:var(--small-size);text-align:center}
.brand strong{display:block;font-size:var(--body-size)}
.brand span{display:block;color:var(--muted);font-size:var(--small-size)}
.slide--dark .brand span{color:#aeb4aa}
.signal{position:absolute;right:var(--pad-x);bottom:var(--pad-y);width:clamp(110px,22vh,200px);aspect-ratio:1;
 border:clamp(12px,2.3vh,22px) solid var(--acc);border-right-color:var(--coral);transform:rotate(18deg);z-index:-1;opacity:.8}
.tag{display:inline-flex;align-items:center;min-height:1.7rem;padding:.2rem .6rem;border:1.5px solid currentColor;
 border-radius:4px;font-size:var(--small-size);font-weight:800;margin-right:.5rem}
.big-number{font-size:clamp(3.4rem,16vh,10rem);font-weight:900;line-height:.85;color:var(--acc);font-variant-numeric:tabular-nums}
.two-col{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);align-items:center;gap:clamp(1rem,5%,4.5rem)}
.three-col{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(.55rem,2%,1.2rem)}
.plain-panel{min-width:0;padding:clamp(.8rem,2.2vh,1.4rem);border:1px solid var(--line);border-top:5px solid var(--acc);background:rgba(255,255,255,.9)}
.plain-panel:nth-child(2){border-top-color:var(--yellow)}
.plain-panel:nth-child(3){border-top-color:var(--coral)}
.plain-panel p{color:var(--muted);font-size:var(--small-size)}
.plain-panel .score{font-size:clamp(1.6rem,5vh,2.8rem);font-weight:900;color:var(--deep)}
.timeline{position:relative;display:grid;grid-template-columns:repeat(7,1fr);gap:.3rem;padding-top:2.3rem}
.timeline::before{content:"";position:absolute;left:1%;right:1%;top:1.1rem;height:4px;background:var(--ink)}
.timeline-step{position:relative;padding-top:.4rem}
.timeline-step::before{content:"";position:absolute;top:calc(-1.5rem + 2px);left:0;width:.9rem;height:.9rem;
 border:4px solid var(--paper);border-radius:50%;background:var(--acc)}
.timeline-step:nth-child(6)::before{background:var(--coral)}
.timeline-step:nth-child(7)::before{background:var(--acid-deep)}
.timeline-step strong{display:block;font-size:var(--small-size)}
.timeline-step span{display:block;margin-top:.2rem;color:var(--muted);font-size:var(--small-size)}
.old-flow{display:grid;gap:clamp(.5rem,1.4vh,.9rem);counter-reset:of}
.old-flow div{counter-increment:of;display:grid;grid-template-columns:3rem 1fr;align-items:center;
 min-height:clamp(3rem,8.5vh,5rem);border-bottom:1px solid #464b43}
.old-flow--light div{border-bottom:1px solid var(--line)}
.old-flow div::before{content:"0" counter(of);color:var(--acc);font-size:var(--small-size);font-weight:900}
.old-flow strong{font-size:clamp(.95rem,2.8vh,1.55rem)}
.formula-row{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:clamp(.4rem,1.8vh,1rem);
 font-size:var(--body-size);font-weight:850}
.formula-row span{min-width:clamp(5rem,15vh,8.5rem);padding:clamp(.5rem,1.6vh,.9rem);border:1.5px solid var(--ink);
 background:var(--white);text-align:center}
.slide--dark .formula-row span{border-color:#f7f8f3;background:#252a24}
.formula-row em{font-style:normal;color:var(--acc);font-weight:900}
.chain-flow{display:grid;grid-template-columns:repeat(7,1fr);gap:clamp(.3rem,1vw,.8rem);align-items:stretch}
.chain-node{min-height:clamp(4.4rem,13vh,8rem);padding:clamp(.55rem,1.8vh,1rem);border:1px solid #596057;background:#252a24}
.chain-node strong{display:block;color:var(--acc);font-size:var(--small-size)}
.chain-node span{display:block;margin-top:.35rem;color:#b9c0b5;font-size:var(--small-size);line-height:1.4}
.evidence-scale{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(.55rem,2%,1.2rem)}
.evidence-item{padding:clamp(.8rem,2.2vh,1.4rem);border:1px solid var(--line);background:var(--white)}
.evidence-item b{display:block;font-size:clamp(1.8rem,6vh,3.8rem);line-height:1;color:var(--deep)}
.evidence-item:nth-child(2) b{color:#287352}
.evidence-item:nth-child(3) b{color:var(--coral)}
.evidence-item p{margin:.5rem 0 0;color:var(--muted);font-size:var(--small-size)}
.boundary{display:grid;grid-template-columns:auto 1fr;gap:.8rem;align-items:center;padding:clamp(.7rem,1.9vh,1.15rem);
 border-left:6px solid var(--coral);background:#fff5f2;margin-top:var(--gap)}
.boundary strong{font-size:var(--body-size)}
.boundary span{color:var(--muted);font-size:var(--small-size)}
.ask-list{display:grid;gap:clamp(.5rem,1.6vh,.9rem)}
.ask-item{display:grid;grid-template-columns:clamp(2.2rem,5.5vh,3.6rem) 1fr;align-items:center;
 min-height:clamp(3rem,9vh,5.2rem);border-bottom:1px solid var(--line)}
.slide--dark .ask-item{border-bottom-color:#464b43}
.ask-item b{color:var(--acc);font-size:var(--h3-size)}
.slide--dark .ask-item b{color:var(--acc)}
.ask-item strong{font-size:clamp(.95rem,2.8vh,1.55rem)}
.doc-panel{padding:clamp(1rem,3vh,1.8rem);border:2px solid var(--ink);background:var(--white);
 max-height:clamp(300px,58vh,460px);overflow:auto}
.doc-panel h3{color:var(--deep)}
.doc-panel p{font-size:var(--small-size);line-height:1.7;margin:.35rem 0}
.doc-panel b{color:var(--deep)}
.sticky{background:#fff9e6;border:1px solid #e5cf8a;box-shadow:3px 3px 0 rgba(152,96,16,.25);transform:rotate(-.6deg)}
.rgy{display:inline-block;min-width:1.4rem;text-align:center;padding:.1rem .45rem;border-radius:3px;color:#171816;font-weight:900;font-size:var(--small-size)}
.rgy--r{background:#ffd9d0}.rgy--y{background:#ffedbd}.rgy--g{background:#d9f2dc}
.footer-mark{position:absolute;left:var(--pad-x);bottom:clamp(.45rem,1.7vh,1rem);color:var(--muted);
 font-size:clamp(.58rem,1.3vh,.78rem);font-weight:700}
.slide--dark .footer-mark{color:#8e958b}
.present-nav{position:fixed;right:clamp(.6rem,2%,1.4rem);bottom:clamp(.6rem,2vh,1.2rem);z-index:50;display:flex;
 align-items:center;gap:.45rem;padding:.35rem;border:1px solid rgba(23,24,22,.2);border-radius:5px;background:rgba(255,255,255,.9);backdrop-filter:blur(10px)}
.present-nav button{width:2rem;height:2rem;padding:0;border:0;background:transparent;color:var(--ink);cursor:pointer;font-size:1.05rem}
.slide-count{min-width:3.8rem;text-align:center;font-size:.72rem;font-weight:800}
.progress{position:fixed;inset:0 0 auto;z-index:60;height:4px;background:rgba(23,24,22,.12)}
.progress span{display:block;width:10%;height:100%;background:var(--coral);transition:width 220ms ease}
.speaker-notes{display:none;position:absolute;left:var(--pad-x);right:var(--pad-x);bottom:clamp(1.6rem,4vh,2.8rem);
 z-index:30;max-height:30vh;overflow:auto;padding:.8rem 1rem;border:1px solid var(--ink);background:rgba(255,255,255,.96);
 color:var(--ink);font-size:clamp(.66rem,1.55vh,.9rem);line-height:1.55}
body.show-notes .slide.is-active .speaker-notes{display:block}
[data-reveal]{opacity:0;transform:translateY(18px);transition:opacity .42s ease,transform .42s ease}
.is-active [data-reveal]{opacity:1;transform:translateY(0)}
.is-active [data-reveal]:nth-child(2){transition-delay:80ms}
.is-active [data-reveal]:nth-child(3){transition-delay:150ms}
.is-active [data-reveal]:nth-child(4){transition-delay:220ms}
@media (max-width:760px){.two-col,.three-col,.evidence-scale{grid-template-columns:1fr}
 .timeline{grid-template-columns:1fr;padding-top:0}.timeline::before,.timeline-step::before{display:none}
 .chain-flow{grid-template-columns:1fr}.signal{opacity:.5}}
@media (prefers-reduced-motion:reduce){*[data-reveal]{opacity:1;transform:none;transition:none}}
@media print{html,body{overflow:visible;height:auto}
 .slide{page-break-after:always;height:100vh}.present-nav,.progress{display:none}
 [data-reveal]{opacity:1;transform:none}}
"""

JS = """
'use strict';
class PC{constructor(){this.slides=[...document.querySelectorAll('.slide')];this.index=0;this.lock=false;
 this.p=document.querySelector('#pf');this.c=document.querySelector('#sc');
 this.ob=new IntersectionObserver(e=>this.on(e),{threshold:.62})}
 start(){this.slides.forEach(s=>this.ob.observe(s));
  document.querySelector('#pv').addEventListener('click',()=>this.go(this.index-1));
  document.querySelector('#nx').addEventListener('click',()=>this.go(this.index+1));
  document.addEventListener('keydown',e=>this.k(e));
  document.addEventListener('wheel',e=>this.w(e),{passive:true});
  this.go(this.index,false)}
 on(es){const v=es.find(x=>x.isIntersecting);if(!v)return;this.index=this.slides.indexOf(v.target);
  this.slides.forEach((s,i)=>s.classList.toggle('is-active',i===this.index));this.u()}
 k(e){const n=e.key.toLowerCase();
  if(['arrowright','arrowdown','pagedown',' '].includes(n)){e.preventDefault();this.go(this.index+1)}
  else if(['arrowleft','arrowup','pageup'].includes(n)){e.preventDefault();this.go(this.index-1)}
  else if(e.key==='Home')this.go(0);else if(e.key==='End')this.go(this.slides.length-1);
  else if(n==='n')document.body.classList.toggle('show-notes')}
 w(e){if(this.lock||Math.abs(e.deltaY)<18)return;this.lock=true;
  this.go(this.index+(e.deltaY>0?1:-1));setTimeout(()=>this.lock=false,520)}
 go(i,s=true){this.index=Math.max(0,Math.min(this.slides.length-1,i));
  this.slides[this.index].scrollIntoView({behavior:s?'smooth':'auto',block:'start'});this.u()}
 u(){this.c.textContent=`${this.index+1} / ${this.slides.length}`;
  this.p.style.width=`${((this.index+1)/this.slides.length)*100}%`;
  history.replaceState(null,'',`#s${this.index+1}`)}}
const c=new PC(),h=Number(location.hash.replace('#s',''));
if(Number.isInteger(h)&&h>=1)c.index=h-1;c.start();
"""

MODES = ['dark','paper','white','paper','white','dark','white','paper','white','paper','white','dark']

def slide(i, mode, body, mark, notes=''):
    return (f'<section class="slide slide--{mode}" id="s{i}" aria-label="第{i}屏">'
            f'<div class="slide-content">{body}</div>'
            f'<aside class="speaker-notes">{notes}</aside>'
            f'<span class="footer-mark">{i:02d} / 12 · {mark}</span></section>')

def brand(t):
    return ('<div class="brand" data-reveal><div class="mono-badge">' + t['code'] + '</div>'
            f'<div><strong>{t["brand"]}</strong><span>{t["sub"]}</span></div></div>')

def tags(marks):
    return ''.join(f'<span class="tag">{m}</span>' for m in marks)

def cover(t, meta):
    return (brand(t) +
      f'<div data-reveal><p class="eyebrow">GOAI 无界应用 · AI+工业制造 // {t["code"]}</p><h1>{t["h1"]}</h1></div>'
      f'<p class="lede" data-reveal>{t["lede"]}</p>'
      f'<div data-reveal style="display:flex;flex-wrap:wrap;align-items:center">{tags(t["marks"])}'
      f'<span class="tag">作品层 {meta["score"]} · {meta["tier"]}</span><span class="tag">{meta["anchor"]}</span></div>')

def anchor3(rows, pick, reason):
    cols = ''.join(
      f'<section class="plain-panel{" sticky" if r.get("sticky") else ""}">'
      f'<h3>{r["name"]}</h3><div class="score">{r["score"]}</div><p>{r["desc"]}</p></section>' for r in rows)
    return (f'<div data-reveal><p class="eyebrow">SCENE ANCHOR · PRD §1</p>'
            f'<h2>三个候选场景，选{pick}</h2></div>'
            f'<div class="three-col" data-reveal>{cols}</div>'
            f'<p class="lede" data-reveal style="margin-top:.4rem">{reason}</p>')

def pain(big, unit, h2, flow, note):
    items = ''.join(f'<div><strong>{f}</strong></div>' for f in flow)
    return (f'<div class="two-col"><div data-reveal><p class="eyebrow">THE PAIN · PRD §3</p>'
            f'<div class="big-number">{big}<span style="font-size:.35em">{unit}</span></div>'
            f'<h2>{h2}</h2><p class="lede">{note}</p></div>'
            f'<div class="old-flow old-flow--light" data-reveal>{items}</div></div>')

def formula(parts, lede):
    row = ''.join(f'<span>{p}</span>' if not p.startswith('→') else f'<em>{p}</em>' for p in parts)
    return (f'<div data-reveal><p class="eyebrow">THE OFFER · PRD §2</p>'
            f'<h2>把流程交给系统，把决定留给人</h2></div>'
            f'<div class="formula-row" data-reveal style="margin:clamp(.6rem,3vh,1.6rem) 0">{row}</div>'
            f'<p class="lede" data-reveal>{lede}</p>')

def agents(cards, loop_line, gate_line):
    cols = ''.join(
      f'<section class="plain-panel{" sticky" if c.get("sticky") else ""}"><h3>{c["n"]}</h3><p>{c["d"]}</p></section>'
      for c in cards)
    return (f'<div data-reveal><p class="eyebrow">AGENT CREW · PRD §4</p>'
            f'<h2>微循环自主，宏流程门禁</h2></div>'
            f'<div class="three-col" data-reveal>{cols}</div>'
            f'<div class="boundary" data-reveal><strong>{loop_line}</strong><span>{gate_line}</span></div>')

def steps7(names, notes):
    nodes = ''.join(f'<div class="chain-node"><strong>{i+1} {n}</strong><span>{d}</span></div>'
                    for i, (n, d) in enumerate(names))
    return (f'<div data-reveal><p class="eyebrow">CLOSED LOOP · PRD §5（手册 8.2）</p>'
            f'<h2 style="color:#f7f8f3">一条链走完，七步都有落点</h2></div>'
            f'<div class="chain-flow" data-reveal>{nodes}</div>'
            f'<p class="lede" data-reveal style="color:#c7ccc2">{notes}</p>')

def evidence(items, lede):
    cols = ''.join(f'<section class="evidence-item"><b>{e[0]}</b><p>{e[1]}</p></section>' for e in items)
    return (f'<div data-reveal><p class="eyebrow">EVIDENCE & METRICS · PRD §6/§7</p>'
            f'<h2>知道什么，和模拟什么，分开写</h2></div>'
            f'<div class="evidence-scale" data-reveal>{cols}</div>'
            f'<p class="lede" data-reveal style="margin-top:.4rem">{lede}</p>')

def boundary_slide(title, rows, lede):
    bs = ''.join(f'<div class="boundary" data-reveal><strong>{a}</strong><span>{b}</span></div>' for a, b in rows)
    return (f'<div data-reveal><p class="eyebrow">SAFETY BOUNDARY · PRD §8</p><h2>{title}</h2></div>'
            f'{bs}<p class="lede" data-reveal>{lede}</p>')

def timeline3(rows):
    steps = ''.join(f'<div class="timeline-step"><strong>{a}</strong><span>{b}</span></div>'
                    f'<div class="timeline-step"><strong>{c}</strong><span>{d}</span></div>'
                    for a, b, c, d in rows)
    return (f'<div data-reveal><p class="eyebrow">ROADMAP · PRD §9</p>'
            f'<h2>三档排期：材料、可运行、现场</h2></div>'
            f'<div class="timeline" data-reveal>{steps}</div>')

def opensource(rows, risk):
    cols = ''.join(f'<section class="plain-panel{" sticky" if r.get("sticky") else ""}"><h3>{r["n"]}</h3><p>{r["d"]}</p></section>' for r in rows)
    return (f'<div data-reveal><p class="eyebrow">OPEN SOURCE & RISKS · PRD §10/§11</p>'
            f'<h2>留下的不只是演示，是可复用的件</h2></div>'
            f'<div class="three-col" data-reveal>{cols}</div>'
            f'<div class="boundary" data-reveal><strong>最大风险与对策</strong><span>{risk}</span></div>')

def intro8(paras):
    body = ''.join(f'<p><b>{k}</b>{v}</p>' for k, v in paras)
    return (f'<div data-reveal><p class="eyebrow">500-WORD BRIEF · PRD §12</p>'
            f'<h2>参赛简介 · 八要素（≤500 字）</h2></div>'
            f'<div class="doc-panel" data-reveal>{body}</div>')

def review(asks):
    items = ''.join(f'<div class="ask-item"><b>{i+1:02d}</b><strong>{a}</strong></div>' for i, a in enumerate(asks))
    return (f'<div class="two-col"><div data-reveal><p class="eyebrow">REVIEW · 你的审核位</p>'
            f'<p style="font-size:var(--h2-size);font-weight:900;line-height:1.1;max-width:14ch">'
            f'看完这一份，<span class="accent">留下三句话</span></p></div>'
            f'<div class="ask-list" data-reveal>{items}</div></div>'
            f'<p class="lede" data-reveal style="color:#c7ccc2">审核结论：☐ 转正式 PPT　☐ 修改后再审　☐ 冻结为模块　（按 N 看演讲备注）</p>')

S7 = [('任务输入','告警/工单/缺口流入'),('意图理解','分类·定级·影响面'),('任务规划','追溯/求解/起草计划'),
      ('能力调用','库·API·求解器'),('结果交付','证据链/动作包'),('验证反馈','命中率·回放·人确认'),('安全边界','终点决策留给人')]

META = {
 'M1A': dict(score='86.6 分', tier='第二梯队 · 引擎模块', anchor='S19 半导体/精密机加'),
 'M3C': dict(score='84.3 分', tier='模块库', anchor='S13 机械/汽配多源监测'),
 'M3B': dict(score='77.8 分', tier='内置模块', anchor='S16 机械/汽配周度请购'),
 'M1E': dict(score='85.5 分', tier='收官模块', anchor='S25 机加车间案例库'),
}

CONTENT = {
'M3C': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S13 机械/汽配多源监测', score='90.5 ✓', desc='与计划、请购同厂闭环；四源值守 loop 完整'),
   dict(name='S15 芯片供应风险', score='85.8', desc='公开交期指数稀缺，数据源成问题'),
   dict(name='S14 原材料价格波动', score='84.8', desc='叙事偏金融研判，容易被归入 AI+金融的观感')],
   pick='闭环里最顺的一个', reason='S13 与齐途（M3-A）、齐购（M3-B）同一条数据主线：风险哨兵发现的缺口，直接变成计划重算和请购动作。'),
 dict(f='pain', big='逾期后', unit=' 才发现', h2='断供的真相', flow=[
   '交期延误散落在邮件和聊天记录里','单一供应商依赖，集中度无人量化','应急切换无预案、无影响分析'],
   note='预埋剧本口径：风险平均在交付逾期后才暴露，预警提前量 ≥5 天就是价值。'),
 dict(f='formula', parts=['四源信号','+','评分分级','→','预警 + 备选包'],
   lede='切换供应商、催单、索赔是采购的决策；哨兵只负责在正确的时间，把正确的影响分析放到桌上。'),
 dict(f='agents', cards=[
   dict(n='信号聚合 Agent', d='交期延误 × 物流事件 × 质检退货 × 订单集中度，标准化去重'),
   dict(n='风险评估 Agent', d='规则 + 时序综合评分，R/G/Y 分级与趋势、归因明细'),
   dict(n='备选准备 Agent', d='替代供应商候选 + 切换影响分析（在途订单/模具/认证周期/成本）')],
   loop_line='微循环：事件流入 → 评分 → 分级预警 → 备选包生成，全程自主值守',
   gate_line='宏门禁：切换供应商 / 催单 / 索赔 / 高成本预案 = 采购与经理拍板'),
 dict(f='steps7', names=S7, notes='把 S7 换成供应域落点：事件流输入、供应商与物料判定、排查计划、采购库存物流调用、分级预警+备选包、剧本回放、商务决策人工。'),
 dict(f='evidence', items=[
   ('3/3','预埋风险剧本全检出（交付滑坡/物流中断/集中度超标）'),
   ('≥5 天','较"逾期才发现"基线的预警提前量（模拟口径）'),
   ('≤1 次','每模拟周误报上限；备选包字段完整率 100%')],
   lede='评分主观性是这套系统最大的质疑点——所以归因明细面板与剧本回放，都是一级公民。'),
 dict(f='boundary', title='它不替你做任何商务决定', rows=[
   ('不自动下达任何采购变更', '切换、催单、索赔全部人工确认（手册 9.3）'),
   ('模拟数据无真实供应商', '信号流与供应商库全模拟，逻辑披露（FAQ Q7）')],
   lede='哨兵的价值是"备好再问"，不是"替你签字"。'),
 dict(f='timeline3', rows=[('初赛 8.16','P3 叙事一页','复赛 9.3','哨兵面板可运行（回放）'),('决赛 9.22','实时注入事件','联动','风险→缺口→请购 全链')]),
 dict(f='opensource', rows=[
   dict(n='风险信号 schema', d='四源事件的标准化定义'),
   dict(n='事件流模拟器', d='含三组风险剧本，可复算'),
   dict(n='评分规则模板', d='规则可解释，归因面板配套')],
   risk='信号模拟失真 → 剧本化 + 字段说明；评分黑箱 → 规则可解释 + 归因面板。'),
 dict(f='intro8', paras=[
   ('项目名称：','供脉哨兵 SupplySentinel——供应商多源风险预警智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','机械/汽配厂采购员与供应商质量工程师'),('核心问题：','供应商突发断供发现晚、应急无预案、订单集中度风险无人盯'),
   ('解决方案：','三 Agent 值守：信号聚合标准化四源事件，风险评估输出分级与归因，备选准备生成替代候选与切换影响分析'),
   ('创新点：','微循环自主（聚合-评分-备包）、宏流程门禁（切换/催单/索赔由人拍板）；与齐套计划、缺料请购构成同厂闭环'),
   ('开放/复用价值：','开源风险信号 schema、事件模拟器与评分模板'),('当前进展：','方案设计完成，原型开发中，提交时附回放演示')]),
 dict(f='review', asks=['情报台气质是否成立？','四源信号的可信表达够不够？','作为 M3-A 的联动模块，独立叙事是否站得住？']),
],
}

BUILDERS = dict(cover=cover, anchor3=anchor3, pain=pain, formula=formula, agents=agents,
                steps7=steps7, evidence=evidence, boundary=boundary_slide, timeline3=timeline3,
                opensource=opensource, intro8=intro8, review=review)

def build(key, t):
    slides = []
    for i, spec in enumerate(CONTENT[key], 1):
        f = spec.pop('f')
        if f == 'cover':
            html_ = cover(t, META[key]); mark = '微循环自主 · 宏流程门禁'
            notes = f'这是{t["name"]}的审核稿。按 N 可以看每屏的演讲备注。'
        else:
            html_ = BUILDERS[f](**spec)
            mark = {'anchor3':'场景为什么这么选','pain':'痛点的量化假设','formula':'定位一句话',
                    'agents':'Agent 分工与门禁','steps7':'闭环七步（手册 8.2）','evidence':'证据与指标',
                    'boundary':'安全合规口径','timeline3':'三档排期','opensource':'开源物与风险',
                    'intro8':'参赛简介','review':'你的审核位'}[f]
            notes = ''
        slides.append(slide(i, MODES[i-1], html_, mark, notes))
    doc = ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{t["name"]} · {key} 审核稿</title>'
           f'<style>{CSS}</style></head><body style="--acc:{t["acc"]};--deep:{t["deep"]}">'
           '<div class="progress" aria-hidden="true"><span id="pf"></span></div><main id="deck">'
           + '\n'.join(slides) + '</main>'
           '<nav class="present-nav" aria-label="演示导航"><button id="pv" aria-label="上一页">←</button>'
           '<span class="slide-count" id="sc">1 / 12</span><button id="nx" aria-label="下一页">→</button></nav>'
           f'<script>{JS}</script></body></html>')
    (OUT / f'deck_{key}.html').write_text(doc, encoding='utf-8')

if __name__ == '__main__':
    for k, t in DECKS.items():
        build(k, t)
        n = (OUT / f'deck_{k}.html').read_text(encoding='utf-8').count('class="slide')
        print(f'OK deck_{k}.html slides={n}')
