---
name: vc-investor-master
description: |
  风险投资人 / 早期投资判断(GP + Principal — Deal sourcing / 尽调 / 估值与 term sheet / 投后服务 / 退出 + LP 关系与 fundraising — 涵盖 US 美元基金 + 国内 RMB / 美元基金) (Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战) Master OS — automated mastery of Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战 problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「VC」「venture capital」「风险投资」「early stage」「天使投资」
triggers:
  - "VC"
  - "venture capital"
  - "风险投资"
  - "early stage"
  - "天使投资"
  - "种子轮"
  - "A 轮"
  - "Series A"
  - "Series B"
  - "GP"
  - "general partner"
  - "LP"
  - "limited partner"
  - "fund of funds"
  - "deal sourcing"
  - "diligence"
  - "尽调"
  - "term sheet"
  - "SAFE"
  - "convertible note"
  - "estimated valuation"
  - "估值"
  - "投后"
  - "board service"
  - "IPO 退出"
  - "M&A 退出"
  - "secondary sale"
  - "carry"
  - "management fee"
  - "DPI"
  - "TVPI"
  - "fund returns"
  - "power law"
  - "anti-portfolio"
  - "founder market fit"
  - "TAM"
  - "go-to-market"
  - "PMF"
  - "investor thesis"
  - "投资逻辑"
  - "RMB 基金"
  - "美元基金"
  - "fundraising"
  - "IT 桔子"
  - "Crunchbase"
  - "PitchBook"
industry: "Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战"
industry-cn: "风险投资人 / 早期投资判断(GP + Principal — Deal sourcing / 尽调 / 估值与 term sheet / 投后服务 / 退出 + LP 关系与 fundraising — 涵盖 US 美元基金 + 国内 RMB / 美元基金)"
locale: "global"
last_research_date: "2026-05-14"
source_count: 146
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 风险投资人 / 早期投资判断(GP + Principal — Deal sourcing / 尽调 / 估值与 term sheet / 投后服务 / 退出 + LP 关系与 fundraising — 涵盖 US 美元基金 + 国内 RMB / 美元基金) · Master OS

> This skill makes the agent operate as a senior Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战 practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战 相关的问题时（关键词：VC, venture capital, 风险投资, early stage, 天使投资, 种子轮, A 轮, Series A, Series B, GP, general partner, LP, limited partner, fund of funds, deal sourcing, diligence, 尽调, term sheet, SAFE, convertible note, estimated valuation, 估值, 投后, board service, IPO 退出, M&A 退出, secondary sale, carry, management fee, DPI, TVPI, fund returns, power law, anti-portfolio, founder market fit, TAM, go-to-market, PMF, investor thesis, 投资逻辑, RMB 基金, 美元基金, fundraising, IT 桔子, Crunchbase, PitchBook），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：Venture capital / early-stage investor — 风险投资人(GP / Partner / Principal)的早期投资判断与基金运营实战 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: power-law 适配度评估（推导自心智模型 1.1）
- 看什么: 这个 deal / 这家公司有没有可能单独 return the fund——市场是不是 winner-take-most 型、有没有 outlier 的上行空间，以及「错过它」的 false-negative 成本有多大。不是「会不会亏」，是「能不能赚到 50-100x」。
- 在哪看: 公司所在赛道近 N 年的退出倍数与头部集中度（PitchBook / CB Insights）；同赛道是否出过 fund-returner 级别的 outlier；对照 Bessemer anti-portfolio 式的「错过名单」逻辑判 false-negative 成本。
- 输出: 「该 deal 的 power-law 适配度 = {能 / 不能成为 fund-returner，理由 1 句}；false-negative 成本 = {高 / 中 / 低}；结论：{值得为它投入贵资源 / 只配快速 pattern match}。」

#### 维度 2: founder & founder-market fit 核查（推导自心智模型 1.3）
- 看什么: 创始人与所做市场的匹配度——为什么是这个人做这件事（领域洞察、网络、执着），co-founder 关系稳不稳、过往逆境怎么处理；不是看名校 / 大厂背景。
- 在哪看: off-list 独立 reference call（绕开创始人给的 friendly reference，从自己网络找前同事 / 前投资人 / 客户）；创始人的领域 insight 是否在公开访谈 / 产品里可验证；Gompers 问卷确认「team 是 VC 决策首要因素」作锚。
- 输出: 「founder-market fit = {强 / 一般 / 弱，1 句理由}；off-list reference 信号 = {正面 / 有红旗：具体哪项}；co-founder / 团队风险 = {有 / 无}。」

#### 维度 3: 市场 / 赛道 / why-now 判定（推导自心智模型 1.2）
- 看什么: 市场天花板能不能容下一个 return-the-fund 的 outlier（独立核 TAM，自下而上 + 自上而下）；以及「why now」——这个市场的窗口为什么是现在。
- 在哪看: 自己独立算 TAM（不接受 pitch 给的数字）；赛道近 N 年融资金额 / 活跃投资人 / 成熟度（PitchBook / CB Insights / 国内 IT 桔子 / 烯牛）；行业老兵的 expert call 校准（成长期 deal）。
- 输出: 「市场天花板 = {能 / 不能装下一个 fund-returner，TAM 独立估算值}；why-now = {成立 / 不成立，1 句}；market-vs-team 取舍提示 = {若市场一般但团队极强，按你所属流派给倾向}。」

#### 维度 4: deal 条款与单位经济学体检（推导自心智模型 1.4）
- 看什么: 估值是 pre 还是 post、option pool 算在哪侧（定创始人实际稀释）；liquidation preference 结构（participating / 2x+ 是隐性税）；traction 是「健康增长」还是「烧钱买的增长」（unit economics：LTV/CAC、毛利、回收期）。
- 在哪看: term sheet 原文逐条款核（对照 Feld《Venture Deals》的 economics / control 两分法、NVCA 模板的市场标准）；公司真实使用 / 留存 / 收入数据 + cap table review（Carta）；可比交易的轮次结构与 preference（PitchBook）。
- 输出: 「估值口径 = {pre/post + option pool 在哪侧}；条款体检 = {标准 / 有隐性税：具体哪条}；unit economics = {健康 / 烧钱买的，关键数字}；结论：{高估值+好条款 / 高估值+差条款不是好 deal}。」

#### 维度 5: portfolio construction & fund-math 定位（推导自心智模型 1.7 + 1.1）
- 看什么: 这一笔在基金组合里占哪个格——ownership target 够不够（power-law 要求每个 deal ownership 足够高）、reserve 留够没有（业内估计常见 40-60%）、check size 与组合宽度是否匹配；以及这支基金的 fund size / lifecycle 阶段对这笔投资的约束。
- 在哪看: 基金自己的 portfolio construction 模型（fund size → check size → 项目数 → ownership → reserve，Notion / Coda 自建 + Carta fund admin 跟踪实际 vs 计划）；可比 deal 的 check size / ownership 行情（PitchBook）；对照 Neumann 的 portfolio math 框架。
- 输出: 「该 deal 在组合里 = {占哪个格、ownership target 是否达标、reserve 是否留够}；fund-math 约束 = {基金当前 lifecycle 阶段对这笔的限制}；结论：{check size + reserve 留法建议}。」

#### 维度 6: 周期 & vintage 语境判定（推导自心智模型 1.5）
- 看什么: 当前处于资本周期的哪一段——是估值高点、寒冬、还是局部反弹；这决定「该快还是该慢」「该不该在这个时点 all-in」「条款行情松还是紧」。2025-2026 是「AI / 热门赛道竞速 + 其他赛道仍寒冬」的两极分化。
- 在哪看: PitchBook 季度 Venture Monitor、近期 IPO / M&A 窗口状态、LP 募资环境（All-In 宏观 + 国内投中 / 投资界）；近期 down round / 结构性条款的出现频率；对照 Gurley《On the Road to Recap》式的周期判断。
- 输出: 「当前周期 = {高点 / 寒冬 / 局部反弹，按赛道分}；对该 deal / 该基金的含义 = {该快 / 该慢、条款行情松紧}；vintage 提示 = {评判基金回报须用 vintage 同期 benchmark}。」

#### 维度 7: locale & 监管语境判定（推导自智识谱系 §7.4）
- 看什么: 这是海外美元 / 国内 RMB / 国内美元哪条路径——locale 决定整套工具栈、deal 结构（国内有对赌 / 回购）、退出环境、监管底座；若涉及国内，自动触发监管语境核查。
- 在哪看: 基金 / deal 的资金来源与注册地；若海外，查 SEC accredited investor / Reg D / QSBS（§1202）/ ILPA / NVCA 标准；若国内，查《私募投资基金监督管理条例》+ 中基协登记备案 + 回购诉讼相关司法口径 + 引导基金返投诉求。
- 输出: 「locale = {US 美元 / 国内 RMB / 国内美元}；适用工具栈 = {海外 Carta+PitchBook+Affinity / 国内 IT 桔子+烯牛+微信+本地 fund admin}；监管风险点 = {1-3 条 + 须前置的合规动作}。」

#### 维度 8: 方法论流派定位（推导自智识谱系 §7.1 + 心智模型 1.7）
- 看什么: 这个投资人 / 这个判断属于或想走哪一派（thesis-driven / concentrated / spray-and-pray / 平台化大基金 / solo GP）——同一个早期 deal，不同派给完全相反的「该不该投、投多少、投后管多深」答案。
- 在哪看: 对方的 thesis 清晰度、check size / 项目数 / ownership target / 是否拿 board 的取向（这是流派之争最硬的可观测落点）；对照 §7.1 五派代表（Fred Wilson/a16z = A，Gurley/Benchmark = B，PG/YC = C，a16z = D，Elad Gil = E）的路径特征。
- 输出: 「该投资人 / 判断属于流派 {A/B/C/D/E 或混合}；因此对『该集中还是该分散 / 该不该深尽调 / 该不该做平台』的倾向 = {按该派逻辑给答案}；提示：换一派会给相反建议。」

#### 维度 9: 公开信号可信度核查（推导自诚实边界 §8.3）
- 看什么: 遇到的「VC playbook / GP 公开发言 / 收入 / 业绩数字」——是 fund math 驱动的真实工作还是给 LP 看的市场推广 / 个人品牌；收入 / fund return 数字的口径（自报 / 概数 / 业内估 / 不公开）、分布（头部 vs 中位）、样本（含不含失败者）。
- 在哪看: 数字 / 说法的原始出处（本人发言 vs 第三方）；对照 intake warning「个人 brand ≠ 投资能力」「公开数据是冰山一角」；Kaplan & Lerner 的 VC 数据偏差论文作方法论锚；优先采用「figure 谈具体判断标准 / 具体陷阱」的样本而非「谈宏大叙事」的样本。
- 输出: 「该公开信号性质 = {真实工作 / 个人品牌营销}；收入 / 业绩数字口径 = {自报 / 第三方 / 业内估 / 不公开}，可信度 {打几折}；结论：{可参考 / 须大幅打折 / 不可作复制依据}，原因 1 句。」

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

> 7 个，均通过三重验证（跨场景复现 / 生成力 / 排他性）。候选 C4「thesis 演化」、C5「投后即产品」、C9「长期主义复利」、C13「便宜实验买信息」未达 ✅✅✅ 或与既有模型重叠，降级到 §2 playbook / §7 谱系。每个心智模型的 `**figures:**` 行多人融合，`**evidence**` 跨 ≥ 2 source、尽量跨 track。

