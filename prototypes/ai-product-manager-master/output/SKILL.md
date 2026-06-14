---
name: "ai-product-manager-master"
description: "Use when aI \u4ea7\u54c1\u7ecf\u7406 (LLM \u5e94\u7528 / \u751f\u6210\u5f0f AI / Agent \u4ea7\u54c1 / Copilot \u5d4c\u5165 \u2014 \u8de8\u6a21\u578b\u8bc4\u4f30 / \u5de5\u4f5c\u6d41\u8bbe\u8ba1 / \u4ea7\u54c1-\u5de5\u7a0b\u534f\u540c) (AI Product Manager \u2014 LLM application / generative AI / agent product \u7684\u4ea7\u54c1\u7ecf\u7406\u5b9e\u6218) Master OS \u2014 automated mastery of AI Product Manager \u2014 LLM application / generative AI / agent product \u7684\u4ea7\u54c1\u7ecf\u7406\u5b9e\u6218: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.\nTrigger this skill when the user works on AI Product Manager \u2014 LLM application / generative AI / agent product \u7684\u4ea7\u54c1\u7ecf\u7406\u5b9e\u6218 problems and wants industry-grade thinking, tool selection, or workflow guidance.\n\u89e6\u53d1\u8bcd\uff1a\u300cAI \u4ea7\u54c1\u7ecf\u7406\u300d\u300cAI PM\u300d\u300cLLM \u4ea7\u54c1\u300d\u300cGenerative AI product\u300d\u300cRAG \u4ea7\u54c1\u300d\n"
triggers: ["AI \u4ea7\u54c1\u7ecf\u7406", "AI PM", "LLM \u4ea7\u54c1", "Generative AI product", "RAG \u4ea7\u54c1", "agent \u4ea7\u54c1", "Copilot \u7c7b\u4ea7\u54c1", "AI \u52a9\u624b", "AI \u5de5\u5177", "\u591a\u6a21\u6001\u4ea7\u54c1", "model eval", "evaluation", "prompt engineering", "prompt \u5de5\u7a0b", "model selection", "context window \u8bbe\u8ba1", "AI \u6570\u636e\u98de\u8f6e", "AI feature gating", "AI \u6210\u672c\u63a7\u5236", "\u5e7b\u89c9\u63a7\u5236", "hallucination", "AI \u5931\u8d25\u6a21\u5f0f", "AI \u5b89\u5168 / \u7ea2\u961f", "AI roadmap", "BrainTrust", "LangSmith", "vector DB \u4ea7\u54c1"]
industry: "AI Product Manager \u2014 LLM application / generative AI / agent product \u7684\u4ea7\u54c1\u7ecf\u7406\u5b9e\u6218"
industry-cn: "AI \u4ea7\u54c1\u7ecf\u7406 (LLM \u5e94\u7528 / \u751f\u6210\u5f0f AI / Agent \u4ea7\u54c1 / Copilot \u5d4c\u5165 \u2014 \u8de8\u6a21\u578b\u8bc4\u4f30 / \u5de5\u4f5c\u6d41\u8bbe\u8ba1 / \u4ea7\u54c1-\u5de5\u7a0b\u534f\u540c)"
locale: "global"
last_research_date: "2026-05-14"
source_count: 159
profile: "practitioner"
generator: "master-skill v1.3"
----

# AI 产品经理 (LLM 应用 / 生成式 AI / Agent 产品 / Copilot 嵌入 — 跨模型评估 / 工作流设计 / 产品-工程协同) · Master OS

> This skill makes the agent operate as a senior AI Product Manager — LLM application / generative AI / agent product 的产品经理实战 practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 AI Product Manager — LLM application / generative AI / agent product 的产品经理实战 相关的问题时（关键词：AI 产品经理, AI PM, LLM 产品, Generative AI product, RAG 产品, agent 产品, Copilot 类产品, AI 助手, AI 工具, 多模态产品, model eval, evaluation, prompt engineering, prompt 工程, model selection, context window 设计, AI 数据飞轮, AI feature gating, AI 成本控制, 幻觉控制, hallucination, AI 失败模式, AI 安全 / 红队, AI roadmap, BrainTrust, LangSmith, vector DB 产品），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 AI Product Manager — LLM application / generative AI / agent product 的产品经理实战 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：AI Product Manager — LLM application / generative AI / agent product 的产品经理实战 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 模型能力近 3-6 月迭代轨迹 + 该层会不会被模型 native 化
- 看什么: 近 3-6 个月 frontier 模型(GPT / Claude / Gemini)发布了什么新能力;用户当前依赖的某个 capability(长 context / 工具调用 / reasoning / 多模态)有没有被模型 native 化、哪些第三方层(RAG / prompt 优化 / agent 框架)正被吃掉一层。
- 在哪看: Simon Willison weblog(新模型发布当天评测)+ 他的年度「year in LLMs」;各 vendor 官方 news(Anthropic / OpenAI / Hugging Face blog,作事实源);artificialanalysis.ai 类模型对比(作榜单,不作判断源)。
- 输出: 1-2 句:「过去 X 个月模型新增了 ___ 能力;用户依赖的 ___ 层 [会 / 不会] 在 6-12 个月内被模型 native 化,建议 [现在投入 / 按周末能不能剥掉判断 / 推迟]。」

#### 维度 2: eval / error analysis 现状诊断
- 看什么: 用户的产品有没有针对自己 failure mode 的 eval 套件(不是公开 benchmark);有没有 golden set(30-50 个、PM+领域专家共建);LLM-judge 校准了没(75-90% 一致);PM 有没有亲自做过 error analysis。(「golden set 30-50 个」「judge 校准 75-90% 一致」均出自 Hamel evals-FAQ T03-S016,详见 §8.4)
- 在哪看: Hamel Husain blog(field-guide / evals-FAQ / 选型文)+ Eugene Yan eval-process;Track 03 workflow 3/4 的入门 SOP 作 checklist;用户自己产品的 trace 和现有评估流程。
- 输出: 1-2 句:「eval 成熟度 = [无 / 有 dashboard 无 error analysis / 有 golden set 未校准 judge / 完整];最高 ROI 的下一步是 ___(通常是 PM 先读 10-50 条 trace 做 error analysis)。」

#### 维度 3: workflow vs agent 边界判定
- 看什么: 用户的需求能不能跑在预定义代码路径上;如果说要做 agent,是真需要 LLM 自主决策多步,还是一个 routing / chaining workflow 就够;有没有更便宜的低层方案没试。
- 在哪看: Anthropic「Building Effective Agents」(五种 workflow 模式作对照)+ Simon Willison 的 agent 定义;Track 02 选型决策树 Branch 2d;Track 03 workflow 5 step 1 的判断门。
- 输出: 1-2 句:「这个需求是 [workflow / agent / 混合];推荐用 ___(若 workflow,指明五模式里哪个);若坚持 agent,ship 门必须是 pass^k。」

#### 维度 4: 单用户 token 经济模型 + cost-quality-latency 硬约束定位
- 看什么: token 单价 × 预期用户行为 × 留存 → 单用户成本能不能撑住定价;这个场景 cost / quality / latency 哪个是硬约束;agent 多轮对话有没有二次方 token 增长陷阱。
- 在哪看: vendor API 定价页(OpenAI / Anthropic / Gemini docs)+ CloudZero 类对比;Chip Huyen《AI Engineering》的 cost-quality-latency 三角章;Track 03 workflow 1 step 5。
- 输出: 1-2 句:「单用户/月预估 API 成本 ≈ ___ vs 定价 ___,[能 / 不能 / 勉强] ship;硬约束是 ___,建议倒推方案 ___。」

