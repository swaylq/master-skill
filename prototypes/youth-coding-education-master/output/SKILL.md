---
name: youth-coding-education-master
description: |
  青少年编程教育 (Youth Coding Education) Master OS — automated mastery of Youth Coding Education: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on Youth Coding Education problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「少儿编程」「青少年编程」「编程教育」「编程启蒙」「Scratch教学」
triggers:
  - "少儿编程"
  - "青少年编程"
  - "编程教育"
  - "编程启蒙"
  - "Scratch教学"
  - "Python入门"
  - "信息学奥赛"
  - "信奥赛"
  - "NOIP"
  - "NOI"
  - "机器人教育"
  - "STEAM教育"
  - "创客教育"
  - "计算思维"
  - "编程培训"
  - "youth coding"
  - "kids coding"
  - "CS education K12"
  - "coding for kids"
  - "computational thinking"
  - "robotics education"
  - "scratch programming"
  - "block-based programming"
industry: "Youth Coding Education"
industry-cn: "青少年编程教育"
locale: "global"
last_research_date: "2026-05-26"
source_count: 155
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 青少年编程教育 · Master OS

> This skill makes the agent operate as a senior Youth Coding Education practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 Youth Coding Education 相关的问题时（关键词：少儿编程, 青少年编程, 编程教育, 编程启蒙, Scratch教学, Python入门, 信息学奥赛, 信奥赛, NOIP, NOI, 机器人教育, STEAM教育, 创客教育, 计算思维, 编程培训, youth coding, kids coding, CS education K12, coding for kids, computational thinking, robotics education, scratch programming, block-based programming），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 Youth Coding Education 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：Youth Coding Education 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 课程设计与年龄匹配
- 看什么: 目标学生年龄段 + 认知发展阶段 + 已有编程经验 + 学习目标 (兴趣/竞赛/升学)
- 在哪看: Piaget 认知发展理论 + CSTA K-12 CS Standards 年级对齐表 + 中国信息科技课标 + Code.org 课程年龄推荐
- 输出: 「推荐: {年龄段} → {工具} + {教学法} + {评价方式}; 不推荐: {工具} (原因: {认知发展不匹配}); 过渡方案: {桥接课程}」

#### 维度 2: 竞赛路线评估与规划
- 看什么: 学生数学基础 + 编程能力 + 投入意愿 + 目标赛事 (CSP-J/S / NOIP / NOI / IOI)
- 在哪看: 洛谷题目难度评级 + CCF 官网赛事日历 + 历年真题分析 + 省选/NOI 录取分数线 (各省不同)
- 输出: 「当前水平: {洛谷评级}; 目标赛事: {赛事} (约 {难度}); 训练计划: {知识板块序列} × {每周时长}; 预期时间: {月}; 风险: {政策变化/心理压力}」

#### 维度 3: 工具选型与技术栈
- 看什么: 教学目标 (启蒙/进阶/竞赛/创客) × 学生年龄 × 预算 × 教师技术能力
- 在哪看: 工具官方文档 + CSTA 推荐工具列表 + 教育技术评测 (EdSurge/Common Sense Media) + 硬件价格比较
- 输出: 「推荐: {工具栈}; 人均成本: {金额}; 教师培训需求: {时长}; 替代方案: {低成本选项}; 避坑: {不推荐的工具及原因}」

#### 维度 4: 政策合规审查
- 看什么: 办学形式 (线上/线下/进校) × 地域 × 课程类型 (学科/素质) × 收费模式
- 在哪看: 教育部双减政策文件 + 各地教育局实施细则 + 校外培训行政处罚暂行办法 (2023) + COPPA/GDPR (海外市场)
- 输出: 「合规状态: {合规/灰区/违规}; 关键要求: {3-5 条}; 最高风险: {预付费/资质/内容审查}; 建议: {合规路径}」

#### 维度 5: 教师招聘与培训评估
- 看什么: CS 背景比例 + 教学经验 + 编程能力 (能否独立写中等复杂度项目) + 与学生互动能力
- 在哪看: CSTA 教师标准 + ISTE 认证体系 + 中国信息科技教师资格要求 + 行业薪资数据
- 输出: 「当前教师画像: {背景分布}; 缺口: {N 人 × 能力维度}; 培训方案: {时长 × 内容}; 预算: {人均}; 留存策略: {激励机制}」

#### 维度 6: 家长沟通与预期管理
- 看什么: 家长核心诉求 (升学/兴趣/能力) + 对编程教育的认知水平 + 付费意愿
- 在哪看: 家长常见问题库 (本 skill playbook 8 提供框架) + 竞赛政策最新动态 + 行业续费率数据
- 输出: 「家长核心问题: {列表}; 诚实回答: {每个问题的事实+限制}; 不应承诺: {列表}; 展示方式: {作品/视频/竞赛成绩}」

#### 维度 7: AI 工具整合评估
- 看什么: AI 工具类型 (辅助编程/自动评测/对话辅导) × 学生年龄 × 教学目标 × 竞赛规则
- 在哪看: Khanmigo 负责任 AI 框架 + IOI 2024+ AI 使用规定 + Code.org Hour of AI + 教师反馈
- 输出: 「AI 适用场景: {列表}; 禁用场景: {列表, 特别是竞赛}; 护栏设计: {技术+流程}; human-in-the-loop: {教师审核机制}」

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 制作即学习 (Making Is Learning)

