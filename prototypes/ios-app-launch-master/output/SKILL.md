---
name: ios-app-launch-master
description: |
  iOS 应用上架大师 (审核 + ASO + 合规 + 国内/海外多区 + 付费策略) (iOS App Store launch — submission, review, ASO, compliance, post-launch monetization) Master OS — automated mastery of iOS App Store launch — submission, review, ASO, compliance, post-launch monetization: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on iOS App Store launch — submission, review, ASO, compliance, post-launch monetization problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「iOS 上架」「App Store 上架」「App 审核」「App Review」「TestFlight」
triggers:
  - "iOS 上架"
  - "App Store 上架"
  - "App 审核"
  - "App Review"
  - "TestFlight"
  - "App Store Connect"
  - "ASO"
  - "审核被拒"
  - "rejection"
  - "App Review Guidelines"
  - "iOS 隐私"
  - "ATT"
  - "App Tracking Transparency"
  - "应用上架"
  - "iOS 发布"
  - "上架大师"
industry: "iOS App Store launch — submission, review, ASO, compliance, post-launch monetization"
industry-cn: "iOS 应用上架大师 (审核 + ASO + 合规 + 国内/海外多区 + 付费策略)"
locale: "global"
last_research_date: "2026-05-10"
source_count: 169
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# iOS 应用上架大师 (审核 + ASO + 合规 + 国内/海外多区 + 付费策略) · Master OS

> This skill makes the agent operate as a senior iOS App Store launch — submission, review, ASO, compliance, post-launch monetization practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 iOS App Store launch — submission, review, ASO, compliance, post-launch monetization 相关的问题时（关键词：iOS 上架, App Store 上架, App 审核, App Review, TestFlight, App Store Connect, ASO, 审核被拒, rejection, App Review Guidelines, iOS 隐私, ATT, App Tracking Transparency, 应用上架, iOS 发布, 上架大师），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 iOS App Store launch — submission, review, ASO, compliance, post-launch monetization 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：iOS App Store launch — submission, review, ASO, compliance, post-launch monetization 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 学派语境 (用户在 6 派哪派)
- 看什么: 用户用什么术语. 判断他在 Apple 官方派 / 海外 Indie / 大厂 release eng / ASO 优化派 / 反 Apple 反垄断 / 国内合规 哪派. 决定 §2 决策规则的应用版本
- 在哪看: 看用户原话关键词. 例: "ARG 5.1.1 条款" → Apple 派; "我又被拒了" / "ATP 提到" → Indie 派; "CPP A/B / keyword 排名" → ASO 派; "30% Tax / DMA" → 反 Apple 派; "ICP 备案 / 算法备案 / 8 大市场" → 国内合规派
- 输出: 一行学派标签 (e.g. "用户在 Indie 派, 最相关心智模型 1.6 拒绝是日常 + 决策规则 D2 Resolution Center 短回复")

#### 维度 2: stage 边界 (0→1 上架 vs 已运营 vs scale-up)
- 看什么: 用户处于什么阶段. 0→1 第一次上架 / 已上架持续运营 / scale-up 多区扩展 / 拒审救火 / 政策适配
- 在哪看: 用户问题的具体动作 (e.g. "我准备提审" → 0→1; "我又被拒了" → 拒审救火; "扩到 EU 还是 CN" → 多区扩展; "Privacy Manifest 怎么搞" → 政策适配)
- 输出: stage 标签 + 适用决策规则号 (e.g. "stage = 拒审救火, 走 D2 + W2 工作流")

#### 维度 3: 区域语境 (US / EU / CN / 多区)
- 看什么: 用户上架的目标区域. US 默认 Apple 单家 / EU DMA 后允许 link-out + sideloading / CN 4 件套 (ICP + 算法备案 + 游戏版号 + 8-10 应用市场) / 多区策略
- 在哪看: 用户原话区域线索 (e.g. "在国内上架" → CN; "Lemon Squeezy" → 海外 indie; "DMA 后" → EU; "多区策略" → 多区)
- 输出: 区域 + 必应 obligations (e.g. "区域 = CN, 必应 D5 + D7 + D8 国内 4 件套, 不能抄海外 link-out")

#### 维度 4: 时效新鲜度 (12 月内 vs 老攻略)
- 看什么: 用户依赖的政策 / 工具 / 数字是不是 12 月内的. iOS 政策高频变化 (年度 WWDC + 季度 ASC + iOS major). 老的需先 D3 复盘
- 在哪看: 用户引用的 deadline / 规则 / 工具版本. 例: "Privacy Manifest 强制 2024-05-01" / "iOS 26 SDK 2026-04-28" / "Age Rating 5 档 2026-01-31" / "DMA 2024-03-07" 都是 12 月内强制
- 输出: 时效标签 (新鲜 / 12 月内 / 老攻略需复盘) + 强制 deadline 提醒

#### 维度 5: 学派分歧识别 (6 派会怎么各自答)
- 看什么: 同一问题 6 派会怎么各自答. 揭示分歧根源是学派身份 (Apple 派 vs 反 Apple) / GTM 哲学 (Indie audience-first vs ASO 数据驱动) / 区域 (海外 vs 国内) 而非 "对错"
- 在哪看: §7 智识谱系 6 派对照矩阵 + §1.4 / 1.5 / 1.6 跨派 mental model
- 输出: 列出 2-3 派的不同 take, 标"分歧根源 = X". 用户自己看选哪派, 不强加

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 Apple App Review 是黑盒 — 治理"概率", 不是"通过保证"

**核心**: Apple 不公开拒绝率 (业内估 20-40%). 不存在"保过审"的人或方法. 任何"代过审" / "保证通过审核" 都是骗子. 资深 dev 治理的是**降低拒绝率 + 拒绝时快速恢复**, 而不是"保证一次过".

- **流派归属**: 跨派必修 (5 派全部认同, 反 Apple 派 + 大厂派最强烈)
- **衍生用途**: §2 D1 (拒绝处理决策树) + §4 W2 工作流
- **局限**: Apple 偶有"特殊渠道"(大客户 Account Manager + WWDC 私下 alignment), 但对 indie 不开放
- **evidence**: [T01-S001, T01-S016, T04-S001, T03-S005, T06-S001]

### 1.2 双合规体系不可一刀切 (海外 Apple 单家 vs 国内多重备案)

