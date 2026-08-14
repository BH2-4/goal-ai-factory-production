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

 'M2A': dict(sig='#2F6B4F', code='ENF-01', brand='FIELD SERVICE DECK',
   name='气脉助手 AirFix', sub='报修-修复-沉淀主链 · 售后服务台 · 非官方审核稿',
   h1='报修电话的另一端，<span class="accent">不该总在等专家</span>',
   lede='单票全旅程：问诊、检索、备件、工单、指导、沉淀，四 Agent 自主跑完——诊断确认与高危作业由人拍板，每次维修都沉淀为厂商知识资产。',
   marks=['单票全链','沉淀飞轮','双端形态']),
 'M2B': dict(sig='#A03A2A', code='ENF-02', brand='FLEET SENTINEL CONSOLE',
   name='气脉哨兵 AirSentinel', sub='批次故障哨兵 · 机队哨戒台（旗舰 91.2）· 非官方审核稿',
   h1='批次故障，<span class="accent">不该等客户来教你发现</span>',
   lede='机队哨兵持续聚类工单与遥测流：识别批次模式、生成影响面清单、起草售后 8D——服务通报与召回，由厂商管理层拍板。',
   marks=['跨工单值守','8D 自动起草','召回人拍板']),
 'M3A': dict(sig='#2B5C8A', code='ENF-04', brand='PLANNING OPS CONSOLE',
   name='齐途 QiPlan', sub='齐套核算+插单冲突解释 · 计划控制台 ★主推 · 非官方审核稿',
   h1='插单的答案，<span class="accent">不该靠电话和 Excel</span>',
   lede='求解器管最优化，LLM 管交互与解释：齐套核算、可行排产、冲突归因、动作包——计划采纳与交期承诺，由计划员拍板。',
   marks=['冲突解释','LLM×求解器契约','计划人拍板']),
 'M1B': dict(sig='#8A5A0A', code='ENF-05', brand='ANDON WATCHTOWER',
   name='安灯中枢 AndonCop', sub='Andon 值守循环 · 值守塔（第一备选）· 非官方审核稿',
   h1='车间的异常，<span class="accent">不该靠吼来传递</span>',
   lede='事件值守塔：分诊、派单、超时升级、关闭复盘全程自主；停线与结案由主管拍板——升级策略可解释、可配置。',
   marks=['事件值守','可解释升级','停线人拍板']),
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
 'M2A': dict(score='86.4 分', tier='第二梯队 · 数据底座', anchor='S01 空压机厂商售后'),
 'M2B': dict(score='91.2 分', tier='第一梯队 · 旗舰', anchor='S04 空压机机队监测'),
 'M3A': dict(score='89.7 分', tier='第一梯队 · 主推', anchor='S10 机械/汽配二级供应商'),
 'M1B': dict(score='89.9 分', tier='第一备选', anchor='S22 机加车间混合 Andon'),
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

