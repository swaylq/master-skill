---
name: education-saas-master
description: |
  教育SaaS (Education SaaS) Master OS — automated mastery of Education SaaS: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on Education SaaS problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「教育SaaS」「education saas」「招生管理系统」「排课系统」「在线教室」
triggers:
  - "教育SaaS"
  - "education saas"
  - "招生管理系统"
  - "排课系统"
  - "在线教室"
  - "校园数字化"
  - "教务ERP"
  - "学习管理系统"
  - "LMS"
  - "edtech saas"
  - "education platform"
  - "classroom management software"
  - "student information system"
  - "SIS"
  - "enrollment management"
industry: "Education SaaS"
industry-cn: "教育SaaS"
locale: "global"
last_research_date: "2026-05-26"
source_count: 104
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 教育SaaS · Master OS

> This skill makes the agent operate as a senior Education SaaS practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 Education SaaS 相关的问题时（关键词：教育SaaS, education saas, 招生管理系统, 排课系统, 在线教室, 校园数字化, 教务ERP, 学习管理系统, LMS, edtech saas, education platform, classroom management software, student information system, SIS, enrollment management），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 Education SaaS 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：Education SaaS 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 市场定位与竞品分析
- 看什么: 目标细分市场 (K-12 / 高等 / 职教 / 企业培训) 的现有玩家格局
- 在哪看: 
- 输出: 

#### 维度 2: 合规与数据治理
- 看什么: 目标地域的教育数据合规要求 (FERPA/COPPA/GDPR/PIPL/等保 2.0)
- 在哪看: 
- 输出: 

#### 维度 3: 标准互操作评估
- 看什么: 目标 LMS/SIS 生态支持哪些标准 (LTI/SCORM/xAPI/OneRoster)
- 在哪看: 
- 输出: 

#### 维度 4: 教师 Adoption 策略
- 看什么: 目标用户群体的技术接受度 + 痛点优先级
- 在哪看: 
- 输出: 

#### 维度 5: 采购周期与预算节奏
- 看什么: 目标客户的预算审批周期 + 决策链
- 在哪看: 
- 输出: 

#### 维度 6: 产品定价与商业模型
- 看什么: 同类产品的定价结构 + NRR benchmark
- 在哪看: 
- 输出: 

#### 维度 7: AI 能力评估
- 看什么: AI 功能在教育场景的实际效果 vs 营销承诺
- 在哪看: 
- 输出: 

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 2-Sigma 产品北极星

教育 SaaS 的终极使命是用技术规模化一对一辅导效果（Bloom 1984 2-sigma）。所有产品功能是否沿这条轴线设计，决定了产品深度 vs 仅做行政数字化。当前最佳实践（ITS d≈0.76）仅约一半效果，AI tutoring 正在推动逼近但独立 RCT 证据仍缺失。

**figures**: Josh Coates / Sal Khan / Michael Horn
**evidence**: [T04-S013, T04-S028, T01-S005]
**局限**: 2-sigma 在随机对照实验中难以完全复现（约 0.3-0.5σ 稳定），避免过度夸大 AI 辅导效果（业内估）

### 1.2 低端颠覆进入路径

教育 SaaS 的经典增长路径是从小机构/职业教育起步（做大玩家不屑做的），再向上攻高校/大型 K12 学区。直接与整合型巨头（Ellucian/PowerSchool）正面竞争失败率极高。Canvas 先做高等教育中的创新型小校→再攻 Ivy，Moodle 先做发展中国家→再渗透欧美。

**figures**: Michael Horn / Clayton Christensen / Josh Coates
**evidence**: [T04-S001, T01-S001, T02-S003]
**局限**: 中国市场颠覆路径不完全适用——政策驱动（双减/信息化 2.0）可能直接打开 top-down 通道

### 1.3 多租户 × 数据隐私双重约束

教育数据天然敏感（未成年人、家庭信息），FERPA/COPPA/PIPL 构成护城河。合规成本淘汰不合规竞争者，同时使切换成本变高（数据迁移 + 合规重新认证）。"数据隔离做到什么程度"是架构决策第一问。

**figures**: Phil Hill / 张以弛 / Jason Lemkin
**evidence**: [T04-S021, T06-S008, T02-S007]
**局限**: 合规要求跨地域差异巨大（FERPA vs GDPR vs PIPL），不存在"一次合规全球通用"

### 1.4 政策双轨：B2C 压缩 × B2B 扩张