**核心**: 海外只 Apple 一家审核, 国内是 Apple + ICP (工信部) + 算法备案 (网信办) + 游戏版号 (出版署, 仅游戏) + 8-10 个国内应用市场各自审核. 流程 / 时间 / 成本完全不同. 抄海外路径做大陆 = 死. 反例: link-out (DMA EU 后允许) 国内不允许.

- **流派归属**: 国内合规派 vs 海外 indie / 大厂 / 反 Apple — 主要分歧轴
- **衍生用途**: §2 D5 (多区策略) + §4 W5 国内合规 W6 多区上架
- **局限**: 国内出海团队需双栈, 不能省任何一边. 海外团队 + 国内 ICP 通常需要本地法人 (个体/外资公司)
- **evidence**: [T06-S004, T06-S006, T06-S008, T03-S009, T04-S015]

### 1.3 政策时效衰减极快 (12 月不 update = 下架风险)

**核心**: Apple 政策年度大改 (WWDC 6 月) + 季度小改 (ASC monthly notes) + 强制日期 (Privacy Manifest 2024-05-01 / Anti-steering 2024-01 / DMA 2024-03-07 / iOS 26 SDK 2026-04-28 强制). 12 月不更新 = 政策变化 → app 下架. 这条是 ios-app-launch 跟传统软件最大区分.

- **流派归属**: 跨派. Apple 官方派最强 (Apple 自己 push), 大厂派次之 (有 release schedule), indie 派最弱 (常忽视).
- **衍生用途**: §2 D8 (政策跟踪节奏) + §4 W8 持续维护
- **局限**: 经典 SaaS 不存在这条 — 第三方平台没有 Apple 强制日期式约束
- **evidence**: [T06-S003, T06-S008, T03-S010, T04-S002, T01-S004]

### 1.4 ASO 数据驱动 vs Indie audience-first (流派 GTM 分歧)

**核心**: 同一个上架后增长问题, ASO 派 (Sensor Tower / Mobile Action / Eric Seufert / Thomas Petit) 主张系统化数据 (keyword / screenshot A/B / install volume) 驱动. Indie 派 (Marco Arment / David Smith / Federico Viticci) 主张 audience-first (Twitter / blog / podcast 累积关系) 驱动. 都对, 但完全不同 commercial OS.

- **流派归属**: ASO 优化派 vs 海外 Indie 派 — GTM 哲学分歧
- **衍生用途**: §2 D4 (ASO 决策) + §4 W3 工作流
- **局限**: ASO 派需要预算 (Sensor Tower 等数据工具不便宜); Indie 派需要预先 audience (Pieter Levels 模式 12 年累积才行)
- **evidence**: [T01-S005, T01-S006, T01-S007, T01-S010, T05-S007, T05-S009]

### 1.5 30% Apple Tax 是事实, 不是争议 (反 Apple 派 vs 接受派)

**核心**: 30% (small biz 15%, subscription 第二年 15%) 是事实约束, 不是"应该不应该". 反 Apple 派 (Sweeney / Spotify / DHH) 公开战这是商业哲学 + 反垄断诉讼策略, 但单个 dev "我不交 30%" 不是选项 — 要么接受 + 在 IAP 内成功, 要么走 reader app / 商业模型外置 (web subscription) / 反例 link-out (EU DMA 后)). Day 0 Paywall 反例就是没接受这个事实.

- **流派归属**: Apple 派 + Indie 派 (接受) vs 反 Apple 派 (公开战) — 商业模型分歧
- **衍生用途**: §2 D6 (商业模型 / 定价) + §4 W7 订阅付费
- **局限**: EU DMA 2024-03 后允许 link-out (Apple 同时收 0.50€ Core Technology Fee), 大陆完全不允许. 这条规则在演化
- **evidence**: [T06-S007, T06-S009, T04-S012, T04-S013, T01-S013, T01-S015]

### 1.6 拒绝是日常, 不是失败 (rejection 救火心态)

**核心**: 资深 dev 把 rejection 当 "和 Apple 沟通的一种 channel". Resolution Center 短 + 具体 + 引 ARG 条款号 通常 24-48h 解决. Expedited Review (限频, 关键发布前救命). 反例: 第一次 rejection 就 panic, 公开 Twitter 发疯 (除非是 DHH/Sweeney 级别有反 Apple 战略). 95% rejection 是 metadata + 隐私披露错, 改了重传即可.

- **流派归属**: 跨派必修. Indie 派最常见单 dev 处理, 大厂有专门 release engineering team.
- **衍生用途**: §2 D2 (rejection 处理) + §4 W2 工作流
- **局限**: 部分 rejection 是 functional (4.x Design / 2.x Performance), 这些需要重做产品, 不只是改 metadata
- **evidence**: [T01-S001, T01-S016, T03-S004, T04-S001, T06-S015]

---



## 标准 Playbook

1. **D1 — 拒绝率治理: 降低拒绝率 + 快速恢复**

- **trigger**: 准备首次提审 / app 重大版本
- **decision**: pre-submit checklist (HIG 自检 + Privacy Manifest + nutrition labels + ARG 5.x 国别 ATT 对照) → 提审 → 拒绝 24-48h Resolution Center 修复 → 重提
- **关键**: 不期望"一次过", 期望"快速恢复". 关键发布期保留 Expedited Review quota
- **学派对照**: indie (单人 1-3 周完成) / 大厂 (release engineering team + Bitrise + Fastlane) / 国内出海 (双栈 + ICP 备案先行)
- **案例**: Hey vs Apple 公开战 (DHH 反 IAP 强制) — 是商业战略不是常规处理. 99% rejection 应私下 Resolution Center 解决, 不公开战
- **evidence**: [T01-S001, T01-S013, T03-S004, T04-S001]

2. **D2 — Rejection 处理: Resolution Center 短/具体/引 ARG**

- **trigger**: 收到 Apple 拒绝信
- **decision**: 不 panic. 短回复 (50-200 字) + 具体修改 + 引 ARG 条款号 (e.g. "已按 ARG 5.1.1(v) 修改隐私描述"). 24-48h 通常解决.
- **学派对照**: indie 直接 Resolution Center / 大厂 通过 Apple Developer Account Manager / 国内 5.6 China Mainland 行政申诉路径
- **案例**: Marco Arment 在 ATP podcast 多次提到 "rejection 是 Apple 的一种通信方式, 不是审判" (T01-S001 ATP); Spotify 反 anti-steering 通过 EU DMA 立法不是 Resolution Center
- **evidence**: [T01-S001, T01-S013, T03-S004, T04-S001]

3. **D3 — 政策时效跟踪节奏**

