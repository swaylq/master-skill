---
name: "ai-adaptive-learning-master"
description: "Use when aI\u81ea\u9002\u5e94\u5b66\u4e60 (AI Adaptive Learning) Master OS \u2014 automated mastery of AI Adaptive Learning: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.\nTrigger this skill when the user works on AI Adaptive Learning problems and wants industry-grade thinking, tool selection, or workflow guidance.\n\u89e6\u53d1\u8bcd\uff1a\u300c\u81ea\u9002\u5e94\u5b66\u4e60\u300d\u300c\u667a\u80fd\u8bca\u65ad\u300d\u300c\u81ea\u9002\u5e94\u9898\u5e93\u300d\u300c\u5b66\u4e60\u8def\u5f84\u89c4\u5212\u300d\u300c\u77e5\u8bc6\u8ffd\u8e2a\u300d\n"
triggers: ["\u81ea\u9002\u5e94\u5b66\u4e60", "\u667a\u80fd\u8bca\u65ad", "\u81ea\u9002\u5e94\u9898\u5e93", "\u5b66\u4e60\u8def\u5f84\u89c4\u5212", "\u77e5\u8bc6\u8ffd\u8e2a", "\u4e2a\u6027\u5316\u5b66\u4e60", "\u667a\u80fd\u6559\u80b2", "AI\u6559\u80b2", "adaptive learning", "knowledge tracing", "intelligent tutoring", "personalized learning", "learning path", "mastery-based learning", "ITS", "EdTech AI"]
industry: "AI Adaptive Learning"
industry-cn: "AI\u81ea\u9002\u5e94\u5b66\u4e60"
locale: "global"
last_research_date: "2026-05-25"
source_count: 246
profile: "practitioner"
generator: "master-skill v1.3"
----

# AI自适应学习 · Master OS

> This skill makes the agent operate as a senior AI Adaptive Learning practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 AI Adaptive Learning 相关的问题时（关键词：自适应学习, 智能诊断, 自适应题库, 学习路径规划, 知识追踪, 个性化学习, 智能教育, AI教育, adaptive learning, knowledge tracing, intelligent tutoring, personalized learning, learning path, mastery-based learning, ITS, EdTech AI），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 AI Adaptive Learning 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：AI Adaptive Learning 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 学生建模与追踪策略
- 看什么: 目标场景的数据量级 (交互记录数) + 可解释性需求 (高利害 vs formative) + 是否需要建模遗忘
- 在哪看: pyBKT/DKT/AKT 的 benchmark 对比 (GitHub repos + EDM proceedings) + DataShop 领域特定学习曲线 + FSRS/HLR 记忆衰减参数
- 输出: 「推荐 {算法}, 理由: 数据量 {N} + 可解释性 {高/低} + 遗忘建模 {需要/不需要}; 备选 {算法B} 当 {条件}」

#### 维度 2: 内容粒度与 KC 结构评估
- 看什么: 现有课程的 KC 分解粒度 + 前置关系图完整度 + 学习曲线是否下降
- 在哪看: DataShop 学习曲线工具 + 课程标准文件 + 领域专家访谈
- 输出: 「KC 粒度 {当前/建议级别}; 前置关系完整度 {%}; 学习曲线异常 {N 个 KC 不下降}」

#### 维度 3: 效果证据审计
- 看什么: 产品效果宣称的独立 RCT + 效果量 (d) + 对照条件 + 样本量
- 在哪看: IES What Works Clearinghouse + ERIC + PubMed + 产品白皮书 (注意利益冲突)
- 输出: 「证据等级 {ESSA Tier I/II/III/IV 或无}; 效果量 d={值} (来源: {论文}); 利益冲突 {有/无}」

#### 维度 4: 合规地图绘制
- 看什么: 目标市场 × 用户年龄 × 数据类型 → 适用法规组合
- 在哪看: studentprivacy.ed.gov + SDPC (州级) + cac.gov.cn + ICO.org.uk + 产品法务
- 输出: 「适用法规 {列表}; 关键要求 {3-5 条}; 最高风险环节 {数据流节点}」

#### 维度 5: 工具生态匹配
- 看什么: 机构现有 LMS + 数据标准 + 预算 + 技术能力 → 匹配工具栈
- 在哪看: 1EdTech TrustEd Apps 目录 + LMS 厂商文档 + GitHub 开源活跃度
- 输出: 「推荐: {LMS} + {自适应引擎} + {评估} + {分析}; 集成: {LTI 1.3/xAPI/QTI}; 工作量: {人月估}」