双减压缩了中国 B2C 培训赛道，但同时推高了 B2B 校园数字化需求（信息化 2.0 + 智慧教育平台）。教育 SaaS 的增长极从"学科辅导工具"转向"教务管理/排课/招生 CRM"。这个模式在全球市场也有变体——COVID 后 LMS 预算从"nice-to-have"变成"基础设施"。

**figures**: 张以弛 / 宋军波 / 黄荣怀
**evidence**: [T04-S008, T01-S011, T01-S014]
**局限**: 政策可逆——中国教培政策 3-5 年一个周期，双减后的 B2B 红利窗口不必然永续

### 1.5 PLG 混合模式：自下而上 + 自上而下

教育 SaaS 的 PLG 不同于纯 B2B SaaS——教师/学生是用户，但付费方是学校/机构。需要"自下而上渗透"（teacher adoption）+ "自上而下签约"（admin/district deal）的混合路径。Google Classroom / Canvas 都走这条路。单纯的 sales-led 或单纯的 PLG 在教育市场都走不通。

**figures**: Jason Lemkin / Tomasz Tunguz / John Baker
**evidence**: [T04-S024, T04-S030, T01-S002]
**局限**: 教师作为免费用户的 adoption 不等于学校愿意付费——转化需要独立的"管理员价值叙事"

### 1.6 互操作标准是生态位之锚

在教育 SaaS 市场，是否遵守 LTI/SCORM/xAPI/OneRoster 等标准决定了产品能否进入既有生态。"接入 Canvas/Moodle 的 LTI 集成"是 EdTech 创业公司获取分发的最低门槛。标准合规不是锦上添花——是进入条件。

**figures**: Martin Dougiamas / Phil Hill / 1EdTech Consortium
**evidence**: [T06-S001, T04-S009, T02-S017]
**局限**: 中国教育市场标准化程度远低于欧美，自研协议仍是主流

### 1.7 完课率是虚荣指标——意图分层才有意义

Ho et al. 研究显示，用意图分层后完课率差异达 4 倍。教育 SaaS 的产品指标设计应使用"意图调整完课率"而非原始完课率。同理，DAU/MAU 在教育产品中有不同语义——学期开始/结束天然造成使用波峰波谷。

**figures**: Daphne Koller / George Siemens / Phil Hill
**evidence**: [T04-S006, T05-S001, T01-S006]
**局限**: 意图标注本身依赖主观数据（问卷），无法完全消除 selection bias

---



## 标准 Playbook

1. **如果是 LMS 选型**: 先看学校 IT 团队规模——有 ≥ 3 人专职 IT 选 Moodle/开源（总 TCO 低但运维重），无专职 IT 选 Canvas/Brightspace（SaaS 托管）。案例: 加州社区大学系统 2022 从 Blackboard 迁至 Canvas（约 80% 教师满意度提升，业内估, T02-S001）

2. **如果是进入北美高等教育市场**: 先做 LTI 1.3 认证 + SOC 2 Type II → 找 1-2 个种子学校做 pilot（学期制，至少跑完一个完整学期）→ 拿到 case study 后攻 consortium/district deal。案例: Turnitin 先做单校 pilot → 扩展到 16,000+ 机构（约 20 年积累，T02-S005）

3. **如果是进入中国教育 SaaS 市场**: 先确认是 B2B 校园（教务/排课/招生）还是 B2C 学习（双减后受限）。B2B 路径: 接入钉钉教育/企业微信生态 → 做区域代理 → 拿政府采购标。案例: 校宝在线从培训机构 SaaS → 全日制学校 → 700 亿年交易额（约, T01-S011）

4. **如果是教育 SaaS 定价**: 避免按学生人头收费（学校预算按年固定，人头浮动让预算审批困难）。推荐按学校/机构固定年费 + 增值模块 addon。案例: Canvas 对高等教育按 institution 定价而非按 student（T02-S001）

5. **如果是 SIS 数据迁移**: 先做数据质量审计（约 30-40% 历史数据有质量问题，业内估）→ 建立"最小可运行数据集" → 分阶段迁移（学生 → 课程 → 成绩 → 历史报表）。绝不大爆炸迁移。案例: PowerSchool 推荐 6-12 月分阶段（T03-S015）

6. **如果完课率低于预期**: 先做意图分层（casual learner / certificate seeker / degree pursuer），对不同意图群体设不同基准。不要用统一完课率作 KPI。案例: Coursera 2014 年 Ho et al. 研究后改用 intention-weighted metrics（约, T04-S006）