### 1.1 Power-law 是世界观，不是事后观察到的结果 — 错过比投错致命

- **一句话**：VC 的整门生意建立在「一支基金 80%+（业内估计，幂律分布的概数）回报来自 1-2 个 outlier、其余多数 deal 回本或归零」之上；因此判断一个 deal 的第一性问题不是「它稳不稳 / 会不会亏」，而是「它有没有可能单独 return the fund」——「最多亏 1x，可能赚 50-100x」，所以 false negative（错过 outlier）比 false positive（投错一笔）代价大得多。
- **figures:** Vinod Khosla / Bill Gurley / Sebastian Mallaby / Jerry Neumann — Khosla「风投有意思的地方在于你最多只会亏一倍钱……如果你能赚 50 倍、只亏 1 倍，这是笔相当好的交易」，且主张「不介意单个项目失败概率更大，只要每只基金里有足够分散」；Mallaby 的 VC 行业史书名直接叫《The Power Law》，把它从「观察到的收益分布」升格为「主动的投资世界观」；Neumann 的 portfolio math 长文把它学术化；Bessemer 把「看过却拒投后来大成」做成公开的 anti-portfolio 页，正是「错过比投错致命」的行业自觉。
- **evidence**: [T01-S016, T04-S004, T04-S010, T06-S001]
- **应用方式**（when to invoke）：面对任何「这个 deal 值不值得投 / 该不该深尽调」，第一刀永远是「它能不能成为 fund-returner」——答案是否，再稳健的生意、再漂亮的 unit economics 都次要；面对「我看过的好项目不少为什么基金回报不行」，先查 portfolio 里有没有一个真正的 fund-returner，而不是算平均命中率。它也是一切反直觉行为（容忍 90% 失败〔业内估计的概数〕、集中加倍、刻意复盘 false negative）的根。
- **局限**：① 「过度分散」和「集中加倍」是 power-law 的一体两面，只记住「广撒网容忍失败」而漏掉「在 winner 上重注 ownership」是对它最常见的误用（见 §7 concentrated vs spray 之争——两派都信 power-law 却推出相反打法）；② power-law 在「能产生 winner-take-most 结果的赛道」（早期科技 / 平台 / AI）特别成立，对低天花板、稳健现金流型生意不成立——但那类生意本就不是 VC 的标的。

### 1.2 市场 / 赛道决定论 — 但「市场 vs 团队谁第一」是本行未决的派系张力

- **一句话**：这一行有一条强力镜片——「好团队遇上烂市场，市场赢；烂团队遇上好市场，市场赢」，市场天花板能不能容下一个 return-the-fund 的 outlier 是早期判断的硬约束；但与之并存的是另一极——多数 VC 在问卷里把 team 排在 market 之上，这条「市场 vs 团队」的排序分歧本身就是必须捕捉的行业张力，而不是可以抹平的。
- **figures:** Marc Andreessen / 张磊 / 朱啸虎 / Paul Gompers 等（学术问卷）— Andreessen《The Only Thing That Matters》是「market wins」一派的总纲；张磊「与伟大格局观者同行」、朱啸虎「壁垒在 AI 之外、看赛道商业化」都是赛道/市场优先的变体；但 Gompers/Strebulaev 对 ~900 家 VC 的问卷实证显示多数 VC 自陈 team 权重最高——同一行业内的两份「权威」给出相反排序。
- **evidence**: [T01-S004, T01-S020, T01-S025, T04-S012]
- **应用方式**：面对一个 deal，强制独立核 TAM（自下而上 + 自上而下各算一遍），先验证「市场大到能容下一个 outlier 吗」——这是 market 派的硬动作；同时要清楚自己/对方站在哪一极（market-first 还是 team-first），因为它直接决定「市场一般但团队极强的 deal 投不投」这类问题的答案。面对新赛道（如某个 AI 应用方向），先问「why now / 这个市场的窗口为什么是现在」。
- **局限**：① 这是「行业放大版」心智模型——「关注市场」本身是通用商业道理，VC 的特化在于把它推到「市场天花板必须能装下一个 fund-returner」这个 power-law 约束下的极端版本；脱离 power-law 谈「市场重要」就退化成八股；② market 派与 team 派的排序之争至今无行业共识（见 §7、§8），任何「市场一定比团队重要」的断言都是站队，不是事实。

### 1.3 早期投资本质是投人 — founder-market fit 是信息最稀薄阶段的最强信号

- **一句话**：种子 / 早期阶段数据太薄、产品常是半成品，可核查的「硬证据」极少，所以判断收敛到「人」——不是看名校 / 大厂背景，而是看 founder-market fit（「为什么是这个人做这件事」：领域洞察、网络、近乎偏执的执着），以及 co-founder 关系稳不稳、逆境时怎么处理。
- **figures:** Ben Horowitz / Paul Graham / 张磊 / Reid Hoffman — Horowitz 把 a16z 的「founder-CEO 优先」制度化，主张陪跑「没有标准答案的艰难时刻」而非换职业经理人；PG「找点子的动词不是『想出来』而是『注意到』」，强调创始人要在「未来」里浸泡到能注意到别人看不见的缺口；张磊「与伟大格局观者同行」押的是 founder 的格局而非短期数字；Gompers 问卷实证 team 是 VC 决策首要因素。
- **evidence**: [T01-S018, T01-S003, T01-S020, T04-S012]
- **应用方式**：尽调一个早期 deal，把 founder reference call 当不可跳过的核心动作——而且要绕开创始人给的「友好 reference」，从自己网络里找 off-list 独立信源交叉验证（这是区分新手和老手最明显的尽调动作）；判断创始人时把问题从「简历好不好」换成「为什么是这个人做这件事、他对这个领域的 insight 别人有没有」。
- **局限**：① 「投人」在种子 / 早期阶段成立，到成长期 / 大额 check 信息变厚，judgment 的重心会向 unit economics、market、竞争格局迁移——把「早期投人」的轻尽调模板套到后期是错配；② founder-CEO 优先被批评是 a16z 抢 deal 的营销话术——当 founder 利益与基金利益冲突时（该不该卖公司），「friendly」会让位（见 §8 VC 与创始人利益不对齐）；③ pattern matching 判断「这个人像不像成功创始人」是双刃剑，行业内部对它「固化偏见、错过 non-obvious founder」有持续反思。

### 1.4 估值与条款的单位经济学纪律 — 高估值 + 差条款不是好 deal

- **一句话**：VC 用估值和条款两种语言判断一个 deal，而这一行的纪律是「不被单一漂亮数字带走」——同样的营收，留存 / 毛利 / 获客成本结构天差地别（「不是所有收入生而平等」）；同样的高估值，配上 participating preferred / 2x liquidation preference / option pool 算在 pre 侧，实际是把回报和稀释悄悄吃掉的隐性税。
- **figures:** Bill Gurley / 朱啸虎 / Tomasz Tunguz / Brad Feld — Gurley《All Revenue Is Not Created Equal》《The Dangerous Seduction of the LTV Formula》——LTV 公式「让你用漂亮终值掩盖获客越来越贵、留存越来越差的真相」；朱啸虎「创业本质是做生意，要算账——看付费意愿、销售周期、留存率」；Tunguz 把 SaaS unit economics 做成公开教材；Feld《Venture Deals》逐条款拆解「economics（钱怎么分）vs control（决策权归谁）」，1x non-participating 是市场标准、任何超出都是隐性税。
- **evidence**: [T01-S002, T01-S025, T04-S001, T04-S021]
- **应用方式**：看 traction，区分「健康增长」和「补贴 / 烧钱买的增长」，算 unit economics（LTV/CAC、毛利、回收期）而非只看增速；看 term sheet，先确认估值是 pre 还是 post、option pool 算在哪侧（这一步定创始人实际稀释），再查 liquidation preference 结构——看到 participating / 2x+ 立刻警觉；判断一个「高估值 offer」时，把估值和条款合起来看，而不是只比估值数字。
- **局限**：① 种子 / 早期阶段数据太薄，深抠 unit economics 是另一种错——资深人在种子期把尽调收敛到「人 + 市场天花板 + 一个核心假设」，重量化留给成长期；② 条款的「市场行情」随周期波动（2021 高点条款极松、2022-2024 寒冬 participating / 结构化轮次回潮），「什么算非标」本身是动的，不是绝对值。

### 1.5 周期与 vintage 意识 — VC 行为必须放进资本周期里读

- **一句话**：VC 是强周期生意——同一个 deal、同一套打法，在 2021 估值高点和 2022-2024 寒冬里是完全不同的决策；基金回报高度受 vintage year（开始投资的年份）影响，「速度优先于效率」（blitzscaling）在扩张期是对的、在下行期要改成「精准判断哪里仍值得用速度换位置」，估值纪律的核心就是不在单一高点把基金打光。
- **figures:** Reid Hoffman / Bill Gurley / 朱啸虎 / Ramana Nanda 等（学术）— Hoffman 的 blitzscaling 是扩张期总纲，又专门写《Bear Market Blitzscaling》回应下行期「哪些地方仍值得用速度换位置」；Gurley《On the Road to Recap》论 2015-16 估值泡沫、反复警告高估值是慢性毒药；朱啸虎「商业路径不清就批量退出（人形机器人）」是周期性减仓的公开样本；Nanda「Investment Cycles and Startup Innovation」把「热钱周期如何改变被投公司画像」学术化。
- **evidence**: [T01-S028, T01-S002, T01-S021, T04-S013]
- **应用方式**：判断「现在该快还是该慢」前，先定位当前周期——2025-2026 是「AI / 少数热门赛道竞速 + 其他赛道仍寒冬」的两极分化状态（写时间戳）；部署基金时刻意把 investment period 摊到多个年份 / 多个市场环境（vintage diversification），别因 FOMO 在单一高点 all-in；评判一支基金的回报，先看它的 vintage 同期 benchmark，而不是跨 vintage 比。
- **局限**：① 周期判断容易事后正确、事前两难——「狼来了」风险真实存在（Gurley 2015 年后多次泡沫预警但市场又涨了数年）；② 「速度 vs 效率」的钟摆本身在 2022-2024 被广泛反思——blitzscaling 被指助长烧钱不计回报（WeWork 成反例），这条镜片要和「单位经济学纪律」（1.4）一起用，不能单独奉行。

### 1.6 VC 是「基金管理人」，GP 自己也受 LP 约束 — 想预测 VC 行为，先看它的 fund math