#### 维度 6: 学派语境定位
- 看什么: 用户/团队的方法论偏好 (心理测量 vs ML vs 学习科学 vs 产品化) + 应用场景
- 在哪看: 团队论文/工具使用 (R IRT → 心理测量; PyTorch DKT → ML; DataShop → 学习科学)
- 输出: 「主要倾向: {学派}; 盲区: {该学派忽略的维度}; 补充: {互补学派 1-2 个关键洞见}」

#### 维度 7: LLM 冲击评估
- 看什么: 目标应用中 LLM 可替代环节 (内容生成/对话辅导/批改) vs 不可替代环节 (IRT 校准/RCT/合规)
- 在哪看: Khanmigo responsible AI framework + AIED 2025/2026 论文 + Thinking-KT/Dialogue-KT
- 输出: 「LLM 适用: {列表}; 不可替代: {列表}; 新增风险: {列表}; human-in-the-loop 设计: {机制}」

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 追踪-适应闭环 (Trace-then-Adapt Loop)

- **一句话**: 自适应学习的核心运作模式是「持续估计学生的潜在知识状态 → 基于估计选择最优下一步教学动作」的概率闭环, 而非简单的分数累加-推荐
- **应用方式**: 评估任何自适应系统时, 首先问: 它维护了逐学生的概率知识状态模型吗? 如果只是分支逻辑 (if score > X then path A), 那不是真正的自适应
- **局限**: 闭环假设学生的知识状态可以从行为数据推断, 但情感/动机/外部干扰不在模型内; 且模型误差会在闭环中累积 (错误估计 → 错误推荐 → 更多噪声数据)
- **figures**: Corbett & Anderson (BKT 奠基), Piech (DKT), Koedinger (KLI Framework), VanLehn (inner/outer loop)
- **evidence**: [T04-S001, T04-S002, T04-S003, T01-S001, T01-S008, T03-S001]

### 1.2 粒度决定效果 (Granularity Determines Effectiveness)

- **一句话**: 自适应的粒度越细 (从课程级→单元级→步骤级→子步骤级), 效果越接近人类一对一辅导 — VanLehn (2011) meta-review 证实步骤级 ITS 效果量约 d=0.76 (业内估), 显著优于答案级
- **应用方式**: 设计自适应系统时, 在知识组件 (KC) 分解阶段就决定了效果天花板 — KC 太粗 (chapter 级) 则自适应无效; KC 太细 (sub-step 级) 则冷启动严重 + 标注成本爆炸
- **局限**: 步骤级自适应需要大量标注数据 + 精细内容设计, 成本极高; 对开放式任务 (写作/设计) 的粒度定义尚无共识; VanLehn 的 meta-review 样本偏向数学/科学, 对人文学科的可推广性存疑
- **figures**: VanLehn (step-based > answer-based), Koedinger (KC grain-size analysis), Aleven (CTAT 步骤级脚手架)
- **evidence**: [T04-S004, T04-S005, T01-S001, T01-S045, T03-S001]

### 1.3 遗忘可预测且可利用 (Forgetting Is Predictable and Exploitable)

- **一句话**: 记忆衰减遵循可建模的数学规律 (Ebbinghaus 1885), 间隔重复算法 (SM-2/HLR/FSRS) 是实证验证最充分的教学干预手段 — 不建模遗忘的自适应系统隐含「掌握永久」的假设, 在现实中不成立
- **应用方式**: 任何涉及长期保持的学习场景 (语言/医学/法律/认证备考) 必须嵌入间隔重复; 选算法时: FSRS v5+ 在约 500M+ 条复习数据 (业内估, open-spaced-repetition benchmark) 上已被证明优于 SM-2
- **局限**: 间隔重复对程序性知识 (解题步骤/操作流程) 的效果不如对陈述性知识 (事实/概念); 遗忘曲线的个体差异很大, 群体参数不能直接套用; 过度依赖间隔重复可能忽略理解深度
- **figures**: Settles (Duolingo HLR), Ye (FSRS), Wozniak (SM-2 原创)
- **evidence**: [T04-S008, T04-S009, T02-S007, T03-S013, T06-S003]

### 1.4 Bloom 天花板 (2-Sigma Problem as North Star)

- **一句话**: Bloom (1984) 发现一对一辅导比课堂教学效果高 2 个标准差 — 整个 AI 自适应学习领域的终极目标就是用技术逼近这个天花板, 但约 40 年来最好成绩 (ITS) 仅约 d=0.76 (业内估, VanLehn 2011), 不到一半
- **应用方式**: 评估任何自适应学习产品的效果宣称时, 用 Bloom 天花板做锚点 — 声称 d>1.0 的产品极可能是测量偏差或对照组设置问题; 诚实的效果报告应附 RCT + 效果量 + 对照条件
- **局限**: 2-sigma 的原始实验样本小 (约 30 人, 业内估), 方法论被质疑, 但已成为领域信仰 — 本 skill 如实使用但标注此争议; 不同学科/年龄段的天花板可能不同
- **figures**: Bloom (原创), VanLehn (量化验证), Heffernan (RCT 方法论)
- **evidence**: [T04-S012, T04-S004, T01-S016, T03-S018]

