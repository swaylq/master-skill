# Track 02 — 工具地图｜自动驾驶 / 智能驾驶（Autonomous Driving）

> locale = `zh-CN` 受众 · 覆盖 L2 组合驾驶辅助与城区/高速领航、L3、L4 Robotaxi；感知-预测-规划-控制；端到端 ⇄ 模块化；数据闭环与长尾；仿真与安全论证；法规与量产落地。
> **不含**：人形机器人具身智能、LLM agent 基础设施、芯片制造工艺、整车三电与电子电气架构。
> 所有 `last_checked` = `2026-09-06`。GitHub star / push 时间来自本轨 seed 快照 `seeds/github_repos.jsonl`（抓取日 2026-09-02），文中标注为「seed 快照 2026-09-02」。
>
> **本轨的特殊性**：这一行的工具栈被**两条互不通约的现实**撕开——研究侧（论文、开源、公开榜单）和量产侧（车规芯片、闭源工具链、Tier1 供应链）。同一个名字在两边意思常常不同。本文件对每个工具都写清它属于哪一侧、能不能跨过去。

## Source Manifest

| source_id | url | bucket | last_checked | author/org | note |
|-----------|-----|--------|--------------|------------|------|
| T02-S001 | https://github.com/ros-tooling/rosbag2_storage_mcap | verified_primary | 2026-09-06 | ros-tooling | rosbag2 的 MCAP 存储插件 |
| T02-S002 | https://github.com/foxglove/mcap | verified_primary | 2026-09-06 | Foxglove | MCAP 容器格式规范与多语言实现 |
| T02-S003 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | surrogate_primary | 2026-09-06 | Foxglove | 自有博客 own publication，MCAP 成默认 bag |
| T02-S004 | https://docs.foxglove.dev/docs/introduction | surrogate_primary | 2026-09-06 | Foxglove | vendor docs，可视化与数据平台能力口径 |
| T02-S005 | https://github.com/autowarefoundation/autoware | verified_primary | 2026-09-06 | Autoware Foundation | Autoware 元仓库 |
| T02-S006 | https://github.com/autowarefoundation/autoware_core/releases | verified_primary | 2026-09-06 | Autoware Foundation | Core release notes，版本与日期口径 |
| T02-S007 | https://github.com/orgs/autowarefoundation/discussions/5835 | reference | 2026-09-06 | Autoware Foundation | 引入 Agnocast 的公开讨论帖 |
| T02-S008 | https://autowarefoundation.github.io/autoware-documentation/main/design/autoware-concepts/difference-from-ai-and-auto/ | secondary | 2026-09-06 | Autoware Foundation | Core/Universe 与 AI/Auto 的定位差异 |
| T02-S009 | https://github.com/ApolloAuto/apollo | verified_primary | 2026-09-06 | 百度 Apollo | 开源自动驾驶平台主仓库 |
| T02-S010 | https://github.com/ApolloAuto/apollo/blob/master/docs/04_CyberRT/CyberRT_FAQs.md | verified_primary | 2026-09-06 | 百度 Apollo | Cyber RT 为什么不用 ROS 的官方说明 |
| T02-S011 | https://arxiv.org/abs/2501.18942 | verified_primary | 2026-09-06 | 独立作者组 | Autoware 与 Apollo 的系统性对比论文 |
| T02-S012 | https://arxiv.org/abs/2510.11448 | verified_primary | 2026-09-06 | 独立作者组 | 中间件延迟/内存实测，Cyber RT vs FastDDS |
| T02-S013 | https://github.com/eclipse-cyclonedds/cyclonedds | verified_primary | 2026-09-06 | Eclipse Foundation | Cyclone DDS 实现 |
| T02-S014 | https://github.com/eProsima/Fast-DDS | verified_primary | 2026-09-06 | eProsima | Fast DDS 实现，ROS 2 默认 RMW |
| T02-S015 | https://github.com/ros2/rmw_zenoh | verified_primary | 2026-09-06 | ROS 2 项目 | 非 DDS 的 Zenoh RMW |
| T02-S016 | https://github.com/tier4/agnocast | verified_primary | 2026-09-06 | TIER IV | rclcpp 兼容真零拷贝 IPC |
| T02-S017 | https://arxiv.org/abs/2506.16882 | verified_primary | 2026-09-06 | TIER IV 等 | Agnocast 论文，ISORC 2025 |
| T02-S018 | https://index.ros.org/p/autoware_agnocast_wrapper/ | verified_primary | 2026-09-06 | ROS Index | Autoware 侧封装包的官方索引 |
| T02-S019 | https://developer.nvidia.com/drive | surrogate_primary | 2026-09-06 | NVIDIA | vendor docs，DRIVE 开发者总入口 |
| T02-S020 | https://developer.download.nvidia.com/drive/docs/nvidia-drive-agx-thor-platform-for-developers.pdf | surrogate_primary | 2026-09-06 | NVIDIA | vendor docs，Thor 平台开发者白皮书 |
| T02-S021 | https://developer.nvidia.com/tensorrt | surrogate_primary | 2026-09-06 | NVIDIA | vendor docs，推理编译与量化 |
| T02-S022 | https://www.horizon.auto/solutions/horizon-journey/horizon-journey6 | surrogate_primary | 2026-09-06 | 地平线 Horizon | vendor docs，征程 6 系列产品页 |
| T02-S023 | https://developer.horizon.auto/forum | surrogate_primary | 2026-09-06 | 地平线 Horizon | vendor docs，供应商自有开发者社区 |
| T02-S024 | https://www.qualcomm.com/products/automotive/automated-driving/snapdragon-ride-platform | surrogate_primary | 2026-09-06 | Qualcomm | vendor docs，Snapdragon Ride 平台页 |
| T02-S025 | https://www.vector.com/int/en/products/products-a-z/software/canoe/canoe-adas/ | surrogate_primary | 2026-09-06 | Vector Informatik | vendor docs，CANoe.ADAS 能力页 |
| T02-S026 | https://www.vector.com/int/en/products/products-a-z/software/canape/ | surrogate_primary | 2026-09-06 | Vector Informatik | vendor docs，CANape 测量标定页 |
| T02-S027 | https://github.com/open-mmlab/OpenPCDet | verified_primary | 2026-09-06 | OpenMMLab | 激光雷达 3D 检测工具箱 |
| T02-S028 | https://github.com/open-mmlab/mmdetection3d | verified_primary | 2026-09-06 | OpenMMLab | 通用 3D 感知训练框架 |
| T02-S029 | https://github.com/fundamentalvision/BEVFormer | verified_primary | 2026-09-06 | 上海 AI Lab 等 | 纯视觉时空 BEV 参考实现 |
| T02-S030 | https://github.com/mit-han-lab/bevfusion | verified_primary | 2026-09-06 | MIT HAN Lab | 统一 BEV 空间的多模态融合 |
| T02-S031 | https://github.com/hustvl/MapTR | verified_primary | 2026-09-06 | HUST Vision Lab | 在线矢量高精地图构建 |
| T02-S032 | https://github.com/PJLab-ADG/SensorsCalibration | verified_primary | 2026-09-06 | 上海 AI Lab | OpenCalib 多传感器标定工具箱 |
| T02-S033 | https://docs.acados.org/ | verified_primary | 2026-09-06 | acados 团队 | 嵌入式最优控制求解器官方文档 |
| T02-S034 | https://github.com/acados/acados | verified_primary | 2026-09-06 | acados 团队 | 源码与 QP 后端矩阵 |
| T02-S035 | https://github.com/osqp/osqp | verified_primary | 2026-09-06 | OSQP 团队 | 一阶算子分裂 QP 求解器 |
| T02-S036 | https://web.casadi.org/ | secondary | 2026-09-06 | CasADi 团队 | 符号建模与自动微分前端 |
| T02-S037 | https://github.com/commaai/openpilot | verified_primary | 2026-09-06 | comma.ai | 开源 L2 辅助驾驶，可装真车 |
| T02-S038 | https://github.com/AtsushiSakai/PythonRobotics | verified_primary | 2026-09-06 | Atsushi Sakai | 规划/定位算法可运行样例库 |
| T02-S039 | https://github.com/Farama-Foundation/HighwayEnv | verified_primary | 2026-09-06 | Farama Foundation | 决策层强化学习环境集 |
| T02-S040 | https://github.com/OpenDriveLab/UniAD | verified_primary | 2026-09-06 | OpenDriveLab | 面向规划的一体化端到端参考实现 |
| T02-S041 | https://github.com/autonomousvision/transfuser | verified_primary | 2026-09-06 | Chitta / Geiger 组 | 模仿学习 + 传感器融合闭环基线 |
| T02-S042 | https://github.com/autonomousvision/carla_garage | verified_primary | 2026-09-06 | Chitta / Geiger 组 | Leaderboard 2.0 starter kit 与偏差研究 |
| T02-S043 | https://github.com/opencv/cvat | verified_primary | 2026-09-06 | CVAT.ai / OpenCV | 开源标注平台 |
| T02-S044 | https://www.cvat.ai/resources/blog/3d-point-cloud-annotation | surrogate_primary | 2026-09-06 | CVAT.ai | vendor docs，点云标注能力说明 |
| T02-S045 | https://github.com/naurril/SUSTechPOINTS | verified_primary | 2026-09-06 | 南方科技大学 | 3D 点云标注平台，IV 2020 论文实现 |
| T02-S046 | https://github.com/xtreme1-io/xtreme1 | verified_primary | 2026-09-06 | BasicAI | 带自动标注的多模态标注平台 |
| T02-S047 | https://arxiv.org/abs/2401.12888 | verified_primary | 2026-09-06 | 多机构综述作者组 | 数据闭环与自动标注综述，定义与流水线 |
| T02-S048 | https://github.com/carla-simulator/carla | verified_primary | 2026-09-06 | CARLA team | 开源驾驶仿真器主仓库 |
| T02-S049 | https://github.com/carla-simulator/carla/releases/tag/0.10.0 | verified_primary | 2026-09-06 | CARLA team | 0.10.0 release 记录，UE5.5 迁移 |
| T02-S050 | https://carla.org/2024/12/19/release-0.10.0/ | secondary | 2026-09-06 | CARLA team | 0.10.0 发布说明与双分支共存策略 |
| T02-S051 | https://carla.readthedocs.io/en/latest/adv_rss/ | verified_primary | 2026-09-06 | CARLA team | RSS 传感器与限制器文档 |
| T02-S052 | https://leaderboard.carla.org/ | secondary | 2026-09-06 | CARLA team | Leaderboard 官方规则与提交口径 |
| T02-S053 | https://github.com/lgsvl/simulator | verified_primary | 2026-09-06 | LG Electronics | SVL Simulator 仓库，已停止维护 |
| T02-S054 | https://www.asam.net/standards/detail/opendrive/ | surrogate_primary | 2026-09-06 | ASAM e.V. | 协会 association 标准页，OpenDRIVE |
| T02-S055 | https://www.asam.net/standards/detail/openscenario-dsl/older/ | surrogate_primary | 2026-09-06 | ASAM e.V. | 协会 association 版本历史页 |
| T02-S056 | https://publications.pages.asam.net/standards/ASAM_OpenDRIVE/ASAM_OpenDRIVE_Specification/v1.9.0/specification/index.html | surrogate_primary | 2026-09-06 | ASAM e.V. | 协会 own publication，1.9.0 规范正文 |
| T02-S057 | https://www.appliedintuition.com/blog/asam-openscenario-v2 | surrogate_primary | 2026-09-06 | Applied Intuition | vendor docs，DSL 更新解读 |
| T02-S058 | https://www.appliedintuition.com/products/simulation | surrogate_primary | 2026-09-06 | Applied Intuition | vendor docs，仿真产品线宣称 |
| T02-S059 | https://www.foretellix.com/what-is-asam-openscenario-dsl/ | surrogate_primary | 2026-09-06 | Foretellix | vendor docs，DSL 与覆盖度方法宣称 |
| T02-S060 | https://ipg-automotive.com/en/products-solutions/software/carmaker/ | surrogate_primary | 2026-09-06 | IPG Automotive | vendor docs，CarMaker 车辆动力学仿真 |
| T02-S061 | https://www.dspace.com/en/pub/home/products/systems/adas_hil.cfm | surrogate_primary | 2026-09-06 | dSPACE | vendor docs，ADAS 硬件在环方案 |
| T02-S062 | https://github.com/eclipse-sumo/sumo | verified_primary | 2026-09-06 | Eclipse / DLR | 微观交通流仿真 |
| T02-S063 | https://www.mathworks.com/products/automated-driving.html | surrogate_primary | 2026-09-06 | MathWorks | vendor docs，Automated Driving Toolbox |
| T02-S064 | https://www.ansys.com/products/safety-analysis/ansys-medini-analyze | surrogate_primary | 2026-09-06 | Ansys | vendor docs，HARA/FMEA/FTA/SOTIF 工具 |
| T02-S065 | https://github.com/intel/ad-rss-lib | verified_primary | 2026-09-06 | Intel | RSS 形式化安全模型开源实现 |
| T02-S066 | https://scsc.uk/scsc-141C | surrogate_primary | 2026-09-06 | SCSC 安全关键系统俱乐部 | 协会 association，GSN 标准发布页 |
| T02-S067 | https://github.com/nutonomy/nuscenes-devkit | verified_primary | 2026-09-06 | Motional / nuTonomy | nuScenes 评测口径的可执行定义 |
| T02-S068 | https://www.nuscenes.org/nuscenes | secondary | 2026-09-06 | Motional | 数据集与指标定义页 |
| T02-S069 | https://github.com/motional/nuplan-devkit | verified_primary | 2026-09-06 | Motional | nuPlan 闭环规划评测框架 |
| T02-S070 | https://github.com/waymo-research/waymo-open-dataset | verified_primary | 2026-09-06 | Waymo Research | WOD 工具包与评测代码 |
| T02-S071 | https://waymo.com/open/challenges/ | secondary | 2026-09-06 | Waymo | 各赛道题目与时间口径 |
| T02-S072 | https://github.com/Thinklab-SJTU/Bench2Drive | verified_primary | 2026-09-06 | SJTU ThinkLab | 闭环端到端多能力基准 |
| T02-S073 | https://arxiv.org/abs/2406.03877 | verified_primary | 2026-09-06 | Jia, Yang 等 | Bench2Drive 原文，NeurIPS 2024 D&B |
| T02-S074 | https://arxiv.org/abs/2406.15349 | verified_primary | 2026-09-06 | Dauner, Chitta 等 | NAVSIM 原文与 PDMS 定义 |
| T02-S075 | https://github.com/autonomousvision/navsim | verified_primary | 2026-09-06 | Chitta / Geiger 组 | NAVSIM 官方实现与 v2 |
| T02-S076 | https://arxiv.org/abs/2306.07962 | verified_primary | 2026-09-06 | Dauner, Chitta 等 | PDM，开环与闭环脱节的关键实证 |
| T02-S077 | https://arxiv.org/abs/2511.10403 | verified_primary | 2026-09-06 | 独立作者组 | nuPlan-R，反应式多智能体重评 |
| T02-S078 | https://arxiv.org/abs/2510.26125 | verified_primary | 2026-09-06 | Waymo 等 | WOD-E2E 与 Rater Feedback Score |
| T02-S079 | https://developer.nvidia.com/omniverse/nurec | surrogate_primary | 2026-09-06 | NVIDIA | vendor docs，NuRec 神经重建库 |
| T02-S080 | https://github.com/NVIDIA/instant-nurec | verified_primary | 2026-09-06 | NVIDIA | 前馈式 3DGS 重建，驾驶日志转可仿真场景 |
| T02-S081 | https://github.com/hyzhou404/HUGSIM | verified_primary | 2026-09-06 | 浙大等 | 3DGS 闭环仿真器官方实现 |
| T02-S082 | https://arxiv.org/abs/2412.01718 | verified_primary | 2026-09-06 | Zhou 等 | HUGSIM 原文，帧率与基准规模口径 |
| T02-S083 | https://github.com/NVlabs/alpamayo | verified_primary | 2026-09-06 | NVIDIA Research | 开放 10B 驾驶 VLA 与推理链 |
| T02-S084 | https://github.com/OpenDriveLab/DriveLM | verified_primary | 2026-09-06 | OpenDriveLab | 图式视觉问答驱动基准与工具 |