- **一句话**：VC 不是「拿自己的钱投项目的人」，是 LP 把钱托付给 GP 的两层受托结构——GP 的日常工资来自 management fee（约 2%/年 × 基金规模），真正的上行收入 carry（标准 20% 利润分成）要等基金 7-10+ 年生命周期后才兑现；所以要预测一个 GP / 一家基金为什么那样行动（为什么追规模、为什么催 outlier exit、为什么寒冬里盯 DPI），先看它的 fund size、lifecycle 阶段、carry 经济学和 LP 结构。
- **figures:** Scott Kupor / Steven Kaplan & Antoinette Schoar / Doug Leone — Kupor《Secrets of Sand Hill Road》从 a16z 内部系统讲 GP-LP 双层结构、J-curve、carry vesting；Kaplan & Schoar 的 persistence 实证显示「头部 GP 业绩有持续性、但资本流入会侵蚀未来回报」，解释了 GP-LP 市场的马太效应；Doug Leone 的 stewardship 观（「卖掉 Sequoia 一部分意味着留给下一代分的饼更小」）正是「GP 行为被 fund / 机构的长期结构约束」的极端自觉。
- **evidence**: [T04-S003, T04-S018, T01-S007]
- **应用方式**：读任何「VC playbook / GP 公开发言」时，先问「这是 fund math 驱动的真实工作，还是给 LP 看的市场推广」；评判一个 GP（或自评），寒冬里看 DPI（真金白银退回多少）不看 TVPI（含未退出账面）——「账面价值不是钱」；想理解「为什么大基金催你卖公司、小基金陪你长跑」，看的是 carry 经济学和基金剩余生命周期，不是 GP 个人善恶。
- **局限**：① 这条解释力强但不浪漫——它会把「投资判断」还原成「激励结构」，但 fund math 是必要条件不是充分条件，真正的 alpha 仍在判断力；② solo GP / 微型基金模糊了 GP-LP 边界，但「受托管理别人的钱 + carry 周期极长」这个结构本身不变。

### 1.7 VC 的资深 = 知道在哪里不必用力，以及把单个 deal 绑回组合

- **一句话**：早期投资的信息本就稀薄，资深投资人的判断力不体现在「把所有步骤做全」，而体现在两件事——(a)知道在低信号 / 低 ROI 处省力（冷 inbound 不精读、强引荐 deal 跳过分阶段尽调、种子期跳过重量化尽调、标准 deal 跳过逐条款谈判、对明确 loser 快速降投入）；(b)不孤立评估任何单个 deal——它的价值由它在 power-law 组合里的位置（ownership 够不够、reserve 留多少、与 thesis 的关系）决定，而非它自身好不好。
- **figures:** （多人融合，来自 Track 03 对 W1-W8 资深路径的横切）— Fred Wilson 在 AVC.com 写资深 GP 把 partner meeting「从逐个念清单优化成只讨论真有分歧的 deal」、固定留「无议程」时间做 thesis 思考；Brad Feld《Venture Deals》主张标准化早期 deal 直接用 NVCA / YC SAFE 模板把谈判收敛到两个数；Jerry Neumann 的 portfolio construction math 是「每个 deal 都要回组合对一遍」的经典文本；Bill Gurley 的 concentrated 打法本身就是「在低信号处不投、把火力集中到高 conviction」的极端制度化。
- **evidence**: [T03-S001, T03-S005, T04-S001, T04-S010]
- **应用方式**：面对「这个 deal 我该做多重的尽调 / 多硬的谈判 / 多深的投后」，先判断它的信号强度和 ROI——强引荐 + thesis 命中 + 标准条款的早期 deal，资深做法是快、轻、收敛；冷 inbound、非标条款、明确 loser，资深做法是极快 pass 或快速降投入；做任何单个 deal 决策（出 term sheet / follow-on / 加注）前，强制回 portfolio construction 对一遍。新手「平均用力填 checklist」，资深「找致命伤 + 对组合」。
- **局限**：① 「知道在哪里可以省」是经验的产物，新人没有这个判断力时，跳步是高风险捷径而非智慧——「强引荐 deal 跳过尽调」只在「自己 thesis 极深 + 引荐源极可信」时成立，错用会直接踩雷；② 这条心智模型的排他性偏「行业放大版」——「抓重点、系统视角」是通用能力，VC 的特化在于「早期信息稀薄 + power-law 组合约束」让「在哪里省力」「单 deal 绑回组合」有了这一行特定的判据。



## 标准 Playbook

> 行业快速决策规则。每条 = `**如果 X**，则 Y` + 案例 + evidence，跨 figures / workflows / canon / glossary 多轨。10 条。

1. **如果在评估一个 deal 该不该投或该不该深尽调**，则第一刀永远先问「它有没有可能单独 return the fund」——答案是否，再稳健的生意、再漂亮的 unit economics 都次要；尽调危机期公司同理，不看银行余额，看「增长曲线能否在 runway 用完前转正」（default alive）。
   - **案例**：canon 把 power-law 列为「VC 一切反直觉行为的根」，对应判据「这个公司有没有可能单独 return the fund」；Khosla「最多亏 1x、可能赚 50x」；PG「Black Swan Farming」论 false negative 成本。
   - **evidence**：[T04-S004, T01-S016, T04-S007]

2. **如果一个 deal 是冷 inbound 或不在自己 thesis 命中区**，则用极快的 pattern match（30 秒 deck / 一段话邮件）直接处理，把 first meeting、深尽调这类最贵的资源只留给网络内强引荐 + thesis 命中项。
   - **案例**：NFX 数据「70%+ top deal 来自既有网络」；W1/W2/W4/W5 的资深 skip 全是这个模式——资深 GP 跳过对绝大多数 inbound 的「正式 first meeting」；冷 inbound 命中率极低，first meeting 是最贵的资源。
   - **evidence**：[T03-S004, T03-S018]

3. **如果在做任何单个 deal 的决策（尽调 / 出 term sheet / follow-on / 加注）**，则先回 portfolio construction 对一遍——这一笔在组合里占哪个格、ownership 够不够、reserve 留多少——而不是孤立看这个 deal 自身好不好。
   - **案例**：W2/W6/W8 的资深 add 全是「把单个 deal 绑回 portfolio construction」；Neumann 的 portfolio math 把它学术化；新手「孤立看单个 deal」是 03 失败模式 7。
   - **evidence**：[T03-S005, T04-S010, T03-S011]

4. **如果某资源是关系型的（deal flow / LP / 投后帮扶网络）**，则定期、主动、提前经营它，把它当复利资产养，别等需要时才找；并在 close / 启动后立刻约定固定的信息更新节奏，把「信息失明」当头号风险防。
   - **案例**：W1 每周固定见「不是为了投」的人；W3 资深 GP 募新基金先找老 LP re-up（老 LP 的钱最便宜）、从第 1 年起经营 LP；W4 scout network；W7「投后失明——公司出事最后一个知道」是 03 失败模式 3。
   - **evidence**：[T03-S004, T03-S001, T03-S015]

5. **如果在分配尽调时间 / 投后精力 / reserve 资金**，则按 power-law 给它们分级——winner 和「还能救」的公司优先，对明确的 loser 快速降投入甚至主动 write-off，拒绝平均用力。
   - **案例**：W5 资深尽调「找致命伤而非填 checklist」；W7 资深「投后精力集中到 winner，对明确失败的快速降投入」；W8 reserve 加倍到 winner；power-law 下 winner 的边际帮助远比救 loser 值钱。
   - **evidence**：[T03-S016, T03-S011, T04-S004]

6. **如果看到一个高估值的 offer**，则先确认估值是 pre 还是 post、option pool 算在哪侧（这一步定创始人实际稀释），再查 liquidation preference 结构——participating / 2x+ multiple 是把回报悄悄吃掉的隐性税，高估值 + 差条款不是好 deal。
   - **案例**：canon「1x non-participating 是市场标准，任何超出都是隐性税」；Gurley 反复警告高估值 + 结构化条款的危险；W6 失败模式「只谈估值数字、忽略 option pool 在哪侧」「接受非标 liquidation preference 而不自知」。
   - **evidence**：[T04-S001, T04-S005, T03-S002]

7. **如果在建一支新基金的组合**，则先留够 reserve（行业常见 40-60%）再投初始 check——首轮把基金投满、winner 起飞却无钱 follow-on，是新基金最常见的结构性错误；reserve 是活的，要随 winner / loser 浮现持续重算。
   - **案例**：W3/W8 都把「reserve 不够、winner 接不住」列为「新基金第一大结构性错误」；Fred Wilson 在 AVC.com 反复写 reserve / follow-on 的重要性；资深 GP 把静态 reserve 比例优化成动态 reserve 管理。
   - **evidence**：[T03-S011, T04-S005, T03-S005]

8. **如果在谈一个标准化的早期 deal 的 term sheet**，则直接用市场标准的 SAFE / NVCA 模板，把谈判收敛到「估值 + 投资额」两个数——逐条款都想赢是 negative-sum，会输掉 7-10 年的关系；真正要守住的只有估值合理性、pro-rata、董事会。
   - **案例**：W6 资深 skip「对标准化早期 deal 几乎跳过逐条款谈判，用 YC SAFE / NVCA 模板」；Feld《Venture Deals》是逐条款圣经但也主张早期别在标准条款上较劲；「term sheet 是 7-10 年关系的第一次握手」。
   - **evidence**：[T03-S003, T03-S013, T04-S001]

9. **如果遇到任何 VC 问题（工具 / 流程 / 退出 / 监管）**，则先问 locale——海外美元 / 国内 RMB / 国内美元是三条几乎不互通的路径：两套生态、两套工具栈、两套监管、两套退出环境、甚至两套 deal 结构（国内有对赌 / 回购这种海外没有的类债化条款）。
   - **案例**：Track 02 选型决策树的根节点就是 locale，海外工具（PitchBook / Carta / Affinity）与国内套件（IT 桔子 / 烯牛 / 鲸准）几乎不互通；W2/W5/W7 国内路径多了「回购条款 + 创始人个人连带风险评估」环节；glossary outsider-tell #9「把『中国 VC』当一个整体谈」。
   - **evidence**：[T02-S001, T02-S014, T03-S014]

10. **如果遇到「该走什么模式 / 该集中还是该分散 / 该不该做平台」这类方法论问题，或遇到「XX 月入 N 万、7 步进 VC」这类成功叙事**，则先问对方属于或想走哪一派（thesis-driven / spray-and-pray / concentrated / solo GP / 国内多元化），并对收入 / 业绩数字追问分布、样本、口径——同一问题不同派给完全相反的答案，且公开 brand ≠ 投资能力、公开数据是冰山一角。
    - **案例**：04 列出 team-vs-market、集中-vs-广撒、要不要做平台三大未决分歧；同一个「该不该开付费墙式的集中下注」，Gurley / Benchmark 与 PG / YC 给相反建议；intake warning 2/6/7「个人 brand 优秀 ≠ 投资能力」「GP fund returns 多不公开」；All-In 群体是「公开多 ≠ 投得好」的活样本。
    - **evidence**：[T04-S012, T01-S002, T01-S017]



## 工具栈与选型决策树

> 直接消化 Track 02。一致性 sanity-check：必备层 4 个（≥ 3 ✅）、场景特化层 6 个（≥ 5 ✅）、新兴层 3 个（≥ 2 ✅）、选型决策树 9 节点（5-10 区间 ✅）、避坑清单 9 条（≥ 5 ✅）。**GitHub stars 阈值不适用**——VC 工具栈几乎全是 SaaS / 闭源平台，Track 02 改用「≥ 3 个独立 source 点名 + 行业 default 共识」作必备层判据。

### 3.1 三层结构