7. **如果教师 adoption 卡住**: 找到"种子教师"（early adopter, 约占 10-15%，业内估）→ 让他们创造可见成果 → peer influence 扩散。不要做全校强制培训——教师 resistance 是 EdTech 失败第一原因。案例: Canvas 的 Teacher Community 策略（T01-S001）

8. **如果面对开源 vs 商业选型争论**: 真实 TCO 计算必须包含运维人工成本 + 插件兼容性维护 + 升级 downtime。Moodle 总 TCO 在 3 年后可能超过 Canvas SaaS 如果没有专职维护团队。案例: UK Russell Group 大学从 Moodle 迁出趋势（约 2022-2025, T02-S003）

9. **如果是学术诚信检测**: AI 检测工具（Turnitin AI / GPTZero）误报率在 ESL 学生群体中显著高于平均（约 15-25% false positive, 业内估）。必须保留教师人工判定为最终裁定，工具仅作辅助信号。案例: Turnitin 2024 增加"AI writing indicator"置信度分级而非二值判定（T03-S007）

10. **如果是跨境教育 SaaS 部署**: 数据驻留（data residency）是第一问——GDPR 要求欧盟学生数据不出境，中国 PIPL 同理。必须 multi-region 架构或分别部署。案例: ClassIn 东南亚扩张时建立新加坡数据中心（T01-S012）

---



## 工具栈与选型决策树

### 3.1 必备工具 (12 件, 约 80% 教育 SaaS 从业者使用)

1. **Canvas (Instructure)** — 北美高等教育 LMS #1, 约 50% 学生份额 (业内估, T02-S001)
2. **Moodle** — 全球部署最广的开源 LMS, 约 5 亿用户, 中低收入国家主流 (T02-S003)
3. **Google Classroom** — K-12 免费入口, 约 1.5 亿用户, PLG 标杆 (T02-S004)
4. **Microsoft Teams for Education** — 企业生态延伸, 与 Office 365 深度集成 (T02-S005)
5. **PowerSchool** — 北美 K-12 SIS #1, 约 23% 市场份额 (业内估, T02-S006)
6. **Ellucian (Banner/Colleague)** — 高等教育 ERP #1, 约 35% 份额 (业内估, T02-S007)
7. **Turnitin + Gradescope** — 学术诚信 + AI 评分, 16,000+ 机构 (T02-S008)
8. **Zoom for Education** — 同步在线教室事实标准, COVID 后渗透率最高 (T02-S009)
9. **Slate (Technolutions)** — 高等教育招生 CRM #1, 2,000+ 高校 (T02-S010)
10. **D2L Brightspace** — K-12 + 高等教育 LMS, 北美市场 #3 (T02-S011)
11. **LTI 1.3 / LTI Advantage** — 工具互操作协议, 接入 LMS 生态的必要通行证 (T06-S001)
12. **SCORM/xAPI** — 内容打包与学习行为追踪标准, 课程资产可迁移性基础 (T06-S002)

### 3.2 场景特化 (7 类, 按子场景分组)

**招生管理**: Slate (高教) / 校管家 (中国培训)
**在线教室**: ClassIn (OMO混合) / BigBlueButton (开源替代)
**考试监控**: Proctorio / Respondus (注意: Respondus Monitor 2025 年 5 月停服)
**学习分析**: Civitas Learning / Brightspace Insights
**中国教务**: 校宝在线 (培训机构) / 正方教务 (高校)
**数字凭证**: Credly + Accredible (micro-credentials)
**排课系统**: 走班排课 SaaS (中国新高考催生)

### 3.3 新兴工具 (6 件, 近 12 个月出现或起势)

1. **Khanmigo** — AI tutor, 用户从 7 万增至 70 万 (约 10 倍, 2024-2025, T02-S018)
2. **ALEKS (McGraw-Hill)** — 自适应学习, 知识空间理论 (T02-S019)
3. **Ed-Fi v5 + OneRoster 合并** — K-12 数据标准统一化 (T04-S009)
4. **Open Badges 3.0** — Verifiable Credentials 整合, 2023 发布 (T06-S015)
5. **AI Course Design** — AI 辅助教学设计工具 (多家, 尚未有明确赢家)
6. **cmi5** — SCORM 继任者, 企业培训 + 军事 EdTech 先发机会 (T06-S003)

### 3.4 避坑清单

