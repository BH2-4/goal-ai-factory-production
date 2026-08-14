#!/usr/bin/env python3
"""终末地工业风 deck 生成器（编辑部级）—— M1A / M3B / M1E 重制用。
美术语言：冷白工业纸面 + 碳黑 + 琥珀警示 + 钢青；切角面板、HUD 角括号、等高线、
黄黑警示条、mono 编号标注（ENF-XX / AGT-01）、方形里程碑、蓝图文档卡。
交互骨架与绝区零版同源（滚动吸附/N 键备注/进度条/reveal/打印）。
用法：python3 slides/build_endfield_decks.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'slides'; OUT.mkdir(exist_ok=True)

DECKS = {
 'M1A': dict(sig='#B4540A', code='ENF-06', brand='ROOTCAUSE FORENSICS UNIT',
   name='质源侦探 RootCause Cop', sub='质量异常根因链 · 工业取证台 · 非官方审核稿',
   h1='批次异常的真相，<span class="accent">不该靠翻五个系统</span>',
   lede='SPC 告警进入取证台：四源数据自动对齐，假设逐条验证成证据链，8D 初稿自动成文——结论可复核，放行归人。',
   marks=['证据链可复核','四源对齐','放行人拍板']),
 'M3B': dict(sig='#2B5C8A', code='ENF-08', brand='PROCUREMENT DISPATCH DESK',
   name='齐购 QiBuy', sub='缺料请购联动 · 采购调度台 · 非官方审核稿',
   h1='从缺料到请购单，<span class="accent">不该花掉一下午</span>',
   lede='调度台自动接收缺口、分级、起草请购包与比价矩阵，并持续跟踪交期——起草归系统，签字归采购。',
   marks=['缺口自动分级','比价矩阵','采购签字']),
 'M1E': dict(sig='#8A5A0A', code='ENF-09', brand='SHOP FLOOR ARCHIVE',
   name='车间记忆 ShopMemory', sub='沉淀飞轮 · 车间档案室 · 非官方审核稿',
   h1='老师傅走了，<span class="accent">经验不该跟着走</span>',
   lede='每一次异常关闭自动归档成结构化案例；复发早期自动调出历史预案——归档是系统的工序，不是人的负担。',
   marks=['自动归档','复发预警','SOP 人工审定']),
}

CSS = """
:root{--ink:#16181D;--muted:#5B6472;--line:#C9CFD5;--paper:#EDEFF1;--white:#FAFBFC;
 --amber:#E8630A;--steel:#3D5A6C;--sig:#B4540A;
 --mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
 --title-size:clamp(1.9rem,6.4vh,4.2rem);--h2-size:clamp(1.45rem,4.6vh,2.9rem);
 --h3-size:clamp(.95rem,2.6vh,1.4rem);--body-size:clamp(.8rem,2.05vh,1.2rem);
 --small-size:clamp(.66rem,1.6vh,.9rem);--pad-y:clamp(1rem,4.6vh,3.6rem);
 --pad-x:clamp(1rem,5%,5.2rem);--gap:clamp(.7rem,2.8vh,2rem);
 font-family:"Avenir Next","PingFang SC","Noto Sans CJK SC","Microsoft YaHei",sans-serif}
*{box-sizing:border-box}html,body{height:100%;overflow-x:hidden}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth;background:var(--paper)}
body{margin:0;color:var(--ink)}
.slide{width:100vw;height:100vh;height:100dvh;overflow:hidden;scroll-snap-align:start;display:flex;
 flex-direction:column;position:relative;isolation:isolate;border-bottom:1px solid var(--line);
 background-color:var(--paper);background-image:linear-gradient(rgba(22,24,29,.03) 1px,transparent 1px),
 linear-gradient(90deg,rgba(22,24,29,.03) 1px,transparent 1px);background-size:64px 64px}
.slide--white{background-color:var(--white)}
.slide--dark{color:#E8EBEE;background-color:#14171B;border-bottom:1px solid #2A2F36;
 background-image:linear-gradient(rgba(232,235,238,.05) 1px,transparent 1px),
 linear-gradient(90deg,rgba(232,235,238,.05) 1px,transparent 1px);background-size:64px 64px}
.hazbar{position:absolute;left:0;right:0;top:0;height:8px;
 background:repeating-linear-gradient(-45deg,var(--ink) 0 12px,var(--amber) 12px 24px)}