- **一句话**: 编程教育的核心不是教「编程语言语法」, 而是让学生通过创造可分享的外部作品来建构内部知识 — Papert 的建构主义 (constructionism) 是整个领域的哲学根基
- **应用方式**: 设计课程时, 每个单元必须有一个学生可以「做出来给别人看」的作品 (游戏/动画/机器人/网站), 而非做完 20 道选择题. Resnick 的 4P 框架 (Projects/Passion/Peers/Play) 是操作化版本
- **局限**: 建构主义对结构化知识传授效率低于直接教学 (direct instruction), 在信奥赛等需要系统性知识积累的场景中需要与直接教学混合; 纯项目式学习容易「做了很多但基础不扎实」; Kirschner 2006 对 minimal guidance 的批评在实证上有支持
- **figures**: Papert (建构主义奠基) / Resnick (4P + Scratch) / Martinez & Stager (Maker 教育) / Tim Bell (CS Unplugged 具身化)
- **evidence**: [T04-S009, T04-S008, T01-S002, T01-S003, T04-S018]

### 1.2 低地板、高天花板、宽墙壁 (Low Floor, High Ceiling, Wide Walls)

- **一句话**: 好的编程教育工具必须同时满足三个维度 — 入门门槛低 (low floor, 6 岁能开始)、能力上限高 (high ceiling, 能做复杂项目)、创作方向广 (wide walls, 不限于一种项目类型) — 这是 Scratch 的设计哲学, 也是评估任何 K12 编程工具的核心框架
- **应用方式**: 选型编程教学工具时, 用这三个维度打分: Scratch floor 极低 + ceiling 中等 + walls 极宽; C++ floor 高 + ceiling 极高 + walls 窄 (竞赛). 大多数工具只满足 1-2 个维度, 找到平衡点是课程设计的核心决策
- **局限**: 追求 low floor 容易牺牲 high ceiling (Scratch 的天花板确实有限, 复杂算法表达困难); wide walls 可能导致学生分散注意力而非深入; 这个框架对评估硬件工具 (机器人) 适用度较低
- **figures**: Resnick (Scratch 设计) / Malan (CS50 的 low floor 设计) / Bau et al. (Blocks and Beyond)
- **evidence**: [T01-S003, T01-S001, T04-S016, T04-S011]

### 1.3 计算思维不等于编程 (CT ≠ Coding)

- **一句话**: 计算思维 (Computational Thinking) 是抽象、分解、模式识别、算法设计四种跨学科思维能力的组合 — 它的价值不在于「写出可运行的代码」, 而在于用计算方式思考任何领域的问题. 把编程课等同于 CT 培养是行业最常见的概念错位
- **应用方式**: 课程设计时, CT 的四个维度 (抽象/分解/模式识别/算法) 应该出现在数学、科学、甚至语文课中, 不只是编程课; CS Unplugged 证明不用电脑也能教 CT; 但反过来, 纯 CT 教学如果完全不接触编程, 「迁移」(transfer) 的实证支持也很弱
- **局限**: Wing 2006 的 CT 定义被批评过于宽泛 (Guzdial: 「什么都算 CT 就什么都不算」); CT 能否迁移到其他学科的实证证据不一致 (Grover & Pea 2013 综述); 中国新课标把 CT 作为核心素养, 但一线教师对 CT 的理解差异很大
- **figures**: Wing (CT 概念提出) / Grover & Pea (CT 综述) / Guzdial (CT 批评) / 熊璋 (中国课标落地)
- **evidence**: [T01-S005, T04-S001, T04-S006, T01-S028, T01-S029]

### 1.4 年龄决定抽象层 (Age Determines Abstraction Layer)

- **一句话**: K12 编程教育的核心设计约束是 Piaget 认知发展阶段 — 6-9 岁 (具体操作期) 只能处理视觉化的积木编程, 10-12 岁 (形式操作期过渡) 可以开始文本编程, 13+ 岁才能处理递归/数据结构等抽象概念. 违反这个规律的课程设计 (如 4 岁学 Python) 是伪科学营销
- **应用方式**: 课程体系按年龄分 3 层: 积木层 (Scratch/ScratchJr, 6-10) → 文本层 (Python/JavaScript, 10-14) → 竞赛/工程层 (C++/数据结构, 13-18). 每层之间需要桥接课程 (如 Scratch→Python 的「从积木到代码」过渡课). 跳层是最常见的教学失败原因
- **局限**: 个体差异很大, 部分儿童 8 岁就能处理文本编程; Piaget 的年龄划分不是硬性边界; 「Use-Modify-Create」等教学法可以在一定程度上突破年龄限制; 中国信奥赛体系实际上要求 10-11 岁就接触 C++, 与认知发展理论存在张力
- **figures**: Resnick (ScratchJr 4-7岁设计) / Bau et al. (Blocks and Beyond 桥接研究) / Brennan & Resnick (CT 评估框架含年龄维度)
- **evidence**: [T04-S008, T04-S016, T04-S005, T06-S001]

### 1.5 竞赛与普及是两条平行赛道 (Competition ≠ Universal Education)