- **必备层（4 个，≥ 80% 从业者用，渗透率为业内估计）**：Carta（cap table / 409A 估值 / fund admin，2025 北美早期股权基础设施事实标准，decay low）、PitchBook（私募市场 deal / 估值 / LP 全量数据库，机构 default，高价机构订阅，decay low）、Crunchbase（轻量 startup / funding 数据库，sourcing 的低成本起点，freemium，decay low）、Affinity（relationship intelligence CRM，自动从邮箱 / 日历抓关系网络，VC 关系驱动工作的 CRM default，decay medium——Affinity vs Attio 王座之争未定）。
- **场景特化层（6 个）**：AngelList SPV / RUV / fund admin（把「成立一次性投资载体 / syndicate / 小基金」从几周律师流程压到几天，SV solo GP / scout default）、CB Insights（market intel + 预测，thesis / 赛道地图研究，与 PitchBook 高度重叠）、AlphaSense（含 Tegus）/ GLG（expert call network，深尽调买专家访谈的标准渠道）、DocSend（deck 分发 + 逐页阅读分析，inbound 信号 + LP 材料追踪）、Notion / Coda（投资 memo + portfolio tracking 的低成本自建内部系统）、国内套件 IT 桔子 / 36 氪 / 鲸准 / 烯牛数据 / FellowPlus（RMB / 国内美元基金的 deal 数据 + 行业情报 default，海外工具在国内 deal 几乎不可用，decay high）。
- **新兴层（3 个，近 12-24 个月起势）**：Attio（API-first 可定制 CRM，Affinity 的现代挑战者）、AI sourcing 层（Glasswing EVE / 各大基金自研如 Sequoia Arc 类，LLM 辅助 sourcing + 信号打分，2024-2025 起势但整层 `stability: experimental`、工具碎片化无 default）、Eqtble（people analytics 进尽调与投后健康监控，VC 场景渗透早期）。三者 decay risk 全 high。**关键盲区**：头部基金（Sequoia / a16z）的内部 AI / sourcing 工具闭源不可验证，新兴层真实成熟度可能被低估（见 §8）。

### 3.2 选型决策树（9 节点）

- **根节点 = locale**（海外 vs 国内，两套生态几乎不互通，一票否决式分叉）。
- **海外分支** → 第二层是 **fund structure**：
  - **solo GP / scout / syndicate lead**（还没机构基金结构）→ 数据 / sourcing 用 Crunchbase 免费档起步 + DocSend 看 inbound deck 信号；载体 / 行政用 AngelList SPV / RUV（别自建 fund admin）；CRM 用 Attio 或 Notion 自建（别上 Affinity）。**不推荐**：PitchBook（年费数万美元 / 席位，solo 体量不划算）、Carta fund admin（规模没到）。
  - **机构基金的 GP / Partner / Principal / Associate** → 第三层是 **bottleneck**：① 瓶颈在 deal flow / 关系网络 → Affinity（VC CRM 事实标准）+ PitchBook + Crunchbase + AI sourcing 层（实验性叠加）；② 瓶颈在深度尽调（成长期 / 大额 check）→ AlphaSense（含 Tegus）/ GLG 买专家访谈 + CB Insights 做赛道地图，**不推荐**种子 / 天使阶段花 expert network 的钱（单笔体量小不划算）；③ 瓶颈在基金运营 / 投后 / LP 报告 → Carta（cap table + fund admin）+ Notion / Coda 自建 memo + portfolio tracking + DocSend 发 LP update。
- **国内分支** → ① sourcing / 竞品 / 行业研究 → IT 桔子 / 烯牛 / 鲸准 + 36 氪信息流；② CRM / 基金运营 / LP-GP → 现实是微信 + 自建表格 + 国内 CRM，cap table / fund admin 走本地有限合伙 + 券商托管 / 本地 fund admin（Carta fund admin 在国内不适用），投资 memo 仍可用 Notion / Coda（通用工具不受 locale 限制）。
- **决策树关键变量**（供 Phase 3 抽 `cli/decision/*.sh`）：`locale`（一票否决式分叉）→ `fund_structure`（solo GP / scout vs 机构基金）→ `bottleneck`（deal flow / 尽调 / 运营，决定买哪类工具）→ `stage`（种子 vs 成长期，决定 expert network 等高单价工具是否划算）。

### 3.3 避坑清单（9 条，摘要）

不要在 solo GP / scout 阶段就买 PitchBook（年费数万美元，先用 Crunchbase）｜不要把 Carta 当 syndicate / 一次性 SPV 工具、也不要把 AngelList 当机构 cap table（不同生态位）｜不要用海外工具覆盖国内 deal（反之亦然，两套生态不互通）｜不要把工作流深度绑定单一国内创投数据供应商（随 RMB 周期 + 政策剧烈波动，FellowPlus 整合即先例，保留数据可迁移性）｜不要把 DocSend 当数据室（VDR）用｜不要在种子 / 早期天使阶段花 expert network（GLG / AlphaSense / Tegus）的钱（单笔体量小 ROI 不成立）｜不要把 AI sourcing 工具当投资决策的替代（只是初筛放大器，judgment 仍在人，且整层 experimental）｜不要急着为「投资 memo + portfolio tracking」采购专门软件（早期 Notion / Coda 自建足够）｜不要因为「Affinity 老牌」或「Attio 现代」就盲目选 / 盲目迁（CRM 迁移有真实数据 + 习惯成本，按可定制性 / 预算 / API 需求理性选）。

### 3.4 工具流派分裂（→ §7 智识谱系）

「采购专门 VC 软件」派（Carta + Affinity + PitchBook 专门栈）vs「通用工具自建内部 OS」派（Notion / Coda / Attio / Airtable 自建）——分界主要是基金规模 + 阶段 + 预算，不是「谁更对」；「数据深度」派（预算压在 PitchBook / CB Insights，sourcing 靠系统化扫描）vs「关系网络」派（预算压在 Affinity，sourcing 靠网络）；「人 judgment 为核心」派 vs「AI / 数据信号前置」派（Glasswing 等 AI-native 基金，2024-2025 才显性化、尚未收敛）。海外 vs 国内不是「流派」而是**生态隔离**，按 locale 分章处理。



## 工作流 / Pipeline

> 直接消化 Track 03 的 8 个 workflow，每个一个 `### W..` 子节。一致性 sanity-check：8 个 workflow **全部备齐 skip + optimize + add 三类、每类 ≥ 1 处**（合计每个 ≥ 3 处资深差异，缺失率 0%〔本文档机械自检口径，非业内数据〕，远超「≥ 2 类、≥ 2 instance」硬门槛）、全部有 Last_updated + 近期变化字段。VC 工作流要在三个时间尺度上画：W1=「一周」、W2=「一个 deal」、W3=「一个 fund 的 7-10 年生命周期」，W4-W8 是穿插其中的专项。decay：high 1（W4）/ medium 4（W1/W2/W5/W7）/ low 3（W3/W6/W8）→ §8 须警告 W4（deal sourcing）衰减最快。

### W1. 一个 GP / 投资人的一周（三尺度之「周」）

把一个早期 VC 的一周从「无序救火」变成「有节奏的并行流水线」——deal review / pitch 会 / partner meeting / board meeting / LP & founder 触达五条线同时滚动。入门 SOP 5 步：周一 partner meeting / deal review 准备 → partner meeting 本身（集体 go / no-go）→ 本周 pitch 会（见 3-8 个新公司）→ 进行中 deal 的尽调动作 → portfolio / board / LP 触达。

- **skip**：资深 GP 跳过对绝大多数 inbound deal 的「正式 first meeting」——用 30 秒 deck / 一段话邮件 + pattern match 直接 pass，只把 first meeting 留给网络内强引荐或 thesis 命中项。理由：冷 inbound 命中率极低，first meeting 是最贵的资源。(evidence: [T03-S004, T03-S018])
- **optimize**：把「周一准备 + partner meeting」优化成「持续在 CRM 里异步维护 + 会上只讨论真有分歧的 deal」——不逐个念 pipeline，partner meeting 从 3 小时压到 1 小时。(evidence: [T03-S012, T03-S018])
- **add**：额外做两件初学者忽略的事——(a)固定留「无议程」时间做 thesis 思考 / 写作 / 行业深挖（Fred Wilson 的 AVC.com 本身就是这种产物）；(b)每周固定见 N 个「不是为了投」的人（其他 GP、潜在 scout、portfolio 创始人的朋友），把网络当复利资产养。(evidence: [T03-S001, T03-S004])
- **近期变化**：2024-2025 寒冬 + DPI 压力下，一周里「portfolio triage / 危机处理 / 帮 portfolio 公司续命」时间占比上升，board meeting 议题从「how to grow faster」转向「default alive 还是 default dead」；2025 AI cycle 拐点起，AI 赛道 first meeting 密度回升且竞速窗口极短（< 1 周），但只在 AI / 少数热门赛道——「周一 partner meeting + 全周 pitch + 投后触达」骨架多年未变，变的是时间配比。
- **Last_updated**：2026-05-14（骨架稳态，时间配比近 12 个月有变）
- **Decay**：medium——骨架结构稳定，但「各段时间配比」随周期（寒冬 vs AI cycle）持续移动，12-24 个月会再变。

### W2. 一个 deal 从 inbound 到 close 的完整路径（三尺度之「一个 deal」）

把一家公司从「pipeline 里的一行」推到「钱打进对方账户、股权进 cap table」。入门 SOP 6 步：sourcing + 初筛（30 秒背景核查）→ first meeting（30-60 分钟见创始人，问 team/market/product/traction）→ 尽调 → 写投资 memo + IC / partner meeting 拿 go/no-go → 出 term sheet + 谈判 → 法律文件 + close。

- **skip**：资深投资人对网络内强引荐 + thesis 命中的 deal，跳过「正式分阶段尽调」里的若干步，靠 pattern recognition 在 1-2 次会内给 term sheet（尤其 2025 热门 AI deal 的竞速行情）。**注意**：这是高风险捷径，只在「自己 thesis 极深 + 引荐源极可信」时用。(evidence: [T03-S004, T03-S018])
- **optimize**：把「first meeting → 决定」优化成 first meeting 当场就走「软 term」——先口头给估值区间锁住创始人，再倒回去补尽调和 IC；把竞速顺序从「尽调完才报价」改成「先报价占位再尽调」。(evidence: [T03-S006, T03-S018])
- **add**：额外做两件——(a)绕开创始人给的「友好 reference」，自己从网络里找独立信源（off-list reference）做背调，这是最能区分新手与老手的尽调动作；(b)在出 term sheet 前先想清楚「这个 deal 在我的 portfolio construction 里占哪个格 / 留多少 reserve」（把 W2 和 W8 接起来）。(evidence: [T03-S005, T03-S011])
- **近期变化**：2025 AI cycle 起，头部 AI deal 的「inbound → term sheet」周期被压缩到几天甚至更短，寒冬赛道的 deal 反而走得更慢、尽调更重——同一行业内 deal 节奏两极分化是当前最显著变化；AI 辅助尽调起势（LLM 做 market sizing 初稿 / 竞品扫描 / deck 初筛打分，但 judgment 仍在人）；国内 deal 的 close 阶段近年多了「回购条款谈判 + 创始人个人连带风险评估」环节（2023-2024 回购诉讼潮触发），海外没有这一环。
- **Last_updated**：2026-05-14（骨架稳态，节奏 + AI 辅助 + 国内回购环节近 12 个月有变）
- **Decay**：medium——「sourcing → 尽调 → IC → term sheet → close」骨架是 VC 数十年核心流程不会消失，但每段耗时 + AI 辅助渗透 + 国内条款环节 12-24 个月会持续变。

