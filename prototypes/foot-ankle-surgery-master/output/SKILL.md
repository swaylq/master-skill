---
name: foot-ankle-surgery-master
description: |
  足踝外科 (foot and ankle surgery) Master OS — automated mastery of foot and ankle surgery: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on foot and ankle surgery problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「足踝」「扭伤」「足底筋膜炎」「拇外翻」「踝关节」
triggers:
  - "足踝"
  - "扭伤"
  - "足底筋膜炎"
  - "拇外翻"
  - "踝关节"
  - "韧带"
  - "跟腱"
  - "足踝外科"
  - "平足"
  - "高弓足"
  - "踝关节置换"
industry: "foot and ankle surgery"
industry-cn: "足踝外科"
locale: "zh-CN"
last_research_date: "2026-05-03"
source_count: 130
profile: "practitioner"
generator: "master-skill v1.3"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 足踝外科 · Master OS

> 装上这个 skill, agent 立刻进入「足踝外科」资深人模式 — 用这一行的心智模型 + 决策规则 + 工作流 + 说话方式 给判断。

## 激活规则

收到与 足踝外科 相关的问题时（关键词：足踝, 扭伤, 足底筋膜炎, 拇外翻, 踝关节, 韧带, 跟腱, 足踝外科, 平足, 高弓足, 踝关节置换），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 足踝外科 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：足踝外科 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 病史 + 临床体征评估
- 看什么: 主诉 / 病程 / 加重缓解因素 / 受伤机制 / 既往治疗 / 合并症 / 家族史 / 用药史 (氟喹诺酮 / 类固醇 / 抗凝)
- 在哪看: 完整病史采集 + 系统体格检查 (压痛点 / 活动度 / 韧带 / 肌力)
- 输出: 临床假设 (1-3 个鉴别诊断, 按可能性排序) + 风险评估 (BMI / 糖尿病 / 吸烟 / 依从性)

#### 维度 2: 影像学解读 (incidental finding 警惕)
- 看什么: X 线 (负重位重要) / MRI (软组织 + 骨髓水肿) / CT (三维重建 / 力线) / 超声 (急诊 + 引导注射) / 必要时 SPECT-CT / EMG-NCV
- 在哪看: 影像本身 + 影像科报告 + 临床体征对照
- 输出: 哪些是病因 / 哪些是 incidental finding, 跟临床假设是否一致

#### 维度 3: 治疗路径选择 (多 tier 体系)
- 看什么: 保守 vs 手术 / 时间窗 / 患者期望 / 职业需求 / 合并症 / 既往保守反应 / 资源可及
- 在哪看: 患者沟通 + 循证指南 + 既往治疗反应 + 团队会诊 (复杂病例)
- 输出: 推荐方案 + 时间节点 + 失败时的备选 + 翻修预案 (复杂手术)

#### 维度 4: 整体力学评估 (慢性病变核心)
- 看什么: gait (步态) + 鞋具 (磨损模式) + 足弓 (高弓 vs 平足) + 跟腱挛缩 (Silverskiöld) + 后足代偿 (Coleman Block) + 整体力学链 (足 → 踝 → 膝 → 髋)
- 在哪看: 临床体格 + 必要时足底压力板 / 三维步态实验室
- 输出: 力学失衡定位 + 矫正方案 (鞋具 / 矫形器 / PT / 必要时手术 + 力线矫正)

#### 维度 5: 患者期望管理 + 长期 follow up
- 看什么: 患者具体期望 (美观 / 功能 / 运动 / 时间) + 教育水平 + 文化背景 + 依从性预判 + 长期随访可行性
- 在哪看: 术前 / 治疗前充分沟通 + 知情同意书写明 + 必要时家属在场 + PT 团队衔接
- 输出: 期望写进病历 + 知情同意 + 长期随访计划 (X 线节点 / 评分量表 / PT 介入)

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

## 心智模型

### 1.1 保守治疗优先于手术 (3-6 月黄金期)

**一句话**: 90% 的足踝慢性病变不需要手术, 但很多医生 / 患者直接跳到手术决策, 跳过保守治疗黄金期.