- **trigger**: 持续运营 + WWDC / iOS major / ASC 更新
- **decision**: 每年 6 月 WWDC 必看 "What's New in App Review" + "What's New in App Store Connect"; 9 月 iOS major 前 30 天必跑兼容性 test; ASC 月度更新邮件订阅; ARG 关键变化 (ATT / Privacy Manifest / Anti-steering / DMA / Age Rating) 12 月内必适配
- **学派对照**: Apple 派 (强制 deadlines, 不 compromise) vs Indie (常 12 月内才适应, 反例 12 月不更新 → 下架风险)
- **案例**: Privacy Manifest 2024-05-01 强制后 Q1 2025 多数 indie app 因 SDK 漏 Privacy Manifest 被拒 (12% Q1 2025 拒审率, T03-S006); iOS 26 SDK 2026-04-28 强制提审 — 没适配 = 提审失败
- **evidence**: [T06-S003, T06-S008, T03-S010, T04-S002]

4. **D4 — ASO 优化: 数据驱动 vs Audience 驱动**

- **trigger**: 上架后 30-90 天 + 持续 iterate
- **decision tree**:
  - 有预算 + 主流类目 → ASO 派路径: Sensor Tower + keyword optimization + screenshot A/B (Custom Product Pages 35→70 槽位, 2026-Q1 扩) + Apple Search Ads
  - 无预算 + niche → Indie 路径: Twitter/X build-in-public + podcast (ATP / Under the Radar) + 长博客 audience-first
  - 国内出海 → 双栈: 海外 ASO + 七麦/鸟哥笔记国内
- **关键反例**: 把 ASO + audience 混打 (没 ASO 预算的 indie 强行做 ASO 派 = 钱进黑洞; 没 audience 的大厂团队学 indie audience-first = 6 月白干)
- **案例**: Pieter Levels Photo AI 100% audience (12 年 Twitter 累积); Sensor Tower / data.ai 客户 Day 1 数据驱动. 都赚钱, 不混合
- **evidence**: [T01-S005, T01-S006, T01-S010, T05-S007, T05-S009, T03-S005]

5. **D5 — 多区策略: US / EU / CN**

- **trigger**: 决定上架哪些地区
- **decision**:
  - 美区: 默认必上, 流程标准 (Apple 单家)
  - EU: DMA 2024-03 后允许 link-out + 第三方 marketplace + 0.50€/install Core Technology Fee (CTF). 不一定要利用 — 看商业模型
  - 中国: ICP 备案 (工信部) + 算法备案 (网信办, 推荐 / 生成式 AI 强制) + 游戏版号 (仅游戏) + 国内 8-10 应用市场各自审核. 流程 4-12 周, 需本地法人. 不要抄海外做大陆.
  - 其他亚太 (日本 / 韩国 / 印度) / 拉美: 通常 Apple 单家审核, 有 5.7 韩国 / 5.8 印度 等专属条款
- **关键**: 国内 vs 海外不是"翻译"问题, 是不同合规体系
- **学派对照**: indie 通常只做美区 + 自己国家 / 大厂跨区策略 / 出海团队跨大陆海外双栈
- **案例**: 国内 SaaS 出海到美区简单 (Apple 单家); 海外 SaaS 进国区难 (ICP 备案 + 算法备案 + 国内市场 8-10 家) 通常需要找本地代运营
- **evidence**: [T06-S004, T06-S006, T06-S008, T03-S009]

6. **D6 — 商业模型: 接受 30% Tax + IAP 内优化, 不抗议**

- **trigger**: 决定 monetize 路径
- **decision**:
  - 接受 30% Tax (small biz 15%, subscription 第二年 15%) 是事实约束
  - IAP 内优化 (StoreKit 2 + paywall A/B 用 RevenueCat / Adapty / Superwall) — 单 dev 默认路径
  - 商业模型外置 (web subscription, 用户在 web 注册付费, app 仅 login): 合法但需 careful (反 anti-steering 案后 app 内 link-out 美区 2025-04 起允许, EU DMA 完全允许, 大陆完全不允许)
  - Reader Apps 例外 (3.1.3a, e.g. Spotify, 仅"读"内容应用, 允许 web 付费 + app 内消费, 但需明确 Reader 类目)
  - 反例: Day 0 Paywall (新 dev 第一天就强收, 反垄断派抗议 30% 但作为 indie 抗议 = 没 ship; 接受是务实)
- **学派对照**: Apple 派 (接受 + 优化 IAP) / Indie (默认接受) / 反 Apple (Sweeney/Spotify/DHH 战略性抗议, 普通 dev 不学) / 国内 (微信支付 替代 IAP, 但仅限非 IAP 类目)
- **案例**: RevenueCat State of Subs 2026 (T05-S009): hard paywall 转化率 10.7% vs freemium 2.1% — 但需要在已有 audience / 高质量 app 前提下. Day 0 hard paywall 没 audience = 失败
- **evidence**: [T06-S007, T06-S009, T04-S012, T01-S013, T01-S015, T05-S009]

7. **D7 — 隐私合规: ATT + Privacy Manifest + GDPR 三件套**

- **trigger**: 提审 / 持续运营
- **decision**:
  - **ATT (App Tracking Transparency, 2021-04-26)**: opt-in tracking. iOS 14.5+ 强制 prompt. 25% 用户 opt-in (业内估计). SKAdNetwork (SKAN 4.0) 是替代方案
  - **Privacy Manifest (2024-05-01 强制)**: .privacy 文件描述 SDK 数据访问. 漏 SDK 一个 = 拒审. iOS dev 主要痛点
  - **GDPR (EU 2018+)**: consent banner / data subject rights / 数据 erasure
  - **CCPA / CPRA (California)**: opt-out / "Do Not Sell"
  - **COPPA (儿童 ≤ 13, 美国)**: special handling
  - **国内 PIPL (2021)**: 个人信息保护法, 中文协议 + 详细数据收集说明
- **学派对照**: Apple 派 / Indie 派 (常漏 Privacy Manifest 一个 SDK) / 大厂派 (OneTrust / 法务部门 全套) / 反 Apple (DHH 抗议 ATT 但仍要遵守) / 国内合规 (PIPL + 等保)
- **案例**: 2024-05-01 Privacy Manifest 强制后 12% Q1 2025 拒审是 Privacy Manifest SDK 漏 (T03-S006). Marco Overcast 提前 6 月开始 audit 第三方 SDK
- **evidence**: [T06-S001, T06-S002, T06-S008, T03-S007, T04-S008]