- **一句话**: 信息学奥赛 (OI/NOI/IOI) 和全民编程教育 (CS for All) 是目标、方法、工具、评价标准完全不同的两条赛道 — 混淆二者是中国少儿编程行业最大的认知陷阱, 导致大量不适合竞赛的孩子被推入竞赛训练, 或者竞赛生被困在过于基础的普及课程中
- **应用方式**: 入学评估后第一个决策点: 这个孩子适合普及路线 (创意编程 + 项目式学习) 还是竞赛路线 (算法训练 + OJ 刷题)? 两条路线的工具链不相通 (Scratch vs C++/洛谷), 教师能力模型不同 (创意引导 vs 算法教练), 过早分流和过晚分流都有害
- **局限**: 现实中两条赛道有交叉地带 (如 Python 既是普及语言也是 CSP-J 考试语言); 部分家长把竞赛当升学工具而非兴趣选择, 这个心智模型不能改变家长决策逻辑; 竞赛路线也需要创造力, 不是纯刷题
- **figures**: 刘汝佳 (竞赛路线标杆) / Partovi + Guzdial (CS for All 路线) / 李天驰 (两条赛道都做的商业实践)
- **evidence**: [T01-S017, T01-S007, T01-S025, T04-S013]

### 1.6 教师是瓶颈, 不是工具 (The Bottleneck Is Teachers, Not Tools)

- **一句话**: 全球 K12 编程教育推广的最大障碍不是缺工具 (Scratch 免费, Code.org 免费, micro:bit 约 15 美元), 而是缺合格教师 — 大多数 K12 学校没有受过 CS 教育训练的教师, 现有教师把编程当「又一门学科」而非「一种思维方式」来教
- **应用方式**: 任何编程教育方案的可行性, 先问「教师从哪里来?」Code.org 的核心价值不是课程内容而是教师培训体系 (约 10 万+ 教师培训, 业内估); CAS 的成功是因为 4.3 万+ 教师社区; 培训机构的教师流失率是核心运营风险
- **局限**: AI 辅助教学 (Khanmigo 等) 正在部分缓解教师瓶颈, 但 2026 年仍缺乏独立 RCT 验证; 教师瓶颈在中国尤其严重 (信息科技课标 2022 要求所有小学开设, 但合格教师缺口巨大); 过度依赖教师也是问题 — 好的工具应该降低对教师能力的依赖
- **figures**: Peyton Jones (CAS 43000+ 教师社区) / Yongpradit (Code.org 教师培训) / Guzdial (教师作为研究者) / 熊璋 (中国教师培训政策)
- **evidence**: [T01-S021, T01-S008, T01-S010, T01-S028]

### 1.7 作品是最好的评价 (Portfolio Over Test Score)

- **一句话**: 编程教育的成果评价不应该是选择题考试, 而是学生创作的作品集 (portfolio) — 一个能运行的 Scratch 游戏比 100 道 CT 选择题更能证明学生掌握了编程思维. 但行业现实是考试和等级证书更容易卖给家长
- **应用方式**: 课程评价体系分两层: 形成性评价用作品 (每课一个小项目 + 每学期一个大项目 + 公开展示); 终结性评价用 Brennan & Resnick 的 CT 评估框架 (概念/实践/视角三维度) 而非纯选择题. 竞赛路线评价天然是作品 (算法提交 + OJ 判定)
- **局限**: 作品评价缺乏标准化, 难以跨机构比较; 家长和学校更信任量化分数和证书; 等级考试 (中国电子学会等) 有市场需求但评价效度存疑; CT 的标准化评估工具 (如 Bebras / Dr. Scratch) 仍在研究阶段, 尚无 canonical 工具
- **figures**: Brennan & Resnick (CT 评估框架) / Resnick (Scratch 社区展示机制) / Bell (CS Unplugged 评估方法)
- **evidence**: [T04-S005, T04-S003, T01-S013, T03-S001]

---



## 标准 Playbook

1. **如果学生是 6-9 岁初学者**: 则从 Scratch 或 ScratchJr 开始积木编程, 不要从文本语言开始 — 积木编程消除了语法错误障碍, 让学生聚焦于逻辑和创意. 案例: Code.org CS Fundamentals 课程对齐 K-5, 全球约 5000 万+ 学生使用 (业内估, Code.org 2025 年报)

2. **如果学生从积木编程过渡到文本编程**: 则选 Python 而非 C++/Java 作为第一文本语言 (除非目标明确是信奥赛) — Python 语法接近自然语言, 缩进强制代码结构, 交互式解释器支持即时反馈. 过渡期用「Use-Modify-Create」教学法 (先用别人的代码 → 修改 → 自己创造). 案例: 英国 CAS 课标推荐 Python 作为 KS3 (11-14 岁) 核心语言 (evidence: [T01-S021, T06-S001])

3. **如果要判断一个孩子适合竞赛路线还是普及路线**: 则看三个信号: (a) 是否对「解出难题」本身感到快乐 (而非被家长/奖励驱动); (b) 数学基础是否在年级前 10% (业内估); (c) 是否愿意持续投入 (每周约 10-15 小时, 业内估). 三项都是 → 竞赛; 否则普及. 案例: 中国信奥赛体系 (NOI) 每年约 15 万+ 考生参加 CSP-J/S (业内估, CCF 公告), 但最终进省队的不到 1% (evidence: [T01-S017, T04-S013])