## 总览

必备 14 / 场景特化 30 / 新兴 8

> 上面这行是机器可读的 sanity 行，数字与下面三张表的行数一致。

### 必备（14 个）

| 工具 | 一句话 | Decay | 主要 evidence |
|------|--------|-------|---------------|
| ROS 2 + rosbag2 | 研究与 L4 侧的通用节点/话题骨架与录制层 | low | T02-S001, T02-S011 |
| Autoware | 唯一有基金会治理的完整开源自动驾驶栈 | low | T02-S005, T02-S006 |
| Baidu Apollo + Cyber RT | 模块化量产栈的公开教科书，自带确定性调度中间件 | low | T02-S009, T02-S010 |
| MCAP | 自描述、可索引的多通道日志容器，ROS 2 默认 bag | low | T02-S002, T02-S003 |
| Foxglove | 车端日志的可视化与回放前端 | medium | T02-S004 |
| NVIDIA DRIVE 平台 | 中外大量高阶智驾项目的车端算力与 SDK 基座 | low | T02-S019, T02-S020 |
| TensorRT | 把训练好的网络压到车规延迟预算里的编译/量化层 | low | T02-S021 |
| Vector CANoe.ADAS + CANape | 量产侧总线分析、测量标定与传感器回放的事实工具 | low | T02-S025, T02-S026 |
| OpenPCDet | 激光雷达 3D 检测的通用基线与复现基准 | medium | T02-S027 |
| mmdetection3d | 多模态 3D 感知的训练脚手架 | medium | T02-S028 |
| CARLA | 开源闭环驾驶仿真的事实基座 | low | T02-S048, T02-S049 |
| ASAM OpenDRIVE + OpenSCENARIO | 路网与场景的描述标准，跨厂商交换的唯一通道 | low | T02-S054, T02-S055 |
| nuScenes + nuscenes-devkit | 多传感器 3D 感知的评测口径可执行定义 | low | T02-S067, T02-S068 |
| Waymo Open Dataset + toolkit | 官方评测实现与多赛道挑战赛 | low | T02-S070, T02-S071 |

### 场景特化（30 个）

| 工具 | 一句话 | Decay | 主要 evidence |
|------|--------|-------|---------------|
| Cyclone DDS / Fast DDS | ROS 2 底下的两种 RMW 实现，实时性表现不同 | low | T02-S013, T02-S014 |
| 地平线征程 6 + 天工开物 OpenExplorer | 中国本土量产项目的车端算力与量化编译链 | medium | T02-S022, T02-S023 |
| 高通 Snapdragon Ride / Ride Flex | 座舱与智驾同芯的混合关键性平台 | medium | T02-S024 |
| BEVFormer | 纯视觉时空 BEV 的参考实现 | medium | T02-S029 |
| BEVFusion | 相机 + 激光在统一 BEV 空间融合 | medium | T02-S030 |
| MapTR | 在线矢量高精地图，去重图路线的关键件 | medium | T02-S031 |
| OpenCalib | 多传感器标定工具箱 | medium | T02-S032 |
| acados + CasADi + OSQP | 嵌入式 MPC 的建模-求解组合 | low | T02-S033, T02-S034, T02-S035, T02-S036 |
| PythonRobotics | 规划与定位算法的可运行教材 | low | T02-S038 |
| HighwayEnv | 决策层强化学习的轻量环境 | medium | T02-S039 |
| UniAD | 面向规划的一体化端到端参考实现 | medium | T02-S040 |
| TransFuser + carla_garage | CARLA 闭环模仿学习的强基线与 starter kit | medium | T02-S041, T02-S042 |
| openpilot | 唯一能装到量产车上的开源 L2 | medium | T02-S037 |
| CVAT | 通用开源标注平台，含点云 | medium | T02-S043, T02-S044 |
| SUSTechPOINTS | 点云标注平台，学术出身、可自建 | medium | T02-S045 |
| Xtreme1 | 带自动标注的多模态标注平台 | high | T02-S046 |
| IPG CarMaker | 车辆动力学保真的闭环仿真 | low | T02-S060 |
| dSPACE ADAS HIL | 硬件在环，把真 ECU 接进仿真回路 | low | T02-S061 |
| Applied Intuition | 商业仿真与验证平台 | medium | T02-S057, T02-S058 |
| Foretellix Foretify | 抽象场景 + 覆盖度驱动的验证平台 | medium | T02-S059 |
| SUMO | 微观交通流仿真，做背景流量 | low | T02-S062 |
| MATLAB/Simulink Automated Driving Toolbox | 控制与功能安全侧的建模-代码生成链 | low | T02-S063 |
| Ansys medini analyze | HARA / FMEA / FTA / FMEDA / SOTIF 的一体化工具 | low | T02-S064 |
| ad-rss-lib | RSS 形式化安全模型的可运行实现 | medium | T02-S065, T02-S051 |
| GSN 安全案例记法 | 安全论证的图式标准，工具生态薄 | low | T02-S066 |
| nuPlan devkit | 闭环规划评测框架 | medium | T02-S069, T02-S076 |
| CARLA Leaderboard 2.0 | 最难的公开闭环榜单，也最少人能提交 | medium | T02-S052, T02-S042 |
| Bench2Drive | 220 条短路线的闭环多能力基准 | medium | T02-S072, T02-S073 |
| NAVSIM | 非反应式伪仿真，PDMS 单标量分 | medium | T02-S074, T02-S075 |
| DriveLM | 图式视觉问答驱动，语言接口的评测入口 | high | T02-S084 |

### 新兴（8 个 · 全部 `stability: experimental`）

| 工具 | 一句话 | 首次公开 | Decay | 主要 evidence |
|------|--------|----------|-------|---------------|
| rmw_zenoh | ROS 2 的非 DDS 中间件替代 | 随 Jazzy 引入（2024） | high | T02-S015 |
| Agnocast | 支持不定长消息的真零拷贝 IPC | ISORC 2025 | high | T02-S016, T02-S017 |
| NVIDIA Omniverse NuRec | 3DGS 神经重建，真日志转可渲染场景 | 2025 GA | high | T02-S079 |
| InstantNuRec | 前馈式重建，一次前向出 3DGS 场景 | 2026-07 | high | T02-S080 |
| HUGSIM | 3DGS 闭环仿真器 + 跨数据集基准 | 2024-12 arXiv | high | T02-S081, T02-S082 |
| nuPlan-R | 用学习式反应智能体重做 nuPlan 闭环 | 2025-11 arXiv | high | T02-S077 |
| WOD-E2E + RFS | 长尾场景端到端评测与人评分数 | 2025-10 arXiv / CVPR 2026 | high | T02-S078, T02-S071 |
| NVIDIA Alpamayo-1 | 开放 10B 驾驶 VLA + 因果链推理 | 仓库建于 2025-11-19 | high | T02-S083 |