'M2A': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S01 空压机厂商售后', score='89.8 ✓', desc='IoT 远程监控渗透率最高的通用装备；服务合同模式成熟'),
   dict(name='S02 注塑机厂商售后', score='84.0', desc='液压/温控/控制器三域，竞品密度更高'),
   dict(name='S03 数控机床厂商售后', score='82.5', desc='报警码体系庞大（数千条），知识在厂商专家手里')],
   pick='IoT 与服务合同最成熟的一个', reason='落选在案：注塑与机床竞品密度更高、与 P2 其他 MVP 协同弱；S01 与机队哨兵（S04）、装机档案（S07）同数据域。'),
 dict(f='pain', big='24h+', unit=' 响应', h2='一次报修的等待成本', flow=[
   '报修靠电话微信，现象描述失真','专家出差诊断，差旅约占售后成本三成','修完记录散落，下次从头再来'],
   note='量化假设：响应 ≥24 小时；专家差旅占售后成本 30-40%；同故障重复诊断率高——耗材型工单占比高且重复，是沉淀飞轮的燃料。'),
 dict(f='formula', parts=['客户报修','+','手册×案例','→','备件工单 + 指导 + 案例'],
   lede='检索与起草归系统；诊断确认由工程师签字，高压电气与压力容器作业强制转持证人员——每张沉淀的案例，都让下一次更快。'),
 dict(f='agents', cards=[
   dict(n='问诊 Agent', d='多轮交互式故障树（症状+照片识别部件状态），澄清缺失信息'),
   dict(n='知识检索 Agent', d='手册 RAG + 历史工单 CBR，Top-K 相似案例带证据'),
   dict(n='备件工单 Agent', d='备件 BOM 匹配与库存查询、工单草案、技能匹配建议'),
   dict(n='沉淀 Agent', d='维修记录 → 结构化案例（现象/根因/措施/备件/耗时）回流知识库')],
   loop_line='微循环：单票报修从受理到「工单+指导+案例草稿」全程自主',
   gate_line='宏门禁：诊断确认 = 工程师；高危作业 = 转持证人员；案例入库 = 存档审核'),
 dict(f='steps7', names=S7, notes='七步落点：照片/语音/故障码输入、故障分类与紧急度、问诊与检索计划、手册/案例/备件/工单调用、诊断+备件单+工单+分步指导、维修结果回填与命中率统计、高危分级提示与人工确认。'),
 dict(f='evidence', items=[
   ('200 条','自建模拟工单（故障码/现象/措施/备件/耗时），ground truth 可复算'),
   ('≥70%','Top-3 诊断命中率；备件建议准确率 ≥90%'),
   ('≤5 轮','平均问诊轮次；案例沉淀字段完整率 ≥95%')],
   lede='无公开数据集是硬伤（D 维 3.8）——所以 ground truth 工单集的构建逻辑全部披露，自造 2-3 本模拟手册规避版权。'),
 dict(f='boundary', title='远程支持的安全底线', rows=[
   ('诊断仅辅助确认', '工程师确认后执行；高压电气/压力容器作业强制转持证人员（手册 9.3）'),
   ('双端数据全模拟', '手册自建规避版权；客户信息不落地（FAQ Q7）')],
   lede='双端产品（客户报修端+工程师工作台）；失败分支（信息缺失→澄清、检索失败→转人工）是演示的一部分，不是事故。'),
 dict(f='timeline3', rows=[('初赛 8.16','保底叙事主线（本项目）','复赛 9.3','双端可运行 Demo'),('决赛 9.22','完整旅程+失败分支','角色','数据底座 + 单票旅程叙事')]),
 dict(f='opensource', rows=[
   dict(n='售后知识库 schema', d='手册/案例/备件三库结构定义'),
   dict(n='问诊决策树 DSL', d='可配置的多轮问诊路径'),
   dict(n='工单案例 CBR 模板', d='相似案例检索与引用')],
   risk='维修问答机同质化 → 三件套显性化（工单备件动作闭环、沉淀飞轮、双端形态）；照片识别不稳 → 降级为部件定位辅助。'),
 dict(f='intro8', paras=[
   ('项目名称：','气脉助手 AirFix——空压机售后报修修复沉淀智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','空压机厂商售后工程师与客户工厂设备管理员'),('核心问题：','报修靠电话、诊断靠专家出差、备件靠翻表、修完知识蒸发'),
   ('解决方案：','四 Agent 协作的单票全旅程闭环：问诊 Agent 多轮交互定位故障（支持拍照识别），知识检索 Agent 融合手册 RAG 与历史案例推理，备件工单 Agent 自动查询库存并起草工单，沉淀 Agent 将维修记录结构化回流知识库'),
   ('创新点：','微循环自主、宏流程门禁——诊断确认与高危作业由人拍板；闭环终点是"动作+知识"而非"答案"'),
   ('开放/复用价值：','开源售后知识库 schema、问诊决策树 DSL、案例模板与模拟数据生成器，可迁移至其他装备行业'),('当前进展：','方案设计完成，双端原型开发中，提交时附演示视频')]),
 dict(f='review', asks=['售后服务台的工业感是否成立？','双端叙事在 12 屏里讲清了吗？','作为 M2-B 的数据底座，定位传达够不够？']),
],
'M2B': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S04 空压机机队批次监测', score='97.2 ✓', desc='全场最高分；与售后主链同数据域，根因引擎复用 M1-A'),
   dict(name='S05 光伏逆变器机队', score='88.0', desc='偏能源叙事，稀释装备售后主线'),
   dict(name='S06 电梯机队监测', score='84.7', desc='监管门禁刚性（G2 部分可重构），维保流程法定')],
   pick='全场分最高的一个', reason='落选在案：S05 偏能源、S06 监管刚性。S04 的价值在视角而非数据——跨工单哨兵，预计全场无同类。'),
 dict(f='pain', big='N 起', unit=' 投诉后', h2='批次问题的发现方式', flow=[
   '同型故障率悄悄爬升，无人察觉','影响面清单靠人工翻工单拼接','召回决策缺数据支撑'],
   note='剧本口径：批次性问题平均在第 N 起投诉后才被识别——哨兵的意义，就是把这个 N 变成 0。'),
 dict(f='formula', parts=['工单+遥测流','+','聚类归因','→','批次警报 + 8D + 影响面'],
   lede='值守与起草归系统；服务通报、召回、客户通知是厂商管理层的决策——这些门禁点在组织里本来就存在。'),
 dict(f='agents', cards=[
   dict(n='聚类监测 Agent', d='故障码与话题聚类，时间/批次/地域聚集度检测（持续值守）'),
   dict(n='根因推理 Agent', d='复用 M1-A 证据链引擎：工单×故障码×批次档案×遥测四源验证'),
   dict(n='报告起草 Agent', d='售后 8D 初稿（D1-D5）+ 影响面清单 + 服务通报建议')],
   loop_line='微循环：新事件流入到「模式警报+8D 草稿+影响面清单」全程自主值守',
   gate_line='宏门禁：服务通报/召回 = 厂商管理层；客户通知 = 售后经理；8D 定稿 = 审核'),
 dict(f='steps7', names=S7, notes='七步落点：事件流输入、聚集度评估、追溯验证计划、工单/遥测/批次档案调用、警报+8D+影响面、已知剧本回放命中率、召回类决策人工。'),
 dict(f='evidence', items=[
   ('2/2','预埋批次模式全检出（同批部件失效/同固件版本缺陷）'),
   ('≥3 天','较"投诉阈值"基线的检出提前量（模拟口径）'),
   ('≥4/5','8D 初稿人工评分采纳率；误报 ≤1 次/模拟周')],
   lede='聚类证据面板（哪些工单、何共性、聚集度数值）让"为什么报警"可查——哨兵最怕的不是漏，是不可信。'),
 dict(f='boundary', title='哨戒台只值守，不越权', rows=[
   ('只监测与起草', '不触发任何自动客户动作；通报与召回由厂商拍板（手册 9.3）'),
   ('剧本全披露', '200+ 模拟工单与遥测的生成逻辑写入合规文档（FAQ Q7）')],
   lede='旗舰定位：单票旅程（M2-A）与全局哨兵（本作）双循环互补——决赛演示"从单票到批次警报"的跨 MVP 旅程。'),
 dict(f='timeline3', rows=[('初赛 8.16','双循环架构页（已备）','复赛 9.3','哨兵面板可运行（回放）'),('决赛 9.22','现场注入新事件','联动','与 M2-A 共仓、M1-A 引擎复用')]),
 dict(f='opensource', rows=[
   dict(n='批次检测管线', d='聚类 + 聚集度规则'),
   dict(n='售后 8D schema', d='结构化报告模板'),
   dict(n='事件流模拟器', d='含批次剧本，可复算')],
   risk='误报伤信任 → 置信度分级 + 人审队列；依赖 M2-A 数据层 → 排期前置一周建设。'),
 dict(f='intro8', paras=[
   ('项目名称：','气脉哨兵 AirSentinel——装备机队批次故障预警智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','空压机厂商质量与售后负责人'),('核心问题：','批次性故障靠客户投诉倒逼才发现，召回决策缺乏影响面数据支撑'),
   ('解决方案：','跨工单持续值守的三 Agent 系统：聚类监测持续聚合工单与遥测流识别批次聚集，根因推理融合四源生成证据链，报告起草自动产出影响面清单与售后 8D 初稿'),
   ('创新点：','微循环自主、宏流程门禁——召回、服务通报与客户通知由厂商拍板；从"处理单票"升维到"盯住全局"'),
   ('开放/复用价值：','开源批次模式检测管线、售后 8D 模板与事件流模拟器，可迁移至其他装备机队'),('当前进展：','方案设计完成，原型开发中，提交时附回放演示')]),
 dict(f='review', asks=['哨戒台的警戒红气质是否压得住旗舰定位？','91.2 分叙事与 12 屏节奏匹配吗？','转正式 PPT 的首选？']),
],
'M3A': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S10 机械/汽配二级供应商', score='90.5 ✓', desc='最贴六要素叙事；BOM 三层适中，依赖图解释最顺'),
   dict(name='S11 PCB/SMT 电子', score='87.3', desc='长单层 BOM、替代料规则复杂，参赛密度高'),
   dict(name='S12 包装/印刷短单', score='86.1', desc='物料域过简单，痛点偏轻')],
   pick='最贴六要素的一个', reason='分差 3.2>3 直接取最高；与供应商哨兵（S13）、周度请购（S16）同厂闭环——计划域一条数据主线。'),
 dict(f='pain', big='2h+', unit=' 每次插单', h2='一次插单评估的成本', flow=[
   'Excel + 电话逐格核对齐套','缺料投产前 1-2 天才暴露','被延订单说不清原因，销售与产线互斥'],
   note='量化假设：插单评估 ≥2 小时；延期无解释，是计划员最消耗信任的日常。'),
 dict(f='formula', parts=['订单变化','+','约束求解','→','排产 + 冲突解释 + 动作包'],
   lede='求解器管最优化，LLM 管交互与解释——LLM 不算数，这是写进契约的。交付物是动作包（工单+请购+交期草案），不是一张表。'),
 dict(f='agents', cards=[
   dict(n='齐套核算 Agent', d='订单 → 三层 BOM 展开 → 毛/净需求 → 缺口清单（程序化可校验）'),
   dict(n='排产求解 Agent', d='OR-Tools 约束求解，输出可行排产与被延订单（LLM 不做数值计算）'),
   dict(n='冲突解释 Agent', d='延期归因（缺哪个料/哪台机满载/哪班人不够）+ 替代方案对比'),
   dict(n='采购联动 Agent', d='接 M3-B：缺口 → 请购草案，并入动作包')],
   loop_line='微循环：需求/库存/在途变化 → 重算 → 求解 → 归因 → 动作包，全程自主',
   gate_line='宏门禁：计划采纳 = 计划员；交期承诺 = 销售；替代料启用 = 工程确认'),
 dict(f='steps7', names=S7, notes='七步落点：订单/插单/库存变化输入、变更类型与影响面、重算求解计划、BOM/库存/在途/产能日历+求解器调用、排产+解释+动作包、硬约束零违反校验与基线对比、纯建议域声明。'),
 dict(f='evidence', items=[
   ('100%','齐套核算准确率（程序可校验）；排产硬约束零违反'),
   ('≥15%','延期订单数较 FIFO 基线下降'),
   ('≤30s','插单全流程响应（重算+求解+解释）')],
   lede='证据硬度全场最高的一档：每个数字都能被复算——这是 D 维 5.0 的由来。'),
 dict(f='boundary', title='计划权留在计划员手里', rows=[
   ('纯计划建议系统', '不写真实 ERP；计划采纳与交期承诺由人决定（手册 9.3）'),
   ('契约公开', 'LLM 与求解器分工写进技术文档，评审可查')],
   lede='与 APS 的关系是答辩必考题：定位是中小厂用不起 APS 的轻量入口 + 自然语言交互 + 传统 APS 最缺的解释性。'),
 dict(f='timeline3', rows=[('初赛 8.16','架构 + 契约图','复赛 9.3','齐套+插单解释链可运行'),('决赛 9.22','交互式插单演示','联动','风险→缺口→请购 全链')]),
 dict(f='opensource', rows=[
   dict(n='模拟数据生成器', d='BOM×库存×在途×订单×产能日历'),
   dict(n='齐套引擎封装', d='MRP 逻辑可程序校验'),
   dict(n='冲突解释模板', d='归因 Prompt + 依赖图组件')],
   risk='排产红海 → 主打插单冲突解释错位；LLM 算数质疑 → 契约显性化 + 界面强制采纳确认门禁。'),
 dict(f='intro8', paras=[
   ('项目名称：','齐途 QiPlan——机加厂齐套核算与插单冲突解释智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','中小机械/汽配厂计划员、物控与销售'),('核心问题：','插单靠电话与 Excel 评估，缺料发现晚，被延订单说不清原因'),
   ('解决方案：','LLM×求解器分工的计划副驾：齐套核算做三层 BOM 展开与缺口清单，排产求解用约束求解生成可行排产，冲突解释归因每张被延订单并给替代方案，采购联动把缺口变成请购草案'),
   ('创新点：','求解器管最优化、LLM 管交互与解释的清晰契约；主打传统 APS 最缺的插单冲突解释；计划采纳与交期承诺由人拍板'),
   ('开放/复用价值：','开源制造模拟数据生成器、齐套引擎与解释模板，中小厂可直接复用'),('当前进展：','方案与数据模型设计完成，原型开发中，提交时附演示')]),
 dict(f='review', asks=['计划控制台的钢蓝气质是否到位？','求解器×LLM 契约一屏讲清了吗？','主推作品的叙事顺序建议？']),
],
'M1B': [
 dict(f='cover'),
 dict(f='anchor3', rows=[
   dict(name='S22 机加车间混合 Andon', score='89.3 ✓', desc='AI4I 数据集支撑最硬；与车间记忆（S25）同数据流'),
   dict(name='S23 SMT 产线 Andon', score='88.5', desc='分差 0.8<3，D2 平后回总分；电子参赛密度高'),
   dict(name='S24 食品/饮料灌装线', score='84.0', desc='卫生合规面宽，叙事偏离装备制造')],
   pick='数据最硬的一个（0.8 分差按规则定夺）', reason='分差 0.8<3 → 先比 D2（均 5 平）→ 回总分取 S22；AI4I 在手，事件模拟器与车间记忆共用一套数据流。'),
 dict(f='pain', big='30min+', unit=' 响应', h2='车间异常的传递方式', flow=[
   '靠吼 + 微信群，责任漂移','超时无兜底升级，靠人盯','处理记录散落，事后无结构化数据'],
   note='量化假设：平均响应 ≥30 分钟；值守塔的 SLA 与升级策略是可配置、可解释的——这是它不是"通知机器人"的原因。'),
 dict(f='formula', parts=['事件流','+','技能矩阵','→','分诊 + 派单 + 升级 + 复盘'],
   lede='值守归系统；停线与结案确认归主管。每一次关闭的记录，都会流进车间记忆（M1-E）的案例库。'),
 dict(f='agents', cards=[
   dict(n='分诊 Agent', d='设备/质量/缺料事件分类分级，可融合现场照片辅助判断'),
   dict(n='调度 Agent', d='技能矩阵 × 班次 × 负荷 → 通知对象与升级策略（含备件关联）'),
   dict(n='工单跟踪 Agent', d='SLA 超时自动升级，处理记录结构化'),
   dict(n='复盘 Agent', d='异常 Pareto、复发预警、SOP 修订建议（数据喂给 M1-E）')],
   loop_line='微循环：事件流入 → 分诊 → 派单 → 超时升级 → 关闭，值守循环全程自主',
   gate_line='宏门禁：停线 = 主管；结案确认 = 发起人/主管'),
 dict(f='steps7', names=S7, notes='七步落点：设备/质量/缺料事件流输入、分类与严重度、响应与升级策略、排班/技能/备件/SOP 调用、处理卡+工单+通知、关闭确认与时长统计、停线结案人工。'),
 dict(f='evidence', items=[
   ('AI4I','UCI AI4I 2020（1 万条合成·5 类故障模式）驱动设备告警流'),
   ('≥85%','分诊准确率（ground truth 事件集）'),
   ('≥40%','模拟平均响应时长较人工分诊基线下降')],
   lede='升级策略执行率 100%（无超时遗漏）——值守系统最怕的"漏"，被做成可验证指标。'),
 dict(f='boundary', title='值守塔不碰设备', rows=[
   ('不控制任何设备', '停线、重启仅生成建议并要求人工确认（手册 9.3、FAQ Q13）'),
   ('照片为辅助信号', '分诊不依赖单一模态，降级路径明确')],
   lede='第一备选定位：若 P2/P3 任一受阻即启用；关闭→案例→复发预警的收官模块吸收 M1-E。'),
 dict(f='timeline3', rows=[('初赛 8.16','值守循环骨架页','复赛 9.3','事件面板可运行（回放）'),('决赛 9.22','实时注入 + 照片分诊','联动','与 M1-E 飞轮串联')]),
 dict(f='opensource', rows=[
   dict(n='Andon 事件 schema', d='设备/质量/缺料统一事件模型'),
   dict(n='分诊与升级 DSL', d='规则可解释、策略可配置'),
   dict(n='事件流模拟器', d='AI4I 映射 + 自建事件剧本')],
   risk='通知机器人化 → 分诊可解释面板 + 升级策略输出为核心；照片分诊不稳 → 定位辅助信号。'),
 dict(f='intro8', paras=[
   ('项目名称：','安灯中枢 AndonCop——车间异常响应值守智能体'),('行业赛题：','AI+工业制造'),
   ('目标用户：','机加车间产线主管、班组长与维修工程师'),('核心问题：','设备、质量、缺料异常响应靠现场吼人与微信群，责任漂移、超时无人升级、事后无结构化数据'),
   ('解决方案：','四 Agent 值守：分诊对事件流分类分级（可融合现场照片），调度按技能矩阵与负荷派单并生成升级策略，工单跟踪超时自动升级，复盘输出 Pareto 与复发预警'),
   ('创新点：','事件驱动微循环全程自主，停线与结案由主管拍板；升级策略可解释、可配置'),
   ('开放/复用价值：','开源事件 schema、分诊与升级策略模板、事件流模拟器，可迁移至各类车间'),('当前进展：','方案设计完成，基于公开数据集的原型开发中，提交时附回放演示')]),
 dict(f='review', asks=['值守塔的棕色警戒气质是否成立？','第一备选的定位传达清楚了吗？','与 M1-E 的关系一屏够吗？']),
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