4. **如果在信奥赛训练中选择 OJ 平台**: 则中国学生首选洛谷 (14000+ 题, 中文社区, CSP/NOIP 真题全覆盖), 补充 Codeforces (国际赛事训练); USACO 用于模拟美赛难度; LeetCode 不适合信奥赛 (面向面试而非竞赛). 案例: 洛谷赛前日提交量约 15-25 万次 (业内估, 2026) (evidence: [T02-S001, T01-S017])

5. **如果选择机器人/硬件教育路线**: 则按预算分层: 低预算 (约 15 美元/人) → BBC micro:bit (传感器丰富 + MakeCode 积木 + Python 双模式); 中预算 (约 100-200 美元/人) → Makeblock mBot (图形化 + Python + 金属结构); 高预算 (约 400+ 美元/人) → LEGO SPIKE Prime (成熟课程体系 + 竞赛级). 注意: LEGO Mindstorms EV3 已停产 (2022), 不要再采购. 案例: 英国 BBC 于 2016 年向全国 100 万名 7 年级学生免费发放 micro:bit (evidence: [T02-S001, T01-S018])

6. **如果开设培训机构的编程课**: 则课消 (课时消耗率) 而非招生数才是核心健康指标 — 课消 = 已消耗课时 / 已售课时. 课消低意味着预收款是负债而非收入; 续费率低于 60% (业内估) 是危险信号. 案例: 2022 年多家少儿编程机构爆雷 (编程猫裁员、VIPCODE 关停) 的共同特征是课消低 + 预收款高 (evidence: [T06-S001, T03-S001])

7. **如果设计编程课的评价体系**: 则采用「作品集 + CT 维度量规」双轨制, 不要只用选择题考试 — Brennan & Resnick CT 框架三维度: 概念 (CT 概念掌握) / 实践 (编程实践能力) / 视角 (对计算的理解). 每个维度 3-4 级量规. 案例: Scratch 社区的 Remix 机制本身就是一种同伴评价系统 (evidence: [T04-S005, T04-S003])

8. **如果家长问「学编程对升学有帮助吗」**: 则诚实回答: (a) 直接加分路径仅剩 NOI/IOI 竞赛省一等奖以上 (各省政策不同, 需核实当年规定); (b) 中考没有直接帮助; (c) 高考强基计划认可信奥赛成绩; (d) 真正的价值是计算思维能力, 不是升学加分. 不要用「AI 时代必学」的恐惧营销. 案例: 2024 年双减后 CCF 持续调整 CSP-J/S 政策边界 (evidence: [T06-S001, T01-S029])

9. **如果引入 AI 辅助编程教学 (如 GitHub Copilot / Khanmigo)**: 则必须: (a) 明确 AI 是助手不是替代; (b) 禁止学生直接让 AI 写完整代码 (违背学习目标); (c) 教师必须审核 AI 生成的代码/反馈; (d) 竞赛训练中完全禁用 AI (IOI 2024+ 明确规定). 案例: Code.org 2025 年推出 Hour of AI 活动, 但始终保持 AI 是 「工具」而非「教师」的定位 (evidence: [T01-S007, T02-S001])

10. **如果课程设计不确定先教什么后教什么**: 则遵循 Scratch 社区验证的「创意螺旋」: 想象 (imagine) → 创造 (create) → 玩耍 (play) → 分享 (share) → 反思 (reflect) → 想象. 不要用「先讲理论再做练习」的传统模式 — 编程教育是实践驱动而非理论驱动. 案例: Resnick 在 *Lifelong Kindergarten* 中用 Scratch 社区约 1.5 亿用户 (业内估, 2025) 的项目数据验证了创意螺旋模式 (evidence: [T04-S008, T01-S003])

---



## 工具栈与选型决策树

### 3.1 必备工具 (8 件, 约 80% 编程教育从业者会用)

1. **Scratch** (MIT, 免费, 6-12 岁积木编程标准, 约 1.5 亿注册用户)
2. **Python** (文本编程主力语言, 10-18 岁全覆盖, 免费)
3. **C/C++** (信奥赛核心语言, NOI/IOI/USACO 必备)
4. **Code.org** (K-12 课程+平台一体, 免费, 约 80M+ 学生)
5. **洛谷** (中国信奥赛 OJ 标准, 14000+ 题, 免费)
6. **BBC micro:bit** (物理计算入门硬件, 约 15 美元, MakeCode+Python 双模)
7. **在线 IDE** (Replit / Trinket / Thonny, 免去本地环境配置)
8. **LEGO SPIKE Prime** (高端机器人教育标准, FLL 竞赛级)

### 3.2 场景特化 (6 类, 按教学场景分)

- **启蒙/低龄 (4-7岁)**: ScratchJr (MIT, iPad) + Code.org CS Fundamentals + CS Unplugged 不插电活动
- **竞赛训练**: 洛谷 + Codeforces + USACO Training + Vjudge (跨 OJ 聚合)
- **机器人/创客**: micro:bit + Arduino (开源) + Makeblock mBot + VEX (竞赛级)
- **游戏化编程**: CodeMonkey + Tynker + Roblox Studio + Minecraft Education
- **AI/ML 启蒙**: Teachable Machine (Google) + ml5.js + Scratch AI 扩展
- **机构管理**: 校管家/小鹅通 (排课CRM) + ClassIn/Zoom (直播) + 有赞教育

### 3.3 新兴工具 (近 12 个月, 5 类)