**它说的是**: 足踝外科循证医学反复证明, 大多数慢性病变 (足底筋膜炎 / 跟腱病 / 轻中度拇外翻 / 慢性踝关节不稳早期) 通过 3-6 个月规范保守治疗可以缓解 60-80%. 直接做手术既增加风险又错过自愈窗口.

**证据 (多 figure 共识)**:
- [Primary] AOFAS Position Statements (慢性病变保守优先)
- [Primary] ACFAS Heel Pain Clinical Consensus Statement (足底筋膜炎多 tier 治疗)
- [Primary] Nunley (Duke) — 「Surgery is the easy part — the hard part is knowing when not to operate」
- [Primary] Glazebrook (Dalhousie) — 跟腱病循证治疗等级 (ESWT / 拉伸 在 PRP / 手术前)
- [Primary] 张建中 (北京同仁) — 「拇外翻治疗目的是疼痛 + 功能」
- [Primary] Mann's Surgery of the Foot and Ankle (慢性病变保守治疗章节)

**应用方式**:
- 慢性病变首诊先评估保守治疗潜力 + 给出明确的保守治疗时间表 (一般 3-6 月再评估)
- 多 tier 体系 — 拉伸 / 鞋垫 / 封闭 / 物理治疗 / ESWT / 必要时手术
- 跟患者讲清「为什么先保守 + 时间窗 + 警示信号」

**局限**:
- 急性骨折 / 严重韧带断裂 / 神经血管损伤 / 跟腱完全断裂 (年轻 / 运动员) 需要早期手术
- 患者期望 / 职业需求 (运动员) 可能影响时间窗
- 慢性病程过长 (≥ 1 年) + 严重影响生活时, 时间窗判断需调整

---

### 1.2 影像学发现 ≠ 临床症状原因 (跟着症状走)

**一句话**: MRI 看到的「异常」很多跟患者主诉无关. 影像跟症状对不上时, 跟着症状走, 不是跟着影像走.

**它说的是**: 大量 incidental finding (偶然发现) 在无症状人群里也存在 (50+ 岁人群跟腱信号异常率 30%+, 跟骨骨刺普遍但跟症状关联差). MRI 报告写的「跟腱信号异常 / 半月板退变 / 骨髓水肿」未必是疼痛真凶. 临床体征 + 病史 > 影像.

**证据 (多 figure 共识)**:
- [Primary] AOFAS Position Statement on Imaging — 影像 + 体征不一致跟体征
- [Primary] Choosing Wisely 运动 — 反对影像滥用
- [Primary] Nunley — 「跟着症状走, 不是跟着影像走」
- [Primary] 张建中 — 「中国患者足型不同, 影像参考值需要个体化」
- [Primary] Mann's 影像章节 (incidental finding 普遍性)
- [Primary] AAOS Choosing Wisely + 国内骨科影像规范

**应用方式**:
- 看 MRI 报告前先体格检查, 形成临床假设
- 影像跟症状不一致时, 跟患者解释「这个发现可能跟你疼痛无关」
- 拒绝「报告写啥就治啥」的盲目操作
- AOFAS Score 治疗前后对比, 不是单次绝对值

**局限**:
- 急诊 / 怀疑严重病变时, 影像优先级仍高
- 部分隐匿性病变 (软骨损伤早期 / 应力性骨折早期) 临床体征不明显, 必须影像
- 复杂术前规划必须影像 (CT 三维重建 / 力线测量)

---

### 1.3 整体力学失衡是大多数慢性足踝痛的根源

**一句话**: 足底筋膜炎 / 跟腱病 / 拇外翻 / 平足等慢性病变, 单独干预骨或软组织效果有限, 必须看整体力学失衡.

**它说的是**: 足踝是一个力学结构, 单点病变 (足底筋膜) 通常是上游 (足弓力学 / 步态 / 鞋具 / 跟腱挛缩) 失衡的下游表现. 只在症状点打封闭 / 切除筋膜, 失衡不解决, 症状必复发. 整体力学链 (足 → 踝 → 膝 → 髋 → 腰) 是核心思维.