8. **D8 — 国内合规 4 件套 (大陆出海 / 国内市场)**

- **trigger**: 上架国区 / 国内多市场
- **decision** (按时间顺序):
  - **第 1 步 ICP 备案** (工信部 beian.miit.gov.cn): App Store 国区 2024-04 起强制. 个人 / 公司主体, 4-8 周. 没备案号 = 国区下架
  - **第 2 步 算法备案** (网信办 beian.cac.gov.cn): 涉及推荐算法 / 生成式 AI 强制 (2022-, 2026-Q1 累计 800+). 4-12 周
  - **第 3 步 游戏版号** (出版署 nppa.gov.cn, 仅游戏): 极严, 6 月-2 年, 不保过. 国内最大 bottleneck
  - **第 4 步 国内应用市场审核** (华为 AppGallery / 小米 / OPPO / vivo / 应用宝 (腾讯) / 360 / 百度): 各自后台 + 各自标准, 通常比 Apple 严格 (内容审核更严)
  - **第 5 步 隐私协议** (中文 + 详细数据收集) + **PIPL** + **等保** (大型 app 2/3 级)
- **学派对照**: 国内合规派 (鸟哥笔记 / 七麦 / 硬地骇客嘉宾) 主流操作 / 海外派 (大多忽视 — 直到必须做国区)
- **案例**: 国内出海 dev 通常 ICP 在公司主体下 (个人主体限制多), 算法备案 2025-2026 持续收紧 (网信办年度报告)
- **evidence**: [T06-S004, T06-S006, T06-S008, T04-S015, T03-S009]

9. **D9 — 工具栈选择: stage-appropriate**

- **trigger**: 选 build / ASO / 隐私 / 订阅 工具
- **decision**:
  - **必备 (跨 stage)**: Apple 三件套 (Xcode + ASC + TestFlight), Apple Developer Program ($99/yr), Privacy Manifest (2024+), Apple Search Ads (有预算时)
  - **Indie 海外 solo**: + Fastlane (build automation) + RevenueCat (subscription) + AppFollow (评论/ASO 入门免费)
  - **大厂 / scale-up**: + Bitrise (CI/CD) / Xcode Cloud (Apple 官方) + Sensor Tower / data.ai (ASO 数据) + AppsFlyer / Adjust / Branch (归因) + OneTrust (隐私) + Mixpanel (分析)
  - **国内出海**: + 七麦 (双端 ASO 数据) + 备案易 (备案辅助) + 国内多市场后台 (华为 / 小米 / OPPO 等手动)
  - **ASO 顾问**: + Sensor Tower + data.ai + Mobile Action + AppFollow + AppLaunchpad (screenshot 制作)
- **关键反例**: 选错 stage 工具 (indie 上 Sensor Tower 高价 = 钱进黑洞; 大厂还在 manual ASO = scale 时崩)
- **decay**: AppsFlyer / Adjust 在 ATT 后受冲击; Adapty / Superwall 在抢 RevenueCat paywall 中端市场 (18-24 月主流化)
- **案例**: Marco Overcast 单 dev 用 Apple 三件套 + Fastlane + RevenueCat; Stripe iOS 用 Bitrise + Sensor Tower + OneTrust 全栈 (T02-S001 + T02-S013 选型对照)
- **evidence**: [T02-S001, T02-S006, T02-S010, T02-S013, T02-S017, T02-S023]

10. **D10 — 持续维护节奏: 12 月内必 update**

- **trigger**: app 上架后持续运营
- **decision**:
  - 6 月 WWDC: 必看 "What's New in App Review" + "What's New in App Store Connect"
  - 9 月 iOS major: 提前 30 天兼容性 test + Privacy / nutrition labels review
  - 月度: ASC release notes 邮件 + ARG diff watch
  - 季度: 自家 app metrics review (crash / rating / keyword rank)
  - 强制 deadline: ATT (2021-04) / Privacy Manifest (2024-05-01) / Anti-steering (2024-01) / DMA (2024-03-07) / iOS 26 SDK (2026-04-28) / EU CTC (2026-01) / Age Rating 5 档 (2026-01-31)
- **关键**: 12 月不更新 = 政策变化 → app 下架 (反例)
- **学派对照**: Apple 派 (deadline 强 push) / 大厂派 (有 release schedule) / Indie 派 (常忽视, 反例) / 国内合规 (备案续期)
- **案例**: 2024-05-01 Privacy Manifest 强制后 12% Q1 2025 拒审是 indie 没 update 第三方 SDK
- **evidence**: [T06-S003, T06-S008, T03-S010, T04-S002]

---



## 工具栈与选型决策树

### 3.1 Apple 官方核心 cluster (跨 stage 必备, 永恒度高)

- **必备**: Xcode (开发 + 提审 IDE) + App Store Connect (ASC, 提审 dashboard) + TestFlight (官方 beta) + Apple Developer Program ($99/yr) + Privacy Manifest (2024+ 强制 .privacy 文件)
- **场景**: App Store Connect API (自动化 metadata) + Apple Search Ads (ASA, 关键词广告, 多广告位 2026-03-17 扩) + Custom Product Pages (CPP, 35→70 槽位 2026-Q1)
- **decay**: Apple 官方栈本身永恒, 但具体功能 (Bitcode deprecated 2022 / SKAN 4.0 持续演化) 会变

### 3.2 Indie / 出海 cluster (海外 dev / 国内出海 都默认)

- **必备**: Fastlane (build automation, ruby-based, indie 默认) + RevenueCat (subscription infra, indie 默认) + AppFollow (评论 + ASO 入门 free tier) + Sentry / Firebase Crashlytics (crash, 免费 tier)
- **场景**: Bitrise (mobile-friendly CI/CD) / Xcode Cloud (Apple 官方 CI) + Mobile Action / data.ai (ASO 中端) + Adapty / Superwall (paywall A/B, 18-24 月主流)
- **学派对应**: Marco Arment / David Smith / 海外 indie 默认; 国内出海 + 7 麦/鸟哥笔记 国内补充

### 3.3 国内 + ASO 高端 cluster