---

## 1. 车端与中间件

### 1.1 ROS 2（+ rosbag2 / RMW 层）— 必备

- **One-liner**：把感知/规划/控制拆成进程并用话题连起来的骨架，研究侧与多数 L4 团队的默认起点。
- **Maintainer / License**：Open Robotics / ROS 2 项目，Apache-2.0。
- **成熟度**：Autoware 主线在 2026 年执行 Humble → Jazzy 迁移，公开时间表为 Jazzy Docker Beta 2026-02、Jazzy 全量支持 2026-04、Humble 软冻结 2027-01、Jazzy 独占 2027-05 (evidence: [T02-S006])。这条时间表本身说明 ROS 2 在这一行的版本节奏是被下游栈拖着走的。
- **相对优劣**：生态（消息定义、可视化、录制、驱动）没有对手；代价是**默认配置下的实时性与确定性达不到量产控制器要求**。公开实测显示，给 Linux 打 PREEMPT_RT 补丁后 ROS 2 的最坏延迟与端到端抖动可下降约一个数量级，才够到现代自动驾驶控制器的确定性目标 (evidence: [T02-S012])。**没打补丁的 ROS 2 + 默认 DDS 不能直接当量产实时栈用**——这是本轨最常见的外行误判之一。
- **不适合**：ASIL-B/D 的执行链路、硬实时控制环。
- **URL**：https://github.com/ros-tooling/rosbag2_storage_mcap（录制层） (evidence: [T02-S001])
- **Decay risk**：low（24 个月内被取代概率 < 20%）

### 1.2 Autoware（Core + Universe）— 必备

- **One-liner**：唯一有基金会治理、覆盖感知到控制全链路的开源自动驾驶栈。
- **Maintainer / License**：Autoware Foundation，Apache-2.0。
- **Maturity**：元仓库 12,040 star / 3,709 fork，最近 push 2026-09-01（seed 快照 2026-09-02）；`autoware_universe` 1,746 star、483 open issue，最近 push 2026-09-02 (evidence: [T02-S005])。`autoware_core` v1.9.0 发布于 2026-06-26，本次引入 `autoware_command_gate`、倒车动作的基础设施（route planning 的 area primitive、区域可视化、overlapped direction_change 车道上的倒车目标位姿），并大幅扩展 `autoware_agnocast_wrapper`（service/client、Timer API、tf2 API、diagnostic_updater API、ExactTime 消息同步、ON_NODE 宏、launch 封装） (evidence: [T02-S006])。
- **结构要点**：Core 是稳定的最小集，Universe 是快速演进的功能池——**两者的稳定性承诺不同，混用时要按包而不是按仓库判断成熟度** (evidence: [T02-S008])。
- **谁在用**：TIER IV 及其生态；学界的 ROS 2 全栈实验默认从这里起步。
- **相对优劣**：优点是"从传感器到线控的每一环都能读到源码"；缺点是**默认参数是为演示与开发调优的，不是为某个具体 ODD 调优的**，直接跑在新场地上表现会很差。
- **URL**：https://github.com/autowarefoundation/autoware
- **Decay risk**：low

### 1.3 Baidu Apollo + Cyber RT — 必备

- **One-liner**：模块化量产栈的公开教科书，配一个专为确定性调度写的中间件。
- **Maintainer / License**：百度，Apache-2.0。
- **Maturity**：26,819 star / 9,958 fork / 1,046 open issue，最近 push 2026-04-16（seed 快照 2026-09-02） (evidence: [T02-S009])。注意最近 push 距快照约 4.5 个月，**主仓库活跃度低于 Autoware**，选型时要把这条算进去。
- **为什么不用 ROS**：官方 FAQ 的口径是 Apollo 从研发走向量产、需要更高鲁棒性与性能，因此自建 Cyber RT；ROS 版本只保留在 Apollo 3.0 及更早 (evidence: [T02-S010])。
- **中间件实测（第三方，非厂商）**：Cyber RT 走共享内存，在不同负载下延迟更稳定、减少序列化；代价是内存占用比 Fast DDS 高出数十 MB。Fast DDS 在数据量增大时延迟显著上升，主因是多次序列化开销 (evidence: [T02-S012])。**这条是有独立论文支撑的对比，比厂商自述可靠。**
- **厂商宣称（只作宣称记录）**：Apollo 10.0 于 2024-12-04 发布，宣称 Cyber RT 升级后支持零拷贝、微秒级传输、性能提升十倍；应用层资源占用降低 50%，可在单颗 NVIDIA Orin 上实现 L4 能力。**这些数字来自发布口径，没有公开的独立复现，不作为能力证据。**
- **URL**：https://github.com/ApolloAuto/apollo
- **Decay risk**：low（作为学习材料）/ medium（作为可跟随的活跃上游）

### 1.4 Cyclone DDS / Fast DDS（RMW 实现选型）— 场景特化

- **One-liner**：ROS 2 底下真正搬数据的两种实现，换一个 RMW 相当于换掉整套 QoS 与延迟特性。
- **License**：Cyclone DDS = Eclipse Public License 2.0 / EDL；Fast DDS = Apache-2.0。
- **适合 / 不适合**：大消息（图像、点云）高频传输时，Fast DDS 的序列化开销会放大延迟 (evidence: [T02-S012])；此时应优先走共享内存/零拷贝路径而不是调 QoS 参数。跨主机分布式部署、需要成熟发现协议时，DDS 仍是唯一现成答案。
- **URL**：https://github.com/eclipse-cyclonedds/cyclonedds · https://github.com/eProsima/Fast-DDS
- **Decay risk**：low

### 1.5 rmw_zenoh — 新兴（`stability: experimental`）

- **One-liner**：把 ROS 2 的中间件层从 DDS 换成 Zenoh，绕开 DDS 的发现风暴与配置复杂度。
- **状态**：随 ROS 2 Jazzy Jalisco 引入，作为**实验性**发布覆盖 Jazzy / Rolling / Iron，二进制包在各自 Tier-1 平台上提供；当前范围限定在依赖 rcl 的 ROS 2 节点 (evidence: [T02-S015])。
- **重要限定**：`rmw_zenoh` 与 `zenoh-plugin-ros2dds`（DDS↔Zenoh 桥）**用法不同且不能互操作** (evidence: [T02-S015])。混淆这两者是常见坑。
- **不适合**：任何需要与既有 DDS 车载网络互通的项目。
- **Decay risk**：high（12 个月内显著变化概率 > 40%）

### 1.6 Agnocast — 新兴（`stability: experimental`）

- **One-liner**：rclcpp 兼容的真零拷贝进程间通信，专门解决"消息里带 `std::vector` 就零拷贝不了"的问题。
- **来龙去脉**：Autoware 大量使用不定长消息类型（属性里含 `std::vector` 等），既有 IPC 方案（含事实标准 iceoryx）对这类 ROS 2 消息做不到真零拷贝，因此 TIER IV 另起一套 (evidence: [T02-S016])。
- **证据强度**：论文被 IEEE ISORC 2025 接收，生产版本已并入 Autoware；引入过程与设计取舍在基金会的公开讨论帖里可追溯 (evidence: [T02-S007])；官方口径是 IPC 开销与消息大小无关（常数开销） (evidence: [T02-S017])。Autoware 侧封装包 `autoware_agnocast_wrapper` 在 ROS Index 有正式条目 (evidence: [T02-S018])，Core 1.9.0 对它做了大幅扩展 (evidence: [T02-S006])。
- **不适合**：非 Linux、非 C++、跨主机通信。
- **Decay risk**：high（接口仍在扩张，Core 每个小版本都在改）

### 1.7 MCAP — 必备

- **One-liner**：自描述、可索引、支持异构多通道的机器人日志容器。
- **关键事实**：MCAP 从 ROS 2 **Iron 版起**成为默认存储格式，`ros2 bag record` 开箱即写 MCAP (evidence: [T02-S003])。行式追加写保证写入快而可靠，可选索引 + LZ4 / Zstandard 压缩优化读取与体积；一个文件可容纳 ROS、JSON、Protobuf 等多种格式并内嵌 schema，便于长期可读 (evidence: [T02-S002])。
- **为什么它是必备而不是可选**：数据闭环的第一公里就是"车上录了什么、能不能十年后还读得懂"。内嵌 schema 这一条直接决定了老数据在模型迭代若干轮之后还能不能重放。
- **URL**：https://github.com/foxglove/mcap · https://github.com/ros-tooling/rosbag2_storage_mcap
- **Decay risk**：low

### 1.8 Foxglove — 必备

- **One-liner**：录制日志与在线栈的可视化前端，看 3D 场景、话题曲线与时间轴对齐。
- **License / 商业模式**：核心为商业产品（免费额度 + 付费团队/企业版），依赖的 MCAP 与 ROS 桥接为开源。
- **两种接入**：通过 Foxglove Bridge 看运行中的栈，或直接打开 `.mcap` 文件回放 (evidence: [T02-S004])。
- **不适合 / 替代**：只想看 ROS 消息曲线用 `rqt` / PlotJuggler 即可；深度依赖厂商云端数据平台会带来数据出境与合规问题，中国量产项目通常自建。
- **Decay risk**：medium（商业产品，定价与免费额度会变）

### 1.9 NVIDIA DRIVE 平台（DriveOS / DriveWorks / Hyperion）— 必备

- **One-liner**：中外大量高阶智驾项目的车端算力与 SDK 基座；也是"某家车企的软件栈实际长什么样"最可核实的公开材料。
- **厂商宣称（标明为宣称，不作能力证据）**：DRIVE AGX Thor 基于 Blackwell 架构，宣称最高 2,000 FP4 TFLOPS、最高 1,000 INT8 TOPS 的原始深度学习算力；DriveOS 7.0.3 宣称具备 ISO 26262 认证就绪（certification readiness）、安全启动与面向生成式模型的 TensorRT 优化；平台面向 ISO 26262 ASIL-D 与 ISO 21434 开发 (evidence: [T02-S019, T02-S020])。
- **必须保留的限定语**：① **"认证就绪"不等于"已认证"**，两者在功能安全语境下差别很大；② TOPS 是**峰值**数字，与实际帧率无直接换算关系，任何"多少 TOPS 就能跑城区 NOA"的说法都缺少工况前提；③ FP4/INT8 是不同精度口径，不能互相比较。
- **相对优劣**：工具链完整、生态大、招人容易；代价是**成本与功耗高**，且强绑定 CUDA 生态，一旦换平台，量化与部署链路要重做。
- **Decay risk**：low（平台代际约 2-3 年一换，但生态位稳定）

### 1.10 TensorRT — 必备

- **One-liner**：把训练框架里的网络编译成能落进车规延迟预算的推理引擎。
- **厂商宣称**：TensorRT 10 引入动态 kernel 生成与融合、改进的 ModelOpt 量化（含 INT4 AWQ）；在 Blackwell/Thor 上支持 NVFP4 与 INT4 weight-only 量化 (evidence: [T02-S021])。
- **实践要点**：**量化后的精度回归必须在自己的数据上重测**，公开的量化损失数字都带训练集与校准集前提，换域就不成立。
- **不适合 / 替代**：非 NVIDIA 平台上完全不可用；地平线走天工开物、高通走自家 SDK，**这三条链路的量化算子支持集合不同，模型结构选型阶段就要按目标平台反推**。
- **Decay risk**：low