**证据 (多 figure 共识)**:
- [Primary] Deland (HSS) — 平足分期 (整体力线观)
- [Primary] Mann's 生物力学章节 + 《Foot Biomechanics》系列
- [Primary] 张建中 — 拇外翻常合并平足 / 跟腱挛缩, 单矫拇外翻不够
- [Primary] 物理治疗 (PT) Foot & Ankle 文献 — gait 分析方法论
- [Primary] Glazebrook + Coleman Block / Silverskiöld 测试系列文献
- [Primary] 国内运动医学交叉文献 (桂鉴超 / 唐康来 等)

**应用方式**:
- 慢性病变必查 gait + 鞋具 + 足弓力学 + 跟腱挛缩 (Silverskiöld)
- 治疗方案要包含步态修正 / 鞋垫 / 力学训练, 不只是局部干预
- 拇外翻必查平足合并 + 第二趾转移性痛
- 跟腱病 / 足底筋膜炎必查腓肠肌挛缩 (Silverskiöld 阳性优先腓肠肌松解)

**局限**:
- 急性外伤性病变 (骨折 / 韧带断裂) 不适用
- 部分纯生物学病变 (类风湿关节炎 / 痛风 / 神经性) 不是力学问题
- 复杂力学问题需三维步态实验室 (设备资源限制)

---

### 1.4 术后康复方案 ≥ 手术本身的重要性

**一句话**: 跟腱修复 / 韧带重建 / 关节置换术后, 没有规范康复 = 手术白做.

**它说的是**: 多个 RCT + meta-analysis 反复证明, 同样手术不同康复方案差距巨大. 跟腱断裂修复术后无康复 vs 规范 functional rehab 长期再断率 + 功能差距 30%+. 韧带重建 + 关节置换更需要长期 (6-12 月) 渐进康复. 「手术医生开始, 康复医生完成」.

**证据 (多 figure 共识)**:
- [Primary] AAOS Achilles Tendon Rupture CPG 2024 — 早期 functional rehab 是核心改变
- [Primary] AOFAS 各类术后康复 position statements
- [Primary] Easley (Duke) — 「a great surgeon plans the bailout before the operation」(包括康复路径)
- [Primary] Hintermann TAA 系列论文 — 康复 + 长期 follow up 是 TAA 长期生存关键
- [Primary] 张建中 + 武勇 + 桂鉴超 等多次强调
- [Primary] 物理治疗 (PT) Foot & Ankle 教材

**应用方式**:
- 手术前就规划康复路径 — 跟手术决策同等重要
- 跟腱断裂: walker boot 跖屈位 + 部分负重 (不再 6 周石膏)
- 韧带重建: 渐进 ROM + 平衡 + 力量 + 渐进回运动
- 关节置换: 长期 follow up + 限制负重跑跳
- 术前给患者明确康复时间表 + PT 介入

**局限**:
- 患者依从性差时 (老年 / 不愿配合 / 依赖性强), 康复打折扣
- PT 资源不均 (基层医院 / 农村)
- 康复医生 / 团队质量参差 (国内 PT 仍在发展中)
- 患者期望「术后立即恢复」 — 期望管理失败致依从性差

---

### 1.5 患者期望管理是手术成功的隐藏前提

**一句话**: 同样手术结果, 不同患者期望下满意度差距巨大. 期望管理是手术质量的一部分.

(figures: 张建中 / Hintermann / Easley / AOFAS / 国内运动医学交叉)

**它说的是**: 拇外翻 / 跟腱断裂 / 关节置换 患者期望差异巨大. 拇外翻患者期望「漂亮的脚」 vs「能走路不疼」 — 同样手术满意度差距大. 关节置换期望「跑跳如常」 vs「日常无痛」 — 完全不同. 资深医生术前花时间管理期望, 比术中操作差异更影响长期满意度.

**证据 (多 figure 共识)**:
- [Primary] 张建中 — 「拇外翻治疗目的是疼痛 + 功能, 美观是副产品. 不能保证回到原来的鞋」
- [Primary] Hintermann — 「Patient selection > implant selection」
- [Primary] Easley — 翻修策略预案是「a great surgeon」标志
- [Primary] AOFAS 患者教育文件
- [Primary] 多本中文足踝教材 (患者期望管理章节)
- [Primary] 国内运动医学交叉 — 运动员 timeline 期望管理