#### 维度 5: 学派语境定位（用户 / 公司在哪个产品决策流派）
- 看什么: 用户/公司的产品决策实际站在模型派 / 工作流派 / agent 派 / 数据飞轮派的哪一派(或混合);特别是「要不要建数据飞轮当护城河」这个 disputed 问题上的立场;这个立场和他们的实际资源是否匹配。
- 在哪看: Track 04 canon 的四流派种子 + §7 智识谱系;a16z「The Empty Promise of Data Moats」(飞轮祛魅一手观点);Anthropic Building Effective Agents(工作流派奠基)。
- 输出: 1-2 句:「用户当前决策倾向 ___ 派;这一派在 ___ 问题上的已知风险是 ___(如:飞轮派需诚实评估 data moat 是否空头支票);建议保留的反方视角是 ___。」

#### 维度 6: AI PM 角色类型 + 协作边界诊断
- 看什么: 在用户这家公司,「AI PM」具体是 4 种里的哪种(传统 PM+AI 项目 / 技术 PM / eval 专员+PM / AI 业务负责人);PM 和 ML 工程师 / 数据标注 / 法务安全的边界是否清楚;谁拥有 prompt、谁拥有 eval 策略。
- 在哪看: Track 06 glossary「AI Product Manager 角色定义混乱」详条 + Data Science PM / Arize / Product School 的(彼此不一致的)分类法;Track 03「贯穿全流程协作边界」表。
- 输出: 1-2 句:「用户的 AI PM 角色 ≈ 第 ___ 种;与工程师的边界 [清晰 / 模糊在 ___];建议明确归属的事项是 ___(如 error analysis 起点应归 PM)。」

#### 维度 7: 失败模式 / 可靠性现实校准
- 看什么: 用户对 AI 不可靠的预期是否现实(知不知道 pass^k、demo-to-production gap);有没有 defensive UX(设预期 / 可撤销 / 给出处 / 失败回退);ship 门是不是「demo 跑通一次」;有没有把所有错误都笼统叫 hallucination。
- 在哪看: τ-bench 的 pass^k 数据 + Eugene Yan llm-patterns 的 defensive UX 节;Track 03 workflow 5 的失败模式 + CLI 自检项;用户产品的 incident / 失败案例。
- 输出: 1-2 句:「用户对可靠性的预期 [现实 / 过于乐观];当前缺的兜底是 ___(defensive UX / pass^k ship 门 / failure mode 拆分);建议把 ship 标准改成 ___。」

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

> 三重验证（跨场景复现 / 生成力 / 排他性）后,从 18 候选收敛到 6 个心智模型。每个挂 ≥ 2 个 source_id,多数跨 track。

### 1.1 Eval 是地基,不是可选项（别 vibe-check）

- **一句话**: 「AI 产品的『好』不是看几个 case 觉得行就 ship —— 是先针对你**自己产品的失败模式**建一套可重复、可回归的系统化测量;没有 eval 就是在瞎改。」
- **三重验证**: ✅✅✅ —— 跨 scoping / eval 体系搭建 / 迭代循环 / agent ship 四个子场景 + Hamel / Eugene Yan / Chip Huyen / Marily Nika 四个独立 figure + canon 5+ 源(G-Eval / field-guide 等) + glossary 头号黑话。完整通过。
- **应用方式**: 面对任何「这个 AI 改动好不好 / 这个产品能不能 ship」的问题,先问「我有没有一套针对自己 failure mode 的 eval?跑公开 benchmark 不算」。质量是循环不是一次性的门。
- **局限**: 对**冷启动 0→1、还没有任何真实数据**的早期产品,过度强调 eval 会拖慢 —— 此时应先做 error analysis（看 10-20 条手造/早期 trace,trace 条数量级同 Hamel field-guide T03-S001 的 SOP）,而不是先建完整 eval 平台。Hamel 本人也承认「早期没数据建 golden set 时 eval 会拖慢」。
- **figures**: Hamel Husain（Your AI Product Needs Evals / field-guide, T04-S008 / T03-S001）/ Eugene Yan（llm-patterns 的 eval 模式 + 「eval = 科学方法的伪装」, T04-S005）/ Chip Huyen（《AI Engineering》评估章, T04-S013）/ Marily Nika（「minimum viable quality」, T01-S010）—— 4 个独立 figure 跨工程派 + 产品 sense 派同时支持。
- **evidence**: [T04-S008, T04-S005, T04-S013, T01-S010, T03-S001, T06-S004]

### 1.2 先 error analysis,再加功能（PM 亲自看 trace）

- **一句话**: 「质量上不去时,资深 AI PM 的第一反应**不是加功能**,是 PM 亲自拉 10-50 个真实 trace（trace 条数量级见 Hamel field-guide T03-S001 / evals-FAQ T03-S016）逐条标错、自下而上归类成 failure mode —— 所有 eval 指标都得从这里长出来,不能凭空想。」
- **三重验证**: ✅✅✅ —— 出现在 workflow 1（定义成功标准前先看）/ 3（step 1）/ 4（step 1 Analyze）/ 6（采样路由）四个 workflow + Hamel field-guide + Eugene Yan eval-process + Aman Khan 的 PM/工程师边界一手描述。排他性强:这是 AI PM 区别于传统 PM「最硬核」的一段,也区别于 ML 工程师（error analysis 起点是 PM,不是工程师）。
- **应用方式**: 遇到「产品质量不行」「不知道改哪」,强制 step 1 = 阻塞 30 分钟左右、读 10-50 条真实 trace、记开放式笔记、用 LLM 聚成 taxonomy、数每类频率（「阻塞 30 分钟、10-50 条 trace」是 Hamel field-guide T03-S001 的 SOP 量级,非精确硬阈值）。这步不能外包给工程师或标注供应商（PM 是首席领域专家)。
- **局限**: error analysis 的「判断什么算错」是 domain-specific 的,依赖 PM 真的懂这个领域;若 PM 对领域陌生,这一步退化成走过场。也不适用于纯基础设施类问题（延迟、成本)——那是工程指标不是 failure mode。
- **figures**: Hamel Husain（field-guide 的 error-analysis 完整循环, T03-S001 / T04-S010）/ Eugene Yan（eval-process「修流程而非换 judge」, T04-S007）/ Aakash Gupta（AI Evals for PMs 的 analyze 步, T03-S006）—— 另有 Aman Khan（Arize, T03-S008）一手描述 PM/工程师边界:error analysis 起点归 PM。3 个独立 figure 支持。
- **evidence**: [T03-S001, T04-S010, T04-S007, T03-S008, T03-S006]

### 1.3 workflow vs agent 要分清,多数需求是 workflow

- **一句话**: 「『agent』被严重滥用 —— 真正的 agent 是 LLM 自主决定用什么工具、何时用、多步执行;但多数 AI 需求其实是预定义路径能解决的 **workflow**,默认假设是 workflow,只在路径无法预先定义时才上 agent。」
- **三重验证**: ✅✅✅ —— Anthropic「Building Effective Agents」奠基 + Simon Willison 给 agent 收口定义 + swyx 把 Agent Engineering 立为独立主题 + Chip Huyen「Agents」长文 + 出现在 tools 选型树 2d、workflow 5。排他性强:「agentic」是 2025-2026 最滥用的营销前缀,识别 workflow/agent 边界是这一行特有的判断。
- **应用方式**: 面对新 AI 需求,先过一道判断门「这个任务能不能跑在预定义代码路径上?」能 → 用 workflow 五模式（prompt chaining / routing / parallelization / orchestrator-workers / evaluator-optimizer)。不能 → 才考虑 agent,且上线门是 pass^k 不是 demo。
- **局限**: workflow/agent 不是非黑即白,有混合形态（workflow 里嵌一个小 agent 节点);判断「路径能不能预定义」本身需要经验。这条对**非 LLM 类 AI 产品**（推荐系统、CV 检测)不适用。
- **figures**: Simon Willison（给「agent」收口定义:LLM 在循环里调工具达成目标, T01-S015）/ swyx（把 Agent Engineering 立为独立主题, T04-S033）/ Anthropic·Schluntz & Zhang（Building Effective Agents 的 workflow vs agent + 五模式, T04-S023 / T03-S002）—— 2 位个人 figure + Anthropic 工程团队,3 个独立来源。Chip Huyen 的「Agents」长文同向但未单列 source_id。
- **evidence**: [T04-S023, T01-S015, T04-S033, T02-S027, T03-S002]