### 1.11 地平线征程 6 + 天工开物 OpenExplorer — 场景特化

- **One-liner**：中国本土量产智驾项目里最常见的另一条车端算力 + 量化编译链。
- **厂商宣称（标明为宣称）**：征程 6 系列算力覆盖 10 TOPS～560 TOPS，征程 6P 为面向全场景辅助驾驶的旗舰版；天工开物（OpenExplorer）为自研算法工具链，含模型后量化、量化训练、编译优化与部署三大能力，提供量化-优化-编译-仿真-部署-调试全流程支持 (evidence: [T02-S022])。
- **不作为能力证据**："累计赋能超过两百家生态伙伴"这类数字是厂商自述，没有独立核算口径。
- **可核实的一手材料**：官方开发者社区（论坛 + 参考算法 + 工具链文档）是判断"某个模型结构在 J6 上到底能不能跑"的实际入口 (evidence: [T02-S023])。**注意中文技术内容大量散落在第三方博客平台，其中大部分是转载或过期版本，应以官方开发者站为准。**
- **适合**：目标是国内量产、需要成本与供应链本地化的项目。
- **不适合**：需要快速复现学术 SOTA 的研究团队——算子支持与社区样例密度不如 CUDA 生态。
- **Decay risk**：medium（产品代际推进快，工具链版本兼容性变动频繁）

### 1.12 高通 Snapdragon Ride / Ride Flex — 场景特化

- **One-liner**：把座舱与智驾放在同一颗芯片上跑的混合关键性平台。
- **厂商宣称**：Ride Flex 被表述为业界首个商用的混合关键性平台，可在单一硬件上同时承载数字座舱与 ADAS/自动驾驶负载 (evidence: [T02-S024])。
- **公开的落地信号（媒体与厂商口径混合，按较弱证据处理）**：Ride Flex 已在若干全球项目量产，中国 Tier1（德赛西威等）宣布基于 Ride Flex 的量产计划。**具体数字随时间变化快，引用时必须带日期。**
- **适合**：成本敏感、想省掉一颗独立座舱 SoC 的中低阶到中阶项目。
- **不适合 / 风险**：混合关键性意味着**座舱侧的故障隔离必须做到位**，否则功能安全论证反而更难写。这是选型时最容易被销售话术带过去的一条。
- **Decay risk**：medium

### 1.13 Vector CANoe.ADAS + CANape — 必备（量产侧）

- **One-liner**：量产 ADAS 的总线分析、测量标定与传感器数据回放工具，在整车厂与 Tier1 侧几乎绕不开。
- **能力口径（厂商文档）**：CANoe.ADAS 支持用真实路采数据做开环测试，也支持仿真闭环场景；分析模块提供总线流量、信号值与错误帧的实时可视化 (evidence: [T02-S025])。CANape 24 支持 ASAM CMP 协议，兼容 CAN / FlexRay / LIN / 车载以太网（xBASE-T1），面向 Zonal ECU 与高性能计算单元；ADAS 侧可直接可视化可行驶区域与障碍物，评估相机/毫米波/激光的结果 (evidence: [T02-S026])。
- **相对优劣**：优点是与量产标定、诊断、总线协议栈的贴合度无可替代；缺点是**闭源、按席位授权、价格高，且与开源感知栈的数据格式几乎不互通**——研究团队通常完全不接触它。
- **这条为什么重要**：只从 GitHub 看这一行，会完全看不见 Vector 这一层，从而低估量产落地的工具成本。
- **Decay risk**：low

---

## 2. 感知

### 2.1 OpenPCDet — 必备

- **One-liner**：激光雷达 3D 检测的通用工具箱，多数点云检测论文的复现基线。
- **Maturity**：5,697 star / 1,472 fork / 31 open issue，Apache-2.0；**最近 push 2025-10-08**（seed 快照 2026-09-02），距快照约 11 个月，活跃度判为 declining (evidence: [T02-S027])。
- **含义**：仍是可用的强基线，但**不要指望它跟进 2026 年的新方法**；新模型多半只在作者自己的 fork 里。
- **Decay risk**：medium

### 2.2 mmdetection3d — 必备

- **One-liner**：多模态 3D 感知的训练脚手架，配置驱动、数据集适配层完整。
- **相对优劣**：优点是 nuScenes / KITTI / Waymo 的数据管线都现成，换数据集只改配置；缺点是**抽象层厚，调试链路长**，往车端搬的时候几乎要重写推理侧。
- **不适合**：直接当车端推理框架用。它是训练与离线评测的工具，不是部署工具。
- **URL**：https://github.com/open-mmlab/mmdetection3d (evidence: [T02-S028])
- **Decay risk**：medium

### 2.3 BEVFormer — 场景特化

- **One-liner**：用时空 Transformer 把多相机特征投到鸟瞰图（BEV，把各相机图像统一到俯视平面的表示）里的参考实现。
- **Maturity**：4,588 star / 749 fork / 184 open issue，Apache-2.0；**最近 push 2024-08-15**（seed 快照 2026-09-02），已基本停更 (evidence: [T02-S029])。
- **适合**：作为纯视觉 BEV 的教学与消融基线。
- **不适合**：作为 2026 年的起手式生产代码。它的历史价值大于工程价值——**开源仓库的 star 数与它当下的可用性是两件事**。
- **Decay risk**：medium

### 2.4 BEVFusion — 场景特化

- **One-liner**：把相机与激光的特征在统一 BEV 空间里融合，而不是在检测框层面后融合。
- **适合**：有激光雷达、要在检测/分割上同时吃两种模态收益的项目。
- **不适合**：纯视觉路线（无激光）项目；标定误差大的车队（BEV 融合对外参精度敏感，**这条直接把 OpenCalib 拉成前置依赖**）。
- **URL**：https://github.com/mit-han-lab/bevfusion (evidence: [T02-S030])
- **Decay risk**：medium

### 2.5 MapTR — 场景特化

- **One-liner**：在线构建矢量化高精地图，是"去高精地图"路线里真正要落地的那块。
- **Maturity**：1,544 star / 249 fork / 134 open issue，MIT；最近 push 2025-03-03（seed 快照 2026-09-02） (evidence: [T02-S031])。
- **适合**：城区领航要摆脱图商更新周期的项目。
- **不适合**：把在线建图当成"不需要地图"——**在线矢量地图的稳定性与高精地图不是一个量级**，多数量产方案仍保留轻图或导航级先验。这条上业内有明确分歧，不要按单一说法定论。
- **Decay risk**：medium

### 2.6 OpenCalib（SensorsCalibration）— 场景特化

- **One-liner**：相机/激光/毫米波/IMU 的内外参标定工具箱。
- **Maturity**：3,209 star / 705 fork / 145 open issue，Apache-2.0；**最近 push 2024-06-17**（seed 快照 2026-09-02），停更超两年 (evidence: [T02-S032])。
- **适合**：搭自己的采集车、需要一套能读源码的标定流程做起点。
- **不适合**：量产标定线（节拍、可追溯性、一致性要求完全不同，量产侧走 Tier1 的产线标定方案）。
- **Decay risk**：medium（算法本身不过时，但仓库不再维护，需自行适配新传感器）

---

## 3. 预测与规划控制

### 3.1 acados + CasADi + OSQP（嵌入式 MPC 栈）— 场景特化

- **One-liner**：把模型预测控制（MPC，用一个模型往前推几秒、每周期重解一次优化）真正压进毫秒级实时预算的建模-求解组合。
- **怎么组合的**：用户在 MATLAB 或 Python 里用 CasADi 的建模语言写动力学、代价与约束，CasADi 生成高效 C 代码做函数与导数求值；acados 负责最优控制问题结构，可按需搭配积分器（显式/隐式 Runge-Kutta、GNSF-IRK）、Hessian 近似（Gauss-Newton、正则化精确 Hessian、SCQP）与 QP 求解器（HPIPM、qpOASES、OSQP） (evidence: [T02-S033, T02-S034, T02-S036])。
- **真实生产案例**：openpilot 用 acados 做横向与纵向 MPC，通过 Cython 封装调用其 OCP 求解器 (evidence: [T02-S033, T02-S037])。这是少见的"开源 MPC 栈跑在真车上"的可核实案例。
- **不适合**：只想快速验证一个规划想法——直接用 OSQP 写个二次规划或用采样式规划更省事；OSQP 是一阶方法，**大规模稀疏问题上快，但对高精度解的收敛慢于内点法**，控制回路对解精度敏感时要评估 (evidence: [T02-S035])。
- **Decay risk**：low

### 3.2 PythonRobotics — 场景特化

- **One-liner**：规划、定位、控制算法的可运行样例库，当教材用。
- **Maturity**：30,431 star / 7,399 fork，最近 push 2026-09-02（seed 快照当天），是本轨 seed 池中 star 最高且仍在活跃的仓库 (evidence: [T02-S038])。
- **适合**：入行前 3 个月建立算法直觉；面试准备；给非专业同事解释一个规划器在干什么。
- **不适合**：任何生产用途。它明确是教学代码。
- **Decay risk**：low

### 3.3 HighwayEnv — 场景特化

- **One-liner**：决策层（换道、汇入、路口通行）的轻量强化学习环境集。
- **Maturity**：3,302 star / 887 fork / 38 open issue，MIT，最近 push 2026-09-01（seed 快照 2026-09-02），归 Farama Foundation 维护 (evidence: [T02-S039])。
- **适合**：验证"决策策略该不该用 RL"这类问题，几小时内能出结论。
- **不适合**：把在这里训出来的策略当成可迁移的驾驶策略——**运动学被高度简化，其他车的行为是脚本或 IDM，与真实交互不在一个量级**。
- **Decay risk**：medium

### 3.4 UniAD（与 VAD 同族）— 场景特化

- **One-liner**：把检测、跟踪、建图、预测、占据、规划串成一个网络并以规划为导向的参考实现。
- **Maturity**：4,746 star / 550 fork / 127 open issue，Apache-2.0，最近 push 2025-10-29（seed 快照 2026-09-02） (evidence: [T02-S040])。CVPR 2023 最佳论文。
- **适合**：理解"一体化端到端"的模块耦合方式；做消融研究。
- **不适合 / 关键限定**：它在 nuScenes 上的开环规划指标**不能读作驾驶能力**。同期研究表明，只用自车状态（ego status）就能在 nuScenes 开环端到端上拿到有竞争力的指标，说明这套开环口径存在捷径 (evidence: [T02-S076])。
- **Decay risk**：medium

### 3.5 TransFuser + carla_garage — 场景特化

- **One-liner**：CARLA 闭环里的模仿学习强基线，以及 Leaderboard 2.0 的 starter kit。
- **Maturity**：transfuser 1,599 star / 244 fork，MIT，最近 push 2025-10-19（seed 快照 2026-09-02） (evidence: [T02-S041])。
- **独有价值**：carla_garage 的核心贡献之一是**把端到端驾驶模型的隐藏偏差摆出来**（ICCV'23），而不是刷分 (evidence: [T02-S042])。选它做基线的理由是"知道自己在哪里作弊"，不是分数。
- **不适合**：真车部署。CARLA 里的传感器与动力学与真车差距大。
- **Decay risk**：medium

### 3.6 openpilot — 场景特化

