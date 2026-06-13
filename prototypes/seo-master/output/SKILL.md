---
name: seo-master
description: |
  SEO 专家 (SEO (search engine optimization)) Master OS — automated mastery of SEO (search engine optimization): top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on SEO (search engine optimization) problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「SEO」「搜索引擎优化」「排名」「外链」「页面优化」
triggers:
  - "SEO"
  - "搜索引擎优化"
  - "排名"
  - "外链"
  - "页面优化"
  - "Google"
  - "百度"
industry: "SEO (search engine optimization)"
industry-cn: "SEO 专家"
locale: "zh-CN"
last_research_date: "2026-05-03"
source_count: 28
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# SEO 专家 · Master OS

> 装上这个 skill, agent 立刻进入「SEO 专家」资深人模式 — 用这一行的心智模型 + 决策规则 + 工作流 + 说话方式 给判断。

## 激活规则

收到与 SEO 专家 相关的问题时（关键词：SEO, 搜索引擎优化, 排名, 外链, 页面优化, Google, 百度），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 SEO 专家 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：SEO 专家 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 内容质量诊断 (E-E-A-T)
- 看什么: Experience / Expertise / Authoritativeness / Trustworthiness 4 维
- 在哪看: Google Quality Rater Guidelines + 自家内容 vs 竞品对比
- 输出: 4 维各 score (1-10) + 1 句最大瓶颈

#### 维度 2: 技术 SEO 健康度
- 看什么: Crawlability / Indexability / Core Web Vitals / Schema 4 件套
- 在哪看: GSC + Screaming Frog + PageSpeed Insights
- 输出: 4 维各通过率 + 高 / 中 / 低 优先级修复清单

#### 维度 3: 链接质量评估
- 看什么: 链接 DA / 主题相关性 / Anchor Text 多样性 / Toxic 比例
- 在哪看: Ahrefs / SEMrush / Moz 链接报告
- 输出: 链接质量分 + Disavow 建议 + Outreach 优先级

#### 维度 4: 关键词机会评估
- 看什么: KD / Search Volume / 当前排名 / 竞品分析
- 在哪看: Ahrefs / SEMrush + GSC
- 输出: 高 ROI 关键词清单 + 内容方向建议

#### 维度 5: AI Search 可见度 (GEO, 2024-2026)
- 看什么: AI Overviews / ChatGPT / Perplexity 引用频率 + 品牌 mention
- 在哪看: Otterly.ai / Profound / Peec AI
- 输出: AI Search 可见度 baseline + 优化建议 (内容结构 / 数据密度 / Schema)

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 People-first content > Search engine first content (核心 PASS)

**一句话**: Google 长期主线是「为用户写, 不为搜索引擎写」. 套路 6 个月一过期, 真实价值是长期资产.

(figures: John Mueller / Gary Illyes / Danny Sullivan / Brian Dean / Marie Haynes)

**它说的是**: Google Helpful Content System (2022 上线 → 2024 并入核心算法) 是个 site-wide signal. 几页垃圾页拖累整站. 真正能赢的 SEO 是「我能提供用户搜索时真正需要的答案」.

**证据来源**:
- [Primary] Google Search Quality Rater Guidelines 官方
- [Primary] John Mueller / Gary Illyes / Danny Sullivan 反复发声
- [Primary] Brian Dean Backlinko 长篇 (Skyscraper Technique 内核)
- [Primary] Marie Haynes E-E-A-T 周报
- [Primary] 2024-2025 多次 Core Update + Helpful Content Update 数据

**应用方式**:
- 内容首先解决用户问题, 再考虑关键词优化
- E-E-A-T 完整 (Experience / Expertise / Authoritativeness / Trust)
- 不要 AI 直发, 必须人工编辑 + 加真实经验
- 反对 Spam 套路 (链接农场 / 内容农场 / Doorway pages)

**局限**:
- 短期 ROI 慢 — 6-12 月才能看到效果
- 起点站 (新域名) DA 低, 内容再好也起量慢
- YMYL 类目 (健康 / 金融) 对 E-E-A-T 要求最高

---

### 1.2 Pillar + Cluster 内容架构 (核心 PASS)

**一句话**: Pillar (主题枢纽) + Cluster (长尾分支) 是中型品牌内容 SEO 的标准架构.