### W3. 一个 fund 从 fundraising 到 exit 的 7-10 年生命周期（三尺度之「一个 fund」）

把一支基金走完整个 7-10+ 年生命：募资 → 部署期投出去 → 投后 + reserve 跟投 → 收获期退出 → 清算 + 给 LP 返钱（并以此业绩募下一支）。入门 SOP 6 步：fundraising（写 thesis + PPM，见各类 LP，谈 2%/20%/GP commitment（2%/20% 为业内惯例标准，非精确数据），first close → final close）→ portfolio construction 定盘 → 部署期 → 投后 + reserve / follow-on → 收获期 / 退出（IPO / M&A / secondary / write-off）→ 清算 + LP 报告 + 募下一支。

- **skip**：有 track record 的资深 GP 在募资上跳过「广撒网见上百个陌生 LP」——直接回头找上一支基金的老 LP re-up，加少量新 LP，募资周期从 12-18 个月压到几个月。理由：LP 关系是复利资产，老 LP 的钱比新 LP 便宜（尽调成本低、信任已建立）。新 GP 没有这个捷径。(evidence: [T03-S015, T03-S010])
- **optimize**：把「部署期」优化成更纪律化的节奏——不在某个估值高点（如 2021）把基金一次性打光，刻意把部署摊到多个年份 / 多个市场环境，用 vintage diversification 对冲周期。(evidence: [T03-S002])
- **add**：额外做两件——(a)从基金第 1 年就持续、主动地经营 LP 关系（定期 update、闭门会，让 LP 觉得「在场」），而不是等募下一支时才想起 LP；(b)主动管理 DPI 时点——收获期不被动等 IPO，而是用 secondary sale 主动制造流动性给 LP 返钱（尤其寒冬 IPO 窗口关闭时）。(evidence: [T03-S010, T03-S015])
- **近期变化**：2022-2024 寒冬 + 2025，IPO / M&A 窗口收紧 + LP 钱少，「收获期」被整体拉长，DPI 普遍偏低，LP 对 GP 的考核从 TVPI 转向 DPI，secondary sale 从「补充手段」上升为主流流动性工具；2025-2026 ILPA Reporting Template v2.0 进入采用期（费用 / carry 披露颗粒度提升）；国内 RMB 路径因 2023-09《私募投资基金监督管理条例》+ 中基协登记备案新办法，「新基金设立 / 管理人登记 / 产品备案」流程整体变重。
- **Last_updated**：2026-05-14（7-10 年骨架是行业稳态；退出周期拉长 + ILPA v2.0 + 国内法规是近 12-24 个月的变化）
- **Decay**：low——「募资 → 部署 → 投后 → 退出 → 清算」是基金结构本身决定的数十年稳态，变化的是各段时长与外部环境，不是骨架。

### W4. Deal sourcing — 建 proprietary deal flow

把「被动等 inbound deck」升级成「主动、有结构、有专属性的 deal flow 机器」——因为 70%+（业内估计的概数）的 top deal 来自既有网络，sourcing 决定一支基金的回报上限。入门 SOP 4 步：建多渠道入口（inbound + outbound + 引荐网络）→ 持续撒网见人 → 初筛 + pattern match → 录入 + 跟踪 + 复盘（标来源渠道，复盘哪个渠道命中率最高）。

- **skip**：资深 GP 跳过对冷 inbound 的精读——冷 inbound 命中率极低，用极快的 pattern match（或让 associate / AI 工具初筛）处理，把精力全押在引荐网络和 outbound thesis 扫描上。理由：proprietary deal 几乎不来自冷 inbound。(evidence: [T03-S004, T03-S018])
- **optimize**：把「持续见人」优化成「scout network / 杠杆化网络」——不靠自己一个人见所有人，而是建一张 scout 网（给早期信号源小额经济回报），让网络替自己 sourcing，把单点产能放大成网络产能。(evidence: [T03-S004])
- **add**：额外做——把 sourcing 和 thesis 绑死：先写出清晰 thesis（哪个赛道、为什么、什么样的公司），再把 thesis 转成可执行的 outbound 扫描规则，让 sourcing 从「广撒网」变成「在我最懂的地方比别人早看到」。初学者往往撒网但无 thesis，deal flow 大而不专。(evidence: [T03-S005, T03-S009])
- **近期变化**：2024-2025 AI cycle 拐点 + LLM 能力成熟，AI 辅助 sourcing 从概念走进部分基金的实际工作流（自动扫描 GitHub / 招聘 / 产品发布 / 新闻信号生成清单、对 inbound deck 初筛打分，代表 Glasswing EVE、各大基金自研工具）；但具体采用率数据未在调研中验证，Track 02 标注 AI sourcing 整层 `stability: experimental`、工具碎片化无 default，多数基金现实仍是 Crunchbase / PitchBook 筛选 + 人脉网络，AI sourcing 是叠加层而非替代。
- **Last_updated**：2026-05-14（「网络决定 deal flow」是稳态底层，AI 辅助 sourcing 是近 12 个月的活跃变量）
- **Decay**：high——「proprietary deal flow 靠网络」这个底层逻辑不变，但 sourcing 的**执行工具层**（AI sourcing）正在 12 个月级别快速重写，是 Track 03 里 decay 最快的 workflow。

### W5. Due diligence 深做（founder reference call / market sizing / cap table review）

把一个「值得投的感觉」拆成可核查的证据——系统化做 founder reference call、market sizing、产品 / 竞争 / unit economics 核查、cap table review，产出能在 IC 上站得住的尽调结论 + risk 清单。入门 SOP 5 步：founder / team reference call → market sizing（TAM 核查）→ 产品 + 竞争核查 → traction + unit economics 核查 → cap table review + 法律。

- **skip**：资深投资人在种子 / 早期天使阶段跳过重的量化尽调（深抠 unit economics、买 expert call、长法律尽调）——种子期数据太薄，过度量化是另一种错；他们把早期尽调收敛到「人 + 市场天花板 + 一个核心假设」三件事。理由：早期 deal 体量小、信息本就稀薄，重尽调 ROI 不成立。(evidence: [T03-S011, T04-S001])
- **optimize**：把「reference call」优化成「off-list 独立背调」——不止打创始人给的 friendly reference，而是从自己网络里找创始人没列的独立信源（前同事、前投资人、客户）交叉验证。这是区分新手和老手最明显的尽调动作。(evidence: [T03-S005])
- **add**：额外做两件——(a)成长期 / 大额 check 上主动买 expert call（AlphaSense / Tegus / GLG）做独立产品 / 市场验证，绕开创始人提供的友好信息；(b)把尽调聚焦到「这个 deal 最可能 kill it 的那一个假设」上深挖，而不是平均用力做完一张 checklist——资深人尽调是「找致命伤」，新手尽调是「填表」。(evidence: [T03-S011, T03-S018])
- **近期变化**：2024-2025 LLM 工具成熟，AI 辅助尽调起势（LLM 做 market sizing 初稿 / 竞品扫描 / deck 初筛打分），把 associate 尽调时间从「全做」变成「机器做初稿 + 人核校 + 人做 reference call」，但 reference call 这种「投人」的核心动作仍无法被工具替代；2025 AI cycle 下热门 AI deal 尽调被竞速压缩、寒冬赛道尽调反而更重——尽调强度在同一行业内两极分化；国内 deal 尽调多了「回购条款相关的创始人个人连带风险评估」。
- **Last_updated**：2026-05-14（尽调维度骨架稳态；AI 辅助 + 竞速分化 + 国内回购环节是近 12 个月变化）
- **Decay**：medium——「reference / 市场 / 产品 / unit economics / cap table」五维核查是稳态，但 AI 辅助把「初稿环节」12-24 个月内显著重写，且尽调强度随周期波动。

### W6. Term sheet 谈判 + 估值

把「决定要投」翻译成一份双方能签的 term sheet——定估值（pre/post-money + option pool）、选轮次工具（SAFE / 可转债 / priced round）、谈关键条款（董事会 / liquidation preference / pro-rata / anti-dilution），并在「赢条款」和「保关系」之间找平衡。入门 SOP 5 步：定估值结构 → 选轮次工具 → 谈 economics 条款 → 谈 control 条款 → 谈判到签字。

- **skip**：资深投资人对标准化早期 deal 几乎跳过逐条款谈判——直接用市场标准的 SAFE / 标准 term sheet 模板（YC SAFE、NVCA 模板、各家标准 term sheet），把谈判收敛到「估值 + 投资额」两个数。理由：早期 deal 在标准条款上较劲是 negative-sum，赢光条款反而输掉关系和 deal。(evidence: [T03-S003, T03-S013])
- **optimize**：把「定估值」优化成「从 ownership target 倒推」——不先纠结估值数字，而是先定「这个 deal 我要拿到的 ownership %」，再倒推投资额和能接受的估值区间；估值变成 ownership 的结果而非起点。(evidence: [T03-S005])
- **add**：额外做——把 term sheet 谈判当「7-10 年关系的第一次握手」来设计：刻意在不重要的条款上让步、在真正关键的（估值合理性、pro-rata、董事会）上守住，让创始人感到「这是个能共处的投资人」。初学者容易逐条款都想赢，反而在最该合作的起点埋下对立。(evidence: [T03-S003, T03-S006])
- **近期变化**：近 12 个月无重大流程变化（行业稳态）——term sheet 条款体系、SAFE / priced round 工具选择、谈判逻辑是 VC 数十年沉淀的成熟流程，最近一次显著变化是 2013 年前后 YC SAFE 的推广（把早期不定价融资标准化）；周期性的条款行情移动（2022-2024 寒冬 down round / 结构性条款频率上升、2021 高点极松）是「条款行情」随周期波动而非流程变化；国内 deal 的 term sheet 历来有「回购条款」这一海外没有的核心环节，2023-2024 回购诉讼潮让其权重上升。
- **Last_updated**：2026-05-14（流程稳态；条款行情随周期波动但骨架不变）
- **Decay**：low——term sheet 条款体系 + 工具选择是数十年成熟流程，12-24 个月不会有结构性改写。变化的是「条款行情」（随周期）和国内回购环节，不是 workflow 本身。

### W7. 投后服务 / board service

钱投出去之后，把一个 portfolio 公司从「cap table 上一行」变成「被主动帮扶、被监控、危机时被救」的资产——board service、招人、客户介绍、帮融下一轮、危机处理。入门 SOP 5 步：建立沟通节奏（月度 / 季度 update + board meeting）→ 定期 board meeting → 响应式帮扶 → monitor 健康度 + triage（default-alive vs default-dead）→ 危机 / 退出协助。