### 1.4 AI PM 不需会训模型,但要懂 AI 能力边界（别做 feature theater）

- **一句话**: 「AI PM 的核心**不是** prompt engineering、也**不是**会训模型 —— 是懂 AI 能/不能做什么,在用户 pain point 和技术能力之间架桥;脱离 pain point、为了用上某个模型能力而做的 AI 是 feature theater(装饰性 AI)。」
- **三重验证**: ✅✅⚠️ —— 验证 3 PARTIAL（「从问题出发不从能力出发」是通用产品道理的 AI 放大版）。跨 figure:Marily Nika（「pain point ↔ 技术的翻译者」)/ Aakash Gupta（「停止把 AI 当装饰性能力」)/ Chip Huyen（「foundation model 让人人能搭复杂应用,所以更要懂边界」)。**放大程度**:在 AI 这一行,模型能力每几周跳一次、诱惑极大,「被新能力带着走」的反模式比传统产品严重得多;且本行有「prompt engineering = AI PM 核心」的结构性误解需要专门对抗。
- **应用方式**: scoping 一个 AI feature 时强制从用户 pain point 起笔,不从「GPT-5.5 能做 X」起笔;简历/自我定位上说清「我是 4 种 AI PM 里的哪种」。
- **局限**: 「懂能力边界」的深度因「AI PM 是哪种」而异（技术 PM vs 业务负责人需要的深度不同);本条不解决「该懂多深」,只解决「方向是能力边界感而非 prompt 技巧」。
- **figures**: Marily Nika（「pain point ↔ 技术」的翻译者、不需会训模型但要懂能力边界, T04-S002）/ Aakash Gupta（「停止把 AI 当装饰性能力」、feature theater 反面, T01-S018）/ Chip Huyen（foundation model 让人人能搭复杂应用,所以更要懂边界, T04-S013）—— 3 个独立 figure 表述,且横跨产品 sense 派与工程派。
- **evidence**: [T04-S002, T01-S018, T04-S013, T06-S015]

### 1.5 先简单 / 最便宜的假设,验证了才升级复杂度

- **一句话**: 「面对 AI 技术决策,默认从最便宜、最简单的假设起 —— prompt → RAG → agent → finetune 是一道阶梯,工具上 provider SDK → 框架、code-based check → LLM-judge → 自建 viewer 同构;只在低层验证不够时才升级,不一上来堆框架和平台。」
- **三重验证**: ✅✅✅ —— 出现在 workflow 1（prompt→RAG→agent→finetune 阶梯)/ 3（code-based check 先于 LLM-judge)/ 4（改 prompt 先于改架构、finetune 最后)/ 5（LLM API 先于框架)+ tools 选型树「默认用最轻的能跑的」+ Anthropic「简单可组合 > 复杂框架」。排他性:这一行有「一遇不准就 fine-tune」「做 AI 必须有 vector DB」的强反模式,「先简单」是对它们的直接对抗。
- **应用方式**: 任何「该用什么技术 / 该上什么工具」的决策,先定位「最便宜的能验证假设的方案是什么」,从那里起步;只有当低层方案被证明不够,才升级到下一层,且每次升级都要说得出「为什么低层不够」。
- **局限**: 「最便宜的假设」需要对各层成本有判断力,新手可能误判;某些场景（强监管、明确已知的高复杂度需求)确实需要跳过低层 —— 这条是「默认」不是「禁令」。**figure 支持偏薄**:本模型的具名个人 figure 实际只有 Hamel Husain 一位密集背书,另一支柱是 Anthropic 工程团队（机构,非个人 figure);Eugene Yan 的 llm-patterns 有同向的「渐进复杂度」论述但未挂进本模型 evidence 行 —— 故本条按「1 个人 figure + 1 个机构来源」计,弱于第 1-4 个模型的多 figure 共识。
- **figures**: Hamel Husain（field-guide「先简单后复杂」+ eval-tools「默认用最轻的能跑的」, T03-S001 / T02-S020）/ Anthropic·Schluntz & Zhang（Building Effective Agents「简单可组合 > 复杂框架」、prompt→工具→agent 阶梯, T04-S023 / T03-S002）—— 2 个独立来源,但其一为机构而非个人 figure（见「局限」）。
- **evidence**: [T03-S002, T02-S027, T02-S020, T04-S023, T03-S001]

### 1.6 AI 不可靠是常态,用 UX + eval 消化,不假装它可靠

- **一句话**: 「AI 一定会出错（pass^k 现实:SOTA agent 零售域 pass^8 < 25%,数据出自 τ-bench T04-S022)—— 资深 AI PM 不追求零错误,而是用 defensive UX（设预期、可撤销、给出处)+ eval + guardrails 去消化和兜底;ship 门是『多次运行的稳定通过率』,不是『demo 跑通一次』。」
- **三重验证**: ✅✅✅ —— Eugene Yan defensive UX 模式 + τ-bench 的 pass^k 硬数据 + Hamel evals + workflow 5 的 pass^k ship 门 + glossary「demo-to-production gap」几乎成口头禅。排他性强:传统软件「跑通即可发」,AI 产品「跑通一次 ≠ 能 ship」是这一行特有的现实校准。
- **应用方式**: 设计 AI 功能时,默认它会错 —— 在 UX 层设计预期管理、可撤销、可中断、给出处、失败回退;定 ship 标准时用 pass^k（同任务跑 k 次的稳定通过率)而非单次 demo。
- **局限**: 「可接受的不可靠程度」是产品判断,因场景而异（医疗 vs 创意工具容错度天差地别);本条不给具体阈值,只给「用 UX+eval 消化、不假装可靠」的方向。defensive UX 的具体形态也在快速演进。
- **figures**: Eugene Yan（llm-patterns 的 defensive UX 模式, T04-S005）/ Hamel Husain（Your AI Product Needs Evals,把 eval 作 ship 前兜底, T04-S008）—— 另有 τ-bench（Yao et al. / Sierra, T04-S022）提供 pass^k < 25% 的硬数据支撑。2 位个人 figure + 1 篇 benchmark 论文。
- **evidence**: [T04-S005, T04-S022, T04-S008, T03-S002]

---



## 标准 Playbook

> 行业「快速决策规则」。每条 `如果 X,则 Y` 句式 + 具体案例 + evidence。从心智模型降级 + 跨 workflow 反复出现的步骤模式提炼。

1. **如果质量或方向不明**(产品不行、不知道改哪、要定义成功标准),则 PM 先亲自拉 10-50 个真实 trace 逐条标错、自下而上归类成 failure mode,再做任何决策 —— 不要先建指标 dashboard,不要凭直觉加功能。
   - **案例**: Hamel field-guide（T03-S001）的多公司案例:某产品日期处理 66% 失败是靠逐条读 trace 才定位到的,不是靠 dashboard。这一步跨 workflow 1/3/4/6 反复出现。
   - **evidence**: [T03-S001, T04-S010, T03-S006, T03-S008]