- **国内出海**: 七麦数据 (双端 ASO + ICP 备案查询) + 鸟哥笔记 (ASO 教育) + 备案易 (ICP 备案辅助) + 国内多市场后台 (华为 AppGallery / 小米 / OPPO / vivo / 应用宝 / 360 / 百度)
- **ASO 高端 (大厂 / 顾问)**: Sensor Tower (高价 ASO 数据) + AppsFlyer / Adjust / Branch (归因, ATT 后部分功能受限) + OneTrust (隐私 / GDPR / CCPA 合规)
- **关键避坑**:
  - **Privacy Manifest** (2024-05-01 强制) — 漏一个 SDK 直接拒审
  - **ICP 备案** (国区 2024-04 强制) — 没备案 = 下架
  - 选错 stage 工具 (indie 上 Sensor Tower 高价)
  - AppsFlyer 等归因工具在 ATT 后部分功能受限

(完整 26 工具 + 5 决策树见 02-tools.md)

---



## 工作流 / Pipeline

(完整 8 个 workflow + 学派分歧 + 失败模式 / 衰减点见 03-workflows.md)

### W1 上架 0 → 1 主流程 (8 步 SOP)

**Trigger**: 决定做 iOS app + Apple Developer 注册. **Output**: ASC = "Ready for Sale" + 真可下载 link.

1. **Apple Developer 注册** ($99/yr 个人 / 公司主体, 1-3 工作日 D-U-N-S 验证. 注: $299/yr Apple Developer Enterprise Program 是给内部分发的, **不能上 App Store**, 别混淆). 跳 → 无 ship 资格
2. **Xcode 项目配置**: Bundle ID + Provisioning Profile + Distribution Certificate + Capabilities. **iOS 26 SDK + Xcode 26 强制 2026-04-28**
3. **ASC App 创建 + Metadata**: name (30 字) + subtitle (30) + keyword (100) + description + nutrition labels + age rating (**2026-01-31 起新 5 档 4+/9+/13+/16+/18+ 强制**) + Pricing. 跳任一字段 → metadata reject. ARG 2.1 (Information Needed / 资料不完整) 是常见 reject 类目之一 (Apple 不公开具体百分比, 业内观察是 metadata 不完整 ≥ 隐私披露 不一致)
4. **Privacy Manifest + 三方 SDK**: 2024-05-01 强制 + 2025-02-12 起 SDK signed 强制. **Q1 2025 Capgo 第三方数据观察 ~12% 拒审是 Privacy Manifest 违规** (非 Apple 官方公开, 业内估计). 跳 → ITMS-91061/91065 直接拒
5. **Archive & Upload**: Xcode Organizer / Fastlane (`gym` + `pilot`). 跳 Validate App → 浪费 1 review cycle
6. **TestFlight Beta**: 100 internal 无审 / 10000 external **第一版必走 Beta App Review 24-48h**. 跳 → 直接 App Review 踩 crash 1-2 周回炉
7. **App Review 提审**: **Apple 官方公开 90% < 24h** (developer.apple.com/app-store/review/), 48h 数字 Apple 未公开 (业内估 ≥ 95% 但需 self-verify). 首次 + 复杂 case 仍可能 1-2 周. Expedited Review 限频 (~2 次/年, 关键发布前救命)
8. **Release**: Manual / Automatic / Phased Release (7 天 1/2/5/10/20/50/100%, 可暂停 ≤30 天但**不能回滚**)

**资深差异 (skip / optimize / add)**:
- *skip*: 海外 indie (Marco/Smith) 跳 ASA 启动 + ASO 顾问, 1.0 靠编辑推荐 + community shoutout
- *optimize*: 大厂优化为 Fastlane + Bitrise/GHA mac runner + ASC API 全自动; indie 优化为 Xcode Organizer 手提 + 关键词预研 4-6 周前 (name+subtitle+100 字占搜索权重 ≈70%)
- *add*: 资深 add 4 件**额外**步骤 — (a) 下架预演 build < 2h 可重传 (b) 法律审 ARG 用自家 app 对照 5.x 国别条款 (Marco DNA) (c) 关键词预研 4-6 周前 (d) 三方 SDK Privacy Manifest 提前 1 周对账 (30+ SDK 缺 1 拒)

**学派 DNA**: 海外 indie 1-2 人 1-3 周 (Fastlane + RevenueCat + AppFollow free, 跳 CI/CD); 大厂 5-15 人 + release manager 专职 + Bitrise/Xcode Cloud + ASC API 全自动; 国内出海 海外栈 + 七麦 + 国内多市场并行, **备案前置 W5** (没跑通 ICP 不能提国区)

**典型耗时**: 入门 1-3 周 / 资深 3-5 天. **关键失败模式**: Bundle ID 改 = 新 app / Privacy Manifest 漏 SDK / TF 公链当 production / metadata reject 后重传 binary / 首次 external TF 提前 < 1 天

(详见 03-workflows.md W1 完整版)

### W2 Rejection 救火

Resolution Center 短/具体/引 ARG 条款号 (50-200 字, e.g. "已按 ARG 5.1.1(v) 修改隐私描述"). **95% rejection 是 metadata + 隐私披露错**, 改了重传即可. Expedited Review 限频, 关键发布前救命. 学派分歧: indie 公开战 (DHH/Marco) vs 大厂私下 Apple Account Manager vs 国内 5.6 China Mainland 行政申诉.

**资深差异**: *skip*: 老 dev 跳"先 panic 公开吐槽"直接读 ARG 找条款; *optimize*: 大厂 release engineering 优化为 template 化 Resolution 回复 + Apple AM 私下渠道; *add*: 资深 add 自家 ARG 对照 spreadsheet (Marco DNA) + Expedited Review 节奏管理 (~2 次/年额外配额).

### W5 国内合规 4 件套 (大陆出海 / 国内市场)

**第 1 步 ICP 备案** (工信部 beian.miit.gov.cn) — App Store 国区 2024-04 起强制. 个人 / 公司主体, 4-8 周. 没备案号 = 国区下架.
**第 2 步 算法备案** (网信办 beian.cac.gov.cn) — 涉及推荐算法 / 生成式 AI 强制 (2022-, 2026-Q1 累计 800+). 4-12 周.
**第 3 步 游戏版号** (出版署 nppa.gov.cn, 仅游戏) — 极严, 6 月-2 年, 不保过.
**第 4 步 国内应用市场审核** — 华为 / 小米 / OPPO / vivo / 应用宝 / 360 / 百度 各自后台 + 各自标准, 通常比 Apple 更严内容审核.

跟海外完全不同体系. 4-12 周整体. 抄海外路径做大陆 = 死.