.slide--dark .hazbar{background:repeating-linear-gradient(-45deg,#2A2F36 0 12px,var(--amber) 12px 24px)}
.contour{position:absolute;inset:0;opacity:.5;pointer-events:none}
.slide-content{flex:1;width:min(100%,1600px);max-height:100%;margin:0 auto;overflow:hidden;
 padding:calc(var(--pad-y) + 14px) var(--pad-x) var(--pad-y);display:flex;flex-direction:column;
 justify-content:center;gap:var(--gap)}
.mono{font-family:var(--mono)}
.eyebrow{margin:0 0 .4rem;font-family:var(--mono);color:var(--steel);font-size:var(--small-size);
 font-weight:700;text-transform:uppercase;letter-spacing:.14em}
.slide--dark .eyebrow{color:#8FA6B5}
h1{max-width:17ch;margin:0;font-size:var(--title-size);line-height:1.06;font-weight:800}
h2{max-width:22ch;margin:0;font-size:var(--h2-size);line-height:1.12;font-weight:800;
 border-left:8px solid var(--sig);padding-left:14px}
.slide--dark h2{border-left-color:var(--amber);color:#F2F4F6}
h3{margin:0 0 .35rem;font-size:var(--h3-size);line-height:1.2}
p{margin:0;font-size:var(--body-size);line-height:1.55}
.lede{max-width:40ch;color:var(--muted);font-size:clamp(.95rem,2.4vh,1.4rem)}
.slide--dark .lede{color:#A8B2BC}
.accent{color:var(--sig)}
.slide--dark .accent{color:var(--amber)}
.brand{display:flex;align-items:center;gap:clamp(.65rem,1.5vh,1rem)}
.brand .idplate{display:grid;place-items:center;width:clamp(44px,8vh,64px);height:clamp(44px,8vh,64px);
 border:2px solid var(--ink);position:relative;font-family:var(--mono);font-weight:800;font-size:var(--small-size);
 clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,0 100%);background:var(--white)}
.brand .idplate::after{content:"";position:absolute;right:3px;top:3px;width:8px;height:8px;background:var(--amber)}
.slide--dark .idplate{background:#1B2026;border-color:#E8EBEE}
.brand strong{display:block;font-size:var(--body-size);font-family:var(--mono);letter-spacing:.06em}
.brand span{display:block;color:var(--muted);font-size:var(--small-size)}
.slide--dark .brand span{color:#8FA6B5}
.reticle{position:absolute;right:var(--pad-x);bottom:var(--pad-y);width:clamp(120px,24vh,220px);aspect-ratio:1;
 z-index:-1;opacity:.9}
.reticle::before,.reticle::after{content:"";position:absolute;inset:0;border:2px solid var(--sig)}
.reticle::before{clip-path:polygon(0 0,30% 0,30% 6%,6% 6%,6% 30%,0 30%,0 70%,6% 70%,6% 94%,30% 94%,30% 100%,0 100%,70% 100%,70% 94%,94% 94%,94% 70%,100% 70%,100% 30%,94% 30%,94% 6%,70% 6%,70% 0)}
.reticle::after{inset:22%;border:1px solid var(--amber);transform:rotate(45deg)}
.tag{display:inline-flex;align-items:center;min-height:1.7rem;padding:.2rem .6rem;border:1.5px solid var(--ink);
 border-radius:2px;font-size:var(--small-size);font-weight:800;margin-right:.5rem;background:var(--white)}
.slide--dark .tag{border-color:#E8EBEE;background:#1B2026}
.big-number{font-family:var(--mono);font-size:clamp(3.2rem,15vh,9.5rem);font-weight:800;line-height:.88;
 color:var(--amber);font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.two-col{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);align-items:center;gap:clamp(1rem,5%,4.5rem)}
.three-col{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(.55rem,2%,1.2rem)}
.panel{min-width:0;padding:clamp(.8rem,2.2vh,1.35rem);border:1.5px solid var(--line);background:var(--white);
 border-top:3px solid var(--sig);clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,0 100%);position:relative}
.panel .uid{position:absolute;top:6px;right:18px;font-family:var(--mono);font-size:.6rem;color:var(--muted);letter-spacing:.1em}
.panel:nth-child(2){border-top-color:var(--steel)}
.panel:nth-child(3){border-top-color:var(--amber)}
.panel p{color:var(--muted);font-size:var(--small-size)}
.panel .score{font-family:var(--mono);font-size:clamp(1.5rem,4.8vh,2.6rem);font-weight:800;color:var(--sig)}
.ops{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:clamp(.4rem,1.8vh,1rem);margin:clamp(.6rem,3vh,1.5rem) 0}
.ops .op{min-width:clamp(5rem,15vh,8.5rem);padding:clamp(.5rem,1.6vh,.9rem);border:1.5px solid var(--ink);
 background:var(--white);text-align:center;font-weight:800;font-size:var(--body-size);
 clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,0 100%)}
.slide--dark .ops .op{border-color:#E8EBEE;background:#1B2026;color:#E8EBEE}
.ops em{font-style:normal;font-family:var(--mono);color:var(--amber);font-weight:800;font-size:1.3em}
.chain{display:grid;grid-template-columns:repeat(7,1fr);gap:clamp(.3rem,1vw,.8rem)}
.node{min-height:clamp(4.4rem,13vh,8rem);padding:clamp(.55rem,1.8vh,1rem);border:1px solid #3D5A6C;background:#1B2026;
 clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,0 100%)}
.node b{display:block;font-family:var(--mono);color:var(--amber);font-size:var(--small-size)}
.node span{display:block;margin-top:.35rem;color:#A8B2BC;font-size:var(--small-size);line-height:1.4}
.flow{display:grid;gap:clamp(.5rem,1.4vh,.9rem);counter-reset:fl}
.flow div{counter-increment:fl;display:grid;grid-template-columns:3.2rem 1fr;align-items:center;
 min-height:clamp(3rem,8.5vh,5rem);border-bottom:1px solid var(--line)}
.flow div::before{content:counter(fl,decimal-leading-zero);font-family:var(--mono);color:var(--amber);
 font-size:var(--small-size);font-weight:800}
.flow strong{font-size:clamp(.95rem,2.8vh,1.5rem)}
.gauge{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(.55rem,2%,1.2rem)}
.gauge .g{padding:clamp(.8rem,2.2vh,1.35rem);border:1.5px solid var(--line);background:var(--white);
 border-top:3px solid var(--sig);clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,0 100%)}
.gauge .g b{display:block;font-family:var(--mono);font-size:clamp(1.7rem,5.6vh,3.4rem);line-height:1;color:var(--sig)}
.gauge .g:nth-child(2) b{color:var(--steel)}
.gauge .g:nth-child(3) b{color:#2F7D4F}
.gauge .g p{margin:.5rem 0 0;color:var(--muted);font-size:var(--small-size)}
.boundary{display:grid;grid-template-columns:auto 1fr;gap:.8rem;align-items:center;padding:clamp(.7rem,1.9vh,1.1rem);
 border-left:6px solid var(--amber);background:#FDF3EC;margin-top:var(--gap)}
.boundary strong{font-size:var(--body-size)}
.boundary strong::before{content:"⚠ ";color:var(--amber)}
.boundary span{color:var(--muted);font-size:var(--small-size)}
.milestones{position:relative;display:grid;grid-template-columns:repeat(6,1fr);gap:.3rem;padding-top:2.2rem}
.milestones::before{content:"";position:absolute;left:1%;right:1%;top:1rem;height:3px;background:var(--ink)}
.ms{position:relative;padding-top:.4rem}
.ms::before{content:"";position:absolute;top:-1.4rem;left:0;width:.85rem;height:.85rem;background:var(--sig);
 border:3px solid var(--paper);border-radius:2px}
.ms:nth-child(4)::before,.ms:nth-child(5)::before{background:var(--amber)}
.ms:nth-child(6)::before{background:var(--steel)}
.ms strong{display:block;font-size:var(--small-size)}
.ms span{display:block;margin-top:.2rem;color:var(--muted);font-size:var(--small-size)}
.doc{padding:clamp(1rem,3vh,1.7rem);border:2px solid var(--ink);background:var(--white);
 max-height:clamp(300px,56vh,450px);overflow:auto;position:relative;
 clip-path:polygon(0 0,calc(100% - 18px) 0,100% 18px,100% 100%,0 100%)}
.doc::before{content:"BLUEPRINT · PRD §12";position:absolute;top:8px;right:22px;font-family:var(--mono);
 font-size:.6rem;color:var(--muted);letter-spacing:.12em}
.doc h3{color:var(--sig)}
.doc p{font-size:var(--small-size);line-height:1.7;margin:.35rem 0}
.doc b{color:var(--sig)}
.checklist{display:grid;gap:clamp(.5rem,1.6vh,.9rem)}
.chk{display:grid;grid-template-columns:clamp(2.2rem,5.5vh,3.6rem) 1fr;align-items:center;
 min-height:clamp(3rem,9vh,5.2rem);border-bottom:1px solid #2A2F36}
.chk b{font-family:var(--mono);color:var(--amber);font-size:var(--h3-size)}
.chk strong{font-size:clamp(.95rem,2.8vh,1.5rem)}
.footer-mark{position:absolute;left:var(--pad-x);bottom:clamp(.45rem,1.7vh,1rem);font-family:var(--mono);
 color:var(--muted);font-size:clamp(.58rem,1.3vh,.76rem);font-weight:700;letter-spacing:.06em}
.slide--dark .footer-mark{color:#77828D}
.present-nav{position:fixed;right:clamp(.6rem,2%,1.4rem);bottom:clamp(.6rem,2vh,1.2rem);z-index:50;display:flex;
 align-items:center;gap:.45rem;padding:.35rem;border:1.5px solid var(--ink);border-radius:3px;background:rgba(250,251,252,.94)}
.present-nav button{width:2rem;height:2rem;padding:0;border:0;background:transparent;color:var(--ink);cursor:pointer;font-size:1.05rem}
.slide-count{min-width:3.8rem;text-align:center;font-size:.72rem;font-weight:800;font-family:var(--mono)}
.progress{position:fixed;inset:0 0 auto;z-index:60;height:4px;background:rgba(22,24,29,.12)}
.progress span{display:block;width:10%;height:100%;background:var(--amber);transition:width 220ms ease}
.speaker-notes{display:none;position:absolute;left:var(--pad-x);right:var(--pad-x);bottom:clamp(1.6rem,4vh,2.8rem);
 z-index:30;max-height:30vh;overflow:auto;padding:.8rem 1rem;border:1.5px solid var(--ink);background:rgba(250,251,252,.97);
 color:var(--ink);font-size:clamp(.66rem,1.55vh,.9rem);line-height:1.55}
body.show-notes .slide.is-active .speaker-notes{display:block}
[data-reveal]{opacity:0;transform:translateY(16px);transition:opacity .4s ease,transform .4s ease}
.is-active [data-reveal]{opacity:1;transform:translateY(0)}
.is-active [data-reveal]:nth-child(2){transition-delay:80ms}
.is-active [data-reveal]:nth-child(3){transition-delay:150ms}
.is-active [data-reveal]:nth-child(4){transition-delay:220ms}
@media (max-width:760px){.two-col,.three-col,.gauge{grid-template-columns:1fr}
 .milestones{grid-template-columns:1fr;padding-top:0}.milestones::before,.ms::before{display:none}
 .chain{grid-template-columns:1fr}.reticle{opacity:.4}}
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

CONTOUR = ('<svg class="contour" viewBox="0 0 1280 720" preserveAspectRatio="none">'
 '<g fill="none" stroke="#3D5A6C" stroke-opacity=".12">'
 '<path d="M-40 620 Q 300 480 640 560 T 1340 520"/><path d="M-40 660 Q 320 530 660 600 T 1340 570"/>'
 '<path d="M-40 700 Q 340 580 700 640 T 1340 620"/><path d="M900 -40 Q 1050 200 980 420 T 1120 760"/>'
 '<path d="M960 -40 Q 1120 210 1040 430 T 1180 760"/></g></svg>')

MODES = ['paper','white','paper','white','dark','white','paper','white','paper','white','paper','dark']

def slide(i, mode, body, mark, notes=''):
    return (f'<section class="slide slide--{mode}" id="s{i}" aria-label="第{i}屏">'
            f'<div class="hazbar"></div>{CONTOUR if mode!="dark" else ""}'
            f'<div class="slide-content">{body}</div>'
            f'<aside class="speaker-notes">{notes}</aside>'
            f'<span class="footer-mark">{code_of_current} · {i:02d}/12 · {mark}</span></section>')

code_of_current = ''

def cover(t, meta):
    return ('<div class="brand" data-reveal><div class="idplate">' + t['code'].replace('ENF-', 'E') + '</div>'
            f'<div><strong>{t["brand"]}</strong><span>{t["sub"]}</span></div></div>'
            f'<div data-reveal><p class="eyebrow">GOAI 无界应用 · AI+工业制造 // {t["code"]} · UNIT FILE</p>'
            f'<h1>{t["h1"]}</h1></div>'
            f'<p class="lede" data-reveal>{t["lede"]}</p>'
            f'<div data-reveal style="display:flex;flex-wrap:wrap;align-items:center">'
            + ''.join(f'<span class="tag">{m}</span>' for m in t['marks'])
            + f'<span class="tag">作品层 {meta["score"]} · {meta["tier"]}</span>'
            f'<span class="tag">{meta["anchor"]}</span></div><div class="reticle"></div>')

def anchor3(rows, pick, reason):
    cols = ''.join(
        f'<section class="panel"><span class="uid">ALT-{k+1}</span><h3>{r["name"]}</h3>'
        f'<div class="score">{r["score"]}</div><p>{r["desc"]}</p></section>' for k, r in enumerate(rows))
    return (f'<div data-reveal><p class="eyebrow">SCENE ANCHOR // PRD §1</p><h2>三个候选场景，选{pick}</h2></div>'
            f'<div class="three-col" data-reveal>{cols}</div>'
            f'<p class="lede" data-reveal style="margin-top:.4rem">{reason}</p>')

def pain(big, unit, h2, flow, note):
    items = ''.join(f'<div><strong>{f}</strong></div>' for f in flow)
    return (f'<div class="two-col"><div data-reveal><p class="eyebrow">THE PAIN // PRD §3</p>'
            f'<div class="big-number">{big}<span style="font-size:.32em">{unit}</span></div>'
            f'<h2>{h2}</h2><p class="lede">{note}</p></div>'
            f'<div class="flow" data-reveal>{items}</div></div>')

def formula(parts, lede):
    row = ''.join(f'<span class="op">{p}</span>' if not p.startswith('→') else f'<em> {p} </em>' for p in parts)
    return (f'<div data-reveal><p class="eyebrow">THE OFFER // PRD §2</p>'
            f'<h2>流程交给系统，决定留给人</h2></div>'
            f'<div class="ops" data-reveal>{row}</div>'
            f'<p class="lede" data-reveal>{lede}</p>')

def agents(cards, loop_line, gate_line):
    cols = ''.join(
        f'<section class="panel"><span class="uid">AGT-{k+1:02d}</span><h3>{c["n"]}</h3><p>{c["d"]}</p></section>'
        for k, c in enumerate(cards))
    return (f'<div data-reveal><p class="eyebrow">AGENT CREW // PRD §4</p>'
            f'<h2>微循环自主，宏流程门禁</h2></div>'
            f'<div class="three-col" data-reveal>{cols}</div>'
            f'<div class="boundary" data-reveal><strong>{loop_line}</strong><span>{gate_line}</span></div>')

def steps7(names, notes):
    nodes = ''.join(f'<div class="node"><b>{i+1:02d} {n}</b><span>{d}</span></div>' for i, (n, d) in enumerate(names))
    return (f'<div data-reveal><p class="eyebrow">CLOSED LOOP // PRD §5 · 手册 8.2</p>'
            f'<h2 style="color:#F2F4F6">一条链走完，七步都有落点</h2></div>'
            f'<div class="chain" data-reveal>{nodes}</div>'
            f'<p class="lede" data-reveal>{notes}</p>')

def evidence(items, lede):
    cols = ''.join(f'<section class="g"><b>{e[0]}</b><p>{e[1]}</p></section>' for e in items)
    return (f'<div data-reveal><p class="eyebrow">EVIDENCE & METRICS // PRD §6/§7</p>'
            f'<h2>已知与模拟，分开建档</h2></div>'
            f'<div class="gauge" data-reveal>{cols}</div>'
            f'<p class="lede" data-reveal style="margin-top:.4rem">{lede}</p>')

def boundary_slide(title, rows, lede):
    bs = ''.join(f'<div class="boundary" data-reveal><strong>{a}</strong><span>{b}</span></div>' for a, b in rows)
    return (f'<div data-reveal><p class="eyebrow">SAFETY BOUNDARY // PRD §8</p><h2>{title}</h2></div>'
            f'{bs}<p class="lede" data-reveal>{lede}</p>')

def timeline3(rows):
    steps = ''.join(f'<div class="ms"><strong>{a}</strong><span>{b}</span></div>'
                    f'<div class="ms"><strong>{c}</strong><span>{d}</span></div>' for a, b, c, d in rows)
    return (f'<div data-reveal><p class="eyebrow">ROADMAP // PRD §9</p>'
            f'<h2>三档排期：材料、可运行、现场</h2></div>'
            f'<div class="milestones" data-reveal>{steps}</div>')

def opensource(rows, risk):
    cols = ''.join(
        f'<section class="panel"><span class="uid">OS-{k+1:02d}</span><h3>{r["n"]}</h3><p>{r["d"]}</p></section>'
        for k, r in enumerate(rows))
    return (f'<div data-reveal><p class="eyebrow">OPEN SOURCE & RISKS // PRD §10/§11</p>'
            f'<h2>留下的不只是演示，是可复用的件</h2></div>'
            f'<div class="three-col" data-reveal>{cols}</div>'
            f'<div class="boundary" data-reveal><strong>最大风险与对策</strong><span>{risk}</span></div>')

def intro8(paras):
    body = ''.join(f'<p><b>{k}</b>{v}</p>' for k, v in paras)
    return (f'<div data-reveal><p class="eyebrow">500-WORD BRIEF // PRD §12</p>'
            f'<h2>参赛简介 · 八要素（≤500 字）</h2></div>'
            f'<div class="doc" data-reveal>{body}</div>')

def review(asks):
    items = ''.join(f'<div class="chk"><b>{i+1:02d}</b><strong>{a}</strong></div>' for i, a in enumerate(asks))
    return (f'<div class="two-col"><div data-reveal><p class="eyebrow">REVIEW // 你的审核位</p>'
            f'<p style="font-size:var(--h2-size);font-weight:800;line-height:1.12;max-width:14ch">'
            f'看完这一份，<span class="accent">留下三句话</span></p></div>'
            f'<div class="checklist" data-reveal>{items}</div></div>'
            f'<p class="lede" data-reveal>审核结论：☐ 转正式 PPT　☐ 修改后再审　☐ 冻结为模块　（按 N 看演讲备注）</p>')

S7 = [('任务输入','告警/工单/缺口流入'),('意图理解','分类·定级·影响面'),('任务规划','追溯/求解/起草计划'),
      ('能力调用','库·API·求解器'),('结果交付','证据链/动作包'),('验证反馈','命中率·回放·人确认'),('安全边界','终点决策留给人')]

META = {
 'M1A': dict(score='86.6 分', tier='第二梯队 · 引擎模块', anchor='S19 半导体/精密机加'),
 'M3B': dict(score='77.8 分', tier='内置模块', anchor='S16 机械/汽配周度请购'),
 'M1E': dict(score='85.5 分', tier='收官模块', anchor='S25 机加车间案例库'),
}

CONTENT = {
'M1A': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S19 半导体/精密机加 SPC', score='90.7 ✓', desc='SECOM 公开数据集 + 四表模拟，证据链最硬，贴批次-工单叙事'),
   dict(name='S21 化工过程 TEP', score='86.4', desc='学术常见基准，同类作品多，差异化弱'),
   dict(name='S20 注塑工艺异常', score='85.2', desc='商业方案密集，参数下发贴近设备控制域')],
   pick='证据最硬的一个', reason='落选理由在案：TEP 是学术常见基准、注塑商业方案多。S19 的 SECOM 在手，注入式 ground truth 让归因命中率可复核。'),
 dict(f='pain', big='4-48', unit=' 小时', h2='定位一批异常的代价', flow=[
   '跨 QMS / MES / 工艺 / 设备四套系统人工比对','8D 报告写作再花 2-4 小时','复盘缺失，同类异常反复发生'],
   note='痛点量化假设，实现期用行业访谈校准——但每个质量工程师都认识这张图。'),
 dict(f='formula', parts=['SPC 告警','+','四源数据','→','证据链根因','+','8D 初稿'],
   lede='只做辅助分析。根因确认、批次放行、停线建议的终点决策，永远留给质量负责人——这是设计，不是免责声明。'),
 dict(f='agents', cards=[
   dict(n='值守 Agent', d='监听 SPC 控制图与规则触发，判定异常类型与影响面'),
   dict(n='数据侦探', d='批次谱系 × 工艺参数 × 设备日志 × 来料检验，四源拉取对齐'),
   dict(n='根因推理', d='假设生成 → 逐条验证 → 证据链 + 置信度排序，未验证假设单列'),
   dict(n='8D 撰写', d='D1-D8 结构化初稿，附证据引用，D4 根因确认留白给人')],
   loop_line='微循环：单次告警触发的「追溯-归因-草稿」推理链全程自主',
   gate_line='宏门禁：根因确认与处置放行 = 质量负责人拍板（手册 9.3 / FAQ Q13）'),
 dict(f='steps7', names=S7, notes='七步每步都有组件落点：告警卡、对齐面板、假设卡、查询工具、8D 文档、回放评测、边界提示。'),
 dict(f='evidence', items=[
   ('A','SECOM 公开数据集（1567×591 含缺陷标签）：检出与特征归因展示'),
   ('B','四表模拟 + 已知根因注入：ground truth 可复算'),
   ('≥80%','注入根因 Top-3 命中率；追溯 ≤10 分钟；8D 字段完整率 100%')],
   lede='所有数字都能被复算——这正是它与"讲故事的质检工具"的区别。'),
 dict(f='boundary', title='边界写清楚，可信度才立得住', rows=[
   ('仅辅助分析，不替代放行', '批次放行 / 停线决策由质量负责人决定（手册 9.3、FAQ Q13）'),
   ('数据口径全披露', '公开 + 模拟数据，模拟逻辑写入合规文档（FAQ Q7）')],
   lede='证据链可追溯、可审计——边界本身就是产品的解释性。'),
 dict(f='timeline3', rows=[('初赛 8.16','叙事材料已备','复赛 9.3','质量一条链可运行'),('决赛 9.22','现场注入新告警','引擎去向','喂给 M2-B 售后 8D')]),
 dict(f='opensource', rows=[
   dict(n='四表模拟器', d='含根因注入，可复算的 ground truth'),
   dict(n='根因推理模板', d='假设-验证-置信度的 Prompt 与工具链'),
   dict(n='8D schema', d='结构化报告模板，可挂接任意 QMS')],
   risk='归因准确性质疑 → 注入式评测自证；报告模板化 → 证据引用 + 未验证假设清单。'),
 dict(f='intro8', paras=[
   ('项目名称：','质源侦探 RootCause Cop——质量异常根因追溯智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','半导体与精密机加厂质量工程师'),('核心问题：','SPC 告警后跨四套系统人工比对，根因定位数小时至数天，8D 报告耗时'),
   ('解决方案：','四 Agent 链：值守监听告警，数据侦探对齐四源，根因推理生成假设并逐条验证形成证据链，8D 撰写产出结构化初稿并预留人工确认位'),
   ('创新点：','每个结论附证据链与"未验证假设"清单，解释性内建；根因确认与批次放行始终由人拍板；引擎可复用于售后批次分析'),
   ('开放/复用价值：','开源四表模拟器（含根因注入）、根因模板与 8D schema'),('当前进展：','方案设计完成，基于公开数据集的原型开发中，提交时附追溯演示')]),
 dict(f='review', asks=['工业取证台的气质是否成立？','切角面板/角括号/警示条的密度是否合适？','转正式 PPT 前，还需要补哪屏的细节？']),
],
'M3B': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S16 机械/汽配周度请购', score='85.9 ✓', desc='与齐途、哨兵同厂；分差 1.2<3，D2 平后取总分'),
   dict(name='S17 MRO 备品备件', score='84.7', desc='品类杂但偏库存消耗逻辑，Agent 特征弱'),
   dict(name='S18 包装材料', score='82.3', desc='物料域过简单，痛点偏轻')],
   pick='分差最小、依从 D2 规则的一个', reason='这场选优本身就是规则演示：85.9 与 84.7 分差小于 3，先比 D2（用户偏好轴），仍平，才回总分——过程在场景调研文档留档。'),
 dict(f='pain', big='30', unit=' 分钟+', h2='一张请购单的手工成本', flow=[
   '缺口清单人工核对、手工做单','比价信息散落在邮件与聊天记录','下单后交期变化靠人肉跟踪'],
   note='PRD 的定位很诚实：这不是主角，是"动作闭环补全者"——把计划和哨兵的输出变成真的动作。'),
 dict(f='formula', parts=['缺口清单','+','比价矩阵','→','请购包 + 跟踪回写'],
   lede='起草全自动，下单人签字。紧急空运这类高成本动作，还要经理再签一次。'),
 dict(f='agents', cards=[
   dict(n='缺口监听 Agent', d='接齐套核算缺口，按紧急度 × 断料风险分级'),
   dict(n='请购起草 Agent', d='请购单草案 + 多供应商比价矩阵（价格/交期/绩效/风险分），字段级引用来源'),
   dict(n='跟踪回写 Agent', d='下单后交期变化监测 → 异常提醒 → 到货回写')],
   loop_line='微循环：缺口 → 分级 → 起草 → 比价 → 跟踪更新，全程自主',
   gate_line='宏门禁：下单 / 供应商选择 = 采购员；紧急空运等高成本动作 = 经理审批'),
 dict(f='steps7', names=S7, notes='七步在采购域的落点：缺口与交期事件输入、物料与紧急度判定、请购比价计划、BOM 库存供应商库调用、请购包交付、交期达成率统计、商务决策人工。'),
 dict(f='evidence', items=[
   ('100%','请购包字段完整率；交期异常捕获率（剧本口径）'),
   ('≥3 家','比价矩阵每料覆盖供应商数'),
   ('≤5 分钟','紧急缺口（T+3 内断料）起草时长')],
   lede='指标朴素，但都能被程序校验——这正是一个"动作型 MVP"该有的样子。'),
 dict(f='boundary', title='调度台不碰钱，也不碰合同', rows=[
   ('不产生真实订单', '价格与合同信息均为模拟并披露（手册 9.3、FAQ Q7）'),
   ('比价结论附来源与假设', '字段级引用，人可核对（8.1-6 人工确认机制）')],
   lede='它把采购从制表中解放出来，而不是从判断中解放出来。'),
 dict(f='timeline3', rows=[('初赛 8.16','P3 叙事一页','复赛 9.3','与齐途串联演示'),('决赛 9.22','计划-哨兵-请购全链','角色','M3-A 的内置联动模块')]),
 dict(f='opensource', rows=[
   dict(n='请购 schema', d='请购单 + 比价矩阵字段定义'),
   dict(n='审批流模板', d='通过/驳回/改量三分支'),
   dict(n='缺口分级规则', d='紧急度 × 断料风险矩阵')],
   risk='单独参赛单薄 → 强绑定 M3-A/C 联动叙事；规则感重 → 突出交期异常跟踪与比价解释。'),
 dict(f='intro8', paras=[
   ('项目名称：','齐购 QiBuy——缺料请购联动智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','中小机械/汽配厂采购员与物控'),('核心问题：','请购单手工制作、比价信息散落、下单后交期变化靠人肉跟踪'),
   ('解决方案：','三 Agent 联动：缺口监听分级、请购起草生成请购单与比价矩阵、跟踪回写盯交期异常并回写库存'),
   ('创新点：','与齐套计划、供应商哨兵同厂闭环，缺口到请购包分钟级；下单与供应商选择始终由人拍板'),
   ('开放/复用价值：','开源请购与比价 schema、审批流模板与缺口分级规则'),('当前进展：','方案设计完成，原型开发中，提交时附联动演示')]),
 dict(f='review', asks=['采购调度台的工业感是否到位？','"配角叙事"的表达是否清晰？','哪些屏可以砍掉，让 10 屏更紧？']),
],
'M1E': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S25 机加车间案例库', score='86.6 ✓', desc='与安灯中枢同车间同数据流，关闭记录直接入案例库'),
   dict(name='S27 集团知识网络', score='85.3', desc='多厂区数据组织复杂，单机 Demo 单薄'),
   dict(name='S26 注塑配方知识库', score='83.3', desc='调机 AI 商业玩家多，差异化弱')],
   pick='和安灯中枢同一条数据流的', reason='分差 1.3<3：D2 平（4=4），回总分定夺。真正的原因是工程性的：M1-B 的每一次异常关闭，天然就是本 MVP 的一次数据生产。'),
 dict(f='pain', big='30%', unit=' 复发率', h2='同类异常，反复发生', flow=[
   '复盘无人写，处理记录散在微信群','老师傅离职，经验跟着走','复发时从头踩坑，预案不存在'],
   note='量化假设：同类异常复发率 ≥30%（复盘缺失口径）。飞轮的意义，就藏在这个数字里。'),
 dict(f='formula', parts=['异常关闭','+','结构化归档','→','复发预警 + 预案推送'],
   lede='归档是系统的工序，不是人的负担。预案采纳与 SOP 修订，依然由工程师与主管签字。'),
 dict(f='agents', cards=[
   dict(n='案例结构化 Agent', d='关闭记录 → 现象/根因/措施/备件/耗时的结构化案例'),
   dict(n='复发监测 Agent', d='新异常早期特征匹配历史案例，相似度排序，预案推送'),
   dict(n='知识运营 Agent', d='月度 Pareto、复发模式聚类、SOP 修订建议、知识缺口提示')],
   loop_line='微循环 ×2：关闭→结构化→入库；早期→匹配→推送',
   gate_line='宏门禁：预案采纳 = 工程师；SOP 修订 = 主管审批'),
 dict(f='steps7', names=S7, notes='七步落点：关闭事件输入、案例要素抽取、结构化入库计划、向量检索与规则、案例+预案+复盘、复发命中率统计、SOP 走既有审批。'),
 dict(f='evidence', items=[
   ('≥75%','复发剧本 Top-3 命中率（预置 100 条历史案例）'),
   ('≥95%','案例字段完整率；人工抽检队列兜底'),
   ('≤5 分钟','月度复盘报告生成（原 ≥4 小时/月）')],
   lede='价值滞后的痛点用"对比演示"解决：同一异常第二次出现时，有无飞轮的响应差异，一屏看清。'),
 dict(f='boundary', title='档案只记事，不审判人', rows=[
   ('知识建议域', '不替代 SOP 审批与专业判断（手册 9.3）'),
   ('不含人员绩效评价', '案例只记事不记人，规避 HR 敏感；模拟数据披露')],
   lede='档案室只归档"事"，不归档"谁"——这是它能在车间活下来的前提。'),
 dict(f='timeline3', rows=[('初赛 8.16','P1 叙事"飞轮"页','复赛 9.3','与安灯中枢串联'),('决赛 9.22','复发剧本现场回放','角色','M1-B 的收官模块')]),
 dict(f='opensource', rows=[
   dict(n='案例库 schema', d='五要素结构化定义'),
   dict(n='CBR 检索模板', d='向量 + 规则的混合检索'),
   dict(n='复盘生成器', d='Pareto 与复发模式报告')],
   risk='冷启动无案例 → 预置 100 条 + 字段门禁；质量差 → 结构化校验 + 人工抽检。'),
 dict(f='intro8', paras=[
   ('项目名称：','车间记忆 ShopMemory——异常案例沉淀与复发预警智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','机加车间设备、质量与工艺工程师及车间主任'),('核心问题：','同类异常反复发生，处理经验随人员流失，复盘无人写、知识不沉淀'),
   ('解决方案：','三 Agent 飞轮：案例结构化将关闭记录转为结构化案例，复发监测早期匹配并推送预案，知识运营生成 Pareto 与 SOP 修订建议'),
   ('创新点：','把"经验沉淀"从人工义务变成自动飞轮；复发时预案先行；预案采纳与 SOP 修订由人拍板'),
   ('开放/复用价值：','开源案例库 schema、CBR 检索模板与复盘生成器，可挂接任意工单系统'),('当前进展：','方案设计完成，预置案例集制作与原型开发中，提交时附飞轮回放演示')]),
 dict(f='review', asks=['档案室的气质是否成立？','"飞轮"叙事是否讲清楚了？','作为 M1-B 收官模块，要不要并回 M1-B 的 deck？']),
],
}