- **One-liner**：唯一一套可以真的装到量产车上、并且社区规模足够大的开源 L2 辅助驾驶。
- **License / 商业模式**：MIT（软件）+ comma 硬件销售 (evidence: [T02-S037])。
- **独有价值**：它是**开源栈里唯一一个必须直面"真实用户在真实路上会怎么误用"的项目**，因此它的驾驶员监控、接管逻辑、纵横向 MPC 参数都有大量真实里程反馈。
- **不适合 / 必须写清的风险**：装车涉及改装与责任归属，各地法规不同；**它不是、也没有声称是符合 ISO 26262 流程开发的产品**。任何把它的表现当作"开源栈可以上量产车"的论据都跳过了功能安全流程这一层。
- **Decay risk**：medium

---

## 4. 数据闭环

> **本节的诚实边界**：数据闭环是这一行**开源覆盖最差**的一环。采集触发、影子模式回传、难例挖掘、数据版本管理、云端训练评测流水线——这些在头部公司都是自建闭源系统，公开的只有综述与零星工具。本节因此比其它节短，这**不是调研不足，是这一维度本身没有公开工具栈**。

### 4.1 方法学基线：数据闭环与自动标注综述

- 综述系统整理了从手工标注 → 半自动 → 全自动标注的演进，并指出 3D 动态目标自动标注与 3D 静态场景自动标注是 BEV 感知普及后的刚需；Waymo 提出了基于激光点云序列的 3D Auto-Labeling 流水线，Uber 的 Auto4D 把标注推到时空四维尺度 (evidence: [T02-S047])。
- 综述同时指出，现有方案在"数据闭环"与"模型闭环"之间通常是**分开设的两套**，而长尾分布与 corner case 是核心矛盾 (evidence: [T02-S047])。
- **用法**：把这篇当作自建数据闭环时的检查清单，不要指望它给你可运行的代码。

### 4.2 CVAT — 场景特化

- **One-liner**：通用开源标注平台，支持 2D 与点云。
- **License**：MIT（自 2023 年起部分企业功能另行授权，选型时需按版本核对）。
- **适合**：自建标注团队、数据不能出境、需要私有部署。
- **不适合**：大规模 4D 序列标注——通用平台在时序一致性上的工效远不如专用工具 (evidence: [T02-S043, T02-S044])。
- **Decay risk**：medium

### 4.3 SUSTechPOINTS — 场景特化

- **One-liner**：学术出身的 3D 点云标注平台，含可视化定位标注错误、跨帧标注传递。
- **证据**：IEEE IV 2020 论文对应实现，开源；3,209 量级的同类仓库中它是少数有论文背书的 (evidence: [T02-S045])。
- **适合**：小规模自采数据、要能改前端交互的团队。
- **不适合**：要 SLA 与审计追踪的量产标注产线。
- **Decay risk**：medium

### 4.4 Xtreme1 — 场景特化

- **One-liner**：带自动 3D 标注与自动 2D 检测/分割的多模态标注平台，支持多视角点云输入。
- **相对优劣**：功能上覆盖 SUSTechPOINTS 的大部分能力并补上自动化 (evidence: [T02-S046])；代价是依赖更重、部署更复杂。
- **Decay risk**：high（此类平台迭代快，开源与商业版功能边界变动频繁）

### 4.5 日志层（回到第 1 节）

- 数据闭环的入口是**录制格式**，不是标注工具。MCAP 的内嵌 schema 与索引直接决定了历史数据的可重放年限 (evidence: [T02-S002, T02-S003])；Foxglove 决定了工程师能不能在五分钟内定位到那一帧 (evidence: [T02-S004])。**先把这两件事定下来，再谈自动标注。**

---

## 5. 仿真与验证

### 5.1 CARLA — 必备

- **One-liner**：开源闭环驾驶仿真的事实基座，绝大多数公开闭环实验的运行环境。
- **Maturity**：14,352 star / 4,683 fork / 1,192 open issue，MIT，最近 push 2026-09-02（seed 快照当天） (evidence: [T02-S048])。
- **版本分叉（选型必须知道）**：0.10.0 于 2024-12-19 发布，从 Unreal Engine 4.26 迁到 UE 5.5，引入 Lumen 与 Nanite，升级 Town 10 与车辆资产，新增露天矿地图，接入 Inverted AI 的生成式交通流与原生 ROS 集成 (evidence: [T02-S049, T02-S050])。**UE 4.26 与 UE 5.5 两个版本会长期共存**——部分功能与资产尚未迁移，官方明说这是有意为之 (evidence: [T02-S050])。选错分支会导致既有脚本与资产不可用，这是新人最常踩的坑。
- **相对优劣**：优点是免费、可编程、社区大、几乎所有公开闭环基准都建在它上面；缺点是**传感器仿真与真实传感器的域差距（domain gap）大**，感知模型在 CARLA 上的表现与真车几乎不可比。
- **正确用法**：**用它评规划与决策的闭环行为，不要用它证明感知能力。**
- **Decay risk**：low

### 5.2 SVL Simulator（原 LGSVL）— 已停止维护，不进任何层

- 仓库仍可访问，但项目已停止维护 (evidence: [T02-S053])。**2026 年任何"CARLA vs LGSVL 二选一"的建议都是过期材料**，遇到这类文章可以直接判定其时效性有问题。列在这里是为了让读者能识别过期建议。

### 5.3 ASAM OpenDRIVE + OpenSCENARIO 工具链 — 必备

- **One-liner**：路网（OpenDRIVE）与场景（OpenSCENARIO）的描述标准，是跨仿真器、跨供应商交换测试用例的唯一现实通道。
- **版本状态（引用时必须带版本号）**：
  - OpenSCENARIO 在 2024-01 被拆名：1.x → **OpenSCENARIO XML**（具体场景描述），2.x → **OpenSCENARIO DSL**（可写抽象场景、支持大规模覆盖） (evidence: [T02-S055])。
  - OpenSCENARIO DSL **2.1 于 2024-03 发布**；截至 2026 年初，ASAM 在公开评审 **2.2.0 候选版** (evidence: [T02-S055])。
  - OpenDRIVE **1.8.0 为 2023-11 版本**；**1.9.0 规范正文页标注日期 2026-05-08** (evidence: [T02-S054, T02-S056])。
- **相对优劣**：优点是标准化后测试用例可复用、可交付给监管与客户；缺点是**标准本身不含求解器**——同一份 OpenSCENARIO 在不同仿真器上跑出的结果可以不同，这是行业公开的痛点，不是某个工具的 bug。
- **不适合**：内部快速实验（写 XML/DSL 的成本远高于直接写 Python 脚本）。
- **Decay risk**：low（标准），medium（具体版本的工具支持）

### 5.4 IPG CarMaker — 场景特化

- **One-liner**：车辆动力学保真度优先的闭环仿真，整车厂与 Tier1 的常见选择。
- **License / 商业模式**：闭源商业许可 (evidence: [T02-S060])。
- **适合 / 不适合**：需要评估控制器在真实底盘响应下的行为、做操稳与制动相关验证时选它；**要评感知与端到端模型时它不是合适工具**（渲染与传感器建模不是它的强项）。
- **纪律提醒**：厂商页面上的能力清单是宣称，**不能作为"覆盖了某 ODD"的证据**——覆盖度要由自己的场景库和度量来论证。
- **Decay risk**：low

### 5.5 dSPACE ADAS 硬件在环（HIL）— 场景特化

- **One-liner**：把真实 ECU 接进仿真回路，用实时机做传感器与总线注入。
- **适合**：量产项目的 V 模型右侧（集成与验证阶段），尤其是要验证真实控制器时序与故障注入行为时 (evidence: [T02-S061])。
- **不适合 / 成本现实**：HIL 台架是**六位数以上人民币量级的资本支出加持续的工程支持成本**，研究团队与初创通常负担不起，也不需要。
- **Decay risk**：low

### 5.6 Applied Intuition — 场景特化（商业）

- **One-liner**：商业仿真与验证平台，含场景库、验证包与工具链。
- **厂商宣称（严格按宣称处理）**：其验证包（verification packs）覆盖面向法规合规与特定 ODD 的场景；场景创建者基于功能需求写 OpenSCENARIO DSL 抽象场景，工具自动产出逻辑场景与具体场景，再用其自有 Object Sim 场景语言做细化 (evidence: [T02-S057, T02-S058])。
- **可核实的部分**：它对 ASAM OpenSCENARIO v2 的技术解读文章是公开的，可作为理解标准的二手材料 (evidence: [T02-S057])。
- **不能核实的部分**：覆盖度、场景库规模、"通过率"这类数字**没有独立第三方口径**。
- **Decay risk**：medium

### 5.7 Foretellix Foretify — 场景特化（商业）

- **One-liner**：抽象场景 + 覆盖度驱动验证（借鉴芯片验证的 coverage-driven verification 思路）的平台。
- **厂商宣称**：其 V-Suites 提供预置测试计划、抽象场景、地图、覆盖度指标、KPI 与 checker，分 L2 ADAS / L3 高速领航 / L4 卡车 / L4 矿区四条产品线；自称是首个原生实现 OpenSCENARIO DSL 2.1.x 的平台，并在 ASAM 内主导该标准的制定 (evidence: [T02-S059])。
- **保留的矛盾**：**"主导标准制定"既是可信度加分也是利益冲突**——标准的形态与其产品形态相互塑造。这条要写进选型评估，不要单纯当作背书。
- **Decay risk**：medium

### 5.8 SUMO — 场景特化

- **One-liner**：微观交通流仿真，用来造背景车流与路网级别的交通行为。
- **License**：EPL-2.0，Eclipse 基金会 / 德国宇航中心（DLR）出身 (evidence: [T02-S062])。
- **适合**：需要大规模、可标定的背景交通；做交通级别的策略评估。
- **不适合**：单车动力学与传感器仿真。它和 CARLA 是互补而非替代（常见做法是 SUMO 驱动交通、CARLA 渲染与执行自车）。
- **Decay risk**：low

### 5.9 MATLAB / Simulink Automated Driving Toolbox — 场景特化

- **One-liner**：控制与功能安全侧的建模、仿真与代码生成链条。
- **谁在用**：传统整车厂与 Tier1 的控制、底盘、功能安全团队；**感知与端到端团队几乎不用**。
- **相对优劣**：优点是与 ISO 26262 的工具链认证、需求追踪、自动代码生成配套成熟 (evidence: [T02-S063])；缺点是按席位授权成本高，且深度学习工作流远不如 PyTorch 生态顺手。
- **Decay risk**：low

### 5.10 NVIDIA Omniverse NuRec — 新兴（`stability: experimental`）

- **One-liner**：用 3D 高斯泼溅（3DGS，一种把场景表示成大量带颜色与透明度的小高斯体、可实时渲染的方法）把真实传感器日志重建成可交互仿真的场景。
- **能力口径（厂商文档）**：底层表示是 3DGS 的变体 3DGUT（3D Gaussian Unscented Transform），NVIDIA 自研，用于处理鱼眼与卷帘快门这类非线性相机投影；库已与 Isaac Sim、NVIDIA AlpaSim 以及开源 CARLA 集成 (evidence: [T02-S079])。
- **第三方使用信号**：密歇根大学 Mcity 用它给测试场做数字孪生 (evidence: [T02-S079])。这是少数有外部机构名字的采用证据。
- **不适合 / 关键限定**：神经重建解决的是**外观保真**，**不解决"重建场景里其他交通参与者的行为是否真实"**。用它做闭环评测时，行为侧仍需另配交通模型。
- **Decay risk**：high

### 5.11 InstantNuRec — 新兴（`stability: experimental`）