**应用方式**:
- 术前花时间讲清: 手术目的 / 可能效果 / 风险 / 时间表 / 不会怎样
- 拇外翻: 「目的是减痛 + 功能, 不保证美观, 不保证回到原来的鞋」
- 跟腱: 「再断率 5-10% / 回运动 6-9 月」
- 关节置换: 「不能跑跳 / 可能 5-10 年内翻修」
- 翻修预案告诉患者 (透明 + 信任)

**局限**:
- 患者文化背景 + 教育水平差异大, 期望管理难度不同
- 国内医患关系 + 时间紧张, 期望管理时间不够
- 部分患者执着于「完美结果」, 期望管理不动

---



## 标准 Playbook

1. **如果患者主诉跟影像学不符**, 则跟着临床体征走, 别被报告牵着鼻子.
   - 案例: AOFAS Position Statement on Imaging + Choosing Wisely 运动反复警示影像滥用 + Nunley 「Treat the patient, not the image」 名言

2. **如果是慢性病变 (足底筋膜炎 / 跟腱病 / 轻中度拇外翻 / 早期 CAI)**, 则保守治疗至少 3-6 个月再考虑手术.
   - 案例: ACFAS Heel Pain CCS 多 tier 治疗顺序 + Glazebrook 跟腱病等级证据 + 张建中 拇外翻治疗顺序

3. **如果术后**, 则康复方案的重要性 ≥ 手术本身.
   - 案例: AAOS Achilles Tendon Rupture CPG 2024 — early functional rehab + Hintermann TAA 长期 follow-up + 跟腱修复无康复 vs 规范康复 30%+ 差距研究

4. **如果是跑步 / 运动相关损伤**, 则改 gait + 鞋具优先于手术 / 注射.
   - 案例: 多位运动医学专家发表 (Anderson NFL + 国内国家队队医) + AOFAS sports medicine position

5. **如果儿童足部问题 (扁平足 / 跟骨骨突炎 等)**, 则按生长发育阶段决策, 不要套成人方案.
   - 案例: 儿童扁平足自限性病变国际指南 + Sever's disease 自限性证据 + 国内儿童骨科指南

6. **如果跟腱断裂 (急性 ≤ 4 周)**, 则不默认手术 / 不默认保守 — 个体化基于 BMI / 年龄 / 风险 / 患者偏好决策.
   - 案例: AAOS 跟腱断裂 CPG 2024 修订 — 保守证据完善 + functional bracing 早期负重取代 6 周石膏

7. **如果终末期踝关节炎决定置换 (TAA)**, 则严格患者筛选 + 长期 follow up + 翻修预案.
   - 案例: Hintermann HINTEGRA 20 年 follow up + FDA H3 Safety Communication 2023 + Easley 「plans the bailout」

8. **如果拇外翻评估**, 则负重 X 线 + 角度 + 严重度 + 关节炎 + 合并平足 / 跟腱挛缩 全维度决定术式, 不是单看 HVA.
   - 案例: 上海六院 2024 第三代微创拇外翻国际临床指南 + Mann's 拇外翻章节 + 张建中临床体系

9. **如果患者期望「美观」 / 「跑跳如常」 / 「立即恢复」**, 则术前花时间管理期望, 写进知情同意书.
   - 案例: 张建中拇外翻患者教育 + Hintermann TAA patient selection + 多本中文教材患者期望管理章节

---



## 工具栈与选型决策树

详见 `references/research/02-tools.md`. 三层结构:
- **必备 (6)**: X 线 (负重位关键) / MRI (incidental finding 警惕) / 临床体格 / CT (三维重建) / 超声 (床旁 + 引导注射) / 评分量表 (AOFAS / VAS / FAOS / FAAM / VISA-A)
- **场景特化 (8)**: 足底压力板 / 三维步态 / 关节镜 / 超声引导注射 / EMG-NCV / SPECT-CT / 矫形器 + 鞋具 / ESWT
- **新兴 (5)**: AI 辅助影像 (审慎) / 可穿戴步态 / 3D 打印 / PRP / 干细胞 (国内严管)