2. **如果遇到 AI 技术决策**(该用什么技术实现一个需求),则默认从最便宜的假设起 —— prompt-only → RAG → agent → finetune 是一道阶梯,只在当前层被证明不够时才升级到下一层,且每次升级要说得出「为什么低层不够」。
   - **案例**: workflow 4 的标准做法:规格不清就改 prompt/context,泛化不行才动架构,fine-tune 放最后;Anthropic「Building Effective Agents」也是「先简单后复杂」。反例 = glossary 头号反模式「一遇到不准就喊 fine-tune 一下」。
   - **evidence**: [T03-S002, T02-S027, T04-S023, T06-S001]

3. **如果要判断 AI 输出质量**,则用 binary pass/fail + 失败频率计数排优先级,不用模糊的 1-5 / 1-10 分,不用「我觉得这个重要」 —— 专家做二元判断更可靠,频率比直觉更能定优先级。
   - **案例**: workflow 3/4 资深做法 + Hamel evals-FAQ 明示「binary 优于 Likert」;workflow 4 用「这个 failure mode 出现多少次」而非「我觉得」来排序,避免「花一周修一个一年出现两次的边角问题」。
   - **evidence**: [T03-S016, T03-S007, T04-S009, T06-S002]

4. **如果是新 AI 产品或新需求要落地**,则默认 provider SDK + pgvector + 先做 error analysis 起步,不要一上来堆 LangChain 类重框架、不要先买 eval 平台 —— 「默认用最轻的能跑的,感到真实痛点再上框架」。
   - **案例**: tools 选型树 Branch 1:「最常见模式 —— v1 用 pgvector 在已有 Postgres 库里两周 ship 到生产」;Hamel 明示 POC 阶段「别 premature tool outsourcing」。反例 = 2026 还把 LangChain 经典抽象当默认建 app 方式。
   - **evidence**: [T02-S027, T02-S029, T02-S020]

5. **如果在选 eval / observability 工具**,则先确认你的 error analysis / golden set 方法论已经清楚,工具只是把它跑起来 —— eval 是方法论不是工具,别用塞满通用指标的 dashboard 替代人工读失败样本。
   - **案例**: Hamel「eval 是方法论,工具只是 backend data store」;tools 避坑清单「别用 eval 平台替代 error analysis」;eval 平台厂商(LangSmith/Braintrust/Arize)都在把「eval」收编成自家产品功能,要警惕。
   - **evidence**: [T02-S020, T02-S026, T06-S005]

6. **如果遇到新 AI 需求**,则先问「这是预定义路径就能解决的 workflow,还是真的需要 LLM 自主决策的 agent」,默认假设是 workflow —— 多数需求是 workflow,把不是 agent 的需求做成 agent 是无谓的不可靠 + 成本。
   - **案例**: Anthropic「Building Effective Agents」明示多数场景 workflow 就够;tools 避坑「不要把所有 AI 需求都当 agent 来做,更别当 multi-agent」;workflow 5 step 1 强制过这道判断门。
   - **evidence**: [T04-S023, T02-S027, T03-S002]

7. **如果要 ship 一个 agent**,则上线标准是 pass^k（同任务跑 k 次的稳定通过率),不是「demo 跑通一次」 —— 并且要有失败回退 + 用户控制权 + 沙箱大量测试 + guardrails。
   - **案例**: τ-bench 硬数据:SOTA function-calling agent 零售域 pass^8 < 25%;workflow 5 把 pass^k 作 ship 门,「demo 美、生产崩」是典型失败。
   - **evidence**: [T04-S022, T03-S002]

8. **如果要做模型选型**,则先明确这个场景 cost / quality / latency 哪个是硬约束再倒推,且必须算单用户 token 经济模型(token 单价 × 用户行为 × 留存)—— 不算这笔账可能在 scoping 一个 ship 不了的产品。
   - **案例**: workflow 1 step 5「粗算成本约束」+ intake 点名「成本控制是被忽视的硬技能」;agent 多轮对话有「二次方 token 增长」陷阱,单用户成本能直接决定产品死活。
   - **evidence**: [T04-S013, T06-S001, T03-S006]

9. **如果 LLM-as-judge 要上线**,则必须先和人工标注校准到 75-90% 一致再 scale,用 binary 不用 1-5 分 —— 没校准的 judge 等于没用,团队很快不信它,且校准是 domain-specific 的、不能外包给 vendor 的 pre-built judge。
   - **案例**: workflow 3 step 5 + Hamel evals-FAQ 明示「75-90% 一致」阈值;glossary 警告 Arize/Evidently 的「pre-built LLM judge」把校准步骤隐藏在产品里。
   - **evidence**: [T03-S016, T03-S007, T06-S003]

10. **如果做架构决策**,则 LLM 接入用 LiteLLM / provider SDK 抽象层、工具集成走 MCP,不 hardcode 单一 provider、不选私有 tool 协议,且把「这工具还独立吗 / 厂商中立吗」和功能并列评估 —— 模型每几周一版,hardcode 的应用面临 recurring migration projects。
   - **案例**: tools 避坑「model-agnostic infrastructure is no longer optional」;MCP 已是事实标准(78% 企业 AI 团队生产环境用 —— 该 78% 数字出自 MCP 百科 T02-S022 的交叉验证、进 Linux Foundation T02-S021);2026 内 Promptfoo→OpenAI、Statsig→Amplitude、Scale AI←Meta 入股都是独立性变化信号。
   - **evidence**: [T02-S033, T02-S027, T02-S018, T02-S021]

---



## 工具栈与选型决策树

> 直接 reference Track 02 输出(三层结构 + 8 节点选型决策树 + 9 条避坑清单)。本节是一致性 sanity-check,非重新提炼。

### 3.1 三层结构（直接引 Track 02）

- **必备层（8 个,「≥ 80% 从业者用」是多源交叉推断、非 survey 实测 —— 除 MCP 有 78% 硬数据外其余为推断,见 §3.4 / §8.4)**: LLM Provider API(OpenAI / Anthropic / Gemini)/ LiteLLM / provider SDK / MCP / 一个 eval 平台(LangSmith / Braintrust / Phoenix 三选一)/ 一个轻量 CI eval 框架(DeepEval / Promptfoo / RAGAS)/ Langfuse 类 observability / 一个 vector DB(pgvector 起步)/ LangGraph / provider Agent SDK。
- **场景特化层（12 个)**: DeepSeek / Qwen / GLM API(成本敏感 / 国内合规)、LlamaIndex(复杂 RAG)、DSPy、Qdrant / Weaviate / Chroma / Pinecone(不同 vector DB 取舍)、Helicone、PromptLayer、Surge AI / Scale AI、Argilla / Label Studio、Datadog LLM Observability。
- **新兴 / 实验层（7 个,stability: experimental,6 个月后可能不存在 / 大变)**: Claude Agent SDK / OpenAI Agents SDK + Responses API / Google ADK / CrewAI / Lakera Guard / Datadog AI Guard / Amplitude(前 Statsig)实验栈。

### 3.2 选型决策树（直接引 Track 02 决策树 A,8 节点)

核心骨架：**先问「你的 AI 产品在哪个阶段、核心目标是什么」** →
- **Branch 1 POC / demo 阶段** → 一个 frontier provider API 直连 + provider SDK + Chroma 或长 context + 先做 error analysis,不上 eval 平台、不上 LangChain。
- **Branch 2 已有 PMF、做 production-grade** → 按瓶颈分:质量不明 → 两层 eval 工具(CI 框架 + 平台);RAG 检索差 → LlamaIndex ingestion + 按规模选 vector DB;成本算不过来 → LiteLLM + 成本敏感 provider + gateway caching;agent 不可靠 → 先判 workflow vs agent,确需 agent 再 LangGraph / Agent SDK + MCP + guardrails。
- **Branch 3 规模化、特定瓶颈** → 数据飞轮 / finetune 瓶颈在标注 → Argilla/Label Studio 或 Surge AI;严肃实验 / 灰度 → Statsig/LaunchDarkly/Eppo + Datadog/Langfuse 监控。