- **One-liner**：前馈式神经重建，把多相机驾驶日志一次前向就转成可仿真的 3DGS 场景，不再逐场景优化。
- **状态**：项目页与论文于 2026-07 公开 (evidence: [T02-S080])。配套的 Physical AI NuRec 数据集提供 1,500+ 段神经重建场景，每段约 20 秒、6 路相机视角 (evidence: [T02-S079])。
- **为什么值得盯**：逐场景优化是把"路采日志"变成"可仿真资产"的最大成本项；一旦这一步变成前馈，**日志重放与合成场景之间的边界会被抹掉**，这会直接改变仿真验证的成本结构。
- **Decay risk**：high（发布不足两个月）

### 5.12 HUGSIM — 新兴（`stability: experimental`）

- **One-liner**：基于 3DGS 的实时闭环驾驶仿真器，附带跨数据集基准。
- **口径（论文自述）**：把 2D RGB 抬升到 3D 高斯，处理闭环下的视角外推与 360 度车辆渲染，按控制指令动态更新自车与他车状态与观测；宣称超过 30 FPS；基准覆盖 KITTI-360、Waymo、nuScenes、PandaSet 的 70+ 段序列与 400+ 变体场景 (evidence: [T02-S081, T02-S082])。
- **限定语**：30 FPS 与场景数是**作者在其硬件与设置下的数字**，未见第三方复现。
- **Decay risk**：high

---

## 6. 安全与合规工具

> **本节的诚实边界**：安全论证工具的开源覆盖度比仿真还低。HARA / FMEA / FTA 类工具基本被少数商业厂商占据；安全案例（safety case）侧只有记法标准，**没有事实标准的编辑器**。

### 6.1 Ansys medini analyze — 场景特化（商业）

- **One-liner**：把 HAZOP、HARA、FTA、FMEA、FMEDA 放在同一个模型里做的安全分析环境。
- **能力口径（厂商文档）**：支持按 ISO 26262-3 做完整的 HARA（含 ASIL 判定与运行情境分析），并支持按 ISO/PAS 21448（SOTIF，预期功能安全）做危害分析；覆盖 ISO 26262 与 IEC 61508 (evidence: [T02-S064])。
- **谁在用**：整车厂与 Tier1 的功能安全团队；与 Simulink 有官方连接 (evidence: [T02-S063, T02-S064])。
- **不适合**：研究团队与初创（授权成本高，且早期项目的 HARA 用表格也做得动）。
- **保留的矛盾**：**工具能保证形式完整，不能保证危害识别完整**。SOTIF 的难点在"想不到的场景"，这一点没有工具能替你解决。
- **Decay risk**：low

### 6.2 ad-rss-lib — 场景特化

- **One-liner**：责任敏感安全（RSS，用一组可数学检验的最小安全距离与责任规则约束驾驶行为）模型的开源 C++ 实现。
- **License / 采用**：LGPL-2.1；已集成进百度 Apollo 开放平台栈；v1.6 起支持 Python (evidence: [T02-S065])。
- **在 CARLA 里的形态**：作为虚拟 `RssSensor`（检查器）与可选的 `RssRestrictor`（执行器）集成进客户端库，用户不写代码就能观察 RSS 行为——CARLA 负责喂输入并把输出实时施加到自动驾驶系统上 (evidence: [T02-S051])。
- **必须写清的限定**：初版实现的是 RSS 论文中**规则与计算的一个子集**，不是全集 (evidence: [T02-S065])。**"接了 ad-rss-lib"不等于"满足 RSS"，更不等于"安全"。**
- **不适合**：把它当作安全论证的替代品。它是一个可检验的行为约束层，安全案例还得自己写。
- **Decay risk**：medium

### 6.3 GSN（目标结构记法）与安全案例工具 — 场景特化

- **One-liner**：把"为什么我认为它足够安全"画成目标-策略-证据的图，是安全案例的通用记法。
- **状态**：由 SCSC（安全关键系统俱乐部）的保证案例工作组维护并发布标准版本 (evidence: [T02-S066])。
- **工具现实**：**没有事实标准的开源 GSN 编辑器**。可用的选项是商业保证案例工具、通用建模工具的插件、或直接用绘图工具 + 版本管理。这是这一行工具链最薄的一环。
- **为什么仍要列**：因为 UL 4600 与各家 Robotaxi 的公开安全材料都按这个结构组织，看不懂 GSN 就读不懂对方的安全论证。
- **Decay risk**：low（记法稳定）

### 6.4 STPA / 场景覆盖度分析 — 缺口，见第 11 节

- STPA（系统理论过程分析）的工具生态在自动驾驶语境下**没有形成公认选择**；场景覆盖度分析目前主要由商业平台（Foretellix、Applied Intuition）以自有度量提供，**各家度量互不可比** (evidence: [T02-S057, T02-S059])。本轨未找到可核实的开源替代，如实标记为缺口。

---

## 7. 评测基准与榜单：各自考什么、口径缺陷在哪

> **这一节是本轨最重要的部分**。这一行外行最大的误判就是把基准分数当能力。下面每一条都写清"考什么"和"已知缺陷"。

### 7.1 nuScenes（+ nuscenes-devkit）— 必备

- **考什么**：多传感器 3D 检测、跟踪、预测的离线（开环）指标；devkit 里的评测代码就是指标的可执行定义 (evidence: [T02-S067, T02-S068])。
- **已知口径缺陷（必须一起引用）**：在 nuScenes 的**开环端到端规划**口径下，只用自车状态（ego status）就能取得有竞争力的成绩，说明这套评测存在捷径，分数不能读作驾驶能力 (evidence: [T02-S076])。
- **正确用法**：用它比感知模块，不要用它比"端到端谁开得好"。

### 7.2 Waymo Open Dataset（+ toolkit + Challenges）— 必备

- **考什么**：感知、运动预测等多赛道；工具包内含官方评测实现 (evidence: [T02-S070], [T02-S071])。
- **2025-2026 的变化**：2025 年挑战赛于 2025-03-31 至 2025-05-22 举行，新增**基于视觉的端到端驾驶**赛道；赛期结束后排行榜继续开放供基准测试 (evidence: [T02-S071])。
- **WOD-E2E（新增数据与指标）**：4,021 段（约 12 小时）专门挑选的长尾场景，出现频率低于 0.03%；每段含高层路由信息、自车状态与 8 路环视相机。评测用新提出的开环指标 **Rater Feedback Score（RFS）**，衡量预测轨迹与人工评审标注的轨迹偏好标签的接近程度 (evidence: [T02-S078])。
- **口径缺陷**：RFS 仍是**开环**指标，且以人工偏好为参照系——**"更像评审喜欢的轨迹"与"在闭环里不出事"是两件事**。这条限定不能丢。

### 7.3 nuPlan（+ nuplan-devkit）— 场景特化

- **考什么**：大规模闭环规划，含非反应式与反应式两种回放模式 (evidence: [T02-S069])。
- **已知口径缺陷（本轨最该记住的一条）**：nuPlan 原始基准里规则式规划器占优，很可能是**在利用 IDM 智能体被简化的动力学**。在改用学习式反应智能体的 nuPlan-R 上，PDM-Closed 从 91.64 降到 90.62（Test14-Random）、从 75.19 降到 67.33（Test14-Hard）；而多个学习式规划器（GC-PGP、UrbanDriverOL、PlanTF、Diffusion-Planner）在更真实的设置下保持或改善 (evidence: [T02-S077])。
- **含义**：**"规则式规划器打败学习式"这个广为流传的结论，其成立范围依赖于背景交通模型的选择**。引用 PDM 的结论 (evidence: [T02-S076]) 时必须带上这条修正。

### 7.4 CARLA Leaderboard 2.0 — 场景特化

- **考什么**：7-10 公里长路线、密集塞入安全关键场景的闭环驾驶分（Driving Score = 路线完成度 × 违规惩罚系数） (evidence: [T02-S052])。
- **已知缺陷（多条，都要写）**：
  - **提交极少、分数极低**：由于 v2 的长路线极难，提交数很少且驾驶分都极低；carla_garage 的作者在 2024-12 表述其验证路线"大概是当时最难的公开自动驾驶基准" (evidence: [T02-S042])。低分意味着**分数之间的区分度差，名次不稳定**。
  - **无官方训练集**：v2 缺少专家演示数据与官方训练集，导致不同方法的比较是**系统级**而非算法级的（大家用的数据不一样） (evidence: [T02-S073])。
  - **域差距**：CARLA 的传感器与真实传感器差距大，分数不外推到真车。
- **正确用法**：当作压力测试与回归门禁，**不要当作安全证据**。

### 7.5 Bench2Drive — 场景特化

- **考什么**：基于 CARLA Leaderboard 2.0，用 220 条短路线覆盖安全关键场景，做闭环多能力评测；提供大规模带标注的官方训练集与多能力评测集，使比较能落到算法层而不是系统层 (evidence: [T02-S072, T02-S073])。NeurIPS 2024 Datasets & Benchmarks 收录。
- **相对 Leaderboard 2.0 的优劣**：更可比、更容易出区分度；代价是**短路线削弱了长程一致性的考察**。
- **口径提醒**：它仍然在 CARLA 里，仍然不外推到真车。

### 7.6 NAVSIM — 场景特化

- **考什么**：在 nuPlan 的过滤子集上做**非反应式**的"伪仿真"，用单标量 PDM Score 汇总：`PDMS = NC × DAC × (5×EP + 5×TTC + 2×C)/12`，其中 NC = 无自身责任碰撞、DAC = 可行驶区域合规、EP = 自车进度、TTC = 碰撞时间、C = 舒适性 (evidence: [T02-S074])。
- **数据口径**：每帧 8 路高分辨率相机 + 融合点云，2 Hz；标准训练集 navtrain 约 103,000 帧，测试集 navtest 约 12,000 帧；输入 1.5 秒历史，预测 4 秒 8 个航路点 (evidence: [T02-S074])。
- **设计意图**：填开环与闭环之间的沟——**比开环有意义，比闭环便宜** (evidence: [T02-S074, T02-S075])。
- **口径缺陷**：**非反应式**意味着其他车不会对你的动作做出反应，长时程行为的评估仍然失真。NAVSIM v2 引入"伪仿真"（把规划轨迹放进有反应式交通的仿真里执行）与扩展指标 EPDMS 来缓解这一点 (evidence: [T02-S075])。
- **Decay risk**：medium

### 7.7 DriveLM — 场景特化

- **考什么**：把驾驶拆成图结构的视觉问答，评测语言接口下的感知-预测-规划推理链 (evidence: [T02-S084])。ECCV 2024 Oral。
- **口径缺陷**：**语言回答正确不等于会开车**。它评的是可解释性与推理链的一致性，不是控制能力。
- **Decay risk**：high（VLA 方向变动快）

### 7.8 NVIDIA Alpamayo-1 — 新兴（`stability: experimental`）

- **One-liner**：开放权重的 10B 视觉-语言-动作（VLA）驾驶模型，把驾驶轨迹与"因果链（Chain-of-Causation）"推理配对。
- **Maturity**：仓库建于 **2025-11-19**，2,011 star / 337 fork / 70 open issue，Apache-2.0，最近 push 2026-08-29（seed 快照 2026-09-02） (evidence: [T02-S083])。**不足 10 个月，符合新兴层定义。**
- **为什么重要**：它把"端到端能不能给出理由"这件事变成了可下载、可复现的对象，而不是只有闭源演示。
- **不适合**：任何量产判断。开放权重模型没有 ODD 定义、没有安全论证、没有车规部署路径。
- **Decay risk**：high