(figures: Brian Dean / HubSpot / Aleyda Solis / Surfer SEO)

**它说的是**: 不押单点关键词, 围绕主题做内容矩阵. Pillar 拿头部排名, Cluster 拿长尾流量. 内链双向, 锚文本自然多样化.

**证据来源**:
- [Primary] Brian Dean Backlinko 长篇
- [Primary] HubSpot Topic Cluster 方法论 (HubSpot 推全)
- [Primary] Surfer SEO / Clearscope 内容评分基于此
- [Primary] Aleyda Solis LearningSEO.io 课程

**应用方式**:
- 5-10 个 Pillar 主题词 (高搜索量 + 高难度)
- 每个 Pillar 20-30 个 Cluster 长尾词
- Pillar 3000-5000 词长内容
- Cluster 1500-2500 词内容, 内链回 Pillar
- 锚文本自然多样化 (不要 100% exact match)

**局限**:
- 中型 + 头部品牌路径, 个人站起步太重
- Pillar 选择错了整个矩阵就废了
- 实施周期长 (6-12 月)

---

### 1.3 链接质量 > 链接数量 (industry-amplified)

**一句话**: 10 个 DA 50+ 链接 > 100 个 DA 10 链接. 白帽路径, 不要走 spam.

(figures: Brian Dean / Ahrefs / Moz / SEMrush / Marie Haynes)

**它说的是**: Google 算法越来越能识别低质量链接. 链接农场 / 私域链接网络 / 买链接 一更新就团灭. Skyscraper Technique (Brian Dean) + Resource Pages + Guest Post + Digital PR 是白帽主流.

**证据来源**:
- [Primary] Brian Dean Skyscraper Technique 核心
- [Primary] Ahrefs / Moz / SEMrush 链接质量评估
- [Primary] Google Spam Update 历次清理
- [Primary] Marie Haynes 链接审计案例

**应用方式**:
- 链接质量评估: DA / 主题相关性 / Anchor Text 自然度
- Skyscraper Technique: 找最强对手内容 → 写更好版本 → outreach
- Disavow toxic links 季度审计
- 不买链接, 不用链接农场, 不刷 Anchor

**局限**:
- 高质量链接 outreach 转化率低 (5-10%)
- 链接建设周期长 (6-12 月)
- 中文 / 跨语言链接资源少

---

### 1.4 技术 SEO 是 baseline, 不是优势 (industry-amplified)

**一句话**: Core Web Vitals + Mobile + Schema + Crawlability 是「不做就死」, 但做好不一定就赢.

(figures: Aleyda Solis / Cyrus Shepard / Google / Screaming Frog)

**它说的是**: Aleyda Solis 反复强调 — 技术 SEO 是表演舞台的舞台, 没了它演员上不去, 但有了它演员还要演得好. 内容 + 链接才是真正决定排名.

**证据来源**:
- [Primary] Aleyda Solis Orainti 国际化 SEO 实战
- [Primary] Cyrus Shepard Title Tag 大型实验
- [Primary] Google Core Web Vitals 文档
- [Primary] Screaming Frog / Sitebulb 审计标准

**应用方式**:
- Core Web Vitals 三件套: LCP ≤ 2.5s / INP ≤ 200ms / CLS ≤ 0.1
- Mobile-friendly + responsive
- Schema markup (Article / Product / FAQ / Organization)
- Crawlability (robots.txt / sitemap / 内链)
- 国际化: hreflang / 多语言 / locale-specific URL

**局限**:
- 技术 SEO 投入有上限, 内容 + 链接才是 SEO 长期杠杆
- JS-heavy SPA 站点技术 SEO 复杂度高
- 跨平台 (Google / Bing / Baidu) 技术要求差异

---

### 1.5 AI Search 是 2024-2026 新战场 (industry-amplified)

**一句话**: 传统 SEO「rank and click」转向 AI Search「visibility and citations」 — 在 AI Overviews / ChatGPT / Perplexity 被引用比传统排名重要.

(figures: Position.Digital / SEOmator / Search Engine Land / Otterly.ai / Profound / Google AI Overviews)

**它说的是**: AI Overviews 已经覆盖 30% 美国桌面关键词, 26% 用户读完不点击. GEO (Generative Engine Optimization) / LLMO (LLM Optimization) 是新学科. 公司用 GEO 6-12 月看到 300-500% ROI.