- **skip**：资深 GP 跳过对 portfolio 里「明确的中后段 loser」的持续深度投入——不平均分配投后精力，把时间集中到 winner 和「还能救」的公司上，对明确失败的项目快速降低投入（甚至主动 write-off）。理由：投后精力是稀缺资源，power-law 下 winner 的边际帮助远比救 loser 值钱。(evidence: [T03-S016, T04-S004])
- **optimize**：把「响应式帮扶」优化成「主动装能力」（venture assistance）——不等创始人开口，而是预判公司下一阶段缺什么（如 A 轮后缺销售 VP、缺 CFO），主动把能力 / 人 / 客户送过去；a16z 的平台化投后军队就是这种模式的极端制度化。(evidence: [T03-S016, T01-S005])
- **add**：额外做——对 winner 主动管理「下一轮融资的定位」：在公司融下一轮前帮它对接更高阶的投资人、帮讲故事、确保自己的 pro-rata 被接住（把 W7 和 W8 reserve 接起来）。初学者把投后当「被动客服」，资深人把投后当「保护和放大 winner」的主动动作。(evidence: [T03-S016])
- **近期变化**：2022-2024 寒冬延续到 2025，投后重心从「blitzscaling / how to grow faster」转向「省钱续命 / default-alive 管理 / 危机处理」，Reid Hoffman 专门写《Bear Market Blitzscaling》回应这一转变；2025 起退出难，投后多了「主动用 secondary sale 给 LP 制造流动性」这个新动作；国内投后多了「回购条款执行 + 与创始人个人连带的风险处理」环节（2023-2024 回购诉讼潮）——「沟通节奏 + board meeting + 帮扶 + triage」骨架多年未变，变的是议题方向。
- **Last_updated**：2026-05-14（投后骨架稳态；议题方向 + secondary 流动性 + 国内回购执行是近 12 个月变化）
- **Decay**：medium——「沟通节奏 + board + 帮扶 + triage」骨架稳定，但「投后议题方向」随周期（增长 vs 续命）持续移动，且 people-analytics 类工具的渗透是 12-24 个月的变量。

### W8. Portfolio construction + reserve 策略

在投出第一笔钱之前，把整支基金的数学先画出来——用 fund size 反推 check size、目标项目数、ownership target、reserve 比例，让基金的结构本身能容纳一个 power-law 结果。入门 SOP 4 步：从 fund size 反推组合宽度 → 定 ownership target → 留 reserve / follow-on（业内估计常见 40-60%）→ 定「集中 vs 分散」取向。

- **skip**：资深 GP 在募新基金时几乎跳过「从零设计组合数学」——直接沿用上一支基金验证过的 construction（check size / 项目数 / reserve 比例），只按当前周期和基金规模微调。理由：portfolio construction 一旦在一支基金上跑通，是可复用的模板，重新发明没必要。新 GP 才需要从零画。(evidence: [T03-S005])
- **optimize**：把「静态 reserve 比例」优化成「动态 reserve 管理」——不是一开始锁死一个数就不动，而是随部署期里 winner / loser 的浮现持续重算「还需要多少 reserve 接住现有 winner」，把 reserve 当活的而非死的。(evidence: [T03-S011])
- **add**：额外做——把 portfolio construction 和单个 deal 决策绑死：每次 W2 出 term sheet 前都回头对一遍「这一笔在组合里占哪个格、留多少 reserve、ownership 够不够」，让组合约束实时作用于每个 deal。初学者把 portfolio construction 当一次性的「开局设置」，资深人当贯穿全程的「实时约束」。(evidence: [T03-S005, T03-S011])
- **近期变化**：近 12 个月无重大流程变化（行业稳态）——portfolio construction 的数学（fund size → check size → 项目数 → ownership → reserve）是 power-law 商业模式本身决定的数十年稳态逻辑，Jerry Neumann 2015 年的「Jobs-to-be-done of VC」就已把它学术化、至今未被推翻；周期性的参数调整（2022-2024 寒冬「reserve 比例上调 + 组合更集中 + check size 更保守」、2025 AI 赛道「估值极高、check size 被迫放大」）是参数随周期移动，不是 workflow 骨架变化。
- **Last_updated**：2026-05-14（组合数学是稳态逻辑；参数随周期调整但骨架不变）
- **Decay**：low——portfolio construction 的数学由 power-law 商业模式本身决定，数十年未变、12-24 个月也不会有结构性改写。变化的是参数（随周期），不是 workflow。



## 表达 DNA

> 不模拟某个具体 figure，模拟「VC 行业的资深人聚一起讨论时的 register」。多人融合。

### 5.1 维度

| 维度 | 内容 |
|------|------|
| 高频用语 / 黑话 | power law / fund-returner（一切 portfolio 决策的底层语言）；carry / management fee / "2 and 20"（GP 收入结构的口头语）；DPI / TVPI / IRR（「IRR 是 paper，DPI 才是 real」「markups aren't returns」）；pre / post-money（「pre or post?」是反射性追问）；SAFE / convertible note / priced round（早期融资工具三件套）；liq pref / anti-dilution / participating preferred（term sheet 谈判语言，"participating" 一出现就警觉）；deal flow / sourcing / access（「sourcing ≠ winning」）；thesis / conviction / "high conviction"（有具体所指：可证伪的方向判断 / 敢逆共识重注）；dry powder / runway / burn / "default alive vs default dead"；reserve / follow-on / ownership target / check size；anti-portfolio（「错过比投错致命」）；中国特色：对赌 / 回购 / 估值倒挂 / 人民币基金 vs 美元基金 / 引导基金 / 双 GP / 返投 |
| 严肃 register | 长 podcast / conference talk / 长博客里口语化但精确，不端着——爱用「算账」式表达、爱讲具体案例和具体判断标准而非宏大叙事；谈条款 / 基金运营时用全称缩写 + 具体数字（1x non-participating、2 and 20、DPI）；引用周期（2021 高点 / 2022-2024 寒冬 / 2025 AI cycle）作为坐标系；最锋利的资深人（Gurley、朱啸虎）说话直接、不留情面、用数据怼回去 |
| 内 vs 外沟通差异 | 对 LP / 创始人（「客户」面）会把术语展开、讲清楚为什么；同业之间允许大量缩写和「pre or post?」式追问；**注意 intake warning #2：公开博客 / podcast / 著作多是「公开人设版」——给 LP 看的市场推广或个人品牌，与 deal team 真实工作有 gap；真正接近实际工作的是「figure 谈具体判断标准 / 具体陷阱」的样本（Gurley 的 LTV 陷阱、朱啸虎的硬指标、Wilson 的 CEO 三件事），而非「figure 谈宏大叙事」的样本** |
| 外行破绽 | 见 §6 反模式（直接采用 glossary outsider-tell top 10） |
| 厂商话术拒绝 | 见 5.3.4 反例版（直接采用 glossary「行业拒绝的厂商话术 top 5」） |

### 5.2 对话样本库总数与 voice_confidence

合计 9 段（客户/面 LP 版 3 / 同业版 2 / 专业-监管版 2 / 反例版 2）。来源是 Track 01 figures 的 voice_samples 字段——Track 01 的 voice_samples 多数已标「转述」「转译」「推断」（原文常为英文长段、或综合多篇访谈），少数接近原话。按本文口径：9 段、多数标 `(转述)` → **voice_confidence: medium**。Phase 3 写 SKILL.md §5 时每段须带 source_id 让用户回溯；主风格输出有真行业语料支撑，但精度受「转述为主 + 国内一手薄」限制（国内仅张磊 / 朱啸虎 / 李开复三人有可引样本，沈南鹏 / 徐小平 / 雷军未 retain，见 §8）。**4 类样本可区分流派**：Gurley/Khosla 的锋利估值纪律 vs Wilson 的温和长博客 vs 张磊的长期主义哲学 vs 朱啸虎的犀利算账，register 差异明显，不调和成一个平均音。

### 5.3 对话样本库（industry voice 实战语料）

#### 5.3.1 客户 / 面 LP 版（对创始人 / LP 解释、教育）

- 「PMF 没发生时你能感觉到——客户没真正获得价值、口碑不传播、用量涨不快、销售周期太长，很多单子永远 close 不掉。PMF 发生时你也能感觉到——产品被买走的速度跟你能造的一样快。」（source: T01-S004，转述+压缩，原文为英文长段，Andreessen《The Only Thing That Matters》；客户场景：对创始人解释「什么时候算 PMF」）
- 「一位资深 VC 跟我说，CEO 只做三件事——定整个公司的愿景与战略并讲给所有人听；招到、雇到、留住最好的人；确保账上永远有足够的钱。」（source: T01-S001，转述自 Fred Wilson《What A CEO Does》原文框架；客户场景：对创业者 / 新人讲 CEO 到底干什么）
- 「时间会创造复利的价值。有些好企业的竞争优势今天还看不出来，明天可能稍露端倪，要到更长期才会完全显现——所以要做时间的朋友。长期结构性价值投资的核心是反套利、反投机、反零和游戏、反博弈思维。」（source: T01-S020，转述自张磊《价值》核心论点；客户场景：对创业者 / LP 解释「长期主义」与「时间的朋友」）

#### 5.3.2 同业版（私下 / 内训 / 同业访谈）

- 「风投有意思的地方在于你最多只会亏一倍钱。人们倒抽一口气，但你得看另一面——如果你能赚 50 倍、只亏 1 倍，这是笔相当好的交易。我不介意单个项目失败的概率更大，只要每只基金里有足够的分散。」（source: T01-S016，原话转译，Khosla / Moonfare 访谈；同业讨论：对投资人 / LP 讲非对称收益）
- 「今天的 AI 应用创业者要勇于承认自己没有壁垒——有任何技术壁垒都是骗人的、都是忽悠人的。所有应用都是靠底层模型提供能力，壁垒只能建在 AI 之外。创业的本质依然是做生意，要算账——我关注的是你能不能商业化、谁来付钱、销售周期多长、留存率怎么样。」（source: T01-S025，转述自朱啸虎财联社 / 证券时报访谈，接近原话；同业讨论：对创业者讲 AI 应用的壁垒与投资判断标准）

#### 5.3.3 专业 / 监管版（公开场合谈标准 / 估值纪律 / 行业结构）

- 「私募市场的高估值是『纸面上』的——复杂的清算优先权条款让 late-stage 投资人拿到了下行保护，普通员工的期权却没有。LTV 公式有种危险的诱惑——它让你用一个漂亮的终值掩盖掉获客成本越来越贵、留存越来越差的真相。不是所有收入都生而平等。」（source: T01-S002，转述自 Bill Gurley《On the Road to Recap》/《The Dangerous Seduction of the LTV Formula》/《All Revenue Is Not Created Equal》核心论点；专业场景：公开谈估值泡沫与单位经济学纪律）
- 「我不喜欢『个人功劳』这种说法。我们都站在彼此的肩膀上——Michael 站在 Don 的肩上，我站在 Mike 的肩上，这是一个集体的『我们』。卖掉 Sequoia 的一部分，意味着里面的人会更有钱——但留给下一代去分的那块饼，会更小。」（source: T01-S007，转述 + 部分原话转译 "We're all standing on each other's shoulders"，Doug Leone / Acquired 访谈；专业场景：公开谈机构传承观与 stewardship）

#### 5.3.4 反例版（VC 资深人**绝不会**这样说 / 被错位包装的厂商话术）