- AI 辅助编程教学: GitHub Copilot Education Plan + Khanmigo (Khan Academy)
- LLM 辅导: Claude/GPT-4 作为编程导师 (需护栏, 未经独立 RCT)
- MIT OctoStudio: Resnick 团队新作, 移动端积木编程 (2023-)
- Micro:bit V2 生态扩展 (扬声器/麦克风, 新课程线)
- MakeCode Arcade: 微软 block-to-code 游戏开发环境

### 3.4 避坑清单

1. 不要给 6 岁孩子从 Python 开始 (认知发展不匹配)
2. 不要用 LEGO Mindstorms EV3 开新课 (2022 年停产, 配件断供)
3. 不要把 LeetCode 当信奥赛训练平台 (面试导向 ≠ 竞赛导向)
4. 不要在竞赛训练中使用 AI 辅助 (IOI 2024+ 规则禁止)
5. 不要只看 GitHub stars 选教学工具 (教育场景 ≠ 开发场景)
6. 不要把 Replit Teams for Education 写入长期规划 (2024 年 8 月已停止)
7. Tynker 母公司 BYJU'S 2024 年破产保护, 产品稳定性存疑
8. 不要以为 Scratch 可以一路用到高中 (天花板约在初中水平)

---



## 工作流 / Pipeline

### 1. 设计一堂 Scratch 启蒙课

- **Trigger**: 新学期/新班级首次编程课
- **Output**: 60 分钟课件 + 学生可运行项目

**入门 SOP**: 1. 确定教学目标 (选 1-2 个 CT 概念如顺序+循环). 2. 选择项目载体 (动画/游戏/故事). 3. 准备素材 (角色/背景/音效). 4. 设计「演示→模仿→创作」三段式课堂. 5. 准备分层任务卡 (基础版+挑战版). 6. 试讲一遍调整节奏.

- **资深路径**: 跳过 逐步演示 (改用「先让学生猜功能」的探索式引入). 优化 素材准备 (用 Scratch 社区 remix 已有项目而非从零做). 额外 设计「学生互评」环节 (同伴学习).
- **近期变化**: 2025 年起 Scratch 内置 AI 扩展, 可在启蒙课中加入简单 AI 交互
- **last_updated**: 2026-05
- **Decay risk**: low

### 2. 规划 Python 进阶课程体系

- **Trigger**: 学生从 Scratch 毕业 / 新生直接入 Python
- **Output**: 24-48 课时课程大纲 + 配套项目

**入门 SOP**: 1. 学情评估 (有无 Scratch 基础 / 数学水平). 2. 选择路线 (turtle 绘图→pygame 游戏 vs 数据分析→AI). 3. 设计知识点序列 (变量→条件→循环→函数→列表→文件). 4. 每 4 课时配 1 个综合项目. 5. 准备在线 IDE 环境 (Replit/Thonny). 6. 设计形成性评价量规.

- **资深路径**: 跳过 turtle 绘图阶段 (对有 Scratch 基础的学生直接进实用项目). 优化 项目选题 (让学生自选主题而非统一项目). 额外 引入 Git 基础 (让学生管理自己的代码版本).
- **近期变化**: 2025-2026 年 AI 辅助编程 (Copilot/Cursor) 进入教学, 教师需要教「如何与 AI 协作编程」而非单纯写代码
- **last_updated**: 2026-05
- **Decay risk**: medium

### 3. 设计信奥赛训练计划

- **Trigger**: 学生决定走竞赛路线 (通常 10-12 岁)
- **Output**: 12-24 个月分阶段训练计划

**入门 SOP**: 1. 能力摸底 (用洛谷入门题评估当前水平). 2. 制定知识图谱 (基础→提高→省选→NOI). 3. 选定核心教材 (紫书→白书→进阶指南). 4. 每周约 10-15 小时训练 (做题+总结+模拟赛). 5. 每月 1 次全真模拟赛. 6. 赛前 3 个月冲刺 (真题+弱项专练).

- **资深路径**: 跳过 按教材顺序刷题 (改用「弱项驱动」策略: 先做题暴露弱项再针对性学). 优化 模拟赛 (用 Codeforces 虚拟赛代替自制模拟). 额外 心理训练 (比赛策略: 先做确定能做的题, 不在一道题上死磕).
- **近期变化**: 2024 年 CCF 调整 CSP-J/S 题型, 更重视实际问题建模能力而非纯算法套路
- **last_updated**: 2026-05
- **Decay risk**: medium

### 4. 设计机器人/创客课程

- **Trigger**: 机构增设硬件课程线 / 学校 STEAM 需求
- **Output**: 硬件选型 + 课程大纲 + 耗材采购清单

**入门 SOP**: 1. 确定目标年龄和预算. 2. 硬件选型 (micro:bit/Arduino/LEGO). 3. 设计 8-16 课时课程 (每课一个小项目). 4. 采购硬件 + 测试 (含损耗备份约 20%, 业内估). 5. 试运行 1 个班收集反馈. 6. 迭代课程.

- **资深路径**: 跳过 单一硬件路线 (混合多硬件让学生选). 优化 采购 (用开源方案降低人均成本). 额外 对接 FLL/WRO 竞赛标准 (课程产出直接参赛).
- **近期变化**: EV3 停产后 SPIKE Prime 成主流 (2022-), micro:bit V2 新增音频功能拓宽课程空间
- **last_updated**: 2026-05
- **Decay risk**: medium