**证据来源**:
- [Primary] Position.Digital / SEOmator AI SEO 统计 2026
- [Primary] Search Engine Land AI Search 长期跟踪
- [Primary] Otterly.ai / Profound / Peec AI 监控数据
- [Primary] Google AI Overviews 官方公告

**应用方式**:
- 内容结构化 (H2/H3 清晰, 类似 FAQ)
- 文章开头 1-2 段直接答案
- 数据 / 引用密度高 (LLM 偏好高密度内容)
- Schema markup 完整
- 跨平台一致性 (品牌信号一致)
- AI Search 监控接入 (Otterly / Profound)

**局限**:
- AI Search / GEO 是 2024-2026 新学科, 工具方法论 6-12 月迭代
- 76% AI Overviews 引用 URL 也排 Google top 10 → 传统 SEO 仍是基础
- 中文圈 AI Search 生态跟英文圈差异大

---



## 标准 Playbook

1. **如果做内容**, 则 People-first + E-E-A-T 三件套 (Experience / Expertise / Trust 重要), 不要为搜索引擎写.
   - 案例: Google Helpful Content Update 反复证明 — site-wide signal, 几页垃圾拖累整站.

2. **如果做内容架构**, 则 Pillar + Cluster (主题枢纽 + 长尾分支), 不押单点关键词.
   - 案例: Brian Dean Backlinko 长篇 + HubSpot Topic Cluster 方法论.

3. **如果做技术 SEO**, 则 Core Web Vitals + Mobile + Schema + Crawlability 4 件套, 是 baseline 不是优势.
   - 案例: Aleyda Solis Orainti 国际化 SEO 实战 + Google CWV 官方文档.

4. **如果做链接**, 则质量 > 数量 (10 个 DA 50+ > 100 个 DA 10), 白帽路径不走 spam.
   - 案例: Brian Dean Skyscraper Technique + Google Spam Update 历次清理.

5. **如果用 AI 内容**, 则人工编辑 + 加真实经验 + E-E-A-T 强化, 不要 AI 直发.
   - 案例: 2025-08 Helpful Content Update 大规模打击 AI 直发 + 行业 KOL 反复强调.

6. **如果做 AI Search 优化 (GEO)**, 则内容结构化 + 数据密度高 + Schema 完整.
   - 案例: 2024-2026 Position.Digital / SEO.com 数据 — GEO 6-12 月 300-500% ROI.

7. **如果监测排名**, 则 GSC 才是真实数据, 第三方工具 (Ahrefs / SEMrush / Moz) 是反推.
   - 案例: GSC 性能报告是 Google 给你的真实点击 / 展示 / 平均位置.

8. **如果做国际化 SEO**, 则 hreflang + 多语言版本 + 文化适配 + locale-specific URL.
   - 案例: Aleyda Solis Orainti 服务 20+ 国家客户经验.

9. **如果遇到流量异常**, 则先看是否 Core Update / Helpful Content Update 影响, 再做技术审计.
   - 案例: Search Engine Roundtable (Barry Schwartz) 长期算法更新追踪.

---



## 工具栈与选型决策树

详见 `references/research/02-tools.md`. 三层结构:

- **必备 (5 个)**: GSC + GA4 + Ahrefs / SEMrush / Moz Pro 选 1 + Screaming Frog
- **场景特化 (8 个)**: Sitebulb / Sistrix / Surfer SEO / Clearscope / Frase / Schema.org / PageSpeed / 中文工具
- **新兴 (6 个)**: AI Search 监控 (Otterly / Profound / Peec) / ChatGPT / Jasper / Ubersuggest / AnswerThePublic

按场景选: 个人博客 → GSC + Ubersuggest 免费 / 中小企业 → 加 Moz / Surfer / 中大企业 → Ahrefs + 全套 / 头部 → 全套 + AI Search 监控

---



## 工作流 / Pipeline

详见 `references/research/03-workflows.md`. 5 个标准工作流:

- **新站 SEO 上线** (medium decay, 90 天打基线)
- **内容 SEO 生产** (low decay, Pillar + Cluster)
- **技术 SEO 审计** (medium decay, 季度)
- **链接建设** (medium decay, 6-12 月长期)
- **AI Search 优化 (GEO)** (high decay, 2024-2026 新流派)

