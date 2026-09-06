# Synthesis Candidates (raw) — 自动驾驶 / 智能驾驶

> Phase 2 Step 0。候选来自六轨的「Phase 2 接口」段。行业类型 = Technical + Regulated specialized，候选门槛 ≥ 15。

## 候选心智模型 (18 条)

| Candidate | 出现于 tracks | 独立 figures | 类型 | 备注 |
|---|---|---|---|---|
| 任何数字先问分母/口径/年份 | 01,02,03,04,06 | Geiger / Templeton / Koopman / Dolgov | cross-track | 本轮最强共识，四轨独立指向 |
| 安全是论证不是数字 | 01,03,04,06 | Koopman / Urmson / Shashua | cross-track | 四种互不覆盖的证明路径 |
| ODD 是一切承诺的边界 | 03,04,06 | Urmson / Dolgov | cross-track | 越界后的行为比越界前重要 |
| 端到端⇄模块化是「归纳偏置放哪层」 | 01,02,04,06 | Kendall / Shalev-Shwartz / 李弘扬 / Geiger | cross-track | 不是二选一 |
| 中间表示的表达力决定能力上界 | 02,04,06 | 李弘扬 / Geiger | cross-track | 能否表达「不认识但有东西」 |
| 监管形态决定工程节奏 | 03,05,06 | — (制度证据为主) | cross-track | 8 张 high decay 卡片 6 张由法规触发 |
| 论证要带着弱点一起交 | 03,04 | Koopman / Urmson | cross-track | 资深路径最高频的「额外做」 |
| 数据集偏差就是产品偏差 | 02,04 | Geiger | cross-track | 欧美基准不外推中国路况 |
| 失效 ⇄ 性能不足要先选标准域 | 03,06 | — | cross-track | 26262 vs 21448 |
| 长尾有信息论硬限制 vs 规模化可解 | 01,02,04 | Shalev-Shwartz / Kendall / Elluswamy | 分歧 | 保留不抹平 |
| 研究工具与量产工具是两套 | 02,03 | — | cross-track | 跨过去付全额代价 |
| 厂商宣称与可核实能力之间要有硬边界 | 01,02,05 | Templeton | cross-track | |
| 仓库热度≠当下可用性 | 02 | — | 单轨 → playbook | |
| 接管既是兜底也是数据来源，但不能当 KPI | 03,04,06 | Dolgov | cross-track | |
| 仿真的价值在可控可重复不在真实感 | 01,02,03 | Urtasun / Geiger | cross-track | 3DGS 解决外观不解决行为 |
| 人机共驾的风险来自能力与责任错配 | 01,06 | Cummings | cross-track | |
| 证据要能互相寻址 | 03 | — | 单轨 → playbook | SOTIF↔场景库↔问题池↔安全案例 |
| 未生效标准按已生效设计、按未生效表述 | 03,06 | — | 单轨 → playbook | |

## 候选 playbook 规则 (12 条)
| Pattern | 来源 |
|---|---|
| 见安全/性能数字先问分母 | T03 Phase2 接口、T04 核心概念→playbook |
| 见「某榜第一」先问开环闭环与背景交通模型 | T02 避坑、T04 PDM |
| 见「已达 L3」先问依据哪套分级、哪个法域、ODD 是什么 | T04、T06 |
| 见脱离率横向比较直接判无效 | T04-S047、T06 破绽 3 |
| 见「比人安全 N 倍」先问 ODD/人类基准/碰撞类别 | T01 数字口径备忘 |
| 见「无图」先问零先验还是轻图降级 | T04-S057 |
| 见端到端方案先问梯度传到哪层、闭环在哪验 | T04-S004 |
| 中国团队选型先看 GB 47955—2026 时间表 | T04-S051 |
| 约束要机器可读 | T03 卡片 1/8/11/15 |
| 归因先选标准域再找原因 | T03 卡片 2/3/7/12 |
| 交付物按最终申报件反推格式 | T03 卡片 8→13、9→12 |
| 技术尽调三问：标准版本号 / GSN / 开环闭环 | T02 Branch 4 |

## 候选工具流派分裂 (智识谱系)
| Split | A 派代表 | B 派代表 |
|---|---|---|
| 中间件 | 标准生态派 ROS 2 + DDS | 自建确定性派 Cyber RT / Agnocast |
| 仿真 | 物理引擎派 CARLA / CarMaker | 日志重建派 NuRec / HUGSIM |
| 验证 | 覆盖度驱动派 Foretellix | 形式化约束派 RSS ⇄ 统计里程派 Waymo |
| 感知 | 模块化可解释派 OpenPCDet | 一体化端到端派 UniAD / Alpamayo |
| 传感器 | 纯视觉 Tesla | 真冗余 Mobileye |
| 监管 | 事前强标 + 名单制试点（中） | 自认证 + 事后召回（美）⇄ 型式认证（欧） |

## 候选反模式 (来自 T06 第 11 节 + T03 失败模式 + T02 避坑)
14 条外行破绽 + 14 条工具避坑 + 6 条厂商话术，去重后取 10 条进 §6。

## 候选时效信号 (诚实边界用)
| Signal | 来源 | Decay |
|---|---|---|
| GB 47955—2026 实施日 2027-01-01 | T06 13.3 | high |
| NHTSA SGO 第三次修订 + 新一轮征求意见 | T06 13.3 | high |
| 中国准入试点批次扩容 | T06 13.3 | high |
| Euro NCAP 2026 改版过渡期 | T06 13.3 | high |
| 闭环评测口径重估 nuPlan-R | T02 第 10 节 | high |
| Autoware ROS 2 版本迁移窗口 | T02 第 10 节 | medium |

## 候选 Agentic Protocol 维度
| 维度 | 推导自哪个心智模型 |
|---|---|
| 分级与 ODD 定位 | ODD 是一切承诺的边界 |
| 法域与合规路径 | 监管形态决定工程节奏 |
| 数字口径审计 | 先问分母 |
| 安全论证形态 | 安全是论证不是数字 |
| 架构与中间表示 | 端到端⇄模块化 / 中间表示 |
| 评测与数据集偏差 | 数据集偏差就是产品偏差 |
| 证据可核实性分级 | 厂商宣称与可核实能力的硬边界 |