- ❌ 不要把 TCO 等同于 license 费: 开源 LMS (Moodle) 3 年 TCO 可能超商业 SaaS 如果没有专职运维团队
- ❌ 不要忽视 PowerSchool 2024 数据泄露遗留: 迁移到 PowerSchool SIS 前评估数据安全整改进度
- ❌ 不要在中国市场直接替换国际产品: 钉钉/企微生态 + 政策合规 + 本地支付集成是硬门槛
- ❌ 不要把在线监考当万能: GDPR 对 biometric proctoring 有严格限制, Respondus 已停服
- ❌ 不要把 LTI 集成当"已完成": 浅集成 (单点登录) vs 深集成 (成绩回传 + roster sync) 差距巨大
- ❌ 不要选 Blackboard 做新部署: 市场份额持续下滑, Anthology 合并后路线图不清晰
- ❌ 不要把 digital credential 孤岛化: 选 Open Badges 3.0 兼容平台, 不要锁在单一厂商

---



## 工作流 / Pipeline

### 4.1 LMS 选型与部署

**入门 SOP**:
1. 需求调研: 访谈教师/学生/IT/管理层, 列出 must-have vs nice-to-have
2. 候选评估: 对比 3-5 个 LMS (Canvas/Moodle/Brightspace/Blackboard/Google), RFP 发出
3. POC 试用: 选 2 个 finalist, 各跑 4-6 周 pilot (含真实课程)
4. 采购决策: TCO 分析 + 合规审查 + 参考机构调研
5. 数据迁移: 从旧系统导出课程/用户/成绩, 清洗 + 导入
6. 教师培训: 种子教师培训 → peer mentoring → 全校推广
7. Go-live + 反馈循环: 学期初上线, 2 周内收集 friction 点

**资深路径**: 跳过 step 2 的全面对比 (经验告诉他们 Canvas vs Moodle 核心差异, 直接按学校 profile 匹配); 优化 step 6 只培训种子教师 (约 10-15% early adopter 带动其余); 额外做供应商 SLA 谈判 + 退出条款确认 evidence: [T03-S001, T03-S009]

**近期变化**: 2024-2025 起 AI 功能成为 LMS 选型新维度 (AI writing assistant / AI grading / AI tutoring 内置与否) evidence: [T03-S002]
**失败模式**: (1) 教师 resistance 导致 shadow IT — 强制推行不如渐进式 peer adoption (2) "参考机构效应"盲从 — 一所名校选了 X 不代表适合你 evidence: [T03-S009]
**last_updated**: 2026-05

### 4.2 SIS 数据迁移与上线

**入门 SOP**:
1. 数据审计: 盘点历史数据质量, 约 30-40% 有质量问题 (业内估)
2. 最小可运行数据集定义: 确定哪些数据必须迁移 vs 归档冷存
3. 字段映射: 旧系统 schema → 新系统 schema, 处理不兼容字段
4. 分阶段导入: 学生 → 教职工 → 课程 → 成绩 → 历史报表
5. 验证与对账: 抽样验证 + 全量对账, 确保数据完整性
6. 双跑期: 新旧系统并行运行 1-2 学期, 教职员工适应

**资深路径**: 跳过 step 6 的完整双跑 (对数据质量有信心时直接切换); 优化 step 4 用 ETL pipeline 自动化而非手工; 额外做"报表再造"预案 — 历史自定义报表无法自动迁移是最大隐患 evidence: [T03-S015, T03-S010]

**近期变化**: Ed-Fi v5 (2025) + OneRoster 1.2 标准化使跨系统数据交换更可预测 evidence: [T03-S011]
**失败模式**: (1) "报表陷阱" — 数据迁移技术成功但历史报表无法重建 (2) 学期初数据不一致导致选课系统崩溃 evidence: [T03-S015]
**last_updated**: 2026-05

### 4.3 招生漏斗管理

**入门 SOP**:
1. Inquiry 获取: 线上 + 线下渠道, 统一进 CRM
2. Lead nurturing: 自动化邮件/短信序列, 个性化内容
3. Application 引导: 简化申请流程, 减少 friction
4. Admission 决策: 评审 + 发 offer
5. Yield optimization: 5 月 1 日前 (美) / 报名截止前 (中) 催缴定金
6. Enrollment confirmation: 注册完成 + 分班/选课

**资深路径**: 跳过 step 2 的通用 nurture (对高意向线索直接 1v1 跟进); 优化 step 5 用预测模型识别 melt 风险学生; 额外做 yield rate benchmarking 按 peer 院校对标 evidence: [T03-S020, T03-S003]