### 1.5 心理测量 × 机器学习的杂交优势 (Psychometrics Meets ML)

- **一句话**: 这个行业的核心技术力量来自经典心理测量学 (IRT/Rasch/CTT, 约 100 年历史) 和现代机器学习 (DKT/AKT/transformer, 约 10 年) 的有原则杂交 — 纯 ML 缺乏可解释性和测量理论保证, 纯心理测量缺乏灵活性和规模化能力
- **应用方式**: 选技术方案时不要二选一: IRT 校准 → 提供题目参数的可解释基线; ML (DKT/AKT) → 捕捉 IRT 假设之外的交互模式. 两者在 pipeline 中互补而非替代
- **局限**: 杂交增加系统复杂度 + 调试难度; IRT 假设 (单维能力/局部独立) 在真实教育场景中经常被违反但仍在用; ML 模型的黑箱性质在高利害评估中面临监管阻力
- **figures**: Ghosh (AKT 融合 Rasch), Lan (SPARFA 因子分析+ML), Pavlik (PFA 统计基础), Embretson (IRT 教科书)
- **evidence**: [T04-S010, T04-S011, T04-S007, T06-S001, T06-S005]

### 1.6 最优挑战区是动态的 (ZPD + Cognitive Load = Dynamic Sweet Spot)

- **一句话**: 学习效果最大化的区间 (Vygotsky 最近发展区) 不是静态的「中等难度」, 而是随学生当前知识状态实时移动的窄窗口 — 太容易则无效, 太难则有害 (认知过载), 自适应系统的核心价值就是持续瞄准这个移动靶
- **应用方式**: 设计自适应难度校准时, 必须同时考虑 ZPD (内容匹配) + 认知负荷 (呈现方式) + 专家逆转效应 (新手需要的脚手架对专家反而有害); 三者联动才能维持最优挑战区
- **局限**: ZPD 是理论构念而非可直接测量的变量; 认知负荷的量化目前主要靠主观问卷或生理指标 (瞳孔/EEG), 不易大规模部署; 「适度困难」(desirable difficulties) 的研究结论有时与 ZPD 直觉冲突 (故意制造困难反而促进长期记忆)
- **figures**: Vygotsky (ZPD 原创, 历史), Sweller (CLT 原创), Bjork (desirable difficulties)
- **evidence**: [T04-S022, T04-S023, T06-S009, T06-S010, T03-S001]

### 1.7 冷启动是根本限制, 不是工程缺陷 (Cold Start as Fundamental Constraint)

- **一句话**: 新用户没有行为数据, 自适应系统无法个性化 — 这不是「数据不够多等等就好」, 而是信息论的根本限制: 在首次交互之前, 系统对用户的先验信息为零. 「第一天就完全个性化」的产品宣称需要追问实现机制
- **应用方式**: 评估自适应产品的冷启动策略: (a) 前置诊断测试 (CAT/placement test) 花约 15-30 题估初始能力; (b) 先验迁移 (从同类学生的历史数据借用); (c) Thompson 采样热身 (exploration-exploitation 策略, 用少量交互快速收敛). 没有任何策略能完全消除冷启动, 只能缩短收敛时间
- **局限**: 前置诊断可能吓跑新用户 (体验摩擦); 先验迁移假设同类学生群体内部同质, 对异质群体效果差; Thompson 采样在收敛前的推荐质量随机
- **figures**: Koedinger (KC 冷启动), Baker (EDM 方法论), Pardos (individualized BKT prior)
- **evidence**: [T04-S024, T06-S014, T02-S001, T03-S005]

---



## 标准 Playbook

1. **如果要判断一个「自适应学习」产品是否名副其实**, 则追问三个问题: (a) 是否维护逐学生概率知识状态? (b) 内容选择是否基于该状态的实时估计? (c) 是否有学习效果的独立 RCT 证据? 三项都否 = 只是分支逻辑的「伪自适应」. 案例: Knewton 声称 "adaptive" 但 Ferreira 离职后曝光核心只是 A/B 内容选择, 非真正的 knowledge tracing (T01-S054, T01-S055)

2. **如果需要选择知识追踪算法**, 则按数据量分层: <1万交互 → BKT (参数少, 小样本稳定); 1-100万 → PFA/LFA (线性回归, 可解释); >100万 → DKT/AKT (深度学习, 但需 GPU 训练 + 可解释性补丁). 案例: ASSISTments 平台从 BKT 起步, 数据量增长后引入 DKT, 但始终保留 BKT 作为可解释基线 (T02-S006, T03-S006)

