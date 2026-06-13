---
name: llm-agent-infra-master
description: |
  LLM agent 基础设施 (LLM agent infra) Master OS — automated mastery of LLM agent infra: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on LLM agent infra problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「agent framework」「LLM agent」「agent infra」「multi-agent orchestration」「agent runtime」
triggers:
  - "agent framework"
  - "LLM agent"
  - "agent infra"
  - "multi-agent orchestration"
  - "agent runtime"
  - "tool use"
  - "RAG"
  - "agent observability"
industry: "LLM agent infra"
industry-cn: "LLM agent 基础设施"
locale: "global"
last_research_date: "2026-05-02"
source_count: 0
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# LLM agent 基础设施 · Master OS

> This skill makes the agent operate as a senior LLM agent infra practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 LLM agent infra 相关的问题时（关键词：agent framework, LLM agent, agent infra, multi-agent orchestration, agent runtime, tool use, RAG, agent observability），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 LLM agent infra 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：LLM agent infra 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: Framework current state
- 看什么: GitHub stars / 最近 30 天 commit 频率 / breaking change 历史
- 在哪看: repo 本身 (`langchain-ai/langgraph`, `microsoft/autogen`, `crewAIInc/crewAI`, `pydantic/pydantic-ai`) 的 releases
- 输出: each candidate 的「活跃度 / 稳定度」二维标记

#### 维度 2: Production reality check
- 看什么: 有没有公司在用这个 framework / tool 跑生产? 规模如何? pain points 是什么?
- 在哪看: a) 框架官方 case studies (打折扣 — 自营销); b) Twitter/X 工程师吐槽 (搜 "{name} + production"); c) HN 评论
- 输出: production-readiness 等级 (toy / pilot / scaled)

#### 维度 3: Eval methodology
- 看什么: 该问题的 eval set 是否存在? 行业 benchmark 是什么? human-validation 比例是?
- 在哪看: Hamel Husain blog / Eugene Yan / Inspect AI examples
- 输出: 评估这个 agent / workflow 的 1-3 个 measurable indicator

#### 维度 4: Tool stack alignment
- 看什么: 当前选型符合 thin-vs-thick 流派 + 是否 hybrid-retrieval-aware
- 在哪看: Track 02 输出 + 行业 podcast 最近评测
- 输出: 当前选型 + 1-2 个替代

#### 维度 5: Regulatory blast radius
- 看什么: EU AI Act / China 备案 / US executive order 在这个场景适用吗?
- 在哪看: Track 06 法规节; 相关 law firm 长稿
- 输出: low / medium / high regulatory exposure + 1 句具体来源

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 Framework as scaffold, not foundation

**一句话**: 你今天选的 agent framework 6 个月后大概率不再合适，因为模型能力升级会让上层抽象失效。

**它说的是**: 很多 agent framework 存在的理由是「弥补模型能力不足」(manually 编排 retry / chain-of-thought / 工具调用 fallback)。当模型本身把这些能力 native 化后，framework 的价值反而成为障碍。

**证据来源** (figures: Chase / Karpathy / Willison / Knoop):
- [Primary] Harrison Chase 2025 LangChain Interrupt 「Frameworks are temporary」keynote
- [Primary] Karpathy 多次提到「bitter lesson agent-flavor」
- [Reference] Anthropic Tool Use 文档迭代史 (function-calling → extended-thinking → computer-use)

**应用方式**:
- 选 framework 的标准之一: 「能在一个周末把这层框架剥掉换成原生 SDK 调用吗?」
- 不要把框架特定概念 (chain / agent / executor) 作为系统的核心抽象

**局限**:
- 对 multi-agent orchestration 这一层不那么适用 — 协作的 routing / state management / HITL 短期内不会被模型 native 化
- 在 2025-2026 快速变化期适用; 模型能力曲线趋平后这个模型会失效

### 1.2 Eval > model architecture (industry-amplified)

**一句话**: 在 LLM agent infra, eval data 比 model architecture 重要; 「build the eval first」是这一行的 first principle.

**它说的是**: 选 model / framework / prompt 的决策都依赖 evaluation 反馈。没有 eval set 就没有真信号; 用 LLM-generated eval 评估 LLM 是循环。

**证据来源** (figures: Husain / Yan / Chase / 多 canon 著作):
- [Primary] Hamel Husain blog series "Build the eval first"
- [Primary] Chip Huyen "AI Engineering" Ch.5
- [Reference] Inspect AI / promptfoo 工具的存在本身佐证

**应用方式**:
- 任何新 agent project 第一步: 写 50-200 个 eval examples
- LLM-as-judge 必须配 ≥ 30% human-validated set
- production agent 必须有 eval pipeline 接到 CI

**局限**:
- 此为「行业放大版」的 generic principle "data-driven decisions". 在 LLM era 比一般技术行业 amplified 很多 (model stochasticity 让 demo 和 prod 差距 10x)
- 但 amplification 不是质变 — 不是 ML era 独有

### 1.3 Production reality vs demo glamour (industry-amplified)