### 5. 新建少儿编程培训机构

- **Trigger**: 创业/加盟决策
- **Output**: 选址+装修+招生+师资+课程+系统全链条

**入门 SOP**: 1. 市场调研 (区域竞争+目标客群). 2. 选址 (学校周边 200 米内, 业内估 最优). 3. 课程体系选型 (自研 vs 加盟). 4. 招聘+培训教师 (核心瓶颈). 5. 搭建管理系统 (排课/CRM/财务). 6. 开业招生 (公开课→体验课→正课转化).

- **资深路径**: 跳过 加盟 (自研课程利润率更高). 优化 选址 (用数据分析周边学校密度和家庭收入). 额外 政策合规 (办学许可/消防/预付费监管).
- **近期变化**: 双减后非学科类培训监管加强, 预付费不得超过 3 个月 (部分城市已执行)
- **last_updated**: 2026-05
- **Decay risk**: medium

### 6. 招生与转化流程

- **Trigger**: 新学期/寒暑假前 2 个月
- **Output**: 体验课→正课转化漏斗

**入门 SOP**: 1. 设计体验课 (60 分钟, 学生做出一个小作品). 2. 渠道投放 (学校周边/家长群/公众号). 3. 到店接待 (家长旁听+孩子体验). 4. 课后跟进 (24 小时内电话/微信). 5. 转化谈单 (展示学习路径+作品展示). 6. 售后跟进 (第 1/4/8 课回访).

- **资深路径**: 跳过 统一体验课 (改用个性化诊断式体验). 优化 转化 (让已有学员家长做转介绍, 转化率远高于广告). 额外 建立家长社群 (持续运营而非一次性转化).
- **近期变化**: 2025 年起家长对 AI 编程教育兴趣激增, 体验课中加入 AI 元素显著提升到店率
- **last_updated**: 2026-05
- **Decay risk**: low

### 7. 教师培训与认证

- **Trigger**: 新教师入职 / 课程体系升级
- **Output**: 培训方案 + 教学能力评估标准

**入门 SOP**: 1. 评估教师技术基线 (编程能力+教学经验). 2. 分层培训 (技术培训+教学法培训). 3. 试讲考核 (模拟授课+导师反馈). 4. 跟课实习 (跟资深教师 2-4 周). 5. 独立上课 (前 4 周主管旁听). 6. 定期教研 (每周 1 次教研会).

- **资深路径**: 跳过 通用技术培训 (针对弱项专练). 优化 试讲 (用学生真实项目而非模拟题). 额外 建立教师成长路径 (初级→高级→教研→培训师).
- **近期变化**: 2025-2026 AI 工具普及, 教师需额外学习如何在课堂中引导学生使用/不使用 AI
- **last_updated**: 2026-05
- **Decay risk**: medium

### 8. 一堂编程课的交付流程

- **Trigger**: 课前 10 分钟
- **Output**: 学生完成项目 + 教学反思

**入门 SOP**: 1. 复习上节课内容 (5 分钟). 2. 引入新知识 (演示+提问, 10 分钟). 3. 实践 (学生编程, 25-30 分钟). 4. 展示分享 (3-5 个学生展示作品, 10 分钟). 5. 总结+布置课后探索 (5 分钟). 6. 课后写教学反思.

- **资深路径**: 跳过 教师演示 (改用「先让学生试错」的发现式教学). 优化 实践环节 (设置分层任务, 快的学生有挑战任务). 额外 嵌入同伴互评 (学生两两互看代码).
- **近期变化**: AI 辅助编程工具在课堂中的角色定位是 2025-2026 年核心教学设计变化
- **last_updated**: 2026-05
- **Decay risk**: low

### 9. 编程作品评价与展示

- **Trigger**: 单元结束 / 学期末 / 竞赛前
- **Output**: 作品集 + 评价报告 + 展示活动

**入门 SOP**: 1. 明确评价标准 (CT 三维度量规). 2. 学生整理作品集 (选 3-5 个最佳作品). 3. 教师评分 (量规打分+书面反馈). 4. 同伴互评 (每人评 2-3 个同伴作品). 5. 公开展示活动 (家长/全校). 6. 生成评价报告.

- **资深路径**: 跳过 教师统一评分 (改用学生自评+同伴评为主). 优化 展示 (线上+线下混合, 用 Scratch 社区/GitHub Pages 发布). 额外 邀请行业从业者做评委 (增加真实感).
- **近期变化**: 2025 年起 AI 生成代码引发「作品原创性」评价挑战, 需在量规中加入「解释代码」环节
- **last_updated**: 2026-05
- **Decay risk**: medium

### 10. 备战 NOIP/NOI 冲刺

- **Trigger**: 赛前 3-6 个月
- **Output**: 冲刺计划 + 模拟赛 + 心理准备

**入门 SOP**: 1. 真题诊断 (做近 3 年真题, 定位弱项). 2. 专项突破 (每周集中攻一个知识板块). 3. 每周 2-3 次全真模拟赛 (含时间管理训练). 4. 错题复盘 (每题写解题报告). 5. 心理调适 (比赛策略: 先易后难, 不纠结). 6. 赛前 1 周减量 (保持手感, 不学新内容).

