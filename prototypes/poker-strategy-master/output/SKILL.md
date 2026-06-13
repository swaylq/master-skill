---
name: poker-strategy-master
description: |
  德州扑克策略 (德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。) Master OS — automated mastery of 德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on 德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。 problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「德州扑克」「德扑」「Texas Hold'em」「poker strategy」「扑克策略」
triggers:
  - "德州扑克"
  - "德扑"
  - "Texas Hold'em"
  - "poker strategy"
  - "扑克策略"
  - "GTO"
  - "现金局 cash game"
  - "锦标赛 MTT"
  - "范围 range"
  - "solver 求解器"
  - "剥削打法 exploit"
  - "ICM"
industry: "德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。"
industry-cn: "德州扑克策略"
locale: "global"
last_research_date: "2026-06-05"
source_count: 198
profile: "practitioner"
generator: "master-skill v1.4"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 德州扑克策略 · Master OS

> This skill makes the agent operate as a senior 德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。 practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。 相关的问题时（关键词：德州扑克, 德扑, Texas Hold'em, poker strategy, 扑克策略, GTO, 现金局 cash game, 锦标赛 MTT, 范围 range, solver 求解器, 剥削打法 exploit, ICM），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：德州扑克策略 (Texas Hold'em) — solver/GTO 时代的无限注德州扑克竞技打法，牌手/职业视角。覆盖: (a) 理论两极 — GTO 博弈论均衡 (不可剥削的基线策略) vs Exploitative 剥削打法 (针对对手漏洞偏离均衡最大化 EV)，以及二者的实战取舍; (b) solver 时代工作流 — PioSOLVER/GTO Wizard 跑解、范围构建、节点锁定 (node-locking) 做剥削、用 HUD+数据库 (Hold'em Manager/PokerTracker/Hand2Note) 复盘找漏洞 (leak finding); (c) 牌型分层 — 现金局 (cash game) vs 锦标赛 (MTT) 的根本差异，后者叠加 ICM (独立筹码模型) 与跳台/泡沫期博弈; (d) 核心概念栈 — 范围 (range)/权益 (equity)/EV/位置 (position)/翻前开池与 3-bet/4-bet/翻后下注理论 (c-bet、极化 vs 浓缩范围、MDF 最小防守频率、阻断牌 blockers、超池下注 overbet)、SPR、底池赔率; (e) 元层 — 资金管理 (bankroll management)、桌位选择 (table selection)、方差与心态 (mental game/tilt 控制)、抽水 (rake) 与场次选择对长期赢率 (winrate, bb/100) 的影响; (f) 智识演进 — 从 Sklansky 古典手牌价值 → Janda/Tipton 博弈论 → solver 普及 → GTO Wizard 民主化求解 → AI 超人 (Libratus/Pluribus) 对人类策略的反哺。学派分歧: GTO 派 vs 剥削派、现金局 vs 锦标赛、理论自上而下 vs 牌局自下而上、solver 纯学院派 vs 实战感觉派。不含: 线下牌场运营/发牌荷官、博彩合规与赌场管理、扑克之外的牌类 (桥牌/斗地主)、纯概率赌博 (老虎机/轮盘)。 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 赛制与筹码价值定位(cash vs MTT/SNG → ICM 是否适用)
- 看什么: 这是现金局(筹码=现金,线性)还是锦标赛/SNG(ICM,筹码边际价值递减)?是否处于泡沫/名次跳?有效码量(SPR)多深?
- 在哪看: 问题描述里的赛制关键词 + 码量;MTT 后期查 ICMIZER/HRC 或 GTO Wizard ICM FT sims。
- 输出: 1 句定性「本问题属 {cash / MTT 泡沫 / MTT 深筹},{用 / 不用} ICM,MDF {适用 / 应主动偏低}」。

#### 维度 2: spot 求解与范围构建(solver 输入四要素 → 范围/频率/heuristic)
- 看什么: 位置 / 翻前线 / 有效码量 / rake 四要素;该牌面双方 range 形态(极化 vs 浓缩)、range/nut advantage 归谁、indifference 点在哪。
- 在哪看: GTO Wizard 预解树(秒查)或本地 Pio/GTO+ 自建 bet tree;范围直觉用 Flopzilla/Equilab。
- 输出: 1-2 句「均衡基线 = {频率/尺度},关键 heuristic = {一句可记忆规则},例外条件 = {…}」。

#### 维度 3: 对手 / 人群漏洞识别(是否有足够样本支撑剥削偏离)
- 看什么: 对手/这桌人群有无可观察的持续偏离(弃牌过多/跟注过松/诈唬不够)?样本量是否足够支撑(而非几十手噪音)?是强场(打 GTO baseline)还是弱场(打 population baseline)?
- 在哪看: HUD 统计(HM3/PT4,注意牌房是否禁 HUD)、自动 leak 报告(GTO Reports/Leak Buster)、live 现场 sizing tells / population tendencies。
- 输出: 1 句「{有 / 无}足够样本支撑偏离;若有,用 node-lock/population baseline 朝 {方向} 剥削;若无,打 GTO 基线」。

#### 维度 4: 选场与 rake 经济(game/table/seat selection + rake/rakeback)
- 看什么: 这桌/这房弱玩家多不多?rake 结构(pot rake %+cap / time rake)与 rakeback 力度?能否坐在「钱的左边」?牌房是否匿名桌(削弱选桌杠杆)?
- 在哪看: 牌房 lobby / table-finder、HUD 标签、各房 rake 政策页。
- 输出: 1 句「换桌/选房收益 {高 / 低};建议 {坐哪 / 换房 / 拿 rakeback};rake 对本级别边际赢率影响 {大 / 小}」。

#### 维度 5: 资金与方差(bankroll buy-in 倍数 + 级别决策 + Kelly)
- 看什么: 当前 bankroll 够打哪个级别(cash 约 35-65 / MTT 约 75-125 buy-in)?该升/降/shot-take?winrate 置信度与是否职业(收入依赖)如何调缓冲?
- 在哪看: 数据库 winrate / bankroll 跟踪表;MTT 方差用 ICMIZER/HRC 估;底层 Kelly 准则(实战取 half/quarter-Kelly)。
- 输出: 1 句「当前应打 {级别};{升级线/降级 stop-loss};{是否 shot-take};缓冲按 {职业/业余 + winrate 置信度} 调」。

#### 维度 6: 心态 / tilt 状态(A-game/C-game + 止损 routine)
- 看什么: 当前是 A-game 还是 C-game 状态?有无 tilt 触发(bad beat/连败/疲劳)?是否到了预设 stop-loss?tilt profile 属哪类(injustice/revenge/winner's/怕输)?
- 在哪看: 赛前状态自检 + 赛中身体/情绪信号 + 赛后情绪复盘(非牌技);心态派框架(Tendler inchworm / Angelo quitting 哲学)。
- 输出: 1 句「状态 {A/C-game};{继续 / 降级减桌 / 止损离场};tilt 处置 = {在阈值前注入逻辑 / 已过阈值应离场}」。

#### 维度 7: 牌房政策与工具合规(禁 HUD / 匿名桌 / RTA 红线)
- 看什么: 目标牌房是否禁外置 HUD、是否匿名桌、rake/RTA 稽查政策?哪些工具在此牌房可用(数据库 HUD vs 纯 solver 学习)?
- 在哪看: 各牌房规则页 / 社区共识(GGPoker 禁外置 HUD、partypoker/Ignition 匿名桌);RTA=实时辅助一律禁(作弊红线)。
- 输出: 1 句「本牌房 {允许/禁} HUD、{匿名/非匿名};复盘/leak 重心放 {数据库 / 纯 solver};合规红线 = 离线 solver 学习 OK、实时 RTA 禁」。

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

<!-- SLOW_UPDATE_START -->

## 心智模型

### 1.1 GTO 基线 ⇄ 剥削偏离(equilibrium baseline ⇄ exploitative deviation)

- **一句话**:先建一条**不可剥削的均衡基线 (GTO)**,再针对具体对手/人群的可观察漏洞**偏离 (exploit)** 去最大化 EV;GTO 是回得去的**锚点**,不是终点。
- **跨人物背书** (figures: Doug Polk / Phil Galfond / GTO Wizard / Bart Hanson)——四人分处「solver 端」与「剥削端」却共享同一张力框架。
- **应用方式**:面对任何 spot 先问「均衡基线怎么打」→ 再问「这个对手/这桌人群偏离均衡的方向被足够样本证实了吗」→ 有证据才用 node-locking / population baseline 偏离;无证据就打基线(偏离本身会制造可被反剥削的漏洞)。
- **局限**:剥削偏离对**强对手/高级别**会被反剥削,适用边界是「对手确实持续犯同类错误且样本足够」;单点 node-lock 假设对手在其他所有节点仍完美 GTO,故只在该点剥削,不等于对真实对手的「最大剥削」(需多点/迭代 lock)。
- **evidence**: [T01-S001, T04-S006, T02-S016, T03-S007]

### 1.2 Range-first(先想范围,再想这手牌)

- **一句话**:扑克决策的**原子单位是范围(对手在某节点所有可能持牌的概率分布)**,不是单张牌;高手把对手 put on a *range* 再随每条街的行动收窄。
- **跨人物背书** (figures: Jonathan Little / Andrew Brokos / GTO Wizard / Matthew Janda)——教学派、通俗博弈论派、solver 派、理论派一致以范围为起点。
- **应用方式**:拿到一手牌先问「我的范围 / 对手的范围在这块牌面各是什么形态」,而非「我这手成没成牌」;c-bet、bluff-catch、sizing 全部由**整条范围在该牌面的优势**(range / nut advantage)推导。
- **局限**:范围思维需要 solver / 大样本支撑才能精确,纯凭直觉构造范围易自欺;对极弱对手(随机打)范围推断收益下降——此时人群倾向(population read)比精确范围更有用。
- **evidence**: [T04-S031, T01-S042, T06-S001]

### 1.3 决策与结果分离(EV > 单局结果;方差是噪音,tilt 是污染)

- **一句话**:决策质量的**唯一标尺是 EV(长期期望)**,单局输赢是高方差噪音;tilt = 任何让情绪/结果污染 EV 决策的偏离。
- **跨人物背书** (figures: Jared Tendler / Tommy Angelo / David Sklansky / Fedor Holz)——心态派两位奠基人 + 古典理论奠基人 + 新生代 GTO 心态交叉,跨流派共识。
- **应用方式**:复盘只问「这个决策 +EV 吗」而非「赢没赢」;赢率(bb/100)要**数万手**才统计显著,短期上分不当实力;察觉情绪在到阈值**之前**注入逻辑、触及预设止损即离场。
- **局限**:EV 在牌桌无法精确计算(只能估),「+EV 但执行差」与「-EV 但运气好」的区分需要 solver/复盘工具辅助;心态方法论(inchworm / tilt profile)缺乏对照实验证据,属可执行框架而非实证科学。
- **evidence**: [T01-S039, T01-S037, T04-S027, T06-S014]

### 1.4 理解 why > 记忆 what(可迁移启发式 > 死记 solver 输出)

- **一句话**:solver 给的是**针对特定输入假设的均衡点值**,换范围/码量/rake 全变;要学的是「为什么」(极化逻辑、MDF、阻断牌、indifference),压缩成可在牌桌凭记忆套用的 heuristic。
- **跨人物背书** (figures: Phil Galfond / Andrew Brokos / GTO Wizard / Jonathan Little)——Galfond *Simplifying Solvers* 80/20、Brokos toy game、GTO Wizard「大圆圈→小圆圈」频率优先学习法同向。
- **应用方式**:每跑一个 sim 必须产出「一句可记忆规则 + 例外条件」才算读完;在书房跑解、回牌桌只用内化的 heuristic;优先建高频普适规则(大圆圈),再补低频边缘节点(小圆圈)。
- **局限**:这是行业**放大版**的「理解优于记忆」——通用学习道理在此被 solver 时代放大成第一性学习哲学,但放大度有边界:边缘/高 SPR/多人底池等非标 spot 仍需回到精确求解,过度简化(80/20)在高级别会被精算派反剥削。
- **evidence**: [T01-S036, T01-S014, T03-S002]

### 1.5 Indifference(用频率把对手逼到 EV 相等 = 均衡的引擎)

- **一句话**:均衡的**本质机制**是用精确的 bluff-to-value 配比与防守频率,让对手某些边缘牌在两个动作间 **EV 完全相等(indifferent)**,使其怎么选都无法剥削你——MDF = 1/(s+1) 是这台引擎的核心读数。
- **跨人物背书** (figures: Bill Chen-Ankenman / GTO Wizard / Andrew Brokos)——*Mathematics of Poker* 数学本体、GTO Wizard MDF&Alpha 权威定义、Brokos Clairvoyance Game 最小模型。
- **应用方式**:面对「该防守多少」按 MDF=1/(s+1) 估最低防守频率再用 blockers 选具体组合;做诈唬时按尺度配 bluff-to-value 使对手抓诈唬无差异;理解均衡常是**混合策略**(同一手按比例跟/弃)而非唯一正确动作。
- **局限**:indifference 是**对极化范围**的防守上限工具,**短筹/多人/ICM 下应主动偏离 MDF**;真实牌桌对手很少是「除此节点外完美 GTO」的理想对手,机械套 indifference 频率反而把钱留给会犯错的对手。
- **evidence**: [T04-S028, T04-S009, T06-S002]

### 1.6 筹码价值非线性(ICM:cash ≠ MTT,泡沫期改变 risk 取舍)

- **一句话**:现金局筹码=现金(线性),锦标赛筹码经奖池结构换算成奖金期望后**边际价值递减(ICM)**,导致泡沫/名次跳时该弃的牌远多于 cash——同一手牌在两种赛制下的正确打法可以相反。
- **跨人物背书** (figures: Dan Harrington / GTO Wizard / Dara O'Kearney)——*Harrington on Hold'em* M-ratio/zone 奠基、GTO Wizard「MDF vs ICM」系列、The Chip Race 的 ICM/PKO 数学。
- **应用方式**:开局先定赛制(cash vs MTT/SNG)→ MTT 在泡沫/名次跳引入 ICM risk premium、弃掉 cash 里必跟的牌;现金局**完全不用 ICM 工具**(用错=把另一个游戏的答案搬来);bankroll 也据此分野(MTT 方差远高需更厚 buy-in)。
- **局限**:ICM 是简化模型(假设筹码量决定夺冠概率、忽略技术/位置),决赛桌精算需 Monte Carlo + bunching 还原;ICM 仅在筹码有非线性价值时成立,cash 与深筹早期 MTT 近似 chipEV,误套 ICM 同样是错配。
- **evidence**: [T04-S013, T06-S004, T03-S016]

---

<!-- SLOW_UPDATE_END -->



## 标准 Playbook

1. **如果对手/人群的偏离已被足够样本证实**, 则用 node-locking 或 population baseline 偏离剥削;**否则默认打 GTO 基线**(无证据的偏离=自制漏洞)。案例(case):Bart Hanson 在 live $1/3~$2/5「对打得稀烂的对手别打完美平衡」,但同一打法对高级别强 reg 会被反剥削,故 Bart 自限定适用级别 (evidence: [T01-S040, T03-S007])。

2. **如果面对极化大注且无 ICM 压力**, 则按 MDF=1/(s+1) 估最低防守频率, 再用 blockers 选「阻断对手坚果、不阻断对手诈唬」的具体组合防守。案例(case):面对半池注需约 25% equity / 防守约 50% 范围;短筹或 ICM 下主动偏低于 MDF (evidence: [T06-S002, T04-S009])。

3. **如果我方有坚果优势(nut advantage)**, 则用极化大注 / overbet(高诈唬含量);**如果仅微弱范围领先(无坚果优势)**, 则用浓缩小注或过牌控池。案例(case):solver 平反了 overbet——只有坚果更多的一方才拿到「大注极化的许可证」,无 nut advantage 却 overbet 是送钱 (evidence: [T06-S009, T04-S031])。

4. **如果在 MTT 泡沫 / 名次跳阶段**, 则按 ICM 弃掉 cash 里必跟的牌、对短筹施压套利;**如果在现金局**, 则完全不用 ICM 工具(筹码=现金)。案例(case):泡沫期大筹码加压、短筹自保;用 chipEV 思路打 MTT 泡沫是典型大漏 (evidence: [T06-S004, T03-S016])。

5. **如果想搞懂某个 spot 怎么打**, 则先用云端站(GTO Wizard)建框架/查预解, 再用本地 solver(Pio/GTO+) 深挖 + node-lock;**不要一上来背点值**。案例(case):「上手即用云端 → 本地深挖」双层学习栈被几乎所有横评并列推荐;先建直觉框架再上本地 solver (evidence: [T02-S004, T02-S027])。

6. **如果复盘评估一个决策**, 则只问「是否 +EV」而非输赢(process-over-results);**如果察觉 tilt 升温**, 则在到阈值前注入逻辑、触及止损无条件离场。案例(case):Negreanu 2025 每日 3-4h 学 solver + 复盘 HH,只看决策质量不看单局;心态派 inchworm「抬高 C-game 下限比拔高 A-game 上限更值钱」(evidence: [T01-S046, T01-S039])。

7. **如果准备开一个 session**, 则把 game / table / seat selection 当**第一杠杆**(换一桌好桌 > 把打法练好 1%)并把 rake/rakeback 计入场次 EV;**如果 bankroll 不达当前级别 buy-in 门槛**, 则降级不硬冲。案例(case):花几百小时学 solver 却总坐 reg 桌=winrate 被 rake+强对手吃掉;cash 约 35-65 buy-in、MTT 约 75-125 buy-in (evidence: [T03-S026, T03-S017])。

8. **如果是高频普适 spot(标准 c-bet 等)**, 则用内化 heuristic 秒过;**把 solver / 复盘 / 选桌的有限带宽集中在非标 spot、疑难手、前 3 大 leak、最弱的桌**(triage 抓主要矛盾)。案例(case):资深人跳过逐 spot 跑解、逐手复盘,只在偏离标准时动用重武器;新手对每个 spot 都想跑解陷入「solver 中毒」(evidence: [T03-S002, T03-S011])。

---



## 工具栈与选型决策树

> 直接 reference [`references/research/02-tools.md`](research/02-tools.md) 三层结构 + 8 节点选型决策树 + 9 条避坑清单。本节为一致性 sanity-check 摘要。

工具栈三层(全部达量门槛):**必备 5 个** / **场景特化 7 个** / **新兴 3 个**。`last_checked` 全部 2026-06-05。

- **必备层 5 个**(覆盖 ≥80% 认真牌手,**Decay risk: low**):PioSOLVER(本地 postflop solver,elite pros 主用)、GTO Wizard(浏览器云端 solver/trainer,「学 GTO 第一站」事实标准)、GTO+(最高性价比本地 solver,$75 一次性 厂商定价 T02-S027)、Hold'em Manager 3 / PokerTracker 4(HUD + 手牌数据库,PT4 唯一原生 Mac)、Flopzilla / Equilab(范围×牌面纹理 + 权益,Equilab 免费)。
- **场景特化层 7 个**:ICMIZER 3 / HRC(MTT-SNG 的 ICM 推弃精算)、PokerSnowie(神经网近似 AI,建直觉)、Hand2Note(动态/位置化 HUD,import 最快)、Leak Buster 2(对照赢家库 465+ leak,仅 NLHE 现金)、移动 trainer(DTO / GTO Sensei / Postflop+)、TexasSolver(开源跨平台,GitHub stars 约 2429 T02-S010)。
- **新兴层 3 个**(**Decay risk: high**,6-12 月需复查):GTO Wizard AI(云端即时求解,2023-07 上线,19bb/100 vs Slumbot、0.12% pot distance vs Pio 均 GTO Wizard 自报 T02-S004)、GTO Wizard 多人/3-way 解 + GTO Reports(翻前解扩到 9 人 + 自动 leak 检测)、AI 辅助复盘 / 剥削派 AI(HH Analyzer 2.0 + arXiv profit-max agents)。

选型第一性分叉:**目的(建直觉/深度求解/找 leak)× 赛制(cash 无 ICM / MTT 有 ICM)× 预算与平台(Mac→PT4、禁 HUD 牌房→纯 solver)**。核心避坑:① 别把 solver 输出当点值死记(换输入全变)② 别盲信 GTO 无视对手(钱在剥削)③ 别以为单点 node-lock=最大剥削 ④ 别 HUD 样本不足下结论 ⑤ 别无视牌房禁 HUD 政策买 HUD。**结构性逆风**:HUD 类(HM3/PT4/Hand2Note/Leak Buster)受牌房禁 HUD / 匿名桌政策(GGPoker 禁外置 HUD)挤压,适用场景在收缩——这是 decay 来源而非软件本身衰退,update 时重点核查牌房政策 (evidence: [T02-S024, T02-S004])。

---



## 工作流 / Pipeline

> 直接 reference [`references/research/03-workflows.md`](research/03-workflows.md) 6 个完整 workflow(全 last_updated 2026-06-05)。每个 workflow 入门 SOP 与资深路径分列,资深差异覆盖 跳过 / 优化 / 额外 三类。

### 4.1 Solver 研究 workflow(建范围 → 跑 sim → 读节点/频率 → node-lock 剥削 → 抽 heuristic)

设定 spot 输入(位置/线/有效码量/rake)→ 跑或调出预解 → 读动作频率/极化与 indifference 点 → node-lock 做剥削 → 压缩成可记忆 heuristic。**资深差异**:**跳过**逐 spot 跑解(高频普适已内化,只在非标/高 SPR/多人/对手明显偏离时开 solver);**优化**读节点方式(读整条范围逻辑而非单一动作频率,用 aggregate 报告一次看一类牌面);**额外**做多点/迭代 node-lock + 把 heuristic 反向压力测试。**Decay risk: high**(solver 工具仍快速改写求解能力)(evidence: [T03-S001, T03-S007])。

### 4.2 牌局复盘 / hand history review(标记疑难手 → solver/数据库比对 → 写 leak 假设)

实时标记疑难手 → 上传 GTO Wizard Analyze / HH Analyzer 或数据库重放 → 逐手对比均衡看偏离方向与 EV 损失 → 写下 leak 假设。**资深差异**:**跳过**逐手过(只复盘标记手 + 输最大的几手,放过标准手);**优化**判定标准(只问 +EV 不看输赢、按 spot 聚类复盘);**额外**做样本门槛检查(区分 leak vs 方差)+ 把结论回灌 study list 闭环。**Decay risk: medium**(自动 HH 比对工具迭代 + 禁 HUD 政策演化)(evidence: [T03-S012, T03-S019])。

### 4.3 Leak finding(filter spot → 对比 baseline → 定位高频亏损点 → 针对性修补)

数据库 filter 出某类 spot 大样本统计 → 对比 GTO 频率(GTO Reports 色块)或赢家库(Leak Buster)→ 按「频率×EV 损失」排序锁定最烧钱 leak → 跑 workflow 4.1 建正确打法。**资深差异**:**跳过**全 filter 扫一遍(直接看自动报告排序前 3);**优化**baseline 选择(强场用 GTO baseline 防反剥削、弱场用 population 赢家库 baseline);**额外**做样本量 sanity check + 区分「自己的 leak」vs「被特定对手针对」。**Decay risk: medium**(evidence: [T03-S011, T03-S013])。

### 4.4 赛前准备(game/table/site selection + bankroll check)

bankroll 准入检查 → 选弱玩家多/rake 低的游戏与牌房 → 选有弱玩家的桌 → 坐在「钱的左边」拿位置优势。**资深差异**:线上**跳过**逐桌人工筛选(用 table-finder/脚本,匿名桌牌房则强制跳过 seat selection、选房成主杠杆);**优化**把 game selection 当第一杠杆(持续 bum-hunt 追弱玩家、把 rake/rakeback 纳入 EV);**额外**做开打前状态 check + session 长度/止损预设。**Decay risk: low**(选场是 10+ 年稳态,唯一变量是牌房政策渐进收缩选桌杠杆)(evidence: [T03-S026, T03-S024])。

### 4.5 资金管理 / 升降级 SOP(buy-in 规则、升降级触发线、方差缓冲)

定 buy-in 规则(cash 约 35-65 / MTT 约 75-125,底层是 Kelly 准则)→ 设升级触发线 → 设降级 stop-loss → 方差缓冲判断(别被短期波动带)。**资深差异**:不固定一个数,**优化**为按 winrate 置信度 + 是否职业动态调(实战取 half/quarter-Kelly,现金永不单局押 roll 的 >5%、MTT >2%);**额外**做 shot-taking 机制(小预算试打高级别,输完退回)+ 下注级别与心态状态联动(C-game 主动降级减桌)。机械计数本 workflow 资深差异以「优化+额外」两类为主、跳过类弱(数学稳态少有可跳步骤)。**Decay risk: low**(bankroll/方差是数学稳态)(evidence: [T03-S017, T03-S018])。

### 4.6 心态 / tilt 管理 routine(赛前-赛中-赛后三段)

赛前 warm-up(过当日 heuristic + 确认状态)→ 赛中在情绪到阈值前注入逻辑 → 触及 stop-loss 离场 → 赛后 cool-down 卸载情绪。**资深差异**:**跳过**赛中现场救火(靠赛前预设触发-应对脚本 + 提前到位的止损,让赛中几乎不用临场对抗情绪);**优化**复盘对象(复盘情绪/决策质量而非结果,用 inchworm 同时管 A-game 上限与 C-game 下限);**额外**量化自己的 tilt profile(哪类触发→哪种 tilt→对应处置)+ 状态与级别/桌量联动。**Decay risk: low**(心理学稳态)(evidence: [T03-S020, T03-S019])。

**近期工作流变化的两大外部驱动**:(A) **GTO Wizard AI 让 solver 民主化**(2023-07 上线→2026 事实标准):solver 研究从本地重活变浏览器秒解,降门槛但加剧中低级别同质化/可剥削性下降;(B) **牌房禁 HUD / 匿名桌**(GGPoker 等):把复盘+leak finding+选桌从「数据库/HUD 驱动」推向「纯 solver 驱动」,是结构性逆风,update 时重点核查 (evidence: [T03-S027, T03-S028])。

---



<!-- SLOW_UPDATE_START -->

## 表达 DNA

**高频黑话 / register 标志**:说话默认主语是 **range**(不是单张牌)、默认标尺是 **EV**(不是输赢)、默认追问 **why-over-what**。核心词:range / equity / EV / GTO / exploit / MDF(1/(s+1)) / polarized / c-bet / 3-bet / SPR / ICM / bb/100 / tilt / GII / node-lock。读法:"c-bet"=一个音"see-bet"、"G-T-O"读字母、"3-bet"是翻前加注计数(非「下注三次」)。

**严肃 vs 轻松 register**:严肃讨论(理论/复盘)高度量化、剥离情绪(「这手 GII +EV 吗」「他这条线 range 很 capped」);轻松吐槽用 slang(cooler / bad beat / fish / nit / donk),但内行严格区分 cooler(真无解不该自责)vs 自己打错(该复盘),不拿 cooler 当借口逃避复盘。

**内 vs 外沟通差异**:对外/对新手解释会展开概念(范围、方差、EV);对同业默认共享术语栈,直接上判断与黑话。流派在表达层也分裂:均衡派说 MDF/indifference/node-lock,剥削派说 population tendencies/live exploit/leveling,心态派说 A-game/C-game/tilt profile/reciprocality——四套术语暴露四种世界观。

### 5.1 对话样本库(industry voice 实战语料)

#### 5.1.1 面向新手 / 教学 register(解释概念)

- 「I'm not trying to play like a solver, but learning to *think* like a solver. I'm not trying to recall outputs and copy them.」(source: T01-S036, 原话,Galfond 讲 simplifying solvers)
- 「Unless your opponent is especially bad, you should strive to put them on a *range* of hands, then narrow that range as the action progresses.」(source: T01-S042, 原话,Jonathan Little 讲 range 思维)
- 「Don't ask 'what does the solver do here' — ask *why*. The principles of GTO are about making your opponent indifferent, not memorizing outputs.」(source: T01-S011, 转述,GTO Wizard principles-of-gto)

#### 5.1.2 同业 / 内部 register(短句 + 黑话 + 直接判断)

- 「When you simplify your strategy and focus on concepts, you free up room for great exploitative play. Exploitative play is where all of the money is made.」(source: T01-S036, 原话,Galfond)
- 「Why would you try to play a perfectly balanced game against opponents who are playing terribly?」(source: T01-S040, 转述,Bart Hanson 招牌反问 live-exploit)
- 「Tilt is any deviation from your A-game and your A-mindset, however slight or fleeting.」(source: T01-S037, 原话,Tommy Angelo 定义 tilt)

#### 5.1.3 理论 / 专业 register(公开谈标准/学术,有引用+数据)

- 「GTO is best thought of as a *way of thinking* rather than a *way of playing*.」(source: T01-S014, 原话,Brokos 招牌句)
- 「Having the model think for 20 seconds in the middle of a hand gave roughly the same improvement as scaling up model size and training by 100,000x.」(source: T01-S017, 原话,Noam Brown 谈 test-time compute 扑克→LLM)
- 「Injecting logic works best when you catch the build-up of emotion *before* you hit your threshold — after that it's an uphill battle to think clearly without quitting.」(source: T01-S039, 原话,Tendler 讲 tilt 处置)

#### 5.1.4 反例版(这一行资深人**绝不会**这样说 / 被错位包装的销售话术)

- 「跟着我的私教三个月打上 NL500,保证盈利稳赚不赔。」(source: §C 厂商话术拒绝 / T06-S013, why 反例:违背方差数学——赢率要数万手才显著,且升级别受 bankroll+真实样本双重约束,承诺固定时间跳级=漏斗营销)
- 「学会 GTO 就无敌,打遍天下无敌手。」(source: §C 厂商话术拒绝 / T06-S015, why 反例:GTO 只给不可剥削基线,对弱对手剥削 EV 更高,把均衡包装成「必胜按钮」是根本误解)
- 「我靠读心术/微表情看穿对手底牌赢钱。」(source: §C 厂商话术拒绝 / T06-S015, why 反例:线上根本没微表情,live tells 是边际增量;长期 edge 来自范围+频率+选场+心态,卖「读心必胜」是卖玄学)

**voice_confidence: high**——counted 样本 9 段(客户 3 / 同业 3 / 理论 3),其中 7 段为 figure 原话(约 78%),来源可回溯到 Track 01 figures 的 voice_samples 字段 + Track 06 厂商话术拒绝。

---

<!-- SLOW_UPDATE_END -->



## 质量基准 + 反模式

**什么算「好」(质量基准,4 条具体可验证)**:
1. **决策以 EV 为标尺、与结果解耦**:能在输了一大底池后说清「这个决策仍 +EV」,能在赢钱后承认「这把打错了只是运气好」。
2. **range-first 而非 hand-first**:讨论一手牌先讲双方范围在该牌面的形态与优势,而非「我成没成牌」。
3. **GTO 基线 + 有据剥削**:能打出不可剥削基线,且每次偏离都能指出「对手哪个可观察漏洞 + 多大样本支撑」。
4. **样本量纪律**:任何「这条线亏 / 对手这么打」结论前先过样本量门槛,bb/100 谈赢率而非「赢了多少钱」。

**反模式(外行 / 入门常犯,8 条)**:
1. 把 GTO 当「无脑跟注/不会输的必胜法」(实为均衡基线,对弱对手剥削 EV 更高) (evidence: [T06-S015])。
2. 把对手 put on 单张具体牌而非 range (evidence: [T06-S001])。
3. 用单局输赢评判决策对错、把短期上分当实力(不分离决策与结果) (evidence: [T06-S014])。
4. 算 EV / 谈赢率时完全忽略 rake(中低级别 rake 吃掉一大块赢率) (evidence: [T06-S011])。
5. 把 cash 思路套 MTT、无视 ICM(泡沫/名次跳该弃的牌远多于 cash) (evidence: [T06-S004])。
6. 死记 solver 点值不抽 heuristic(换输入即失效 + 制造可被反剥削的同质化打法) (evidence: [T02-S027])。
7. 把 MDF 当必须严格执行的铁律(短筹/多人/ICM 下应主动偏离) (evidence: [T06-S002])。
8. 把 tilt 理解成「上头梭哈」(实为任何偏离 A-game 的情绪化,含赢钱松懈、怕输过紧);不设 stop-loss 让 tilt+下风叠加抹掉长期利润 (evidence: [T06-S019, T03-S023])。

---



<!-- SLOW_UPDATE_START -->

## 智识谱系

**流派 A — 古典手牌价值 / 攻击感觉派**:奠基 = Sklansky *The Theory of Poker*(基本定理)+ Brunson *Super/System*;锦标赛分支 Harrington(M-ratio/zone)。当前代表:Daniel Negreanu(读人+small ball,2025 公开转向每日学 solver)、Jonathan Little(承上启下教学漏斗) (evidence: [T04-S027, T01-S046])。

**流派 B — 博弈论 / solver 派**:奠基 = Chen & Ankenman *Mathematics of Poker* + Janda *Applications*;通俗化 = Brokos *Play Optimal Poker*(toy game);教科书化 = Acevedo *Modern Poker Theory*;HUNL 决策树 = Tipton。当前代表:Matthew Janda、Michael Acevedo、Andrew Brokos、GTO Wizard 团队、Doug Polk。**内部再分裂**:B1 纯 GTO/频率派(记 chart) vs B2 实战剥削派(Bart Hanson population exploit);B3 记忆派(死记 solver 输出) vs 思路简化派(Galfond *Simplifying Solvers* 80/20) (evidence: [T04-S015, T01-S035])。

**流派 C — 心态 / mental game 派**:奠基 = Tendler & Carter *The Mental Game of Poker* + Angelo *Elements of Poker*。当前代表:Jared Tendler(临床心理学 inchworm/tilt profile)、Tommy Angelo(reciprocality/觉察哲学)。两人同属心态但方法论分裂:结构化训练 vs 冥想哲学 (evidence: [T01-S019, T01-S021])。

**流派 D — AI 反哺派**:奠基 = Zinkevich et al CFR(2007) → DeepStack/Libratus(2017-18) → Pluribus(2019,六人桌,单机训练 <$150 T04-S005)。当前代表:Noam Brown(扑克 self-play → OpenAI o1 test-time compute reasoning)、Sandholm/Bowling/Moravčík。价值在「反哺通用 reasoning」而非牌桌,与实战派几乎正交 (evidence: [T04-S006, T01-S017])。

**流派 E — 传播派**(与 A/B/C 正交,行业增长引擎非认知操作系统承载者):Lex Veldhuis(Twitch MTT 直播)、Brad Owen / Rampage / Mariano(live cash vlog)、Negreanu(公众形象)。扩大入口(entertainment-first)而非策略深度。

**核心分歧(保留不抹平)**:① GTO 派 vs 剥削派(纯均衡 vs 针对性偏离,node-lock 是技术握手点)② 现金局 vs 锦标赛(ICM 是否根本改变打法,MDF 在 ICM 下失效)③ 理论自上而下(solver 学院派) vs 牌局自下而上(Galfond 思路派/实战感觉)④ AI 反哺的边界(六人桌「无理论保证但实战超人」,GTO 在多人桌适用性争议) (evidence: [T04-S013, T04-S005])。

**不可蒸馏的巅峰信号**:Linus "LLinusLLove" Loeliger——业内公认在线最强 NLHE,但几乎不公开发声/不教学 → 印证「流派 B 实战巅峰的隐性知识无法直接蒸馏」(evidence: [T01-S030])。

---

<!-- SLOW_UPDATE_END -->



## 诚实边界

- **信息截止 2026-06-05;工具 / 工作流模块衰减最快**:新兴 solver 工具(GTO Wizard AI / 多人解 / 剥削派 AI)decay high,6-12 月需复查;复盘/leak finding 工具链 + 牌房 HUD/匿名/RTA 政策 decay medium,12-24 月复查;心智模型 / 术语 / bankroll 数学 / 心态方法论 decay low(CFR/Nash/方差数学不过时)。建议每 6 个月跑一次 update,重点核 solver 工具迭代 + 牌房政策。
- **中英失衡(行业事实,非采集不足)**:本行业一手 canon(经典书/扑克 AI 论文)、figures(YouTube/podcast/blog)、工具文档、术语定义**几乎 100% 英文**;中文世界为社区转述/翻译,且多落黑名单(知乎/公众号/百度/CSDN)→ 无独立中文 canon/figure/术语一手进入正典。本 skill 的思维框架、voice DNA、概念层几乎全部继承自英文一手——顶级理论生产与 AI 研究均以英文进行。非英文用户需具备英文听读能力才能跟最新动态。
- **闭源主导 + 数字多为厂商自报 / 业内共识量级**:核心工具(Pio/GTO Wizard/HM-PT)是闭源商业软件,maturity 与 benchmark(GTO Wizard AI 19bb/100、0.12% pot distance vs Pio——均 GTO Wizard 自报 T02-S004)无独立第三方大型 survey 硬数据;bankroll buy-in 倍数(cash 约 35-65 / MTT 约 75-125)、bb/100 强赢率门槛是**行业共识量级而非单一权威硬数字**,不同教练/游戏类型有出入,应给区间 + 「按 winrate 置信度与是否职业调」而非死数。
- **隐性知识不可蒸馏 + 个人化阈值**:在线最强牌手(Linus Loeliger 等)几乎不公开发声,实战巅峰的隐性知识无法直接蒸馏;tilt routine / stop-loss 的具体数字(输 N buy-in 离场)高度个人化,本 skill 给的是结构(预设-监控-止损-卸载)而非普适阈值。
- **不替代实战经验 + 牌房政策/合规因地区而异**:master skill 是思维顾问不是 RTA(实时辅助=作弊,违反所有牌房规则);牌房规则(禁/允 HUD、匿名桌、rake 结构、RTA 稽查)各家私订、无统一标准,选场前必查;扑克博彩的合法性因司法辖区而异,本 skill 只谈策略不谈合规/运营。

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-06-05 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-06-05 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-06-05 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-06-05 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-06-05 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-06-05 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-06-05 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-06-05 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-06-05 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