### 7.9 nuPlan-R — 新兴（`stability: experimental`）

- **One-liner**：把 nuPlan 的背景交通从 IDM 换成学习式反应智能体，重做一遍闭环规划评测。
- **首次公开**：2025-11 arXiv (evidence: [T02-S077])。
- **考什么 / 改了什么**：它检验的是"原基准的排名有多少来自背景交通被简化"。结果是规则式规划器的优势明显缩水（PDM-Closed 在 Test14-Hard 上 75.19 → 67.33），而学习式规划器保持或改善；退化最明显的是碰撞时间、自车进度、舒适性与有责碰撞 (evidence: [T02-S077])。
- **为什么值得盯**：它把社区推向"退役 IDM 作为默认反应智能体"，一旦这条被广泛接受，**过去两年基于 nuPlan 的规划器排名都要重读** (evidence: [T02-S077])。
- **不适合**：直接拿来当既有 nuPlan 结果的替代——两套口径的分数不可直接比较。
- **Decay risk**：high（新基准，采纳度未定）

### 7.10 WOD-E2E + Rater Feedback Score — 新兴（`stability: experimental`）

- **One-liner**：Waymo 为长尾场景端到端驾驶专门做的数据集与人评参照指标。
- **首次公开**：2025-10 arXiv，CVPR 2026 收录 (evidence: [T02-S078])。
- **口径**：4,021 段（约 12 小时）出现频率低于 0.03% 的长尾场景，每段含高层路由、自车状态与 8 路环视相机；指标 RFS 衡量预测轨迹与人工评审的轨迹偏好标签的接近程度 (evidence: [T02-S078])。2025 年 Waymo 挑战赛已设基于视觉的端到端赛道，赛期结束后排行榜继续开放 (evidence: [T02-S071])。
- **缺陷**：**仍是开环**，且参照系是人工偏好而非闭环后果。"更像评审喜欢的轨迹"和"在闭环里不出事"是两件事。
- **Decay risk**：high

---

## 8. 选型决策树

> 节点数 8。每个分支的推荐都能回溯到上文的 evidence。

### 决策树入口：你在哪条路线上？

#### Branch 1：L2 / L2+ 量产（城区或高速领航，目标是上车卖钱）

- **车端与中间件**：**不要**用 ROS 1（早已不适合量产），也不要默认 ROS 2 就够。要么走供应商中间件，要么在 ROS 2 上打 PREEMPT_RT 并自证时序 (evidence: [T02-S012])。
- **算力平台**：NVIDIA DRIVE（生态与招人最容易，成本最高） (evidence: [T02-S019]) / 地平线征程 6 + 天工开物（本土成本与供应链） (evidence: [T02-S022]) / 高通 Ride Flex（想省一颗座舱 SoC，但要接受混合关键性带来的隔离论证负担） (evidence: [T02-S024])。**这三条链路的量化算子集合不同，模型结构在立项时就要按目标平台反推** (evidence: [T02-S021, T02-S022])。
- **验证工具**：Vector CANoe.ADAS + CANape 基本绕不开 (evidence: [T02-S025, T02-S026])；场景验证走 ASAM OpenSCENARIO + 商业平台（Foretellix / Applied Intuition），并接受"覆盖度指标各家不可比"这一现实 (evidence: [T02-S057, T02-S059])。
- **安全**：Ansys medini analyze 做 HARA/FMEA/SOTIF (evidence: [T02-S064])；安全案例用 GSN 组织 (evidence: [T02-S066])。
- **不推荐**：把 CARLA 通过率写进安全论证；把 Autoware 直接当量产栈。

#### Branch 2：L4 Robotaxi / 无人物流（自建全栈，有安全员到无安全员的路径）

- **起点**：Autoware（有基金会治理、模块边界清楚） (evidence: [T02-S005, T02-S006]) 或 Apollo（模块化教科书，但主仓库活跃度需自行核对） (evidence: [T02-S009])。
- **中间件**：默认 ROS 2 + Cyclone/Fast DDS；大消息路径上评估零拷贝——Agnocast 是目前唯一支持不定长消息真零拷贝且有论文 + 生产集成的方案 (evidence: [T02-S016, T02-S017])。
- **日志**：MCAP + Foxglove 从第一天就上，别等数据规模上来再补 (evidence: [T02-S002, T02-S004])。
- **仿真**：日志重放为主（真实传感器数据）+ CARLA 做行为压测 + 神经重建（NuRec / HUGSIM）做视角外推的补充 (evidence: [T02-S079, T02-S081])。
- **安全**：ad-rss-lib 可以作为行为约束层，但要明说它只实现了 RSS 的子集 (evidence: [T02-S065])。
- **不推荐**：把开环基准（nuScenes / WOD-E2E）分数写进对外的能力叙述 (evidence: [T02-S076, T02-S078])。

#### Branch 3：研究（发论文 / 做算法预研）

##### Branch 3a：瓶颈在感知
→ mmdetection3d（数据管线全） (evidence: [T02-S028]) + OpenPCDet（激光基线，注意已 declining） (evidence: [T02-S027])；多模态用 BEVFusion (evidence: [T02-S030])，纯视觉 BEV 用 BEVFormer 当基线但知道它已停更 (evidence: [T02-S029])。评测走 nuScenes devkit (evidence: [T02-S067])。

##### Branch 3b：瓶颈在规划 / 决策
→ **不要**只报 nuScenes 开环指标 (evidence: [T02-S076])。闭环用 Bench2Drive（可比、有官方训练集） (evidence: [T02-S073])；想更接近真实数据分布用 NAVSIM (evidence: [T02-S074])；报 nuPlan 结果时必须说明用的是哪种背景交通模型 (evidence: [T02-S077])。

##### Branch 3c：瓶颈在控制
→ acados + CasADi，QP 后端按问题规模在 HPIPM / qpOASES / OSQP 里挑 (evidence: [T02-S033, T02-S034])；想看一个真车上的参考实现就读 openpilot 的横纵向 MPC (evidence: [T02-S037])。教学与直觉用 PythonRobotics (evidence: [T02-S038])。

##### Branch 3d：瓶颈在仿真保真度
→ CARLA 打底 (evidence: [T02-S048])，交通流接 SUMO (evidence: [T02-S062])，外观保真接 3DGS 路线（NuRec / InstantNuRec / HUGSIM），但要接受**它们解决外观不解决行为** (evidence: [T02-S079, T02-S080, T02-S081])。

#### Branch 4：只是要读懂别人的方案 / 做技术尽调

→ 读 ASAM 标准版本号（对方说"支持 OpenSCENARIO"要追问 XML 还是 DSL、哪个版本） (evidence: [T02-S055])；读对方的安全案例是不是按 GSN 组织 (evidence: [T02-S066])；读对方报的基准是开环还是闭环、背景交通是什么 (evidence: [T02-S077])。**这三问能筛掉大部分包装。**

---

## 9. 避坑清单

- ❌ **不要把开源仿真器的通过率当安全证据**。CARLA Leaderboard 2.0 提交极少且分数普遍极低，区分度本身就不足 (evidence: [T02-S042])；且 v2 无官方训练集，比较是系统级而非算法级 (evidence: [T02-S073])。仿真通过率能证明"没退化"，不能证明"足够安全"。
- ❌ **不要把研究基准的 SOTA 当量产可用**。nuScenes 开环端到端可以只靠自车状态刷分 (evidence: [T02-S076])；WOD-E2E 的 RFS 是开环 + 人工偏好口径 (evidence: [T02-S078])。两者都不能外推到闭环行为。
- ❌ **不要把 ROS 1 用在量产车上，也不要以为换成 ROS 2 就解决了实时性**。ROS 2 需要 PREEMPT_RT 之类的手段才能把最坏延迟与抖动压到现代自动驾驶控制器的确定性要求 (evidence: [T02-S012])；Apollo 干脆自建 Cyber RT 的官方理由就是量产鲁棒性与性能 (evidence: [T02-S010])。
- ❌ **不要忽略中间件在大消息上的行为**。Fast DDS 在数据量增大时延迟显著上升（多次序列化）；Cyber RT 走共享内存延迟更稳但多占数十 MB 内存 (evidence: [T02-S012])。**这是一个权衡，不是一个赢家。**
- ❌ **不要把"规则式规划器打败学习式"当成普适结论**。这个结论在换成学习式反应智能体后明显松动：PDM-Closed 在 Test14-Hard 上从 75.19 降到 67.33，而多个学习式规划器保持或改善 (evidence: [T02-S077])。
- ❌ **不要把"接了 ad-rss-lib"读作"满足 RSS"**。初版只实现了论文中规则与计算的一个子集 (evidence: [T02-S065])。
- ❌ **不要把"ISO 26262 认证就绪"读作"已通过认证"**。NVIDIA DriveOS 的公开表述是 certification readiness (evidence: [T02-S019])。这两个词在功能安全语境下的分量差很多。
- ❌ **不要用 TOPS 数字比较平台能力**。厂商给的是峰值且精度口径不同（FP4 TFLOPS 与 INT8 TOPS 不可互换） (evidence: [T02-S020])；实际帧率取决于模型结构、算子支持与内存带宽。
- ❌ **不要按 GitHub star 数选感知框架**。BEVFormer 有 4,588 star 但最近 push 停在 2024-08-15；OpenCalib 有 3,209 star 但停在 2024-06-17（均为 seed 快照 2026-09-02 口径） (evidence: [T02-S029, T02-S032])。**star 记录的是历史影响力，不是当下可用性。**
- ❌ **不要在 CARLA 上选错分支**。UE 4.26 与 UE 5.5 两个版本会长期共存，资产与功能未完全迁移 (evidence: [T02-S050])。
- ❌ **不要再参考"CARLA vs LGSVL"这类对比**。SVL Simulator 已停止维护 (evidence: [T02-S053])，出现这个对比说明材料已过期。
- ❌ **不要把 `rmw_zenoh` 和 `zenoh-plugin-ros2dds` 当成一回事**。两者用法不同且不能互操作 (evidence: [T02-S015])。
- ❌ **不要指望神经渲染仿真解决行为真实性**。3DGS 类方法解决的是外观保真，交通参与者的行为仍需另配模型 (evidence: [T02-S079, T02-S081])。
- ❌ **不要把商业平台的"覆盖度"数字跨厂商比较**。Foretellix 与 Applied Intuition 的覆盖度指标各自定义，且 Foretellix 同时主导相关标准制定（既是加分也是利益冲突） (evidence: [T02-S057, T02-S059])。

---

## 10. 近 12 个月的变化（2025-09 → 2026-09）