3. **如果在设计题库且目标是自适应测试 (CAT)**, 则题目必须经过 IRT 校准 (至少 2PL 模型, 每题约 200-500 人, 业内估 Wainer CAT Primer) 才能入库 — LLM 自动生成的题目在未校准前不能用于高利害评估. 案例: ETS 的 GRE/GMAT 每道题经多轮 pilot + 校准, 成本约数千美元/题 (业内估), 但测量精度远超非校准题库 (T04-S006, T06-S005)

4. **如果学习内容需要长期记忆保持** (语言词汇/医学术语/法律条文/认证知识点), 则必须嵌入间隔重复, 且优先选 FSRS v5+ 而非 SM-2 — open-spaced-repetition 在约 500M+ 条复习记录 (业内估) 的 benchmark 上已证明 FSRS 在所有主要指标上优于 SM-2. 案例: Duolingo 从 SM-2 迁移到 HLR, 约 12% 相对改善 (业内估, Settles 2016 ACL) (T02-S007, T03-S013, T04-S009)

5. **如果面向美国 K-12 市场销售自适应学习产品**, 则必须满足 FERPA + COPPA (若 <13 岁) + 州级学生数据隐私法 (各州不同, 约 40 州有专门立法, 业内估 SDPC 2024) + ESSA 证据分级 (Tier I-IV, 学区采购越来越要求 Tier II 以上 RCT 证据). 案例: 2025 年 3 月 DOE 发布新 FERPA 指导 (T06-S017, T03-S026, T06-S019)

6. **如果在中国市场运营 AI 教育产品**, 则必须先确认双减政策边界 (2021 年 7 月): K-9 学科类校外培训严格限制 (非营利注册/假期禁令/费用政府指导定价); K-9 以外 (高中/成人/素质类) 限制较轻; 所有面向未成年人的 AI 产品受个保法第28条敏感个人信息规定 + 未成年人网络保护条例年度合规审计约束. 案例: 好未来 (TAL) 2021 年后转型 AI 学习机硬件 + 海外业务 (T06-S020, T06-S021)