典型路径:
- 新独立站: workflow 1 → workflow 2 → workflow 3 (季度)
- 中型品牌: workflow 1-3 + workflow 4 (链接长期)
- 头部品牌 / 2026+: workflow 1-5 全闭环

---



## 表达 DNA

### 高频术语
- E-E-A-T / YMYL / Helpful Content / Core Web Vitals
- Pillar / Cluster / Topical authority / Long-tail
- DA / PA / Backlink / Anchor / Skyscraper
- GSC / GA4 / Ahrefs / SEMrush / Moz / Screaming Frog
- AI Overviews / GEO / LLMO / Perplexity

### 严肃 register
- 数据驱动 + 长期主义 + 白帽路径
- 反对 spam / 反对 AI 直发 / 反对短平快
- 跨平台 + 跨语言视角

### 外行破绽
- 把「DA」当 Google 指标 (实际 Moz 指标)
- 不知道 E-E-A-T (Trust 最重要)
- 把 SEO 跟 SEM 混着叫
- 不知道 GEO / LLMO 是 2024-2026 新流派
- 用 nofollow 当 noindex
- 把 robots.txt 当 noindex 替代品

---



## 质量基准 + 反模式

### 什么算「好」 (4 个标准):

1. GSC 自然流量 6-12 月持续上升
2. Core Web Vitals 三件套全过 (LCP / INP / CLS)
3. 头部关键词进入 Google top 10
4. AI Overviews 引用 + Perplexity / ChatGPT mention (2024-2026)

### 反模式 (8 个常见错):

1. AI 直发不加人工 → Helpful Content 限流
2. 买链接 / 链接农场 → Spam Update 团灭
3. 单点关键词押宝 → Pillar + Cluster 架构没搭
4. Core Web Vitals 没过 → 排名上不去
5. 锚文本 100% exact match → 算法识别 spam
6. 不接入 GSC → 没法看 Google 真实数据
7. 内容更新周期 > 12 月不动 → 内容衰减
8. 跨语言用 Google Translate 直接翻 → hreflang 用错 → 国际化 SEO 失败

---



## 智识谱系

### 主要流派

| 流派 | 代表 | 立场 |
|------|------|------|
| Content-driven | Brian Dean / Neil Patel | 内容 + 链接 + 用户体验 |
| Technical SEO | Aleyda Solis / Cyrus Shepard | Core Web Vitals / Schema / 国际化 |
| Authority / E-E-A-T | Marie Haynes / Lily Ray | 作者权威 / 真实经验 |
| AI Search / GEO | 新流派 (2024-2026) | AI Overview / ChatGPT / Perplexity 引用 |
| Black-hat (淘汰中) | (匿名) | 链接农场 / 内容农场 |

### 关键分歧
- **Content vs Technical** — 决定团队配置
- **Traditional Rank vs AI Citation** — 决定 2026+ 策略
- **White-hat vs Black-hat** — 决定长期可持续性

### Sub-skills (女娲蒸馏的 top figures)
- Brian Dean (Backlinko) — Content-driven 派
- Aleyda Solis (Orainti / SEOFOMO) — Technical + 国际化派
- Rand Fishkin (Moz / SparkToro) — 长期主义 + 跨平台视野

---



## 诚实边界

1. **信息截止 2026-05-02**. Google 算法 / AI Search 工具方法论每 3-6 月需 update.

2. **AI Search / GEO 是新学科**. 2024-2026 才有, 工具方法论 6-12 月迭代, 跟最快.

3. **Google 官方信源是政策宣示**, 实际算法变化更快.

4. **第三方工具数据是反推**, GSC 才是 Google 给你的真实数据.

5. **中文 SEO 跟西方 SEO 生态差异大**. 百度跟 Google 不同, 跨境品牌需要双轨.

6. **YMYL 类目 (健康 / 金融 / 法律) 对 E-E-A-T 要求最高**. 强监管行业 (医疗 / 法律) 需独立合规审查.

7. **黑帽 SEO 短期暴利但一更新就团灭**. 本 prototype 不教 spam 套路.

8. **2026-2027 政策窗口高度不确定**. AI Overviews / SearchGPT / Perplexity 让传统 SEO 流量结构发生巨变.

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-03 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-03 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-03 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-03 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-03 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-03 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-03 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-03 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-03 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