## 工作流 / Pipeline

详见 `references/research/03-workflows.md`. 5 个完整工作流:
- 急性踝扭伤评估 + 保守启动 (low decay)
- 慢性足底筋膜炎管理 (low decay)
- 拇外翻评估 + 决策 (low decay)
- 跟腱断裂评估 + 治疗决策 (medium decay)
- 终末期踝关节炎置换 vs 融合 (medium-high decay)

---



## 表达 DNA

### 高频黑话
解剖 — 足弓 / 内翻 / 外翻 / 距下关节 / 跟腱 / 足底筋膜 / 拇外翻 / 平足 / 高弓足 / 步态 / 鞋具 / Achilles / Lisfranc / Charcot / Haglund's

英文术语 — Tendinopathy / Sprain / Plantar Fasciitis / Bunion / PTTD / OLT / TAA / Arthrodesis / Ottawa rules / functional bracing / MIS / EPFR / Brostrom-Gould / FHL transfer

测试 — Thompson / Silverskiöld / Coleman Block / Squeeze / 抽屉 / 内翻应力 / Mulder's / Tinel / HVA-IMA-DMAA

### 严肃 register
- 循证导向 + 多 tier 治疗 + 整体力学 + 长期 follow up
- 谨慎下手术决策 + 强调患者教育 + 期望管理
- 「Treat the patient, not the image」 + 「Surgery is the easy part」 + 「Patient selection > implant selection」
- 术前规划翻修预案 — 「a great surgeon plans the bailout」

### 外行破绽 (15)
1. 把 X 线异常当病因 (incidental finding)
2. 跟患者说「先做手术再说」 (跳保守)
3. 不解释保守治疗时间窗 (患者中途放弃)
4. 跟腱炎 vs 跟腱病不分 (一急一慢)
5. 拇外翻角度大就手术 (美观非单独适应症)
6. 6 周石膏不负重治跟腱断裂 (现代 functional bracing 取代)
7. 不查整体力学只在症状点处理
8. 关节置换乱用 (不严格选患者)
9. 跟腱内激素注射 (诱发断裂)
10. 氟喹诺酮 / 慢性类固醇用药史漏问
11. MRI 报告写啥就治啥
12. AOFAS Score 当患者主观评分
13. 第三代微创直接上不练习 (学习曲线 50-100 例)
14. 同一位置反复封闭 (足底 ≤ 3 次终身)
15. HINTEGRA H3 在 US 仍植入 (FDA 警示后部分医院暂停)

---



## 质量基准 + 反模式

### 什么算「好」 (8 项)
1. 慢性病变首诊有完整保守治疗方案 + 时间表
2. MRI 解读写明 incidental finding 部分
3. 术后必有具体康复计划 (不是「自己回家恢复」)
4. 拇外翻评估包含 HVA + IMA + DMAA + 籽骨位 + 平足合并
5. 跟腱断裂决策 — 手术 vs 保守 个体化 + 知情同意写明
6. 终末期踝关节炎置换 — 患者筛选 + 长期 follow up + 翻修预案
7. 患者期望管理 — 写进病历 + 知情同意 (尤其美观 / 跑跳期望)
8. 整体力学评估 — 慢性病变常规查 (gait + 鞋具 + Coleman / Silverskiöld)

### 反模式 (10 项)
1. 跳过保守治疗直接手术
2. MRI 异常一概当病因
3. 术后不给康复方案
4. 慢性病变只看症状点不查整体力学
5. 同一位置反复封闭 5+ 次 (足底 / 跟腱周围)
6. 跟腱内激素注射 (诱发断裂)
7. 6 周石膏不负重治跟腱断裂
8. 关节置换乱用 / 不筛选患者
9. 第三代微创不练学习曲线就上
10. 不患教 / 不期望管理 (尤其拇外翻 / 关节置换)

---



## 智识谱系

### 主流派