- 「用我们的 AI sourcing 工具，你就拥有了 deal flow，就拥有了 alpha。」（source: T06 厂商话术拒绝 #1，why 反例：内行的共识是 sourcing ≠ winning——顶级 deal 是被 founder 选，工具能扩大「看到」的量，但拿不到「access」和 conviction；把工具等同于能力是典型外行营销。对照 glossary Tier 1 #18 deal flow / sourcing 的 insider def）
- 「跟着我的 7 步就能进入 VC，人人都能做天使投资。」「他公开发声多、LinkedIn 粉丝多，所以投资能力一定强。」（source: T06 厂商话术拒绝 register 层 + intake warning 2/6/9，why 反例：与行业真实就业结构直接冲突——up-or-out 是常态、Partner 席位极稀缺、Associate 走到 Partner 比例极低；且内行清楚「个人 brand 优秀 ≠ 投资业绩好」，self-promotion 是工作之一但不是 track record；把「VC 决策」描述成「数据驱动的客观流程」也是营销——早期投资本质是 high-uncertainty judgment）



## 质量基准 + 反模式

### 6.1 什么算「好」（质量基准，4 条）

1. **判断一个 deal 的第一性问题是「能不能 return the fund」，不是「稳不稳 / 会不会亏」**：成熟投资人评估早期 deal 时，先过 power-law 这一关（市场天花板 + ownership target 够不够支撑一个 fund-returner），再谈其余；把「错过 outlier」当成比「投错一笔」更需要防的成本。(evidence: [T04-S004, T01-S016])
2. **看 traction 区分「健康增长」和「烧钱买的增长」，看条款把估值和 control / economics 合起来看**：好的尽调能算出 unit economics、能识别 participating preferred / option pool 算在 pre 侧这类隐性税；说「估值 1000 万」不指明 pre/post、谈 deal 只看「估值 + 金额」两个数是不及格。(evidence: [T01-S002, T04-S001])
3. **尽调「找致命伤」而非「填 checklist」，且每个单 deal 决策都绑回 portfolio construction**：资深的标志是把尽调火力集中到「这个 deal 最可能怎么死」的那一个假设上、做 off-list 独立 reference call，并在出 term sheet 前对一遍组合（ownership / reserve / 占哪个格）；平均用力填表 + 孤立看单 deal 是新手。(evidence: [T03-S005, T03-S011])
4. **把判断放进周期和 fund math 里读**：好的判断会先定位当前周期（2025-2026 是 AI 竞速 + 其他赛道寒冬的两极分化）、先看一支基金的 vintage / lifecycle / carry 经济学，再下结论；寒冬里看 DPI 不看 TVPI；不跨 vintage 比回报。(evidence: [T01-S028, T04-S018])

### 6.2 反模式（10 条，外行 / 入门常犯——直接采用 glossary outsider-tell + Track 03 失败模式）