**资深差异**: *skip*: 海外 indie 跳整个 W5 (不上国区即可, 失国内市场份额); *optimize*: 国内出海 dev 优化为 4 件套并行启动 + 海外栈 备案前置; *add*: 资深 add 国内代运营 + 多市场 metadata diff (8-10 市场各自审核标准, 不能一套 metadata 应对全部) 额外配置.

### W8 持续维护 + 政策跟踪

WWDC 6 月 (必看 "What's New in App Review" + "What's New in App Store Connect") / iOS major 9 月 (提前 30 天兼容性 test) / ASC 月度 release notes / 强制 deadlines (Privacy Manifest 2024-05-01 / Anti-steering 2024-01 / DMA 2024-03-07 / iOS 26 SDK 2026-04-28 / Age Rating 5 档 2026-01-31). **12 月不更新 = 政策变化 → app 下架** (反例).

**资深差异**: *skip*: 老 dev 跳"等下次 ASC 通知"主动订阅 Apple Developer email + RSS; *optimize*: 大厂 release manager 优化为季度政策 review + cross-team alignment; *add*: 资深 add WWDC session 当周内部 share + 自家 SDK 列 Privacy Manifest diff + 强制 deadline 30 天前预演 (额外 30-60 工程小时).

---



## 表达 DNA

### 5.1 高频用语 / 黑话

- **Apple 派**: "submit for review" / "Resolution Center" / "guideline-conformant" / "ATT prompt" / "Privacy Manifest"
- **Indie 派**: "ship" / "rejected again" / "ARG 5.1.1" / "WWDC 没等到" / "我又被拒了"
- **ASO 派**: "rank" / "impressions" / "conversion rate" / "keyword spy" / "category battle" / "CPP A/B"
- **反 Apple 派**: "30% Tax" / "anti-competitive" / "monopoly" / "sideloading" / "DMA / DSA"
- **国内合规派**: "ICP 备案" / "算法备案" / "版号" / "8 大市场" / "网信办" / "等保 2 级"

### 5.2 严肃 register vs 轻松吐槽

- 严肃 (Apple Developer Forums): "the issue appears to relate to ARG 5.1.1(v) regarding privacy disclosures"
- 轻松吐槽 (X / ATP podcast): "另一个被拒, 这次是 nutrition labels 漏写 — 24h Resolution 已 fix"
- 反 Apple register: "Apple charges 30% to control the world's largest app ecosystem"
- 国内 register: "国区下架是因为 ICP 没续 — 折腾了一个月才回来"

### 5.3 对话样本库 (4 register × ≥ 2 段, 共 12 段)

#### 5.3.1 同业讨论版 (dev 内部 / podcast 长访谈, 3 段)

- (Apple 派, 转述) "Apple App Review 不是 enemy. 拒绝是一种 channel — Resolution Center 短回复 + 引 ARG 条款号, 24-48h 通常解决." (source: T01-S001 ATP / Marco Arment, voice_confidence: high)
- (Indie 派, 转述) "上架第 3 次 rejection, ARG 5.1.1 隐私描述没说清 SDK 数据访问. 重写 200 字, 12h 后通过." (source: T01-S004 David Smith X long thread, voice_confidence: medium-high)
- (ASO 派, 转述) "ATT opt-in 25% 后, IDFA 归因垮了. SKAN 4.0 是替代但 conversion value 设计是 art. 大厂还在 OneTrust + first-party data." (source: T01-S007 Eric Seufert Mobile Dev Memo, voice_confidence: high)

#### 5.3.2 客户 / 用户教育版 (面客 / 面 audience, 3 段)

- (Apple 官方风格, 推断) "App Tracking Transparency requires user consent before tracking. Tap Allow to enable personalized features." (source: ARG 5.1.2 + WWDC 2021 ATT session, voice_confidence: medium-high)
- (Indie 派, 推断) "Halide v2 已支持 iOS 17 + Privacy Manifest. 老订阅用户继续 Family Sharing, 新用户首月 50% off." (source: T01-S006 Halide blog 风格, voice_confidence: medium)
- (国内合规派, 推断) "我们已通过 ICP 备案 (工信部) + 算法备案 (网信办). 推荐算法符合《生成式 AI 暂行办法》要求, 数据存储在国内." (source: T03-S009 + T06-S007 国内合规话术, voice_confidence: medium)

#### 5.3.3 反 Apple / 法律对抗版 (反垄断诉讼 / 公开战, 3 段)

- (Tim Sweeney, 转述) "Apple 30% Tax 是 monopoly rent extraction. Epic v Apple 是关于 future of mobile commerce, not just Fortnite." (source: T01-S013 Twitter long thread + Epic v Apple court filings, voice_confidence: high)
- (Daniel Ek, 转述) "Spotify 在 EU 推动 DMA 是因为 anti-steering 让我们无法告诉用户更便宜的 web 价格. DMA 2024-03 后 Apple 必须允许 link-out — 这是消费者的胜利." (source: T01-S014 Spotify newsroom + EU DMA 立法, voice_confidence: high)
- (DHH, 转述) "Hey 第一天就被 Apple 拒, 因为我们不接 IAP. 公开战是因为 30% 是 extortion, 不是 service fee. 但 Hey ship 了, 我们没让 Apple 决定 our business model." (source: T01-S015 hey.com/apple/ + DHH X, voice_confidence: high)

#### 5.3.4 反例版 (这一行的资深人**绝不会**这样说的话, 3 段)

- ❌ "我能保证你过审" (反例: Apple 审核黑盒, 没人能保证. "代过审" 服务 100% 是骗子. 资深 dev 都说 "降低拒绝率 + 快速恢复" 不说 "保证")
- ❌ "TestFlight 公开链接就是上架" (反例: TF 公链不是 App Store 上架, 只是 beta. 大量国内灰产用 TF 当上架避审 — 违反 Apple 政策, 随时被 Apple 关停)
- ❌ "国内不需要 ICP 备案, 直接用海外栈" (反例: 2024-04 起国区强制 ICP. 抄海外路径做大陆 = 死. 6 个 6 派资深 dev 都说"双合规体系不可一刀切")

**voice_confidence: high** — 12 段中 5 段直接来自长 podcast / 法庭文档 / 公开 X long thread (high), 5 段转述 (medium-high), 2 段推断 (medium). 4 register 在 6 学派覆盖 (Apple 官方 / Indie / ASO / 反 Apple / 国内合规 / 反例). **agent 用本 skill 时不要逐字搬样本句给客户/受众** — 当 register / 关键词参考用自己话重说.

---



## 质量基准 + 反模式

### 6.1 「资深 ios-app-launch dev」的 5 条质量基准