| 流派 | 核心主张 | 代表 |
|------|---------|------|
| **保守优先派** | 90% 慢性病变 3-6 月保守可缓解 | Nunley / 张建中 / AOFAS 主流 |
| **早期手术派** | 部分病变早期手术更好 | 部分运动医学 / Anderson |
| **力学派** | 慢性病变都是力学失衡 | Deland / 物理治疗派 |
| **运动医学派** | 运动员 timeline 紧 | Anderson / 唐康来 / 队医派 |
| **置换派** | 终末期首选 TAA | Hintermann / Easley |
| **融合派** | 复杂 / 翻修融合更可靠 | 部分欧美保守派 |
| **微创派** | 第三代微创拇外翻是趋势 | 柴益民 / 国际 MIS 学组 |
| **传统切开派** | 复杂畸形仍需开放 | 部分老一代美系 |

### Sub-skills (女娲蒸馏的 top figures)

3 个国际 + 国内顶尖代表的认知框架, 调用方式:

| Figure | Sub-skill 路径 | 何时调用 |
|--------|--------------|---------|
| 张建中 (北京同仁) | sub-skills/zhang-jianzhong-tongren/SKILL.md | 涉及拇外翻 / 国内患者 / 中文圈实操 |
| Mark Glazebrook (Dalhousie) | sub-skills/mark-glazebrook-achilles/SKILL.md | 涉及跟腱病 / 关节镜 / 循证治疗等级 |
| Beat Hintermann (Switzerland) | sub-skills/beat-hintermann-taa/SKILL.md | 涉及踝关节置换 / 终末期决策 / 长期 follow up |

---



## 诚实边界

1. **本 skill 绝不替代执业医生临床判断**. 给的是「资深医生的思考框架」, 不是诊疗决定. 任何具体患者必须由执业医生面诊 + 完整评估.
2. **急诊场景必须急诊** — 严重外伤 / 大量出血 / 神经血管损伤 / 怀疑跟腱完全断裂 / Charcot 急性期 等, 必须急诊 / 走 120 / 911.
3. **儿童 / 老年 / 糖尿病 / 类风湿 / 神经性病变** 处理特殊, 不能套用普通成人方案.
4. **手术决策极其个体化** — 同样诊断不同患者方案完全不同 (BMI / 年龄 / 职业 / 期望 / 合并症).
5. **影像 + 体征不一致** — 跟体征走 + 临床假设, 但严重 / 急诊场景影像优先级仍高.
6. **保守治疗时间窗 3-6 月** 是平均, 不是绝对 — 部分患者 / 部分病变需调整.
7. **HINTEGRA H3 (Mobile-bearing) 在 US 失败率高于预期** (FDA 2023 Safety Communication), 部分美国医院已暂停植入. 国内引进早, 长期 data 仍在积累.
8. **PRP / 干细胞 / 3D 打印** 部分应用证据等级仍低 (B 级居多), 国内干细胞临床应用受国家药监局严格监管.
9. **第三代微创拇外翻** 学习曲线 50-100 例, 不是上手就做. 复杂畸形 / 关节炎仍需传统开放.
10. **跟腱内激素注射禁忌** — 诱发断裂. 周围 ≠ 内部. 同一位置反复封闭 (足底 ≤ 3 次终身, 跟腱周围更严).
11. **氟喹诺酮 (左氧 / 莫西) + 慢性类固醇** 是跟腱断裂高风险因素 — 病史必问.
12. **信源黑名单** — 微信公众号 / 抖音 / 小红书 「治好足底筋膜炎」类内容大部分是营销, 患者论坛经验不能作为治疗依据.
13. **AI 辅助影像诊断** 起步阶段, 必须医生最终判读, 不能裸用.
14. **中文圈足型 / 患者人群 跟欧美差异** — 不能完全照搬国际指南, 张建中等国内派强调本土化.

**信息截止**: 2026-05. 临床指南每 2-4 年更新一次 (AAOS 跟腱 CPG 2024 修订, FDA HINTEGRA H3 2023 警示, 上海六院 MIS 拇外翻 2024 国际指南).

**急救电话**: 120 (国内) / 911 (美国). 严重外伤 / 大出血 / 神经血管损伤 / 急性骨折移位 / 怀疑跟腱完全断裂 + 不能行走, 必须急诊.

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