### 3.3 避坑清单（直接引 Track 02,9 条)

不要在 2026 还把 LangChain 当默认建 app 方式 / 不要把 RAG 等同于 vector DB / 不要 premature tool outsourcing / 不要信「AI 自动生成 rubric 又自动打分」的全自动 eval / 不要只用一个 eval 工具想全包 / 不要 hardcode 单一 provider / 不要在 agent 产品里选私有 tool 协议 / 不要忽视工具的「独立性变化」信号 / 不要把所有 AI 需求都当 agent。

### 3.4 一致性 sanity-check 结论

- ✅ **必备层 ≥ 3 个** —— 8 个,达标。注意必备层主体是 vendor API + 协议 + 方法论承载工具,stars 不是它们的信号,靠「≥ 3 独立 source 点名 + 采用率」入层(MCP 有硬数据 78%,出自 T02-S022;其余工具采用率是多源推断、无 survey)。
- ✅ **选型决策树 5-10 节点** —— 8 节点,每个分支挂 evidence,达标。
- ✅ **避坑清单 ≥ 5 条** —— 9 条,达标。
- ⚠️ **软肋(进 §8 诚实边界)**: 本行没有公开的「AI PM 工具栈采用率 survey」,必备层采用率是多源交叉推断;新兴层 7 个全 high decay,agent 框架层尤其 —— 工具栈是衰减最快的模块,按 3-6 个月重校准。国内工具(DeepSeek/Qwen/GLM)只一张合并卡片,vendor docs 未深挖。

---



## 工作流 / Pipeline

> 直接 reference Track 03 输出(6 个 workflow,按产品生命周期串联)。本节是一致性 sanity-check,非重新提炼。
> **[本节 decay 最快 —— 6 个 workflow 无一稳态,Last_updated 2026-05-14,6 个月内大概率需全面 update]**

### 4.1 六个 workflow（按产品生命周期线,直接引 Track 03)

| # | Workflow | Trigger | 入门 SOP 核心 | 资深差异（skip / optimize / add） | Decay |
|---|----------|---------|--------------|----------------------------------|-------|
| 1 | Scoping 一个 AI feature（想法阶段） | 业务方提出「能不能用 AI 做 X」 | 澄清真问题 → 判断该不该用 AI → 技术路线初判 → 定义成功标准 → 粗算成本 → 风险分级 | skip 冗长市场调研 / optimize 用原型替代规格 / add 不确定性管理 + 成本约束前置 | medium |
| 2 | POC / 原型验证（想法→POC） | 存在「不做一个就不知道行不行」的不确定性 | 明确 POC 要回答的问题 → 造为学习而非交付的原型 → 真实约束喂原型 → 真人测试 → go/pivot/kill | skip 工程级代码质量 / optimize 并行造 3-5 版 / add 死磕 desirability 判断 | low |
| 3 | 从 0 搭起 eval 体系（POC→MVP 前置门） | POC 跑通、要认真迭代但无客观度量手段 | PM 亲自看 trace 做 error analysis → 归类 failure mode → 建 golden set → code-based check → LLM-judge 校准 → offline+online 双层 | skip 通用 dashboard / optimize 自建 data viewer / add judge 校准 + online eval 层 | medium |
| 4 | Eval-driven 迭代循环（MVP→生产主循环） | eval 体系已建、质量需持续往上推 | Analyze 看数据找 failure mode → 频率排序 → 根因分析提假设 → Measure 针对性改 + 量化验证 → Improve 回归 → 循环 | skip 加功能冲动 / optimize binary + 频率排序 + 「改 prompt/context 先于改架构、finetune 最后」的最小改动顺序 / add error analysis 作前置门 + Bryan Bischof 式 capability funnel 追踪进展（不只看单点 pass/fail）+ 每轮把新 production 失败回灌 golden set | medium |
| 5 | Agent 产品从 0 到可 ship（high decay） | 出现真需要「LLM 自主决策多步」的需求 | 先判真的需要 agent 吗 → 能用 workflow 五模式就用 → LLM API 直接起步 → 工具工程对标 prompt 工程 → 沙箱测试 + guardrails → pass^k 作 ship 门 | skip 框架抽象层 / optimize 工具设计到 prompt 同等投入 / add pass^k 门 + 失败回退设计 | high |
| 6 | 搭数据飞轮（生产→飞轮,high decay） | MVP 上线、有真实流量、要长期差异化 | 设计反馈采集 → 系统化 log trace → 按计划采样 + 路由专家 → 专家判断回流 eval+finetune → 用沉淀数据更新产品 | skip 早期不建飞轮 / optimize 自动采样路由 / add 飞轮 ROI 诚实评估 | high |

### 4.2 贯穿全流程的协作边界（直接引 Track 03）

- **AI PM ↔ ML/AI 工程师（证据最强)**: PM 拥有产品规格 / 成功标准 / failure mode 分类 / error analysis 起点 / eval 策略 / golden set / 写 prompt(多个一手源明示「工程师不被允许改 prompt」);工程师拥有基础设施 / 复杂技术实现(工具调用 / 架构 / finetune / scorer)。核心边界:「定义产品该做什么 + 用领域知识迭代 prompt + 拥有 eval 策略」是 PM 的。
- **AI PM ↔ 数据/标注（证据中等)**: PM 定标什么 / 采样策略 / rubric;标注团队执行;校准不能外包(domain-specific)。
- **AI PM ↔ 法务/安全/红队（证据薄弱)**: PM 在 scoping 做风险分级判定、定「哪些失败不可接受」的边界;深度合规是法务的活、红队通常是专门安全角色。**此边界证据薄,§8 已降级标注。**

### 4.3 一致性 sanity-check 结论

- ✅ **入门 SOP 与资深路径分清** —— 6/6 workflow 都分开写。强信号:本行资深差异**不在「少做几步」,在「不跳过看似可省的硬步骤」**(error analysis / judge 校准 / pass^k 门 / desirability 验证 / 飞轮 ROI)。
- ✅ **资深差异 ≥ 2 类 + ≥ 2 instances** —— 6/6 都有 skip+optimize+add 三类,达标。
- ✅ **「近期变化」字段填了** —— 6/6 都填了具体日期 + 触发事件,且无一填「稳态」(本行确实没有稳态 workflow)。主要驱动力:AI 原型/eval 工具链成熟(5/6)+ eval-driven development 范式形成 + frontier 模型能力跃迁。
- ⚠️ **软肋(进 §8 诚实边界)**: ① 五阶段完整 SOP 是拼接的,本行 <3 年无一手长文从「想法」走到「飞轮」;② PM↔工程师边界证据强,PM↔数据/标注 中等,PM↔法务/安全/红队 薄弱;③ eval 派幸存者偏差 —— workflow 证据高度来自 eval 派(Hamel/Eugene Yan/Shreya)+ eval 工具厂商,「模型派」少写 workflow 长文;④ decay 全员偏高,6 个月内大概率需全面 update。

---



## 表达 DNA

> 不模拟某个具体 figure,模拟「这一行的资深人聚一起讨论时的 register」。多人融合。来源:Track 06 outsider-tell + 厂商话术拒绝 + Track 01 figures 的 voice_samples。

### 5.1 高频用语 / 黑话（Track 06 Tier 1 + figures 反复用的词）

eval / 「做 evals」(动词化:「我们得先建 evals」)、golden set、trace(「去翻 trace」= 去看完整执行记录做 error analysis)、failure mode(「这是哪个 failure mode」—— 内行把模糊的「不准」逼成具体类别)、LLM-as-judge / 口语直接说「the judge」、RAG(念「rag」一个音节)、ship / 「能不能 ship」、context engineering(2026 内行更愿用它替代「prompt engineering」)、LGTM / 「vibes check」(贬义)、「demo-to-production gap」、pass^k、error analysis、defensive UX。