1. **零拷贝进入 Autoware 主线**：Agnocast 论文被 ISORC 2025 接收，生产版本并入 Autoware (evidence: [T02-S016, T02-S017])；Core 1.9.0（2026-06-26）大幅扩展 `autoware_agnocast_wrapper`，新增 service/client、Timer API、tf2 API、diagnostic_updater API、ExactTime 同步与 launch 封装 (evidence: [T02-S006])。
2. **Autoware 的 ROS 2 版本迁移进入执行期**：Jazzy Docker Beta 2026-02、全量支持 2026-04、Humble 软冻结 2027-01、Jazzy 独占 2027-05 (evidence: [T02-S006])。**现在起新项目不应再从 Humble 起步。**
3. **闭环评测口径被重新审视**：nuPlan-R（2025-11）用学习式反应智能体重做闭环，量化了 IDM 的被动谦让如何抬高分数——TTC、自车进度、舒适性与有责碰撞退化最明显，社区被推向"退役 IDM 作为默认反应智能体" (evidence: [T02-S077])。
4. **长尾端到端有了官方数据与指标**：WOD-E2E（2025-10 arXiv，CVPR 2026）给出 4,021 段长尾片段与 Rater Feedback Score (evidence: [T02-S078])；Waymo 2025 挑战赛新增基于视觉的端到端赛道 (evidence: [T02-S071])。
5. **神经重建从研究走向平台**：Omniverse NuRec 达到一般可用并与 Isaac Sim / AlpaSim / CARLA 集成，Mcity 用它做测试场数字孪生 (evidence: [T02-S079])；InstantNuRec（2026-07）把重建变成单次前向 (evidence: [T02-S080])。
6. **开放驾驶 VLA 出现**：NVIDIA Alpamayo-1 仓库建于 2025-11-19，Apache-2.0，10B 参数、带因果链推理 (evidence: [T02-S083])。
7. **场景标准的版本在动**：OpenSCENARIO DSL 2.2.0 候选版进入公开评审（2026 年初）(evidence: [T02-S055])；OpenDRIVE 1.9.0 规范正文页标注 2026-05-08 (evidence: [T02-S056])。**任何 2024 年写的"当前版本是 1.8 / 2.1"的材料都需要重新核对。**
8. **部分明星感知仓库进入停更**：BEVFormer（2024-08-15）、OpenCalib（2024-06-17）、OpenPCDet（2025-10-08）最近 push 均已较久（seed 快照 2026-09-02） (evidence: [T02-S029, T02-S032, T02-S027])。这是这一行**从"框架竞赛"转向"各家自建闭源"**的信号之一。

---

## 11. 未覆盖缺口 + Phase 2 接口

### 11.1 未覆盖缺口（诚实边界）

1. **数据闭环的核心环节没有可核实的公开工具栈**：采集触发策略、影子模式回传、难例挖掘、数据版本管理、云端训练评测流水线，头部公司均为自建闭源。本轨只能给到综述层面的方法学 (evidence: [T02-S047])，**给不出"用哪个工具"的答案**。
2. **中国量产侧的工具链证据薄**：地平线、蔚小理、华为等的实际内部工具链缺少可核实的一手英文/中文公开材料；本轨对地平线只能引用其官方产品页与开发者社区（均为厂商宣称） (evidence: [T02-S022, T02-S023])。中文技术内容大量沉淀在被本轨列为黑名单的平台上，这是**信源结构性缺口**，不是搜索不足。
3. **商业仿真器的能力无法独立核实**：IPG CarMaker、dSPACE、Applied Intuition、Foretellix 的所有能力描述都来自厂商自有材料，本轨未找到独立第三方评测 (evidence: [T02-S057, T02-S058, T02-S059, T02-S060, T02-S061])。
4. **STPA 与场景覆盖度分析没有公认工具**；GSN 没有事实标准的开源编辑器 (evidence: [T02-S066])。
5. **未覆盖**：V2X / 车路协同工具链、高精地图生产侧工具（图商内部）、线控底盘与执行器诊断工具、OTA 与车云通信框架、车载信息安全（ISO 21434 落地工具）。这些与本轨主题相邻但不重叠，留给后续轨或 Phase 2 决定是否补。
6. **未做**：本轨没有跑基准复现，所有性能数字都是引用而非实测。**引用的每个数字都带了出处与口径，但没有交叉验证。**

### 11.2 Phase 2 提炼提示

**反复出现（≥ 3 source）的工具选型原则（候选 playbook 规则）**：

1. **"分数的口径比分数本身重要"** — 出现于 nuScenes 自车状态捷径 (evidence: [T02-S076])、nuPlan-R 的 IDM 依赖 (evidence: [T02-S077])、CARLA v2 无官方训练集导致系统级比较 (evidence: [T02-S073])、WOD-E2E 的开环 + 人工偏好口径 (evidence: [T02-S078])。**四个独立来源指向同一件事**，这是本轨最强的共识。
2. **"研究工具与量产工具是两套不通的东西，跨过去要付全额代价"** — 出现于 Apollo 自建 Cyber RT 的理由 (evidence: [T02-S010])、ROS 2 需 PREEMPT_RT 才够确定性 (evidence: [T02-S012])、Vector 工具链在开源视野里完全不可见 (evidence: [T02-S025, T02-S026])、openpilot 不走 ISO 26262 流程 (evidence: [T02-S037])。
3. **"厂商宣称与可核实能力之间要留一条硬边界"** — 出现于 DriveOS 的"认证就绪"措辞 (evidence: [T02-S019])、Apollo 10.0 的十倍性能宣称、地平线的生态伙伴数字 (evidence: [T02-S022])、商业仿真器的覆盖度口径 (evidence: [T02-S059])。
4. **"仓库热度不等于当下可用性，要看最近 push"** — 出现于 BEVFormer / OpenCalib / OpenPCDet 的停更事实 (evidence: [T02-S029, T02-S032, T02-S027])、SVL Simulator 已死 (evidence: [T02-S053])。

**显著的工具流派分裂（候选智识谱系条目）**：

- **中间件流派**：*标准生态派*（ROS 2 + DDS，靠社区与工具链取胜，实时性靠打补丁补）vs *自建确定性派*（Apollo Cyber RT、Agnocast，靠共享内存与自研调度换确定性，代价是生态窄）。证据 (evidence: [T02-S010, T02-S012, T02-S016])。
- **仿真流派**：*物理引擎派*（CARLA、CarMaker，从模型出发生成场景，可控但域差距大）vs *日志重建派*（NuRec、InstantNuRec、HUGSIM，从真实数据出发重建，逼真但行为侧仍需外挂）。证据 (evidence: [T02-S048, T02-S060, T02-S079, T02-S080, T02-S081])。
- **验证流派**：*覆盖度驱动派*（Foretellix、Applied Intuition，借鉴芯片验证，用抽象场景 + 覆盖度指标论证充分性）vs *形式化约束派*（RSS / ad-rss-lib，用可数学检验的规则约束行为）vs *统计里程派*（自报里程与事故率对照人类基准）。**三者互不替代，且各有公开批评**。证据 (evidence: [T02-S057, T02-S059, T02-S065])。
- **感知流派**：*模块化可解释派*（OpenPCDet / mmdetection3d 分任务训练）vs *一体化端到端派*（UniAD / VAD / Alpamayo）。证据 (evidence: [T02-S027, T02-S028, T02-S040, T02-S083])。

**新兴工具信号**：
- 当前活跃 / 上升的新工具数：**8**（见新兴层表）。
- 出现 → 主流的速度估计：**12-24 个月**（锚点：Agnocast 从 ISORC 2025 论文到并入 Autoware 生产版本约 12 个月 (evidence: [T02-S016, T02-S006])；MCAP 从提出到成为 ROS 2 默认 bag 格式约 2 年 (evidence: [T02-S003])）。
- 新兴层里 **5/8 与"用真实数据做仿真/评测"有关**（NuRec、InstantNuRec、HUGSIM、nuPlan-R、WOD-E2E）。这是本轨观察到的最集中的方向性信号。

**跨轨衔接**：
- **→ Track 03（workflows）**：第 8 节的四条分支可直接作为 SOP 分叉；第 7 节每条基准的"正确用法"可直接成为工作流的检查点。
- **→ Track 01（figures）**：本轨点到的维护者/作者候选 — Kashyap Chitta 与 Andreas Geiger（carla_garage / transfuser / NAVSIM / PDM，跨四个工具与基准）、TIER IV 的 Agnocast 作者组、OpenDriveLab（UniAD / DriveLM）。若不在 Track 01 已 retained 列表，建议回走。
- **→ Phase 2.1（心智模型）**：上面四条流派分裂 + 四条选型原则可直接进候选清单。
- **矛盾留给 Phase 1.5 裁决**：① Track 04 把 CARLA 列为闭环评测事实基座，本轨则指出其榜单区分度不足且不外推真车——**两者都对，取决于把它当工具还是当证据**；② 开源栈能否上量产车，openpilot 的存在与 ISO 26262 流程缺失同时成立。

**冷僻 / 信号薄弱自检**：
- 必备层 13 个（≥ 3 ✅）；场景特化 29 个（≥ 5 ✅）；新兴层 8 个（≥ 2 ✅）。
- 必备层的"≥ 80% 采用率"**没有行业 survey 支撑**，是从多来源交叉 + seed star 分布推断的。Phase 2.8 应标注「必备层采用率为推断，非调查数据」。
- **数据闭环维度信号薄弱**（见 11.1 第 1 条），Phase 2.8 需在诚实边界节明说。

---

## 12. 收尾自检

| # | 检查项 | 结果 |
|---|--------|------|
| ① | 无未完成标记词（无「填‑充中」类残留） | 通过（见下方核验命令） |
| ② | manifest 行数 = 正文引用的 source 数 | 通过。84 行 manifest = 84 个唯一 source_id = 84 个在正文被引用（2026-09-06 实跑）|
| ③ | 黑名单域名零命中 | 通过，0 命中（2026-09-06 实跑核验命令）|
| ④ | surrogate 行 note 含白名单关键词 | 通过。23 行 surrogate_primary，note 全部含 `vendor docs` / `协会` / `association` / `own publication` / `自有博客` / `供应商` 之一 |
| ⑤ | 总览处有字面为 `必备 N / 场景特化 N / 新兴 N` 的 sanity 行且数字与实际条目数一致 | `必备 14 / 场景特化 30 / 新兴 8`，与三张总览表行数一致 |

**可复跑的核验命令**（在本文件所在目录执行；黑名单词与占位词用变量拼接，避免命令自身被自己的 grep 命中）：

```bash
BL='zh''ihu|mp\.we''ixin|ba''ike\.ba''idu|cs''dn|cn''blogs|ju''ejin|ji''anshu|we''nku\.ba''idu|develo''per\.ali''yun|busine''sswire|prne''wswire|globen''ewswire|g2\.c''om|cape''rra|gar''tner|forr''ester'
PH='填''充中|T''BD|待''补|占''位符'
grep -nEi "$BL" 02-tools.md   # 期望：无输出
grep -nE  "$PH" 02-tools.md   # 期望：无输出
grep -cE '^\| T02-S[0-9]{3} \|' 02-tools.md                                    # manifest 行数，期望 84
grep -oE 'T02-S[0-9]{3}' 02-tools.md | sort -u | wc -l                         # 唯一 source_id 数，期望 84
grep -vE '^\| T02-S[0-9]{3} \|' 02-tools.md | grep -oE 'T02-S[0-9]{3}' | sort -u | wc -l   # 正文引用数，期望 84
grep -c 'surrogate_primary' 02-tools.md                                        # surrogate 行数
```

**bucket 分布**：verified_primary 54 / surrogate_primary 23 / secondary 6 / reference 1，共 84。一手与替代一手合计 91.7%。

**候选探索规模**：本轨共探索候选工具约 62 个（含 seed 30 个仓库 + 搜索新增），保留 52 个进入三层（必备 14 / 场景特化 30 / 新兴 8），10 个因证据不足、已归档或超出行业边界未保留（如 GAAS、AutonomousDrivingCookbook、YOLOP、Ultra-Fast-Lane-Detection、Det3D、mrpt、3D-PointCloud 等 awesome/教学类与停更仓库；SVL Simulator 单列为"已死"示例）。