- **资深路径**: 跳过 按知识点顺序复习 (改用弱项驱动+概率分析: 哪类题出现概率高且自己弱). 优化 模拟赛 (用 Codeforces Div.2 级别模拟, 更贴近真实难度). 额外 建立「比赛日清单」(设备检查/心理调整/时间分配策略).
- **近期变化**: CSP-J/S 2024 改革后题目更重实际建模, 纯模板题比例下降
- **last_updated**: 2026-05
- **Decay risk**: medium

---



## 表达 DNA

### 5.1 高频用语 / 黑话

- CT (计算思维) — 学术圈/政策圈首选词, 培训机构常用「逻辑思维」替代 (降级版)
- 积木编程/图形化编程 — 指 Scratch 类 block-based 语言, 内行不说「拖拽编程」
- OJ (在线评测) — 竞赛圈核心工具, 「在洛谷上 AC 了」是标准表达
- AC / WA / TLE / MLE / RE — OJ 评测结果缩写, 竞赛生日常用语
- 课消 — 课时消耗率, 培训机构核心运营指标, 外行常混淆为「上了多少课」
- Low Floor High Ceiling — MIT 圈评价工具设计的标准表达
- 4P 框架 — Projects / Passion / Peers / Play, Resnick 核心术语
- 信息科技 — 2022 年新课标改名 (原「信息技术」), 内行必须用新名
- CSP-J / CSP-S — CCF 非专业级/专业级考试, 2019 年从 NOIP 改制
- 双减 — 2021 年政策, 影响所有校外培训, 编程属素质类但灰色地带

### 5.2 Outsider tells (外行破绽, 10 类)

1. 把 NOIP 叫「国际比赛」— 是全国联赛 (National), IOI 才是国际
2. 把 CT (计算思维) 理解为「计算机方面的思维」— 是跨学科问题求解框架
3. 把 Constructionism (建构主义) 和 Constructivism (建构论) 混淆 — 前者强调制品, 后者强调认知
4. 把课消高等同于收入高 — 课消低才是收入确认障碍, 预收款高是负债
5. 把双减理解为「编程培训全禁」— 编程属素质类, 有灰色地带
6. 把 CSP (CCF 考试) 理解为网络安全证书 (Certified Security Professional)
7. 把 Block-based 认为只适合低龄 — Snap!/App Inventor 支持高中水平
8. 把等级证书和 NOI/CSP 竞赛证书混为一体 — 完全不同的体系
9. 说「学编程 = 学 Scratch」— Scratch 只是工具之一
10. 说「培养逻辑思维」而不提 CT 四要素 — CT 有严格定义, 「逻辑思维」是商业简化

### 5.3 对话样本库

#### 5.3.1 教学设计场景
- 「We don't teach coding; we teach kids to express themselves through coding. The code is the medium, not the message.」(source: T01-S002, 转述 Resnick, 教育理念场景)
- 「Computational thinking is the thought processes involved in formulating problems and their solutions so that the solutions are represented in a form that can be effectively carried out by an information-processing agent.」(source: T01-S005, 原话 Wing, 学术定义场景)
- 「先不要急着教循环, 让孩子先玩够 — 他发现重复贴积木太累了, 自然会问有没有更快的方法, 那时候再教循环, 一遍就会」(source: T03-S001, 推断, 一线教师场景)

#### 5.3.2 竞赛圈场景
- 「这道题暴力能过 60 分, 正解需要线段树, 你先交暴力保底再想优化」(source: T03-S001, 推断, 竞赛教练场景)
- 「NOIP 不是比谁算法多, 是比谁读题准、打字稳、不犯低级错误」(source: T01-S017, 推断, 竞赛文化场景)

#### 5.3.3 机构运营场景
- 「课消才是真指标. 你招了 500 个学生但课消 30%, 那 70% 是你欠人家的」(source: T06-S001, 推断, 机构运营场景)
- 「体验课最重要的不是教会什么, 是让孩子走出来的时候跟妈妈说『我还想来』」(source: T03-S001, 推断, 招生转化场景)

#### 5.3.4 家长沟通场景
- 「编程不是为了让孩子当程序员, 是让他学会把大问题拆成小问题 — 这个能力写作文、做数学应用题都用得上」(source: T01-S007, 推断, 家长沟通场景)

#### 5.3.5 反例
- 「3 岁学编程, 赢在起跑线」→ 反例: 违反 Piaget 认知发展阶段, 无实证支持, 是焦虑营销
- 「学了编程就能上名校」→ 反例: 只有 NOI 省一以上有直接升学价值, 且政策年年变
- 「AI 时代不学编程就被淘汰」→ 反例: 恐惧营销; 编程≠AI, CT 才是核心, 且不是唯一重要能力
- 「我们的课程全面对标信奥赛」→ 反例: 若课程是 Scratch, 与 NOI (C++) 毫无关系

voice_confidence: medium (教学设计场景一手语料多; 竞赛圈一手在封闭社区; 运营场景推断为主)

---



## 质量基准 + 反模式

### 6.1 质量基准

1. **课程每课有可运行作品**: 不是做完选择题, 是做出东西
2. **CT 四维度覆盖**: 课程体系覆盖抽象/分解/模式识别/算法思维, 不只教语法
3. **年龄-抽象层匹配**: 6-9 积木 / 10-14 文本 / 14+ 竞赛/工程, 不跳层
4. **续费率 ≥ 60%** (业内估): 低于此线说明课程/教师有问题
5. **教师 CS 背景率 ≥ 50%** (业内估): 非 CS 背景教师需额外培训