### 5.2 严肃 register（Track 01 长访谈 + Track 04 textbook 的语气）

口语化但精确,不学术化也不营销化。资深 AI PM 在长 podcast / conference talk 里:用具体数字和案例说话(「日期处理 66% 失败」出自 Hamel field-guide T03-S001、「pass^8 < 25%」出自 τ-bench T04-S022 —— 此处是举「他们怎么说话」的例,两个数字本身的来源见 §8.4),用「先...再...」的步骤句式,拒绝「赋能 / 闭环 / 生态」这类 PPT 话术,愿意直说「这个我们现在还不知道」。把抽象判断逼成可操作的二元问题(「能不能跑在预定义路径上?」「real user 试过没有?」)。

### 5.3 内 vs 外沟通差异（Track 06 outsider-tell 反推）

- **同行间**: 允许 eval / trace / failure mode / pass^k / judge 直接缩写、动词化;直接说判断不铺垫。
- **对外（解释给非从业者 / 业务方）**: 会展开 ——「eval」说成「给 AI 产品做的考试题库 + 打分系统」、「RAG」说成「让 AI 回答前先去查资料」、「pass^k」说成「同一个任务跑 k 次,看稳定成功率」。

### 5.4 外行破绽 top（Track 06 outsider-tell,直接用）

最致命两条:① 「AI PM 核心技能是 prompt engineering」(极高频,一句话暴露 —— 内行:核心是 eval 设计 + 产品 fit 判断 + 团队协作);② 「我们做了 evals」= 跑了个公开 benchmark 分数(极高频 —— 内行:eval 是针对你自己产品 failure mode 的系统化测量)。其余:「RAG」≈「vector DB」/「上传文档」、「vibes check 过了就能 ship」、一遇不准就「fine-tune 一下」、把所有错误答案都叫「hallucination」、「context window 越大越好塞满它」、拿公开 benchmark 分数证明产品好、「agent」= 任何聊天机器人、jailbreak / prompt injection 混用。

### 5.5 厂商话术拒绝（Track 06,直接用 —— 拒绝什么反映行业价值观）

1. 拒绝「我们的 RAG 能消除幻觉」/「agentic RAG」 —— 行业重「诚实的失败模式管理」而非「银弹叙事」。
2. 拒绝「做 AI 产品必须有 vector DB」 —— 行业重「想清楚问题在哪」而非「堆基础设施」。
3. 拒绝「data flywheel 是我们的护城河」 —— 清醒派对「数据自动 = 壁垒」祛魅(a16z「The Empty Promise of Data Moats」)。
4. 拒绝「prompt engineering 速成班,7 天成为 AI PM」 —— 行业对「AI PM = 会写 prompt」强烈反感。
5. 拒绝「我们的 benchmark 分数 SOTA」 —— 行业重「你自己产品的 eval」而非「通用榜单」。

### 5.6 对话样本库（industry voice 实战语料）

> 4 类 × 各 ≥ 2 段,来源是 Track 01 figures 的 voice_samples 字段。voice_confidence 计算见末尾。

#### 5.6.1 客户版（面客 / 教育非技术受众）

- 「你不需要会训模型 —— 现成的 foundation model 已经让搭复杂应用变得人人可及;AI PM 真正要做的,是懂 AI 能做什么不能做什么,在用户的 pain point 和技术之间架一座桥。」(source: T01-S008 / T04-S002,转述,客户场景:向业务方/新人解释 AI PM 是什么)
- 「coding agent 就是一个能写代码、跑代码、看结果、再继续迭代的 LLM 系统 —— 它不是黑魔法,就是『写 → 跑 → 看 → 再改』这个循环。」(source: T01-S014,原话/转述,客户场景:给读者拆解 agent 长什么样)
- 「停止把 AI 当成一个装饰性的能力。问更好的问题:哪个决策因为它变聪明了、哪个 workflow 变容易了、哪个信任问题变得更显眼了 —— 这时候 AI PM 才开始像产品管理,而不是 feature theater。」(source: T01-S018,原话/转述,客户场景:纠正业务方的「为 AI 而 AI」)

#### 5.6.2 同业版（私下 / 内训 / 同业访谈)

- 「失败的产品几乎都有一个共同的根因:没能建起一套稳健的评估系统。」(source: T04-S008,原话/转述,同业场景:Hamel 对工程师+PM 的核心判断)
- 「别再 vibe-check 你的 AI 系统了 —— 换成系统化的 error analysis,先去翻 trace。」(source: T01-S003,转述,同业场景:Hamel 在 podcast/内训反复讲)
- 「一个没救活产品的 LLM-as-judge 救不了你 —— 修你的流程才行。」(source: T04-S007,原话/标题,同业场景:Eugene Yan 对「judge 万能论」的反驳)
- 「『agent』曾经是 buzzword bingo 之王,每个人脑子里的定义都不一样;我在 Twitter 上众包了 211 个互相矛盾的定义之后才敢收口 —— LLM agent 就是在一个循环里调工具来达成一个目标。」(source: T01-S015,原话/转述,同业场景:Simon Willison 给术语祛魅)

#### 5.6.3 专业 / 行业标准版（公开场合谈标准 / 方法论 / 行业走向)

- 「做产品 eval 本质上就是科学方法的伪装:提出假设 → 测量 → 迭代,而不是靠直觉改产品。」(source: T01-S001,转述,专业场景:Eugene Yan 把 eval 定位成科学方法)
- 「AI Engineering 是一门独立学科 —— 用现成的 foundation model 构建并高效部署应用,它不等于传统的 ML engineering,是一个新工种。」(source: T04-S013 / T04-S015,转述,专业场景:Chip Huyen 立学科边界)
- 「过去要五年加一个研究团队才能做的一大类 AI 任务,现在用 API 文档加一个空闲的下午就能做了 —— 涌现的能力,催生了一个涌现的职业(title)。」(source: T01-S017,原话/转述,专业场景:swyx 论证 AI Engineer / AI PM 这个新工种为什么出现)
- 「2026 年开放的 PM 岗位里有 30% 是 AI PM 角色,而市场上不到 5% 的资深 PM 真的 ship 过一个能跑的 AI agent —— 这是 PM 就业市场出现过的最干净的供需失衡。」(source: T01-S018 / T01-S019,原话,专业场景:Aakash 谈行业供需,注:此 30%/5% 为 Aakash 个人估计、非权威 survey,引用需带 caveat)

#### 5.6.4 反例版（这一行的资深人绝不会这样说的话 / 被错位包装的销售话术)

- 「我们的 agentic RAG 能彻底消除幻觉。」(source: T06 厂商话术拒绝 / T06-S018,why 反例:内行知道幻觉无法清零,「agentic」前缀已被点名为营销 hype;真行业语域是「诚实管理失败模式」)
- 「做 AI 产品你必须先上一个 vector DB。」(source: T06 厂商话术拒绝 / T06-S019,why 反例:RAG 失败 80% 在 chunking / 过时 embedding / 噪声源文档,不在数据库;把 RAG 等同 vector DB 是 Pinecone 类厂商的错位包装)
- 「7 天速成,带你成为月入 5 万的 AI 产品经理 —— 核心就是学会写 prompt。」(source: T06 厂商话术拒绝 / T06-S015 + intake warning,why 反例:prompt engineering 只是输出之一,核心是 eval 设计 + 产品 fit + 协作;这是本行信噪比差的头号噪声源)
- 「我们的 benchmark 分数是 SOTA,所以产品质量没问题。」(source: T06 厂商话术拒绝 / T06-S002+S030,why 反例:benchmark 有 contamination 风险且不等于你的 use case,内行只认针对自家产品的 eval)