**近期变化**: 2024-2025 AI chatbot + 预测模型开始用于 inquiry → application 转化预测 evidence: [T03-S003]
**失败模式**: (1) "5 月 1 日悬崖" — 过了 Common Decision Day 未缴定金的学生转化率骤降 (2) 中国培训机构"暑假大战"备战不足 — 70%+ 营收集中暑假 evidence: [T03-S020, T03-S016]
**last_updated**: 2026-05

### 4.4 课程设计与上线

**入门 SOP**:
1. 需求分析: 学习目标 + 受众分析 (ADDIE 的 A 阶段)
2. 教学设计: 按 Gagné 9 Events / Merrill First Principles 设计教学活动
3. 内容开发: 视频/文本/交互 — 遵循 SCORM/xAPI 标准打包
4. LMS 上架: 上传到 Canvas/Moodle, 配置评估/截止日期/LTI 工具
5. 教师准备: 试教 + 反馈 + 调整
6. 学生端发布 + 第一周反馈收集

**资深路径**: 跳过 step 2 的完整 ADDIE 流程 (用 SAM 快速迭代原型); 优化 step 3 用 AI 辅助生成初稿再人工精修; 额外做 learning analytics dashboard 配置以便实时追踪学习行为 evidence: [T03-S004, T04-S005]

**近期变化**: 2025 起 AI 课程生成工具 (AI-assisted instructional design) 开始渗透 step 3 evidence: [T03-S004]
**失败模式**: (1) SCORM 1.2 legacy 内容无法在新 LMS 正常播放 (2) 课程设计忽视认知负荷 — 单页信息量过大导致学生 drop-off evidence: [T04-S011, T04-S029]
**last_updated**: 2026-05

### 4.5 在线混合授课

**入门 SOP**:
1. 教学模式选择: 同步 / 异步 / 混合 (station rotation / flipped)
2. 工具准备: Zoom/ClassIn + LMS + 协作工具
3. 课前准备: 发布预习材料, 设置 breakout rooms
4. 课中互动: 投票/白板/分组讨论/real-time quiz
5. 课后跟进: 作业布置 + 回放发布 + 学习数据收集
6. 教学反思与迭代

**资深路径**: 跳过 step 1 的 deliberation (经验直觉匹配模式); 优化 step 4 用 AI 助教实时总结 + 答疑; 额外做"认知负荷检查" — 每 15 分钟切换活动类型防止注意力衰减 evidence: [T03-S005, T04-S011]

**近期变化**: 2025 AI 助教从实验转实用 (总结、答疑、个性化反馈) evidence: [T03-S005]
**失败模式**: (1) "Zoom fatigue" 导致学生关摄像头假装在线 (2) 异步内容没有 deadline 压力 → 拖延到学期末 evidence: [T03-S005]
**last_updated**: 2026-05

### 4.6 学习分析与教学干预

**入门 SOP**:
1. 数据收集: xAPI/Caliper 收集学习行为数据
2. Dashboard 配置: 设置预警阈值 (出勤率/作业提交/成绩下滑)
3. At-risk 识别: 模型 flag 出高风险学生
4. 干预设计: 1v1 辅导 / 邮件提醒 / peer support
5. 效果评估: 对比干预组 vs 对照组

**资深路径**: 跳过 step 2 的手动阈值配置 (用 ML 模型自动校准); 优化 step 4 做分层干预 (轻度: 自动邮件, 中度: advisor 联系, 重度: 院长面谈); 额外做因果推断而非仅相关性分析 evidence: [T03-S006, T01-S009]

**近期变化**: 2025 预测模型从 logistic regression 升级到 transformer-based, 季度迭代 evidence: [T03-S006]
**失败模式**: (1) "相关 ≠ 因果" — 低 GPA 预测辍学不意味着提高 GPA 就能留住学生 (2) 数据隐私: 过度监控学习行为引发学生反感 evidence: [T03-S006]
**last_updated**: 2026-05

### 4.7 LTI 集成工具接入

**入门 SOP**:
1. 需求确认: 哪些第三方工具需要接入 (Turnitin/Padlet/Hypothesis...)
2. LTI 版本确认: LTI 1.3 / LTI Advantage (AGS/NRPS/Deep Linking)
3. 注册与配置: 在 LMS admin 注册 tool, 交换 public key
4. 成绩回传测试: AGS (Assignment and Grade Services) 端到端测试
5. Roster sync: NRPS (Names and Role Provisioning Services) 验证
6. 上线 + 监控: 学期初并发压力测试