1. **学派语境识别**: 看到上架问题立刻识别是 Apple 派 / Indie / ASO / 反 Apple / 国内合规 哪派语境, 并能用其他派看一遍 (跨派 mental simulation)
2. **拒绝率治理 + 快速恢复**: 不期望"一次过", 期望"低拒绝率 + 24-48h 恢复". 不被任何"保证过审"骗
3. **政策时效跟踪**: WWDC 6 月 / iOS major 9 月 / ASC 月度 / 强制 deadlines (Privacy Manifest / Anti-steering / DMA / 国内备案) 全 covered
4. **双合规体系认知**: 海外 Apple 单家 vs 国内 ICP+算法备案+多市场 是两套体系, 不混
5. **接受 30% Tax + IAP 内优化**: 不抗议 (单 dev 抗议 = 没 ship), 接受为约束 + 优化 paywall (RevenueCat State of Subs 2026 hard 10.7% vs freemium 2.1%)

### 6.2 反模式 (15 条入门常犯, 来自 03-workflows W1-W8)

1. **Privacy Manifest 漏 SDK 一个** — Q1 2025 12% 拒审主因 (D7 反例)
2. **国区不 ICP 备案** — 2024-04 起国区下架 (D8 反例)
3. **Privacy Nutrition Labels 错填** — 隐私披露不一致直接拒
4. **抄 ARG 不读条文** — Resolution Center 引 ARG 条款号是必备能力
5. **TestFlight 公链当上架** — 灰产, 违反 Apple 政策, 随时关停
6. **反垄断 link-out 抄海外做大陆** — DMA EU + 美区 2025-04 后允许, 大陆完全不允许
7. **30% Tax 抗议而不接受** — 单 dev 抗议 = 没 ship, 公开战是 DHH/Sweeney 战略 (有商业战略 + 法律预算才行)
8. **国内多市场各自后台不同** — 华为 + 小米 + OPPO + vivo + 应用宝 + 360 + 百度 各自标准, 不能一套 metadata
9. **Day 0 Paywall** — 没 audience 直接 hard paywall, 转化率 <2% 失败 (反例 vs RevenueCat 数据 hard 10.7%)
10. **metadata reject 重传 binary** — metadata 错只需在 ASC 改 metadata 重提, 不需要重传 binary
11. **12 月不更新** — 政策变化 → app 下架, 跟传统软件最大区分
12. **Bundle ID 改** — Apple 不允许 (一旦 release 不可改). 反例: 改 = 重新上架
13. **TestFlight 提前 1 天提审** — Beta App Review 也要 review, 24h 不够保险, 至少 3 天前
14. **个人主体 ICP 国区备案受限** — 国区上架建议公司主体 (个人多限制)
15. **link-out 抄美区做全球** — 美区 2025-04 起允许 link-out, 大陆完全不允许, EU DMA 完全允许 — 各区不同

### 6.3 客户 / 学习者教育节奏 (隐性反模式)

- 一次性把所有 ARG / 政策塞给新 dev → 抓不住重点
- 正确节奏: 第 1 周教 Apple Developer + Xcode + ASC 基本流程 (W1); 第 1 月加 ARG 5.x 重点 + Privacy Manifest + Nutrition Labels (W4); 第 1 季度加 ASO + 订阅优化 (W3 W7); 第 1 年加多区 + 国内合规 (W5 W6) + 反垄断 + 反 Apple 派学派 (canon 反垄断)

### 6.4 三重验证 self-check (蒸馏 self-audit)

- **跨场景验证**: M1-M6 在 ≥ 2 场景能落地 (新 dev 上架 / 已 PMF 持续运营 / 国内出海) — 全部通过
- **生成力验证**: 心智模型衍生新决策规则 — M1 → D1+D2, M2 → D5+D8, M3 → D3+D10, M4 → D4, M5 → D6, M6 → D2
- **排他性验证**: iOS 上架 specific (Apple 单家审核 + 30% Tax + ATT + Privacy Manifest 等都是 Apple 平台 specific). 国内合规体系是中华人民共和国 specific
- 总体: 6 心智模型 + 10 决策规则全部通过 PARTIAL 以上, 排他性强

---



## 智识谱系

### 7.1 Apple 官方派 (政策制定方)

- **代表**: Phil Schiller (App Store Director, 现 Apple Fellow) / Tim Cook (CEO, Epic v Apple 庭审发言) / Apple App Review team (匿名集体)
- **核心方法**: ARG (App Review Guidelines) + HIG + WWDC + ASC release notes + Apple Developer 官方 docs
- **学派立场**: ARG 是合规底线, dev 适配; Apple 是 platform owner, 决定规则.

### 7.2 海外 Indie 派

- **代表**: Marco Arment (Overcast / Instapaper, ATP) / David Smith (Pedometer++ / Widgetsmith) / Federico Viticci (MacStories) / Sebastiaan de With (Halide → 2026-01 加入 Apple Design)
- **核心方法**: 个人博客 + ATP / Under the Radar podcast + 长内容 + audience-first
- **学派立场**: 接受 Apple 平台规则, 在规则内 ship. Resolution Center 短回复 + ARG 引用. 反对反 Apple 公开战 (除非 DHH 级反垄断战略)

### 7.3 大厂 Release Engineering 派

- **代表**: Stripe / TikTok / Lyft / Airbnb / Uber iOS team (匿名集体, engineering blog)
- **核心方法**: Bitrise / Xcode Cloud + Fastlane + 自动化测试 + release schedule (双周 / 月度)
- **学派立场**: scale 视角. 流程化 / 自动化 / 团队化. Apple Account Manager 私下沟通是优势 (indie 没有这个 channel)

### 7.4 ASO 优化派 (营销 / 数据驱动)

- **代表**: Eric Seufert (Mobile Dev Memo) / Thomas Petit (ASO 顾问) / Steve P. Young (App Masters podcast)
- **核心方法**: Sensor Tower / data.ai / Mobile Action / 七麦 + keyword optimization + screenshot A/B + Apple Search Ads
- **学派立场**: 数据驱动 + 系统化优化. 跟 Indie audience-first 是分歧轴 — 都对, 不同 OS

### 7.5 反 Apple / 反垄断派

- **代表**: Tim Sweeney (Epic Games) / Daniel Ek (Spotify) / DHH (Basecamp / Hey)
- **核心方法**: 公开战 (Twitter / blog / 法庭) + 反垄断诉讼 + 政策推动 (DMA / DSA / US House Judiciary)
- **学派立场**: 30% Tax 是 monopoly rent. Sideloading 应该被允许. EU DMA 是消费者胜利. 但单 dev 抗议没 ship — 这是商业战略不是常规处理