**voice_confidence: medium** —— 4 类 × 共 13 段、覆盖齐全且 ≥ 30 字,但多数标「转述」(来自搜索摘要 + 节目描述 + 文章标题,Track 01 未逐集抓 podcast 字幕);仅少数标「原话/标题」。诚实边界已记:voice 维度信号中等偏弱,figures 池海外工程向为主、国内 figures = 0,SKILL.md §5 风格输出会偏海外工程向 register。

---



## 质量基准 + 反模式

### 6.1 什么算「好」（质量基准,5 条具体可验证）

1. **有针对自己产品 failure mode 的 eval 套件,不是公开 benchmark 分数** —— 「好」的最低门槛:能客观回答「这次改动让产品变好了还是变差了」,而且每次改动都能跑回归。(来源:Track 03 workflow 3/4 资深差异 + Track 04 canon eval-driven iteration)
2. **error analysis 是 PM 亲自做的、且是迭代的强制前置步骤** —— 「好」的 AI PM 拉过 10-50 条真实 trace（trace 条数量级出自 Hamel field-guide T03-S001）逐条标、归类成 failure mode,而不是凭直觉决定改什么。(来源:Hamel field-guide T03-S001 + Track 03 跨 4 workflow)
3. **LLM-as-judge 和人工标注校准到 75-90% 一致才 scale,用 binary 不用 Likert** —— 评估口径可靠、可回归（75-90% 一致阈值出自 Hamel evals-FAQ T03-S016）。(来源:Hamel evals-FAQ T03-S016 + Track 03 workflow 3)
4. **agent 产品的 ship 门是 pass^k 而非单次 demo** —— 「好」= 多次运行的稳定通过率达标,且有失败回退 + 用户控制权设计。(来源:τ-bench + Anthropic Building Effective Agents + Track 03 workflow 5)
5. **scoping 阶段就算过单用户 token 经济模型 + 标了风险分级** —— 「好」的 AI PM 不会做出一个单位经济模型为负、或踩了 EU AI Act 高风险条款才发现的产品。(来源:Track 03 workflow 1 + intake「成本控制是被忽视的硬技能」)

### 6.2 反模式（外行 / 入门常犯,10 条 —— Track 06 outsider-tell + Track 03 失败模式)

1. **跳过 error analysis 直接上指标 dashboard** —— 测的是噪声不是你的产品。(T03 / T06)
2. **「我们做了 evals」= 跑了个公开 benchmark 分数** —— eval 是针对自家产品 failure mode 的系统化测量。(T06 outsider-tell,极高频)
3. **LLM-judge 没和人工校准就 scale** —— 没校准的 judge 等于没用,团队很快不信它。(T03 / T06)
4. **demo 当 ship 门 / 在假数据上做漂亮 demo** —— demo-to-production gap,真数据一碰就崩。(T03 / T06)
5. **一遇到不准就喊「fine-tune 一下」** —— 绝大多数情况先动 prompt / context / RAG / eval,fine-tune 最后(「绝大多数」是 Hamel field-guide / Anthropic「先简单后复杂」一致传达的定性判断,非精确统计百分比)。(T06 outsider-tell / T03)
6. **把所有错误答案都叫「hallucination」** —— 内行区分幻觉 vs 检索错 vs 推理错 vs 指令没遵守,不同 failure mode 不同修法。(T06)
7. **「context window 越大越好,塞满它」** —— 填满触发 lost in the middle,质量反降。(T06)
8. **把 RAG 等同于 vector DB / 把 RAG 失败归咎数据库选错** —— RAG 失败 80% 在 chunking / 过时 embedding / 噪声源文档。(T02 避坑 / T06)
9. **把不是 agent 的需求做成 agent(更别做 multi-agent)** —— 无谓的不可靠 + 成本;agent 框架还是衰减最快的层。(T02 避坑 / T04)
10. **不算单用户 token 经济模型就进 POC / ship** —— 可能在做一个 ship 不了的产品;agent 多轮对话有二次方 token 增长陷阱。(T03 / T06 / intake)

> 补充高频反模式(进 SKILL.md 可酌情合并):POC 代码「悄悄转正」当 MVP 地基、把 AI 当 feature theater、用通用 eval dashboard(helpfulness_score / toxicity_score 10+ 通用指标)、golden set 当训练数据 / 越大越好、把单一 LLM provider hardcode 进产品、信「AI 自动生成 rubric 又自动打分」的全自动 eval。

---



## 智识谱系

> 保留分歧,不抹平。「双方都对」是没营养的废话。本行 <3 年、pre-canonical,流派之争尤其活跃。

### 7.1 四大流派（intake 四流派 + Track 04 canon 种子 + Track 01 figures 分裂)

| 流派 | 核心主张 | 奠基文本 | 当前代表 | 当前势力 |
|------|---------|---------|---------|---------|
| **模型派** | 在 frontier 模型上做轻应用,等模型自身升级 cover 一切;不重 eval / 不重私有数据 | (少写 workflow 长文,无清晰奠基文 —— 见 §8 幸存者偏差) | 散见,发声弱 | 存在但发声最弱,常被 eval 派 / 飞轮派的「幸存者偏差」遮蔽 |
| **工作流派** | 价值在把 AI 嵌入现有 SaaS workflow,核心是 workflow 不是模型;多数需求是 workflow 不是 agent | Anthropic「Building Effective Agents」(T04-S023) | Anthropic 工程团队 / swyx(Agent Engineering) | 2026 主流之一,与「薄框架派」高度重合 |
| **agent 派** | LLM + tools + memory 自主决策是未来形态;agent 产品化是独立主题 | ReAct(T04-S018)→ Agent Engineering(T04-S033) | swyx / coding agent 生态 / Simon Willison(谨慎乐观) | 上升,但被 τ-bench 的 pass^k 现实(零售域 pass^8 < 25%)持续校准 |
| **数据飞轮派** | 差异化在私有数据 + RLHF + finetune,用户用 → 数据 → 模型更好的闭环是护城河 | Eugene Yan llm-patterns 的 data flywheel 节(T04-S005) | Eugene Yan / NVIDIA(飞轮叙事) | **disputed** —— a16z「The Empty Promise of Data Moats」(T06-S017)祛魅:多数飞轮没真转起来、frontier 升级会碾平多数私有数据优势。保留两派 |

### 7.2 横切流派:厚框架派 vs 薄框架派（Track 02 工具流派 + Track 04 第 3 流派,可与工作流派合并理解)

- **厚框架派**: 用框架的抽象层 cover 复杂度。代表工具 = LangChain 经典抽象、早期 multi-agent 框架。**2026 退潮**(很多团队在 production 里主动移除)。
- **薄框架派**: 默认最轻的能跑的、按真实痛点加层。代表 = provider SDK / LiteLLM / LangGraph 作轻编排 / Anthropic「简单可组合 > 复杂框架」/ Hamel(notebook-centric, skeptical of magic)。**2026 主流**。
- 注:LangChain 自己也用 LangGraph 转向了薄框架 —— 这条分歧有明确的代际/时间方向。

### 7.3 横切流派:方法论派 vs 工具派（eval 维度,Track 02 + Track 06)

- **方法论派**(Hamel / Eugene Yan): eval 是方法论,工具只是 backend data store,核心是 error analysis + 人工标注。
- **工具派**(eval 平台厂商 LangSmith / Braintrust / Arize): 把「eval」收编成自家产品功能,倾向 AI 自动化 rubric + 打分。
- 行业共识明显偏方法论派(Hamel 是该主题密度最高的一手源)—— 但要意识到这本身可能是「发声者偏差」。