**资深路径**: 跳过 step 2 的调研 (直接要求 LTI 1.3, 拒绝 LTI 1.1 legacy); 优化 step 6 提前做学期初并发预案; 额外做供应商 uptime SLA + rate limit 确认 evidence: [T03-S019, T06-S001]

**近期变化**: LTI 1.1 sunset 进行中 (1EdTech 推动), 新集成必须 LTI 1.3 evidence: [T06-S001]
**失败模式**: (1) "学期初雪崩" — 全校学生同时首次启动 LTI 工具, 并发超 API limit (2) 浅集成 vs 深集成混淆 — SSO 通了不代表成绩回传也通 evidence: [T03-S019]
**last_updated**: 2026-05

### 4.8 学术诚信审查

**入门 SOP**:
1. 提交收集: 学生通过 LMS 提交论文/作业
2. 自动检测: Turnitin 相似度 + AI writing indicator
3. 报告审阅: 教师查看相似度报告, 判断是否抄袭
4. 学生申诉: 给学生解释机会
5. 处理决定: 按学校学术诚信政策执行

**资深路径**: 跳过 step 2 的盲信工具结果 (了解 AI 检测误报率); 优化 step 3 关注"AI indicator ≠ 作弊判定"; 额外做 ESL 学生群体单独校准 — 误报率约 15-25% (业内估) evidence: [T03-S007, T02-S008]

**近期变化**: 2024-2025 AI 写作检测技术快速演进但准确率仍不稳定, 多数学校转向"process-based assessment"减少对终端检测的依赖 evidence: [T03-S007]
**失败模式**: (1) ESL 误报 — 非母语写作与 AI 生成相似度高 (2) 过度依赖工具判定取代教师专业判断 evidence: [T03-S007]
**last_updated**: 2026-05

### 4.9 培训机构教务全流程 (中国)

**入门 SOP**:
1. 招生获客: 线上广告/转介绍/试听课
2. 咨询转化: 课程顾问跟进, 约试听
3. 签约缴费: 合同签署 + 在线支付
4. 排课分班: 按年龄/水平分班, 教师匹配
5. 上课考勤: 每节课签到 + 课消扣除
6. 续费运营: 课消预警 + 续费提醒 + 转介绍激励

**资深路径**: 跳过 step 1 的广撒网 (用转介绍裂变为主, 约 60% 新客来自老带新, 业内估); 优化 step 4 用 AI 排课优化教室利用率 (约提升 15-20%, 业内估); 额外做"寒暑假大战"预案 — 70%+ 营收集中暑假, 提前 2 月备战 evidence: [T03-S016, T01-S011]

**近期变化**: 双减后素质教育 (编程/美术/体育) 替代学科培训, 招生话术和产品形态全面转型 evidence: [T03-S016]
**失败模式**: (1) 寒暑假峰值系统崩溃 — 平时架构无法支撑 5-10 倍并发 (2) 课消不透明引发家长投诉和退费潮 evidence: [T03-S016]
**last_updated**: 2026-05

### 4.10 EdTech SaaS GTM

**入门 SOP**:
1. 市场细分: K-12 / 高等教育 / 企业培训 / 职业教育 — 选一个切入
2. Pilot 学校获取: 找 2-3 所种子学校, 免费/低价 pilot
3. Case study 产出: pilot 跑完一学期后产出量化案例
4. 扩张路径: consortium deal / district deal / 政府采购
5. 产品化: pilot 阶段的定制化需求抽象为通用功能
6. 规模化: channel partner / reseller / 区域代理

**资深路径**: 跳过 step 2 的冷启动 (利用已有关系网直接锁定 design partner); 优化 step 4 走"参考机构效应" — 一所名校的选择带动 5-10 所跟随; 额外做教育采购周期 alignment — 预算在 fiscal year 初审批, 错过就等一年 evidence: [T03-S009, T03-S018]

**近期变化**: 2025 起 AI compliance (AI 使用政策/数据使用声明) 成为 RFP 新增必答项 evidence: [T03-S018]
**失败模式**: (1) 教育采购周期错配 — SaaS 创业公司按季度算, 学校按学年算 (2) 免费 pilot 没有转化机制 — pilot 完了学校没预算也没动力续约 evidence: [T03-S018]
**last_updated**: 2026-05

---



## 表达 DNA

### 5.1 高频行业用语