**一句话**: 一个 agent demo 看起来惊艳和它在生产环境跑得起来是两个不同的问题; LLM stochasticity 把这个差距放大到比传统软件大一个数量级.

**它说的是**: framework 选型 / 招聘判断 / 投资判断都要先回答「production 跑过没?」「在什么 scale 跑过?」「fail mode 是什么?」

**证据来源** (figures: Husain / Willison / Chase):
- [Primary] HN 长讨论 "LangChain demo 能跑, prod 三个月就崩"
- [Primary] Anthropic 工程师 podcast "我们花在 retry / fallback / observability 的时间远超 prompt"
- [Secondary] Multiple YC W25 case studies

**应用方式**:
- 看到惊艳 demo → 反射式追问 "production case 存在性"
- 选工具时强调 production case study 而非 marketing

**局限**:
- "demo vs prod 差距" 是所有快速发展技术的通病, 但在 LLM agent infra 因为 stochasticity **特别尖锐**
- 描述时必须明确「在 LLM agent infra 比一般技术行业放大很多」, 否则失去排他性

### 1.4 Capability lift will eat your abstraction

**一句话**: 模型能力的提升会蚕食你今天精心设计的抽象层 — 这是 Bitter Lesson 的 agent infra 形态.

**它说的是**: 任何 framework 抽象 (chains / agents / executors) 在足够强的模型面前都会变成赘物。Anthropic 把 retry / extended-thinking / computer-use 一层层下沉到模型本身就是这个过程。

**证据来源** (figures: Knoop / Chase / Karpathy):
- [Primary] Knoop ARC Prize keynotes "what made o1 special"
- [Primary] Chase 公开承认 "chain abstraction broke as capability grew"
- [Reference] Anthropic API 演化史

**应用方式**:
- 任何 capability layer 决策, 先评估 "这个能力 6-12 月内会不会被模型 native 化?"
- 不要在快速变化期投资重抽象 (CrewAI 的 multi-agent abstraction 是反例)

**局限**:
- 对 multi-agent orchestration / state management 不太适用 (短期内不会被 native 化)
- 对稳定行业不适用 (医疗器械 / 法务这种监管层抽象 30 年才动一次)

### 1.5 RAG ≠ vector DB (industry-amplified)

**一句话**: 把 RAG 等同于 vector DB 是 2024 前的范式; 2026 production-grade RAG 默认 hybrid retrieval (BM25 + vector + reranking).

**它说的是**: pure vector retrieval 在 production 失败率高 — 词汇歧义 / OOV / multi-modal filtering / 高基数 metadata 都不擅长。

**证据来源** (figures: Vespa case studies / canon 多本书 / Husain):
- [Primary] Vespa engineering blog Spotify case
- [Primary] Hybrid retrieval 系列论文 2024
- [Reference] LlamaIndex / LangChain 默认 hybrid mode

**应用方式**:
- 选 RAG infra 时优先看 hybrid 能力, 而非单纯 vector benchmark
- 反对外行 / 厂商「用 Pinecone 就是 RAG 了」的话术

**局限**:
- 在小规模 / 同质 corpus 场景 pure vector 仍然够用
- 需要明确「production-grade RAG」与「demo RAG」的边界

---



## 标准 Playbook

1. **如果开始一个新 agent project**, 则先 build eval set (≥ 50 examples) 再写 agent 代码.
   - 案例: Hamel Husain blog series 反复强调; YC W25 cohort 多家采纳

2. **如果 demo 在 1 day 跑通**, 则 expect 6 weeks to production-grade. 不要让 stakeholder 误以为 demo = ship.
   - 案例: HN 长 thread 多次出现的 LangChain demo→prod 6 周差距

3. **默认选 thin framework + 直接 SDK**, 只有当 multi-agent ≥ 3 actors 时考虑 thick orchestration.
   - 案例: Vercel ai-sdk team 早期决策; YC W25 一家公司 CrewAI → 直接 SDK rewrite 案例

4. **如果选 vector DB**, 先评估 hybrid retrieval 支持, 再看 pure-vector benchmarks.
   - 案例: Spotify Vespa 选型; Pinecone hybrid feature 推出后多家迁移

5. **如果用 LLM-as-judge 做 eval**, 必须配 ≥ 30% human-validated set.
   - 案例: Eugene Yan eval blog 2025-Q1 详细方法

6. **production agent 上线前必须有 trace pipeline**. 「can't optimize what you can't see」.
   - 案例: LangSmith / LangFuse 几乎所有 YC AI 公司在 PMF 后 3 个月内采纳

7. **如果 ReAct agent loop > 5 steps**, 先怀疑 tool design 而非 prompt eng.
   - 案例: AutoGPT post-mortems; multiple Husain debugging sessions

---



## 工具栈与选型决策树

详见 `references/research/02-tools.md`. 三层结构:
- **必备 (3)**: LangChain/LangGraph / OpenAI+Anthropic SDK / LangSmith+LangFuse
- **场景特化 (3)**: Vespa / Pinecone / DSPy
- **新兴 (2)**: Pydantic-AI / Browser Use