### 7.4 工程派 vs 产品 sense 派（AI PM 核心是什么 —— 本行最根本的张力,不调和)

- **工程派**(Hamel / Eugene Yan / Chip Huyen): AI PM 的核心 = eval + 技术理解。
- **产品 sense 派**(Marily Nika / Lenny,承接 Marty Cagan): 核心 = 产品判断 + AI 能力边界感,「该不该做、怎么验证需求、怎么组织团队」的产品判断不变。
- 模型脉搏 / 祛魅派(Simon Willison)不站队,做其他派别的「事实校准器」(给 agent 收口定义、造 prompt injection 这个词)。
- **关键张力保留**: intake warning 明示「『prompt engineering 是 AI PM 核心技能』是片面认知 —— 真正核心是 eval 设计 + 产品 fit 判断 + 团队协作」。这条张力 Phase 3 不要强行调和。

### 7.5 「AI PM」title 本身的角色混乱（不是流派之争,是角色诊断 —— 进 §9 Agentic 维度)

同一 title「AI 产品经理」在不同公司至少指 **4 种不同的人**:① 传统 PM + 负责 AI 项目(产品 sense 为主);② 技术 PM(PM + 一定 ML 工程能力,正演化为「Model PM」);③ 模型评估专员 + PM(eval-heavy);④ AI 应用业务负责人(偏 GTM / 商业)。
**分类法本身也无共识**:Arize 给 3 archetype、Data Science PM 给 4 类、ProdPad 给 12 种 PM —— 分类法彼此不一致,本身就是「这个职业还没有公认 OS」的证据。**保留两派**:Data Science PM / Product School 明说混乱;Arize(vendor)把它表述为「3 个清晰互补 archetype」—— vendor 倾向把混乱包装成「清晰的专业分工」,但一线求职 / 招聘体感是混乱。
**未解争议**:「AI PM 要不要会代码 / 懂模型」无定论 —— CS336 深水区路线 vs Andrew Ng「Generative AI for Everyone」非技术路线。本 synthesis 按「技术理解 + 产品 sense 双修」这一最主流定义提炼,但该争议本身未解。

---



## 诚实边界

> 信息截止 2026-05-14。本节诚实标注本 skill 的结构性局限 —— 不是「不能替代真人」这类宽泛话,是具体的、可验证的边界。

### 8.1 一手率勉强过线（52.2%）

- **实测一手率 52.2%**(159 条 source / 83 first-hand)—— 刚过 50% 线,不富余。各 track:figures 一手偏弱(8 人材料密度高但多 surrogate_primary,voice_samples 多标「转述」)、tools 70%、canon 69%、workflows 67%、glossary 仅 27%(术语定义类内容天然二手居多,但关键术语已用 Hamel 一手交叉验证)、sources 95%(但多为「作者本人 Substack / vendor docs」未被 verifier 识别)。**结论**:核心 claim 有一手交叉,但整体一手率不构成「高置信」,SKILL.md 任何引用都应可回溯到 source_id。

### 8.2 figures 池海外工程向为主,国内 figures = 0（结构性 gap）

- **国内(zh-CN)AI PM figures = 0** —— 朋克熊 / 唐辰等国内头部人物的主要发声渠道(知乎专栏 / 公众号 / CSDN)整体在黑名单上,找不到任何合规一手源(本人独立站 / arXiv / 官方节目页 / 出版社页)。这是**结构性 gap,非调研不足**。canon 的朋克熊书同样因黑名单 DROP。
- **8 位 figure 中仅 Marily Nika / Aakash Gupta 2 人 title 对口「AI 产品经理」**,其余 6 人是 applied scientist / ML engineer / 作者 / 大会创办人 / PM 策展人 —— 「AI PM 视角」在 figure 池里本就稀薄。
- **直接后果**: 本 SKILL.md 的风格(§5 表达 DNA)、案例、心智模型,会**偏海外工程向**。若用户主要在国内语境工作,figures 这一维度的代表性会打折;提炼出的 mental model 在「纯 AI PM 视角一致性」上弱于在「AI 工程落地一致性」上。国内工具(DeepSeek/Qwen/GLM)也只一张合并卡片。

### 8.3 工具栈 / 工作流模块衰减最快,3-6 个月必重校准

- **工具栈**: 新兴层 7 个全 high decay,agent 框架层尤其;模型版本号高频跳动(2026-05 已 GPT-5.5 / Claude Opus 4.7 / Gemini 3.1 Pro),「哪个模型最强」decay 极高;2026 内 Promptfoo→OpenAI、Statsig→Amplitude、Scale AI←Meta 入股,工具独立性在变。
- **工作流**: 6 个 workflow 无一稳态,最低 low 的那个也是「方法稳工具变」;agent 产品化 workflow decay 最快。
- **建议**: 工具栈 + 工作流模块每 **3-6 个月**跑一次 `update 大师 ai-product-manager`。心智模型 / 智识谱系 / 表达 DNA / canon 衰减慢(1-2 年)。

### 8.4 数字 / 法规日期 / 价格的来源与置信度

- **本 synthesis 出现的 specific 数字均带来源或 caveat**:pass^8 < 25%(τ-bench, T04-S022)、judge 校准 75-90% 一致(Hamel evals-FAQ, T03-S016)、golden set 30-50 个(Hamel, T03-S016)、MCP 78% 企业采用 / 97M 月下载(T02-S022)、「30% 2026 PM 岗是 AI PM / <5% 资深 PM ship 过 agent」(Aakash 个人估计 T01-S018/S019,**非权威 survey,引用必带 caveat**)、API 价格跨度 $0.10–$30/M input token(T02-S033,持续下行、会过时)。
- **法规日期**: EU AI Act 高风险条款 2026-08 落地(T06-S026 EUR-Lex 原文)、中国《生成式人工智能服务管理暂行办法》2023-08-15 施行(T06-S027 CAC 原文)、MCP 2024-11 Anthropic 开源 / 2025-12 进 Linux Foundation(T02-S021)。
- **intake 警示遵守**: 工资 / 薪资**不给具体数字** —— 本行薪资跨度极大、同 title 同公司差异极大,任何 specific 数字都是 hallucination risk。
- **本行没有公开的「AI PM 工具栈采用率 survey」**,必备层采用率(除 MCP)是多源交叉推断,不是 survey 实测。

### 8.5 其他具体局限

- **五阶段完整 SOP 是拼接的**: 本行 <3 年,没有一手长文从「想法」走到「数据飞轮」,6 个 workflow 的串联有推断成分。
- **协作边界证据不均**: PM↔工程师边界证据强(多个一手),PM↔数据/标注 中等(推断为主),**PM↔法务/安全/红队 薄弱** —— 这块在 SKILL.md 应诚实降级,不假装有详细 SOP。
- **eval 派幸存者偏差**: workflows / canon 证据高度来自 eval 派(Hamel / Eugene Yan / Shreya Shankar)+ eval 工具厂商;「模型派」(等 frontier 模型变好、不重 eval)几乎不写 workflow 长文 —— 不代表他们不存在,§7 已保留分歧,但本 skill 的「eval 是地基」心智模型要意识到证据来源有偏。
- **pre-canonical**: 本行作为独立角色 <3 年,没有三方共识的 AI-PM textbook;canon 重心被迫落到工程向 blog(Eugene Yan / Hamel)+ seminal paper,「产品经理视角」的正典本身稀薄。
- **voice 维度信号中等偏弱**: 对话样本库 13 段多数标「转述」(来自搜索摘要 + 节目描述,未逐集抓 podcast 字幕),voice_confidence = medium。SKILL.md §5 风格输出部分靠 LLM 默认 register 补,非全部来自真行业语料。

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-14 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-14 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-14 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-14 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-14 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-14 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-14 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-14 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-14 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