BUILDERS = dict(cover=cover, anchor3=anchor3, pain=pain, formula=formula, agents=agents,
                steps7=steps7, evidence=evidence, boundary=boundary_slide, timeline3=timeline3,
                opensource=opensource, intro8=intro8, review=review)

def build(key, t):
    global code_of_current
    code_of_current = t['code']
    slides = []
    marks = {'cover':'微循环自主 · 宏流程门禁','anchor3':'场景为什么这么选','pain':'痛点的量化假设',
             'formula':'定位一句话','agents':'Agent 分工与门禁','steps7':'闭环七步（手册 8.2）',
             'evidence':'证据与指标','boundary':'安全合规口径','timeline3':'三档排期',
             'opensource':'开源物与风险','intro8':'参赛简介','review':'你的审核位'}
    for i, spec in enumerate(CONTENT[key], 1):
        spec = dict(spec); f = spec.pop('f')
        html_ = BUILDERS[f](t, META[key]) if f == 'cover' else BUILDERS[f](**spec)
        notes = f'这是{t["name"]}的审核稿。按 N 可看演讲备注。' if f == 'cover' else ''
        slides.append(slide(i, MODES[i-1], html_, marks[f], notes))
    doc = ('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1">'
           f'<title>{t["name"]} · {key} 审核稿</title><style>{CSS}</style></head>'
           f'<body style="--sig:{t["sig"]}"><div class="progress" aria-hidden="true"><span id="pf"></span></div>'
           '<main id="deck">' + '\n'.join(slides) + '</main>'
           '<nav class="present-nav"><button id="pv" aria-label="上一页">←</button>'
           '<span class="slide-count" id="sc">1 / 12</span><button id="nx" aria-label="下一页">→</button></nav>'
           f'<script>{JS}</script></body></html>')
    (OUT / f'deck_{key}.html').write_text(doc, encoding='utf-8')

if __name__ == '__main__':
    for k, t in DECKS.items():
        build(k, t)
        n = (OUT / f'deck_{k}.html').read_text(encoding='utf-8').count('<section class="slide ')
        print(f'OK deck_{k}.html sections={n}')