### 6.2 反模式

1. 给 6 岁孩子教 Python 文本编程 (认知发展不匹配)
2. 把 Scratch 教学等同于 CS 教育全部 (CT ≠ Scratch)
3. 用考试分数作为唯一评价方式 (作品集更有效)
4. 不区分竞赛路线和普及路线 (目标/方法/工具完全不同)
5. 以「升学加分」作为核心卖点 (政策不稳定 + 误导)
6. 教师不会编程只会念课件 (编程教育核心是示范)
7. 课程只教工具不教思维 (Scratch 语法会过时, CT 不会)
8. 预收费超过 3 个月课时 (合规风险 + 跑路风险)
9. AI 辅助编程完全不设限制 (学生直接用 AI 写代码失去学习意义)
10. 竞赛训练只刷题不做项目 (缺乏创造力培养, 与 CT 目标矛盾)

---



## 智识谱系

### 7.1 流派

| 学派 | 奠基 | 当前代表 | 核心主张 |
|------|------|---------|---------|
| 建构主义 (Constructionism) | Papert 1980 (Mindstorms) | Resnick (Scratch/MIT), Martinez & Stager | 学习=制作可分享的作品, 教师是引导者非讲授者 |
| 计算思维 (CT) 理论 | Wing 2006 (CACM) | Grover & Pea, Weintrop, 熊璋 (中国课标) | CT 是跨学科通用能力, 不只是编程技能 |
| CS for All 运动 | Partovi 2013 (Code.org) | Malan (CS50), Guzdial, Yongpradit | CS 是基础素养, 每个学生都应学习 |
| 竞赛教育 (OI/IOI) | NOI 1984 / IOI 1989 | 刘汝佳, 李煜东, USACO | 通过算法竞赛培养精英, 强调问题求解能力 |
| 英国学派 (CAS) | Peyton Jones 2013 (Computing 课标) | Raspberry Pi Foundation, Hello World 社区 | CS 是国家课程核心学科, 教师社区是关键 |
| 不插电 CS (Unplugged) | Tim Bell 1999 (CS Unplugged) | Bell, 各国小学教师 | 不用电脑也能教 CS 核心概念, 降低门槛 |
| 教育技术枢纽 | 余胜泉 (北师大), 任友群 (华东师大) | 中国课标编制组 | 技术与课标融合, 本土化路径 (课标/双减/等级考试) |
| Maker/STEAM 教育 | Dougherty 2005 (Make 杂志) | FIRST (Kamen), Makeblock (Jasen Wang) | 动手制作+跨学科整合, 机器人是最佳载体 |

### 7.2 核心分歧 (保留)

1. **建构主义 vs 直接教学**: Papert/Resnick 阵营 (让孩子自由创造) vs 传统课堂 (系统性知识传授) — 实际教学中需要混合, 纯建构效率低, 纯讲授无趣
2. **竞赛 vs 普及**: NOI/IOI 精英路线 vs CS for All 全民路线 — 中国市场两条赛道并行且经常被混淆
3. **积木 vs 文本**: Scratch 类图形化 vs Python/C++ 文本 — 争论焦点是积木编程是否算「真编程」
4. **CT 定义之争**: Wing 宽定义 (任何人都应具备的计算思维) vs Guzdial 窄定义 (以学习者为中心的具体教学实践)
5. **证书/考试 vs 作品评价**: 等级考试 (中国电子学会等) 提供标准化评价 vs Brennan/Resnick 主张作品集评价更有效
6. **AI 在编程教育中的角色**: AI 辅助编程 (Copilot 帮学生写代码) vs AI 威胁编程教育存在价值 (如果 AI 写代码更好, 为什么还要学?)

---



## 诚实边界

- **信息截止 2026-05-26**, 工具/工作流衰减最快 (建议每 3-6 个月刷新)
- **AI 冲击 in progress**: Khanmigo/Copilot 等 AI 工具正在改变编程教学, 但 2026 年仍缺乏独立 RCT 验证; 本 skill 心智模型主要基于 pre-AI 时代 CS 教育研究
- **中国政策不稳定**: 双减后编程培训的政策边界持续变化, 各地执行口径差异约 30% (业内估); 本 skill 政策信息截止到 2026 年 5 月
- **竞赛信息封闭**: NOI 高段 (省选→集训→IOI) 训练方法论极少公开, 本 skill 竞赛维度信号在省选以上薄弱
- **一手率**: declared 约 96.8% (150/155); auto 约 19.4% (verified_primary 30/155, surrogate 120/155 不在 PRIMARY_DOMAIN_SUFFIXES)
- **voice_confidence**: medium (教学设计/学术 register 语料多; 竞赛圈/机构运营一手封闭, 推断为主)
- **农村/低收入地区覆盖极弱**: 几乎无公开方法论, 本 skill 隐含城市中产家庭语境
- **CT 评估工具研究空白**: 没有 canonical 的 CT 标准化评估工具, Dr. Scratch / Bebras 仍在研究阶段
- **EN 约 60% / zh-CN 约 35% / 其他约 5%**: 反映全球 CS 教育研究以英文为主, 中国产业信息以中文为主的现实分布
- **本 skill 不替代**: 教育学/发展心理学专业训练; 法规内容仅导航非法律咨询; 竞赛教练的实战经验

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