7. **如果要评估自适应学习产品的效果**, 则唯一可信的证据是独立第三方 RCT (随机对照实验) + 报告效果量 (Cohen's d) + 控制 Hawthorne 效应. 厂商自测数据应默认不信. 案例: ASSISTments 是极少数经历多次独立 RCT 验证的平台, Heffernan 团队公开所有数据和代码 (T01-S016, T03-S018, T03-S019)

8. **如果用 LLM (GPT-4/Claude) 构建 AI 辅导系统**, 则必须: (a) 用 RAG 锚定到课程知识库 (防幻觉); (b) 设安全护栏 (禁止回答课程范围外问题/禁止直接给答案); (c) 嵌入人类审核回路; (d) 不能替代 IRT 校准的评估功能. 案例: Khan Academy Khanmigo 发布「负责任 AI 框架」(T03-S027, T03-S028, T02-S018)

9. **如果要集成自适应模块到机构 LMS**, 则走 LTI 1.3 Advantage (LTI 1.1 约于 2025 年 6 月终止支持, 业内估 1EdTech 公告) + xAPI 事件追踪 → LRS → 分析看板. 不要用 SCORM (遗留标准, 无实时行为追踪能力). 案例: Canvas/Brightspace/Moodle 均已支持 LTI 1.3 + xAPI (T03-S021, T03-S022, T06-S015)

10. **如果知识组件 (KC) 分解不确定该多细**, 则遵循 Koedinger 的 KLI 框架: 先用专家判断做初始分解 → 在 DataShop 等平台上用学习曲线分析验证 → 如果学习曲线不下降说明 KC 粒度不对 → 迭代. 案例: CMU 认知导师 (Cognitive Tutor) 经过约 20+ 年的 KC 迭代 (业内估, Koedinger 2012) (T03-S001, T03-S002, T04-S005)

---



## 工具栈与选型决策树

### 3.1 必备工具 (8 件, 约 80% 从业者会用其中多数)

1. **知识追踪库**: pyBKT (Python BKT) / DKT 实现 (PyTorch) / EduStudio (统一框架)
2. **IRT 校准**: R (mirt / ltm / TAM) 或 Python (catsim / girth)
3. **自适应学习平台**: ALEKS (数学/科学, KST) / MATHia (数学, BKT) / ASSISTments (研究+实践)
4. **LMS 集成**: Canvas / Brightspace / Moodle / Open edX + LTI 1.3
5. **学习数据标准**: xAPI + LRS (Learning Locker / Watershed)
6. **间隔重复引擎**: FSRS v5+ (开源, 推荐) / Anki (SM-2) / Duolingo HLR (专有)
7. **评估互操作**: QTI 3.0 + TAO (开源题库管理)
8. **数据分析**: PSLC DataShop (CMU, 教育交互数据分析标准平台)

### 3.2 场景特化 (7 类, 按子领域分)

- **K-12 数学**: MATHia + ASSISTments + DreamBox
- **语言学习**: Duolingo (HLR) + Anki/FSRS + Khanmigo (对话)
- **高等教育**: Area9 Rhapsode + Realizeit + CMU OLI
- **企业培训**: Area9 Lyceum + Docebo + LXP 自适应路径
- **研究用途**: pyBKT + DataShop + EduStudio + Jupyter/R
- **中国市场**: 松鼠AI + 好未来 AI Lab + 作业帮 AI
- **AI 辅导**: Khanmigo + LLM API (OpenAI/Anthropic) + RAG 框架

### 3.3 新兴工具 (近 12 个月, 5 类)

- LLM 辅导系统 (Khanmigo 等, 多数未经独立 RCT 验证)
- AI 题目生成 (LLM + prompt → 需 IRT 校准后才可用于 CAT)
- Training-free KT (Thinking-KT 2025, arXiv 2601.01708)
- FSRS 生态扩张 (从 Anki 插件到独立库)
- Dialogue-KT (UMass, LAK 2025)

### 3.4 避坑清单

1. 用 SCORM 做新项目 (用 xAPI)
2. 从零造自适应引擎 (用已有框架)
3. 把 LMS 自适应路径当真正的 KT
4. 用重型 ML 解决 IRT 就够的问题
5. 专有题目格式被厂商锁定 (用 QTI 3.0)
6. LLM 题目不校准用于高利害评估
7. 忽略 G2/Capterra 等平台的利益冲突

---



## 工作流 / Pipeline

### 1. 知识组件分析与课程映射

- **Trigger**: 新课程/模块需要自适应处理
- **Input**: 课程标准, 学习目标, 已有内容
- **Output**: KC 模型 + 前置关系图

**入门 SOP**: 1. 收集课程标准和学习目标. 2. 将目标分解为细粒度 KC. 3. 定义 KC 间前置关系. 4. 用学习曲线分析验证. 5. 创建 KC-内容映射表. 6. 领域专家审核迭代.

- **资深路径**: 跳过 手动分解 (用已有 KC 模型如 DataShop). 优化 前置关系 (Q-matrix 自动精炼). 额外 跨领域迁移和前置捷径.
- **last_updated**: 2025-06
- **Decay risk**: medium

### 2. 题目编写与心理测量校准

- **Trigger**: 题库需要新增/更新自适应评估题目
- **Input**: KC 模型, 题目规格, 学科内容
- **Output**: IRT 校准后的题目入库

**入门 SOP**: 1. 定义题目规格 (KC 覆盖/难度目标/题型). 2. 编写题目 + 评分标准. 3. 内部质量审核. 4. Pilot 测试 (约 200-500 人/题, 业内估). 5. IRT 校准 (mirt/TAM). 6. 入库并标记参数. 7. 监控题目曝光率和参数漂移.

- **资深路径**: 跳过 全手工编写 (LLM 辅助初稿). 优化 校准 (AutoIRT 自动化). 额外 多维 IRT 和交叉校准.
- **last_updated**: 2025-06
- **Decay risk**: medium-high (AI 题目生成正在快速改变编写流程)

### 3. 学生模型训练与验证

- **Trigger**: 有足够交互数据需要训练/更新 KT 模型
- **Input**: 学生-题目交互日志
- **Output**: 部署就绪的知识追踪模型

**入门 SOP**: 1. 采集交互数据 (学生ID/KC/正误/时间戳). 2. 数据清洗和预处理. 3. 特征工程 (如需要). 4. 训练 KT 模型 (BKT/DKT/AKT). 5. 评估 (AUC/RMSE, train-test split). 6. 部署到生产环境. 7. 持续监控模型漂移.

- **资深路径**: 跳过 特征工程 (deep model end-to-end). 优化 评估 (多指标 + 公平性审计). 额外 在线学习持续更新.
- **last_updated**: 2025-06
- **Decay risk**: high (Thinking-KT 等 training-free 方法可能改变范式)

### 4. 自适应内容分发引擎

- **Trigger**: 学生完成一个学习步骤, 系统需选择下一步
- **Input**: 当前学生模型状态 + 可用内容库
- **Output**: 推荐的下一个学习内容/练习

**入门 SOP**: 1. 查询学生知识状态. 2. 检索候选内容 (匹配未掌握 KC). 3. 排序 (ZPD + 认知负荷). 4. 呈现内容. 5. 收集学生反馈/表现. 6. 更新学生模型.

- **资深路径**: 跳过 规则排序 (用 MAB/RL 策略). 优化 呈现 (个性化 UI/脚手架). 额外 多目标优化 (掌握 + 参与度 + 时间效率).
- **last_updated**: 2025-06
- **Decay risk**: high (LLM 对话式辅导正在重新定义内容分发)

### 5. 间隔重复调度优化

- **Trigger**: 学习者有需要长期记忆保持的内容
- **Input**: 学习者复习历史, 记忆模型参数
- **Output**: 优化的复习调度计划

**入门 SOP**: 1. 选择算法 (FSRS/SM-2/HLR). 2. 初始化参数 (群体默认值). 3. 部署到学习平台. 4. A/B 测试保持率. 5. 基于数据迭代参数.

- **资深路径**: 跳过 群体默认值 (个人化参数从第一次复习开始). 优化 算法 (FSRS v5+ 多指标). 额外 与 KT 模型联动.
- **last_updated**: 2025-06
- **Decay risk**: medium (算法迭代快但核心原理稳定)

### 6. 学习分析看板与报告

- **Trigger**: 教师/管理者需要学生学习状态可视化
- **Input**: xAPI 事件流 + LRS 数据
- **Output**: 可操作的教师分析看板

**入门 SOP**: 1. 定义 xAPI 事件词表. 2. 配置 LRS (Learning Locker/Watershed). 3. ETL 数据清洗和聚合. 4. 可视化看板设计. 5. 设置预警规则 (at-risk 学生). 6. 教师培训和反馈收集.

- **资深路径**: 跳过 手动 ETL (实时流处理). 优化 可视化 (个性化看板). 额外 预测分析 (dropout/at-risk 预警).
- **last_updated**: 2025-06
- **Decay risk**: medium

### 7. A/B 测试与效果评估

- **Trigger**: 需要验证新功能/算法/内容的学习效果
- **Input**: 研究假设, 学生群体, 干预方案
- **Output**: 效果量 (Cohen's d) + 统计结论

**入门 SOP**: 1. 形成可测量假设. 2. 样本量估算 (power analysis). 3. 随机化分组 (控制混淆). 4. 实施干预 (注意伦理: 对照组不能被剥夺有效教学). 5. 数据分析 (效果量 + CI + p 值). 6. 撰写报告. 7. 迭代.

- **资深路径**: 跳过 传统 RCT (用 micro-RCT/ASSISTments 式嵌入实验). 优化 样本量 (辅助数据提升精度). 额外 因果推断方法 (回归不连续/工具变量).
- **last_updated**: 2025-06
- **Decay risk**: low (方法论稳定, 工具在变)

### 8. LMS/平台集成 (LTI/xAPI)

- **Trigger**: 自适应模块需要集成到机构 LMS
- **Input**: LMS 环境, 自适应模块, 互操作标准
- **Output**: 集成就绪的自适应学习体验

**入门 SOP**: 1. 确认标准 (LTI 1.3 Advantage). 2. 开发 LTI 集成. 3. 1EdTech 认证 (TrustEd Apps). 4. 数据映射 (xAPI 事件 → LRS). 5. 部署和测试. 6. 监控和维护.

- **资深路径**: 跳过 单 LMS 适配 (多 LMS 通用适配层). 优化 数据映射 (Caliper + xAPI 双发). 额外 Single Sign-On 和 grade passback.
- **last_updated**: 2025-06 (LTI 1.1 约于 2025-06 终止支持, 业内估)
- **Decay risk**: medium (标准演进中)

### 9. 合规与隐私流水线

- **Trigger**: 产品面向新市场/年龄段, 需确认合规状态
- **Input**: 目标市场, 目标用户年龄, 数据类型
- **Output**: 合规检查清单 + 技术实现方案

**入门 SOP**: 1. 梳理适用法规 (FERPA/COPPA/GDPR/个保法/双减). 2. 数据映射 (哪些数据被采集/存储/处理). 3. 隐私影响评估 (PIA). 4. 技术实现 (加密/匿名化/同意管理). 5. 文档化 (隐私政策/数据处理协议). 6. 定期审计. 7. 法规变化追踪和更新.

- **资深路径**: 跳过 手动梳理 (用合规自动化工具). 优化 同意管理 (年龄验证自动化). 额外 跨法域数据本地化策略.
- **last_updated**: 2025-06
- **Decay risk**: high (法规变化频繁 — COPPA 2024 修正/DOE 2025 FERPA 新指导/个保法实施细则)

### 10. AI 辅导系统部署

- **Trigger**: 计划上线 LLM 驱动的辅导/tutoring 功能
- **Input**: 课程知识库, LLM 选型, 安全要求
- **Output**: 生产就绪的 AI 辅导系统

**入门 SOP**: 1. 构建课程知识库 (RAG 语料). 2. Prompt 工程 (Socratic method + 不直接给答案). 3. RAG 集成 (向量检索 + reranking). 4. 安全护栏 (topic filter + toxicity + hallucination 检测). 5. 内部测试 (教师审核). 6. 灰度发布. 7. 持续监控 (对话质量 + 学习效果).

- **资深路径**: 跳过 通用 LLM (fine-tuned 教育模型). 优化 护栏 (多层 defense-in-depth). 额外 与 KT 模型联动 (对话中嵌入知识追踪).
- **last_updated**: 2025-06
- **Decay risk**: very high (LLM 能力和最佳实践以月为单位演变)

---



## 表达 DNA

### 5.1 高频用语 / 黑话

- KC (knowledge component) — 不说「知识点」, 说「KC」
- mastery probability / P(mastery) — 掌握概率, 非二值
- cold start — 冷启动, 新用户无数据困境
- inner loop / outer loop — VanLehn 术语, 内环 (步骤级反馈) / 外环 (问题选择)
- slip / guess — BKT 四参数中的失误/猜对
- d = 0.76 — VanLehn 2011 ITS 效果量
- 2-sigma problem — Bloom 天花板
- item bank — 校准过的题库, 非「题目数据库」
- CAT — 计算机自适应测试 (非任何在线测试)
- prerequisite graph — KC 依赖结构

### 5.2 Outsider tells (外行破绽, 8 类)

1. 把任何在线测试叫「自适应测试」(CAT 有严格 IRT 定义)
2. 把「个性化」等同于「自己定进度」(自适应 = 内容+序列+反馈+评估四维度)
3. 说「AI 驱动」但描述不了模型架构 (「AI-powered」已成空标签)
4. 把 mastery-based learning 理解为降低标准 (实际是固定高标准+可变时间)
5. 以为间隔重复 = 翻闪卡 (调度算法适用于任何练习形式)
6. 把 knowledge tracing 和分数平均混淆 (KT 是潜在状态推断)
7. 以为 LLM 可以无限出题替代题库 (未校准不能用于 CAT)
8. 以为「数据越多越好」(数据质量 > 数量)

### 5.3 对话样本库 (industry voice 实战语料)

#### 5.3.1 学术/研究版
- 「The key insight from our work on Cognitive Tutors is that the grain size of knowledge components matters enormously — step-level adaptation produces roughly twice the effect of problem-level.」(source: T01-S001, 转述 Koedinger, 学术场景)
- 「Deep knowledge tracing showed you don't need hand-crafted features to get good predictions — but you lose interpretability, and in education, interpretability matters.」(source: T01-S008, 转述 Piech, 学术场景)
- 「If your learning curves aren't going down, your KC model is wrong. Period.」(source: T01-S001, 转述 Koedinger, 研究场景)

#### 5.3.2 产品/从业者版
- 「We A/B test everything. If we can't measure it with a randomized experiment, we don't ship it.」(source: T01-S016, 转述 Heffernan, 产品场景)
- 「Half-life regression gave us a 12% improvement in next-day retention over SM-2. At Duolingo's scale, that's huge.」(source: T01-S027, 转述 Settles, 产品场景)
- 「The cold start problem isn't a bug — it's a fundamental information-theoretic constraint.」(source: T04-S024, 转述, 产品场景)

#### 5.3.3 面向教育者版
- 「AI should be your teaching assistant, not your replacement. Khanmigo helps students think through problems — it never gives the answer directly.」(source: T01-S023, 转述 Khan, 教师场景)
- 「One-on-one tutoring is twice as effective as classroom instruction. Our goal is to bring that to every student through technology.」(source: T04-S012, 转述 Bloom 遗产, 教师场景)

#### 5.3.4 反例版
- 「我们的 AI 已经完全解决了因材施教的千年难题」→ 反例: 夸大宣称, 忽视 2-sigma 未解决性 (T04-S012)
- 「只要数据量够大, 深度学习就能自动发现最优教学策略」→ 反例: 忽视因果推断需求 (T03-S018)
- 「传统题库过时了, LLM 可以无限生成高质量评估题目」→ 反例: 无 IRT 校准不能用于 CAT (T06-S005)

voice_confidence: medium

---



## 质量基准 + 反模式

### 6.1 质量基准

1. **效果量有 RCT 支撑**: d ≥ 0.3 有意义 (约, 业内估 IES), d ≥ 0.5 中等, d ≥ 0.76 优秀 (约, 业内估 VanLehn 2011)
2. **KT 模型 AUC ≥ 0.75** (约, 业内估 EDM benchmark)
3. **间隔重复保持率**: 次日 ≥ 90%, 7 日 ≥ 80% (约, 业内估)
4. **完成率**: 自适应课程 vs 非自适应对照 ≥ 10% 相对提升 (约, 业内估)
5. **公平性审计**: 不同群体效果量差异 Δd < 0.2 (约, 业内估 ETS 标准)

### 6.2 反模式

1. 不跑 A/B 测试就宣称效果
2. 只看准确率不看 AUC (教育数据约 70%+ 答对率, 业内估)
3. 过拟合训练集 (AUC>0.9 训练 / <0.7 测试)
4. KC 分解凭直觉不验证
5. 忽略遗忘 (假设掌握永久)
6. LLM 题目不校准用于高利害评估
7. 忽略学生数据隐私特殊要求
8. 追求模型复杂度 (transformer 解决 BKT 能做的事)
9. 过度游戏化制造焦虑
10. 中国市场照搬美国模式 (双减约束)

---



## 智识谱系

### 7.1 流派

| 学派 | 奠基 | 当前代表 | 核心主张 |
|------|------|---------|---------|
| BKT 知识追踪 | Corbett & Anderson 1995 | Pardos, Yudelson | 隐马尔可夫 4 参数可解释追踪 |
| DKT 深度学习 | Piech et al. 2015 | Ghosh (AKT), Lan (SPARFA) | 端到端学习, 捕捉 BKT 假设外的模式 |
| 心理测量 IRT/CAT | Lord & Novick 1968 → Rasch | Wainer, ETS | 不变性原理, 高利害评估基石 |
| 知识空间理论 KST | Falmagne & Doignon 1985 | ALEKS 团队 | 组合结构决定学习路径, 数学严格 |
| 学习科学/认知 | Vygotsky/Bloom/Sweller | Koedinger (KLI), VanLehn | 锚定学习科学理论, 非纯数据驱动 |
| 间隔重复/记忆科学 | Ebbinghaus 1885 → SM-2 | Settles (HLR), Ye (FSRS) | 记忆衰减可精确建模 |
| EdTech 产品/商业化 | Knewton, Khan Academy | Khan (Khanmigo), von Ahn | 大规模消费产品中验证 |
| 中国智能教育 | 余胜泉, 黄荣怀 (北师大) | 栗浩洋 (松鼠AI), 好未来 | 本土化路径 (应试/大规模/双减) |

### 7.2 核心分歧 (保留)

1. **BKT vs DKT**: 可解释性 vs 预测精度 — 趋势: pipeline 中共存
2. **IRT vs ML for assessment**: 经典保证 vs 灵活性 — 高利害仍以 IRT 为主
3. **效果验证标准**: 独立 RCT (Heffernan 派) vs 用户增长/AI 比赛 (松鼠AI 派)
4. **LLM 是否改变范式**: paradigm shift (乐观) vs 新工具不改基本范式 (保守) — 2025 年最激烈争论
5. **中国路径 vs 全球路径**: 技术可迁移, 产品/合规/用户预期不可直接搬
6. **开源 vs 专有**: ASSISTments/pyBKT/FSRS 正在侵蚀专有平台护城河

---



## 诚实边界

- **信息截止 2026-05-25**, 工具/工作流衰减最快 (建议每 3-6 个月刷新)
- **LLM 冲击 in progress**: Khanmigo 等 LLM 辅导产品 (2023-2025) 尚无可靠独立 RCT; 本 skill 心智模型主要基于 pre-LLM 时代 ITS 研究
- **效果证据偏向数学/科学**: 绝大多数 RCT 在 K-12 数学上做的; 人文/职业技能证据薄弱
- **Bloom 2-sigma 可推广性存疑**: 原始实验样本小 (约 30 人, 业内估), 方法论被质疑, 但已成领域信仰
- **中国 figures/sources 结构性弱**: 学术成果主要中文期刊 (搜索信号弱); 公众号/知乎是主讨论平台但在黑名单内
- **松鼠AI 宣称缺独立验证**: 「超纳米级知识图谱」等核心技术宣称无独立验证
- **一手率**: declared 约 84.6%; auto 约 46.4% (surrogate 域名不在 PRIMARY_DOMAIN_SUFFIXES)
- **voice_confidence**: medium (学术 register 为主, 非逐字口语; 中国 figures voice 薄)
- **本 skill 不替代**: 教育学/心理测量学/ML 专业训练; 法规内容仅导航非法律咨询
- **EN 约 75% / zh-CN 约 20%**: 反映领域学术文献实际分布

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-25 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-25 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-25 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-25 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-25 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-25 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-25 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-25 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-25 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