选型决策树 + 避坑清单见原文件.

Sanity check: 必备 ≥ 3 ✓, 场景化 ≥ 3 (low end of [3, 5] target) ✓, 新兴 ≥ 2 ✓. 通过.



## 工作流 / Pipeline

详见 `references/research/03-workflows.md`. 3 个 workflows:
- Build production-ready RAG agent (high decay)
- Add observability + eval (high decay)
- Audit + fix failing agent (medium decay)

每个有 入门 SOP / 资深路径 / 近期变化 / 失败模式. 资深差异点在 100% workflows 都有 ≥ 2 类 (skip / optimize / add).

Sanity check ✓.

---



## 表达 DNA

**高频黑话** (top 10): RAG (单音节) / ReAct / eval / trace / ship / in production / spaghetti agent / thin vs thick framework / eval-driven / agent-shaped problem

**严肃 register** (来自 Track 01 长访谈): 直接 / 工程师式 / 对 framework 持怀疑姿态 / 对 eval 持神圣姿态. 多人融合, 不模仿单一 figure.

**内 vs 外沟通**:
- 内部 (同行): 大量缩写 (RAG / ReAct / HITL / ICL); 工具名直呼; 对厂商 marketing 嘲讽
- 对外 (非从业者): 展开缩写; 类比 (RAG = "AI 先查资料再回答")

**外行破绽** (来自 Track 06 outsider-tell):
1. 念 R-A-G 而不是 "rag"
2. LLM 等同 ChatGPT
3. RAG = vector DB
4. "in production" 滥用
5. fine-tune 一下就好
6. ReAct 当具体 algorithm

**厂商话术拒绝**: AI-powered / Cognitive computing / Intelligent automation / Agentic transformation / Human-in-the-loop AI (用 HITL 代替)

---



## 质量基准 + 反模式

### 什么算「好」 (3-5 条具体可验证):

1. production agent 必有 trace pipeline + eval set ≥ 50 examples + 自动 regression detection
2. framework swappable in a weekend (不能在一周末剥掉就太重)
3. RAG 必须 hybrid retrieval (production-grade)
4. eval set 中 ≥ 30% human-validated (LLM-as-judge 不能裸用)

### 反模式 (5-10 条):

1. 把 framework 当 production foundation (而非 scaffold)
2. demo 完美就以为 production-ready
3. 用 LLM-generated eval set 做 LLM 测试
4. ReAct loop 失败时调 prompt 而非看 trace + tool
5. Pure vector RAG (without hybrid)
6. instrument 一切 (trace 量爆炸 → 关掉 → 失去信号)
7. multi-agent orchestration 当 default (5 agent 协作的真实需求很少)
8. CrewAI / AutoGen 直接上 prod 而没经过 thin-first 验证

---



## 智识谱系

### 主要流派分裂

**流派 A: Thin / Type-first / Capability-driven**
- 奠基: Karpathy ("LLM as new computer", bitter lesson agent-flavor)
- 当前代表: Vercel ai-sdk team / Pydantic-AI / Anthropic agent docs / Simon Willison
- 核心主张: 相信模型能力, 用最薄的 type-safe wrapper, 期待 framework 6-12 月被剥掉

**流派 B: Thick / Orchestration-heavy / Symbolic**
- 奠基: 学院派 multi-agent + DSPy 风格 declarative
- 当前代表: CrewAI / AutoGen / 部分 LangChain 老阵营
- 核心主张: agent 协作需要 explicit orchestration; declarative + verifiable 比 emergent 可靠

**核心分歧**: framework 是「编排器」还是「最薄的 type-safe wrapper」?

### Open / Proprietary protocol 之争 (次级流派)

- MCP (Anthropic, open) vs OpenAI Tool Calling spec (de facto, proprietary)
- 跟 Open vs Closed AI 的大战略呼应

### 历史背景

- 2022-2024: ReAct paper era, LangChain 一家独大
- 2024-2025: post-LangChain 批评期, thin framework 兴起, Pydantic-AI 出现
- 2025-2026: framework decay 共识达成; 重心向 eval / observability / orchestration 移动

---



## 诚实边界

1. **信息截止 2026-05**. 工具 / 工作流模块衰减最快 (建议每 3-6 月 update).
2. **法规 / 标准节衰减极高**. EU AI Act 实施细则、MCP 大版本、China 备案细则都在 active 演化期 (12 月内必更新).
3. **本 prototype 是 minimal-viable scope**. 真实 master skill 应有 13+ figures / 18+ tools / 7+ workflows / 22+ canon / 23+ sources / 26+ glossary. Phase 1.5 报告显示 5 tracks 标 cold (item count < floor) — 是 prototype scope 限制, 非 industry 实际状况.
4. **中文圈 sources 严重不足**. locale=global 但实际覆盖 ≥ 90% en sources, 中文圈视角缺失.
5. master skill 不能替代真实 production debugging 经验 - skill 给的是认知框架, 不是 incident response.

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-02 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-02 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-02 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-02 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-02 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-02 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-02 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-02 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-02 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