| 术语 | 内行用法 | 外行破绽 |
|------|---------|---------|
| LMS | 特指 Canvas/Moodle/Brightspace 这类平台 | 把任何有课程的网站都叫 LMS |
| SIS | Student Information System, 学籍/成绩/排课的系统级后台 | 跟 LMS 混淆, 或以为是"学生信息安全" |
| NRR | Net Revenue Retention, 不含新客的老客收入增长 | 跟 ARR 混淆, 或理解成"净利润率" |
| LTI | Learning Tools Interoperability, 工具接入标准 | 以为是某个具体产品名 |
| enrollment funnel | 从 inquiry 到入学的全流程漏斗 | 用"招生漏斗"但不知道 yield/melt 阶段 |
| rostering | 名册同步 — 学生/教师/课程的自动对齐 | 以为是"排班" |
| grade passback | LTI 场景下成绩从第三方工具自动回写 LMS | 不知道这是 LTI AGS 的功能 |

### 5.2 Register 差异

- **跟教师沟通**: 强调"减轻工作量"、"让你专注教学"、"不需要学新东西"——教师对技术有本能抵触
- **跟 CIO/CTO 沟通**: 强调"interoperability"、"data governance"、"total cost of ownership"、"vendor lock-in risk"
- **跟校长/管理层**: 强调"student outcomes"、"retention/graduation rate impact"、"accreditation alignment"
- **跟投资人**: 强调"NRR > 110%"、"seat expansion"、"switching cost moat"、"regulatory tailwind"

### 5.3 Voice Samples (8 entries)

1. 「我们不卖软件，我们帮学校省钱。一个教务老师管 300 个学生排课，用我们系统管 3000 个，人效是核心。」(source: T01-S011, 转述 — 张以弛 校宝在线投资者路演)
2. 「Canvas didn't win by being the best LMS. It won by being the LMS teachers actually wanted to use. That's PLG before we called it PLG.」(source: T01-S001, 转述 — Phil Hill On EdTech analysis)
3. 「SCORM is dead, but its zombie walks among us. Every enterprise still has SCORM 1.2 content that 'works' and nobody wants to touch.」(source: T06-S002, 转述 — ADL community discussion on xAPI migration)
4. 「The real metric isn't completion rate. It's whether students who intended to complete actually did. Ho et al. showed that changes everything.」(source: T04-S006, 转述 — Daphne Koller MOOC reflection)
5. 「双减不是灭行业，是换赛道。学科培训没了，但学校的数字化需求反而爆发了。我们从 B2C 转 B2B，营收反而涨了。」(source: T01-S011, 转述 — 张以弛 媒体采访)
6. 「When a district picks Canvas, the five neighboring districts notice. That's the reference institution effect — it's not marketing, it's peer pressure at the superintendent level.」(source: T03-S009, 转述 — EdTech GTM practitioner)
7. 「LTI 1.3 不是可选的。你如果还在跑 LTI 1.1，明年 Canvas 那边就不保证兼容了。1EdTech 说的 sunset 是认真的。」(source: T06-S001, 转述 — 1EdTech conference panel)
8. 「AI detection has a 15-20% false positive rate on ESL students. If you're expelling kids based on Turnitin's AI indicator alone, you're going to get sued.」(source: T03-S007, 转述 — Academic integrity officer community discussion)

---



## 质量基准 + 反模式

### 6.1 什么算「好」

1. **教师 adoption > 70%**: 系统部署后 2 学期内, 超过 70% 教师主动使用 (非强制, 约 80 percentile 学校, 业内估)
2. **NRR > 110%**: 教育 SaaS 的健康 NRR 在 110-130% (seat expansion + module addon)
3. **数据迁移 zero-loss**: SIS 迁移后 100% 学生记录可追溯, 无数据丢失
4. **LTI 集成 < 2 周**: 标准 LTI 1.3 集成从启动到生产不超过 10 个工作日
5. **FERPA/PIPL 合规零违规**: 12 个月内无数据泄露事件或合规投诉

### 6.2 反模式 (外行/入门常犯错误)