1. **报估值不说 pre/post、把 VC 当一个人、把 carry 当 GP 日常收入**——这三条是「没真做过 VC」最快的破绽：不指明 pre/post 稀释算不出来；VC 是 GP-LP 双层受托结构、那是 LP 的钱；日常工资是 management fee，carry 是 7-10 年后才兑现的「期权」。(glossary outsider-tell #1/#2/#10)
2. **跳过独立 reference call 或只打 friendly reference**——早期投资本质是投人却不查人；co-founder 矛盾、人品问题、简历注水只能从创始人没列的 off-list 独立信源查出，这是 write-off 的高频原因。(Track 03 失败模式 5)
3. **孤立看单个 deal、不对 portfolio construction**——投完才发现 check size 和组合不匹配、ownership 不够；正解是出 term sheet 前回组合对一遍。(Track 03 失败模式 7)
4. **reserve 不够、winner 接不住**——首轮把基金投满，winner 起飞却无钱 follow-on，是新基金第一大结构性错误；正解是募资后立刻锁定 reserve 比例（业内估计常见 40-60%），宁可初始少投几家。(Track 03 失败模式 9)
5. **在估值高点把基金一次性打光 + TVPI 高就躺平不主动制造 DPI**——2021 式 FOMO 部署被 down round 打骨折；账面 TVPI 再高、不退出就是「纸面富贵」，LP 要的是 DPI。(Track 03 失败模式 8/11，glossary「markups aren't returns」)
6. **撒网但无 thesis**——见很多公司却没有「我在哪个赛道比别人强」，deal flow 大而不专，出不了 proprietary 优势。(Track 03 失败模式 12)
7. **把 AI sourcing / AI 尽调工具当 judgment 替代**——它只是初筛放大器，judgment 仍在人，且整层 experimental、6 个月后工具可能换一批，别把核心工作流押在单一工具上。(Track 03 失败模式 13，glossary 厂商话术 #1)
8. **种子期死抠 unit economics + 平均用力填尽调 checklist**——对数据太薄的早期公司做重量化尽调是另一种错；每个维度都做但都不深，等于没找到致命伤。(Track 03 失败模式 15/16，canon unit economics 常见误用)
9. **接受非标 liquidation preference 而不自知**——participating / 2x+ multiple 被当正常，在中等退出场景里会吃掉创始人回报；1x non-participating 是市场标准，任何超出都是隐性税。(Track 03 失败模式 18，glossary outsider-tell #5)
10. **逐条款都想赢、输掉 7-10 年关系 + 拿不到 pro-rata 就签**——把 term sheet 当一次性博弈，在最该合作的起点埋下对立；且 pro-rata 是接住 winner 的入场券，早期 deal 哪怕条款让步也要守住。(Track 03 失败模式 19/20)



## 智识谱系

> 保留分歧，不抹平——「双方都对」是没营养的废话。VC 的流派分裂主要在「同一个早期 deal，不同派给完全相反的『该不该投、投多少、投后管多深』答案」这个层面。海外 vs 国内当「分叉」处理（两套生态，不是「谁对谁错」）。

### 7.1 五大方法论流派

- **流派 A — Thesis-driven 主题先行派**：奠基 = Fred Wilson 的 AVC.com + USV 的「投资 thesis 白皮书」实践（每代基金先写 15-20 页主题论文）；另一支是 a16z 的「软件吞噬世界」memo 群。当前代表 = Fred Wilson（USV）、Marc Andreessen / Chris Dixon（a16z）、李开复（创新工场 AI 2.0）、Vinod Khosla（deep tech contrarian）。核心主张：先形成对世界演化的判断，再用它系统筛 deal；thesis 要演化（USV「大网络」→「开放协议」→「加密」是同一 thesis 的迭代）。核心风险：thesis 可能成为「思想牢笼」，对 thesis 外的 outlier 系统性错过。
- **流派 B — Concentrated 高 conviction 派**：奠基 = Bill Gurley 的《Above the Crowd》长博客 + Benchmark 的「平等合伙制」（4-5 人，经济与决策权完全平分，无 junior、无 leader）。当前代表 = Bill Gurley（Benchmark 退休 GP）、Doug Leone / Michael Moritz（Sequoia 老一辈的「市场聚焦 + 创始人优先 + 纪律」更偏此派）。核心主张：少投、重投、深度参与，靠估值纪律和高 conviction；反对 VC 规模化。核心风险：「少投」在 AI 这种需要广撒网才能押中早期 outlier 的周期里，可能系统性 miss。
- **流派 C — Spray-and-pray / 加速器派**：奠基 = Paul Graham 的 essays + YC 加速器模式（标准 SAFE / 标准 deal terms / batch + Demo Day，把早期投资规模化）；学术骨架 = Kerr/Nanda「Entrepreneurship as Experimentation」（投资 = 便宜实验 → 观察 → 加倍下注）。当前代表 = Paul Graham / Sam Altman（YC）、部分天使风格。核心主张：广撒网、标准化 terms、batch + 教育驱动；用少成本买信息再集中 follow-on。核心风险：被批「稀释 conviction」、Demo Day 的「集中融资剧场」人为推高早期估值制造 FOMO。
- **流派 D — 平台化大基金派**：奠基 = a16z 的平台化机构本身（multi-strategy 基金 + 大规模投后服务团队，颠覆传统 VC 编制）+ a16z 经典 memo 群。当前代表 = Marc Andreessen + Ben Horowitz + Scott Kupor（a16z）。核心主张：VC 的规模化是进步，投后即产品（venture assistance 主动装能力），founder-CEO 优先。与流派 B 直接对立——分歧点在「VC 的规模化是进步还是摊薄 carry 的意义」（concentrated 派认为大基金是「AUM 规模游戏」，管理费驱动而非 returns 驱动）。
- **流派 E — Solo GP / solo capitalist 派**：奠基 = AngelList 的 SPV / RUV / fund admin 基础设施（把「一个人管一支机构化基金」变得可行）。当前代表 = Elad Gil / Lachy Groom 等。核心主张：一个人独立募资 + 决策，靠速度和个人 access，不需要机构编制。注意：solo GP ≠ 天使投资人——solo GP 是「一个人管一支有 LP、有 carry、有 fund 结构的机构化基金」。

### 7.2 学术 VC 研究脉络（影响业界但非「派」）

Kaplan / Lerner / Gompers / Strebulaev / Nanda 群——是 Stanford GSB / HBS / Wharton 的 VC 课程底座，给业界提供「行业平均行为」的校准基线：Gompers/Strebulaev 的 ~900 家 VC 问卷（VC 真实工作的硬实证）、Kaplan & Lerner 的 VC 数据偏差论文、Kaplan & Schoar 的 GP 业绩持续性实证、Kerr/Nanda 的「投资 = 实验」框架。它的价值是对冲「公开人设」——长博客 canon（AVC / a16z memo）本身是「被 sanitize / 带个人品牌」的版本，学术 paper 给的「行业平均」可作校准。

### 7.3 仍在争论的核心分歧（保留，不裁决）

1. **team vs market vs thesis 谁第一**：Gompers/Strebulaev 问卷说多数 VC 把 team 排第一；Andreessen《The Only Thing That Matters》反驳说 market 最大。同一行业内的两份「权威」给出相反排序——这是 canon 内部最根本的未决之争之一，写进 §1.2 作为「必须捕捉的张力」。
2. **集中 vs 广撒**：Benchmark / Gurley 的 concentrated（流派 B）vs YC / PG 的 spray-and-pray（流派 C）——**同样信 power-law，却推出完全相反的打法**。这是本行最根本的方法论分歧。
3. **VC 该不该是「平台」**：a16z 的全栈服务 / 平台化模型（流派 D）vs Benchmark 的「小合伙、不做平台」（流派 B）——分歧点是「规模化是进步还是摊薄 carry 意义」。
4. **operator-investor vs analyst-investor**：用运营 / 创业经验做投资判断（Reid Hoffman、Ben Horowitz、李开复的技术背景）vs 用研究 / 估值 / 数据纪律做判断（Bill Gurley 的华尔街研究员出身、Mary Meeker 的卖方分析师出身）——「会管公司 / 懂技术 ≠ 会选公司」与「光环效应」是双方互相的批评。
5. **公开品牌化 vs 安静派**：VC 即媒体 IP（All-In 四人组、朱啸虎高频发声、李开复 keynote）vs 不做个人品牌靠机构与口碑（Doug Leone / Michael Moritz、相对低调的张磊）——**这条分歧特别重要**，intake warning #2/#6 明确指出「公开形象 ≠ 投资能力」，All-In 群体是「公开多 ≠ 投得好」的最佳反面教材（见 §8）。

### 7.4 海外 vs 国内（分叉，不是分歧）

不是「谁对谁错」，是两套范式：**海外 VC** = 纯股权 + NVCA 标准文件 + IPO / M&A 退出 + 生态成熟 + 长博客 / podcast 沉淀厚（AVC.com / Above the Crowd 这种 20 年长跑写作）；**国内 RMB 基金** = 股权 + 对赌 / 回购（把股权做成类债化）+ 引导基金 LP（带返投 / 招商等政策诉求）+ A 股退出 + 双 GP 结构（投资 GP + 募资 / 国资资源 GP）。同名「VC」实为两套范式。**国内一手深度信源结构性偏薄**——主阵地是公众号黑名单 + 闭门会，国内没有 AVC.com / Above the Crowd 的对标物，国内 figures（仅张磊 / 朱啸虎 / 李开复 retain）、workflows、voice 维度都比海外薄（详见 §8）。master skill 必须按 locale 分章。



## 诚实边界

> 至少 3 条具体局限。所有 `%` / 数字 / 价格 / 日期带 source_id 或置信度 caveat。VC 数据透明度极差，本节尤其严格。

### 8.1 关键 caveat —— 一手率的「机械口径」陷阱（必读）

source_verifier 对 VC 行业有系统性低估：它对**作者裸域博客**（avc.com / abovethecrowd.com / paulgraham.com / feld.com / reactionwheel.net）、**VC firm 官网**、**Substack / Medium 子域**一律保守判 `secondary`，不上抬。按此机械口径，146 条 source 里 verified_primary + surrogate_primary 合计仅约 67 条 ≈ **46%**（Track 01 figures 机械口径 8/28 ≈ 29%、Track 03 workflows 5/18 ≈ 28%、Track 04 canon 9/25 ≈ 36%）。**但这个数字系统性低估了真实一手内容比例**——VC 行业的一手内容**恰恰大量发在创始人 / GP 的裸域博客和本人著作里**：Fred Wilson 的 AVC.com（1000+ 篇本人长博客）、Bill Gurley 的 Above the Crowd（本人万字长文）、Paul Graham 的 essays、Brad Feld 的 feld.com term sheet 系列、张磊《价值》、《沸腾新十年》——这些都是真·一手，只是发布渠道的形态让机械 verifier 误判。Track 01 按「实际作者一手文本」重算约 75%，Track 04 canon 实质一手 ≈ 86%。**引用时应理解：机械口径 ~46% 低估了真实一手比例，实际一手内容比例显著高于此**——这是 GLOBAL 行业内容分发的结构性特征，不是调研不力，Phase 4 item 13（URL 一手机械验证）对本行业应按 GLOBAL 规则放宽理解。

（另一面也要诚实：Track 02 工具维度确实一手偏薄——24 条 source 以 vendor docs（`surrogate_primary`）为主，因黑名单覆盖面广（G2 / Capterra / 知乎 / 公众号全禁），第三方独立评测引用密度偏低；工具的抽成 / 定价 / 功能这类**事实**由厂商一手披露可信，但「某工具值不值得用」这类**判断**有 vendor 一面之词的风险，新兴层（Attio / AI sourcing / Eqtble）的 production case 多为 stack-pattern 推断而非可验证案例。）

### 8.2 国内 locale gap（显著，贯穿全部 6 轨）

locale = global，但国内侧信号结构性弱于海外。根本原因：**国内 VC 的一手深度信源主阵地是微信公众号（信源黑名单）+ 闭门分享 + Stanford GSB 式精英圈子的国内对应**，非黑名单的一手长访谈 / 长博客 / 长 podcast 极少。具体：
- **figures 维度**：海外 retain 10 张卡（一手长素材普遍充足），国内仅 3 张（张磊 / 朱啸虎 / 李开复）；**沈南鹏、徐小平、雷军、阎焱因公开长素材不足未 retain**（沈 / 徐降为名片型 manifest 条目）。国内 VC 的真实方法论沉淀在闭门场合，公开可得的远薄于海外。
- **workflows 维度**：国内路径的 workflow 描述（回购环节、RMB 募资变重）是「从行业语境 + 法规 + 媒体报道推断」，而非直接从国内 GP 的一手工作流叙述提炼——国内没有 AVC.com / Above the Crowd 这种可对标的一手长博客。
- **tools / sources / voice 维度**：国内工具卡片主要靠 vendor 官网；国内一手创作者发声渠道几乎收不到（疯投圈是唯一 retain 的中文 podcast 且更新不稳定）；voice DNA 国内侧偏薄。
- **结论**：本 skill 对国内 VC 的画像精度显著弱于海外，国内部分的 mental model / workflow / voice DNA 须做二次校验；agent 在中文创投 source 上的 deep-fluency 期望应低于英文侧。

### 8.3 行业头号陷阱 —— 公开形象 vs 实际工作的 gap（intake warning 2/6/7/8）

这是本行业最需要警惕的元认知问题，多条 intake 警示指向它：
- **多数「VC playbook」是 GP 个人品牌营销，不是实际工作**：公开博客 / podcast / 著作多是给 LP 看的市场推广或个人品牌叙事，不是 deal team 真实工作的逐步记录。本文已尽量优先采用「figure 谈具体判断标准 / 具体陷阱」的素材，但「资深路径」的 skip / optimize / add 仍有部分是从公开叙事 + 工具场景 + canon 流程综合推断，而非直接观察到的 deal team 内部 SOP。**外部能拿到的是 70 分的公开版工作流，顶级 20 分的 deal team 内部 SOP 拿不到**（intake warning 8）。
- **个人 brand 优秀 ≠ 投资能力**（intake warning 6）：大量公开活跃的网红 VC 真实业绩平淡；All-In 群体（Chamath / Sacks / Friedberg / Calacanis）是「公开多 ≠ 投得好」的活样本——Chamath 的 SPAC 标的大面积破发，Calacanis「早期投 Uber」被反复引用但整体投资记录的 power-law 真实分布并不透明。读者要警惕「公开多 ≠ 投得好」。
- **数据透明度极差**（intake warning 7）：GP fund returns 多不公开；公开 deal 数据（PitchBook / Crunchbase / IT 桔子）系统性偏头部、偏后期，种子 / 早期天使 deal 大量缺失——「公开数据是冰山一角」，把数据库当 ground truth 是外行（Kaplan & Lerner 的 NBER 论文把这条警示学术化）。

### 8.4 power-law 业态本身的局限 —— VC 不是「稳定职业」（intake warning 1/9/10）

- **VC 不是稳定职业**（intake warning 1）：90%+ deals 失败或回本，头部 1-2 个 deals 占 fund return 80%（业内通行说法，精确分布因 GP returns 不公开而无法核实）——fund return 极不平均，绝大多数基金 / 投资人达不到「头部」。
- **职业上升路径不透明**（intake warning 9）：Associate → Principal → Partner 极少数能走通，「up-or-out」是常态，Partner 席位极稀缺；Associate 多是 2-3 年合约角色。SKILL.md 应写真实就业市场而非「7 步进入 VC」的励志故事。
- **carry 兑现周期长**（intake warning 10）：GP 日常工资靠 management fee（约 2%/年 × 基金规模，业界标准「2 and 20」的「2」），真正的上行收入 carry（20% 利润分成，头部基金可到 25-30%）要等基金 7-10+ 年生命周期后才兑现，且很多基金一辈子都没等到 carry。VC 不是「高薪稳定职业」。

### 8.5 VC 与创始人利益不对齐 + 学派分歧无共识（intake warning 5/11）

- **VC 与创始人利益不一定对齐**（intake warning 11）：GP 想要 outlier exit（power-law 决定），founder 可能想 build long-term；本 skill 提炼的是「VC 视角的 OS」，**VC playbook 不一定对 founder 最优**——尤其在「该不该卖公司」「该不该再融一轮」这类问题上，GP 和 founder 的最优解可能相反。
- **学派分歧大、无行业共识**（intake warning 5）：team-vs-market、集中-vs-广撒、要不要做平台、operator-vs-analyst（见 §7.3）至今无共识；本 skill 保留分歧而非裁决，任何「VC 应该怎样」的断言都要先问「在哪一派语境下」。

### 8.6 时效衰减 —— 工具栈 / 工作流模块衰减最快

信息截止 2026-05-14。按 extraction-framework 衰减表，**工具栈 + 工作流模块衰减最快**。具体已落地 / 预计变动的（数字均带 source）：
- **2022-2024 寒冬未完全过去 + 2025 AI cycle 局部反弹**：造成「同一行业内 deal 节奏两极分化」（AI / 热门赛道竞速 vs 其他赛道慢节奏），影响 W1 / W2 / W3 / W5 / W7 多个 workflow 的节奏与议题方向（intake warning 4，写时间戳：2025-2026）。
- **AI 辅助 sourcing / 尽调**：Track 02 标注整层 `stability: experimental`、工具碎片化无 default，**采用率数据未在调研中验证**——不能当「已成主流工作流」，只能说「2024-2025 起势、从 AI-native 基金向主流扩散中」；W4（deal sourcing）是 Track 03 里 decay 最快的 workflow。
- **ILPA Reporting Template v2.0**：2025-01 发布，对仍在投资期的基金自 2026 Q1、新基金自 2026-01-01 起替代 2016 版（evidence: [T06-S019]）。
- **QSBS / §1202**：2025-07-04 OBBBA 重大修订——对 2025-07-04 之后取得的 QSBS 引入阶梯持有期、单纳税人单发行人排除上限从 1000 万 → 1500 万美元、公司总资产门槛从 5000 万 → 7500 万美元（evidence: [T06-S004, T06-S020]）；之前取得的股票适用旧规则。
- **SEC accredited investor**：2020-08 修订新增专业资格路径，2025 仍有扩大定义的立法在国会推进，但核心收入 / 净资产数字截至 2026-05 未变（evidence: [T06-S001, T06-S018]）。
- **中国监管**：《私募投资基金监督管理条例》2023-09-01 施行（首部行政法规）、中基协登记备案 2023-05 新办法门槛大幅提高（evidence: [T06-S006, T06-S008]）；2023-2024 回购诉讼潮让国内 deal 多了「回购条款 + 创始人个人连带风险」环节，司法 / 监管口径仍在演化（decay high）。
- **行业属性局限**：VC 行业基本无强制执业认证——美国 GP 无入行证照（Series 65/82 等仅特定活动触发），中国有「基金从业资格」作为登记前置；起「标准」作用的更多是行业协会软标准（ILPA / NVCA）+ 平台事实标准（YC SAFE）。
- **强烈建议每 3-6 个月跑一次 `update 大师 vc-investor`**——AI sourcing 工具层在 12 个月级别快速重写、国内创投工具随 RMB 周期 + 政策剧烈波动即先例。心智模型 / 智识谱系 / canon 衰减慢（1-2 年）。
- **不能替代真人**：本 skill 是「2026-05 的业界共识 + 明显分歧 + 公开形象 vs 实际工作 gap」的提炼，不是「跟我学做 VC」——VC 是 power-law 业态，绝大多数投资人 / 基金达不到头部，且顶级的 deal team 内部 SOP 不公开。




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