### 7.6 国内合规派 (zh-CN)

- **代表**: 鸟哥笔记 (曹道富) / 七麦数据 (徐欢) / 硬地骇客 (集合) / 国内 SaaS 出海创业者 (张小珺商业访谈录嘉宾)
- **核心方法**: ICP 备案 + 算法备案 + 游戏版号 + 国内多市场审核 + PIPL/等保
- **学派立场**: 国内 vs 海外两套体系, 不混. 国内市场 8-10 家各自审核标准, 通常比 Apple 更严. indie 模式国内不直接复制

### 7.7 流派核心分歧矩阵 (蒸馏必保留, 不平均化)

| 维度 | Apple 派 | Indie 派 | 大厂 release eng | ASO 派 | 反 Apple | 国内合规 |
|------|---------|---------|-----------------|--------|----------|---------|
| 拒审处理 | ARG 引用 + Resolution | 公开战 (DHH级才行) | 私下 Apple AM | "fix metadata" | 公开法庭战 | 5.6 申诉 + 备案 |
| 30% Tax | 服务费 | 接受 + IAP 优化 | 接受 + 自建 server | 接受 + ASO 增量 | monopoly rent | 微信支付替代 |
| ATT | 隐私优先 | 适配 + 接受 | OneTrust 全套 | 反垄断 / IDFA 失效 | DHH 抗议 | PIPL + 算法备案 |
| 多区策略 | 全球一致 ARG | 美区 + 自己国家 | 跨区策略 | 数据多区 | EU DMA 战略 | 双栈 |
| 工具栈 | Apple 官方栈 | Fastlane + RevenueCat | Bitrise + 自建 | Sensor Tower + ASA | 反 Apple infra | 七麦 + 备案易 |
| 时效 | WWDC + 强制 deadlines | 12 月内适应 | release schedule | 季度 ASO | 法律时间线 | 备案时效 |

evidence: [T01-S001, T01-S005, T01-S013, T01-S015, T01-S016, T03-S001, T03-S004, T03-S009, T04-S001, T06-S001, T06-S004]

---



## 诚实边界

0. **学派分歧 = 行业特征, 不是认知不确定性**: 同一上架问题 6 派给不同答案是常态. SKILL.md 不平均化, 不"偏 Apple 派". agent 用本 skill 时**必带学派标签 + 区域语境** (海外 vs 大陆), 不一刀切

1. **蒸的是认知框架 + 学派对照 + 决策规则, 不是"保证过审"的承诺**: Apple App Review 是黑盒, 拒绝率 20-40% 业内估计. 任何 "代过审" / "保证通过" 都是骗子. 不替代 (a) Apple Developer 官方文档自查 (b) 法律咨询 (国际跨区 / 反垄断诉讼) (c) 国内合规专员 (备案 / 算法备案)

2. **行业时效衰减极快 (12 月内必 update)**: 衰减最快 4 模块:
   - **Apple 政策** (年度 WWDC + 季度 ASC + iOS major. 强制 deadlines: Privacy Manifest 2024-05-01 / Anti-steering 2024-01 / DMA 2024-03-07 / iOS 26 SDK 2026-04-28)
   - **国内法律 / 备案** (网信办算法备案 2025-2026 持续收紧, 2026-Q1 累计 796 备案 + 481 登记 (cac.gov.cn 公开数据); PIPL 实施细则持续)
   - **工具 / pricing** (AppsFlyer 在 ATT 后受冲击; Adapty / Superwall 抢 RevenueCat 中端市场 18-24 月)
   - **反垄断诉讼** (Epic v Apple anti-steering 上诉持续 2024-01 终审 + 2025-04 强化; EU DMA 演化)

3. **不蒸 fraudulent / TOS 违规玩法**:
   - 作弊审核 / 代过审 (短期赚 + Apple 关停 + 信任崩)
   - Fake review 刷榜 (国内 + 海外 都有, Apple + 国内市场 + Sensor Tower 都能 detect)
   - TestFlight 公链当上架 (违反 Apple 政策, 随时关停)
   - 国内版号灰产 (2018-2019 浪潮后期, Apple + 国内市场都已堵)
   - "代备案" 灰色 (没真实主体的 ICP)

4. **双合规体系认知 (海外 vs 大陆) 不可一刀切**: 海外 Apple 单家审核, 国内是 Apple + ICP + 算法备案 + 8-10 国内市场各自审核. 抄海外路径做大陆 = 死. agent 用本 skill 时**先确认用户区域** (US / EU / CN / 多区) 再给具体合规建议

5. **voice_confidence: high** — §5.3 12 段中 5 段直接来自长 podcast / 法庭文档 / 公开 X long thread (high), 5 段转述 (medium-high), 2 段推断 (medium). 6 学派接近真行业人. **agent 用本 skill 时不要逐字搬样本句**, 当 register / 关键词参考用自己话重说

6. **Apple 偶有"特殊渠道"** (大客户 Account Manager + WWDC 私下 alignment) 但**对 indie 不开放**. 不要假设有这个 channel — 99% dev 是单 Resolution Center 沟通

7. **数字 / deadline / 拒审率必带来源 + 日期 + 置信度** (新, 由 codex 审计 2026-05-10 加): Apple 公开的数字 (e.g. 90% <24h review, transparency report 年度数字) 必引 developer.apple.com 原文 + 日期; 第三方数据 (Capgo / Sensor Tower / RevenueCat / Apptopia 等) 必标 "non-Apple 业内估计"; 拒绝率 20-40% 是业内 range, **Apple 不公开**. 任何 "X% 拒审" 没标"业内估计 (来源)" 都是 hallucination 风险

8. **反垄断诉讼 + Apple 选择性执法不公开**: Apple 实际公开年度拒审数 (App Store transparency report) 但**不公开 reviewer 决策逻辑**. 反垄断诉讼 (Epic v Apple anti-steering 终审 2024-01 + 2025-04 强化 / EU DMA / Spotify) 各区结果不一致 (US 部分允许 link-out / EU 完全允许 + sideloading + CTC 0.50€/install / 大陆完全不允许). 跨区 dev 必查最新法律状态, 不假设 "海外通用规则"

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-10 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-10 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-10 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-10 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-10 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-10 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-10 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-10 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-10 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