1. **强制全校推行 LMS**: 不做渐进式 adoption, 教师 resistance 导致 shadow IT
2. **把完课率当 KPI**: 不做意图分层, 混淆 casual learner 和 degree pursuer
3. **大爆炸 SIS 迁移**: 不做分阶段, 一次性切换导致学期初系统瘫痪
4. **忽视 TCO**: 只看 license 费, 不算运维/培训/集成的真实成本
5. **AI 检测等于抄袭判定**: 不保留教师人工判定环节, 误伤 ESL 学生
6. **把 LTI SSO 当"集成完成"**: 浅集成 (单点登录) ≠ 深集成 (成绩回传 + roster sync)
7. **中国市场用国际产品直接替换**: 忽视钉钉/企微生态 + 支付 + 政策合规差异
8. **教育采购周期错配**: 按 SaaS 创业节奏推进, 忽视学校按学年/财年的预算周期
9. **数据驻留不合规**: 把中国学生数据存海外 / 把欧盟学生数据存美国
10. **忽视"参考机构效应"**: 不找标杆学校做 case study, 缺少 peer influence 杠杆

---



## 智识谱系

### 7.1 流派分布

| 流派 | 奠基 | 当代代表 | 核心主张 |
|------|------|---------|---------|
| 建构主义 EdTech | Piaget → Vygotsky → Papert | George Siemens, Martin Dougiamas (Moodle) | 学习是主动建构, 技术应支持探索而非灌输 |
| 颠覆式创新派 | Christensen | Michael Horn, Josh Coates | 教育变革来自低端市场颠覆, 非 top-down 改革 |
| SaaS 经济学派 | David Skok / Jason Lemkin | Tomasz Tunguz | 教育 SaaS 本质是订阅经济, NRR/CAC/LTV 决定一切 |
| 标准互操作派 | ADL (SCORM) → 1EdTech (LTI/xAPI) | 1EdTech Consortium | 生态系统通过标准连接, 互操作性决定市场位置 |
| 中国政策驱动派 | 教育信息化 1.0/2.0 | 黄荣怀, 余胜泉, 张以弛 | 教育数字化由政策 top-down 推动, 市场跟随政策窗口 |
| 学习科学派 | Bloom → Gagné → Merrill | Todd Rose, 自适应学习公司 | 个性化是终极目标, 技术是实现 2-sigma 的手段 |
| EdTech 批评派 | Audrey Watters | 无当代继承者 (Watters 已退出) | 警惕 EdTech 的 solutionism 和隐私侵蚀 |

### 7.2 核心分歧

1. **开源 vs 商业 LMS**: Dougiamas (开源使命, 教育是公共品) vs Coates (商业 SaaS 推动创新速度)
2. **AI 是功能层还是颠覆层**: Tunguz (AI 效率收益被高估) vs Baker/Khan (AI 使教育真正个性化)
3. **政策驱动 vs 市场驱动**: 中国学派 (政策创造市场) vs 美国学派 (机构自主选择)
4. **规模 vs 互动**: MOOC 路径 (万人同课) vs ClassIn/OMO (小班实时互动)

---



## 诚实边界

### 8.1 信息截止与衰减

- 调研截止 2026-05-26, 工具/工作流模块衰减最快 (约 6-12 月后需刷新)
- AI 功能层变化极快 (季度级), 本 skill 中 AI 相关判断的 shelf-life 约 3-6 个月
- LMS 市场份额数据来自 Phil Hill / Edutechnica 年度报告, 精确数字每年变化 (约 ±3-5%, 业内估)

### 8.2 数据厚度

- EN sources 丰富 (北美高等教育 EdTech 公开材料充足): figures 14 位, sources 28 个, canon 30+ 条
- zh-CN sources 结构性薄弱: 中国教育 SaaS 一手公开材料少 (创始人公开分享 < 5 次/年), 政策文件丰富但产品/运营 know-how 封闭
- surrogate_primary 比例约 65% (大量厂商官网 + 行业媒体, 非直接从 figure 嘴里听到)

### 8.3 不能替代

- 本 skill 不能替代实际教育 SaaS 产品的用户调研和需求验证
- 市场份额数据为行业估算 (非精确审计), 用于趋势判断而非精确预测
- 中国市场政策变化频率高, 双减后的 B2B 红利窗口不必然永续

### 8.4 zh-CN 一手率结构性偏低

中国教育 SaaS 一手内容主要发布在: (1) 微信公众号 (黑名单) (2) 36 氪/芥末堆 (surrogate) (3) 投资人闭门会 (不公开)。公开可引用的中国 figures 一手材料显著少于全球 EdTech 领域。本 skill 的中国部分依赖 surrogate sources (投资报告 + 政策文件 + 少量公开采访), 深度不及英文部分。

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-05-26 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-05-26 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-05-26 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-05-26 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-05-26 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-05-26 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-05-26 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-05-26 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-05-26 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
