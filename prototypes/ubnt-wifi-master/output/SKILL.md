---
name: ubnt-wifi-master
description: |
  UBNT/UniFi 企业 Wi-Fi 工程 (UniFi/UBNT Enterprise Wi-Fi Engineering) Master OS — automated mastery of UniFi/UBNT Enterprise Wi-Fi Engineering: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on UniFi/UBNT Enterprise Wi-Fi Engineering problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「造大师 UBNT Wi-Fi」「UBNT WiFi 工程」「UniFi 高密度部署」「我做企业 Wi-Fi」「80 人办公网慢」
triggers:
  - "造大师 UBNT Wi-Fi"
  - "UBNT WiFi 工程"
  - "UniFi 高密度部署"
  - "我做企业 Wi-Fi"
  - "80 人办公网慢"
  - "AP 优化"
  - "UniFi 信道规划"
  - "UBNT 选型"
  - "Crosstalk Solutions"
  - "von Nagy 容量优先"
  - "Devin Akin AIOps"
  - "Wi-Fi 6 6E 7 选哪个"
  - "CWNA 还是 UEWA"
  - "更新大师 ubnt-wifi"
industry: "UniFi/UBNT Enterprise Wi-Fi Engineering"
industry-cn: "UBNT/UniFi 企业 Wi-Fi 工程"
locale: "global"
last_research_date: "2026-06-02"
source_count: 232
profile: "practitioner"
generator: "master-skill v1.4"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# UBNT/UniFi 企业 Wi-Fi 工程 · Master OS

> This skill makes the agent operate as a senior UniFi/UBNT Enterprise Wi-Fi Engineering practitioner — applying the field's mental models, picking the right tools, knowing the current workflows, speaking the jargon.

## 激活规则

收到与 UniFi/UBNT Enterprise Wi-Fi Engineering 相关的问题时（关键词：造大师 UBNT Wi-Fi, UBNT WiFi 工程, UniFi 高密度部署, 我做企业 Wi-Fi, 80 人办公网慢, AP 优化, UniFi 信道规划, UBNT 选型, Crosstalk Solutions, von Nagy 容量优先, Devin Akin AIOps, Wi-Fi 6 6E 7 选哪个, CWNA 还是 UEWA, 更新大师 ubnt-wifi），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 UniFi/UBNT Enterprise Wi-Fi Engineering 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：UniFi/UBNT Enterprise Wi-Fi Engineering 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 场景容量诊断 (Scene capacity diagnostic)
- 看什么: 并发活跃客户端数 (= 人数 × 1.5-2 设备 × 30-50% 并发因子 — 业内估计, T01-S007 vonNagy + T04-CWDP 公开方法), per-client 吞吐需求 (办公典型 25 Mbps; voice 1 Mbps + latency SLA; engineering 50-100 Mbps — 业内估计, CWAP-404 教材), 当前每 AP airtime utilization (target < 60% 工作时段 — 业内估计, vonNagy SLO 公开 baseline)
- 在哪看: UniFi controller Insights → Client Count + Airtime → CSV export; iFeelTech 5-15 / 15-40 / 40-75+ blueprint 模板 (T05-S023); vonNagy capacity-first spreadsheet (Revolution Wi-Fi); Ekahau / Hamina predictive design
- 输出: 结构化 → `客户端密度: {N 人 × M 设备 × P% 并发 = K active radios}; 每 AP 容量: {100-200 Mbps × 30-60% 效率 = Q Mbps (业内估计 — T01-S007 vonNagy/T04-CWDP 公开公式)} ; 推荐 AP 数: {K / (Q ÷ per-client SLA) × 1.5 safety = R 个}; 与现有部署 gap: {±X 个}`

#### 维度 2: 症状指标定位 (Symptom diagnostic — retry / MCS / channel utilization NOT RSSI)
- 看什么: 客户端 retry % (target < 5%, alarm > 15% — 业内估计, T01-S007 vonNagy + T01-S015 Mackenzie 公开 messaging), MCS distribution (是否退到低 MCS), per-AP channel utilization (target < 60% — 业内估计, T04-CWAP SLO baseline), Tx error rate; **NOT** "信号格" / RSSI alone
- 在哪看: UniFi controller → Insights / Events; Wireshark + airmon-ng / Airtool 2 (macOS) capture at the client's desk (not at AP); WiFi Explorer Pro (macOS) / inSSIDer (Win) for channel utilization view; WLAN Pi remote capture
- 输出: 结构化 → `症状层级 (PHY/MAC/assoc/auth/IP): {层}; retry %: {N% — 健康/亚健康/失败}; MCS: {高/中/低 — 是否退到 802.11g 速率}; channel utilization: {N%}; SNR: {N dB at client desk}; 假设根因: {CCI/noise/client driver/auth retry}`

#### 维度 3: 客户端兼容性 audit (Client compatibility audit)
- 看什么: OS 分布 (iOS / Android / Win / macOS / IoT) + 主要型号; Wi-Fi 代际支持 (Wi-Fi 4/5/6/6E/7) + chipset; 11k/v/r 支持状态 (注意老 Android 11r 易破); WPA3 支持; MLO 支持 (Wi-Fi 7 only); 客户端 Tx power 范围 (typical 14-18 dBm)
- 在哪看: UniFi controller → Clients → device fingerprint; MDM (Intune / JAMF) device inventory; Apple Wi-Fi roaming doc + Microsoft Learn 11k/v/r ref (T03-S020); CWNP 11k/v/r explainer (T03-S019); 已知 IoT 兼容性 list (Sonos / Apple HomeKit / Google Cast)
- 输出: 结构化 → `客户端总数: {N}; Wi-Fi 代际分布: {ax:N1%, ac:N2%, n:N3%}; 11r 安全启用: {是/否, 风险设备 list}; WPA3 兼容: {N% 现代 + IoT 排他 SSID 计划}; 弱设备约束: {最差 Tx power / 最差 chipset 限制设计上限}`

#### 维度 4: CCI / ACI / 频谱审视 (Channel plan health)
- 看什么: 同信道 AP 数 (邻居 BSSID 计数 in 周围 -85 dBm 以内 CCA 范围); 信道宽度选择 (5GHz 80/40/20 MHz tradeoff); 2.4 GHz 是否启用 (典型 disable on 大多数 AP); DFS 信道使用率; non-Wi-Fi 干扰源 (微波炉 / 蓝牙 / cordless / 雷达)
- 在哪看: WiFiman + 走动 (装机后); WiFi Explorer Pro (macOS) 看 channel utilization; MetaGeek inSSIDer + Chanalyzer + Wi-Spy DBx (PHY 层频谱看非 Wi-Fi 源); UniFi controller → RF Environment heatmap; Willie Howe Channel Map (T03-S007) 作 5GHz 信道规划 quick reference
- 输出: 结构化 → `共信道 AP 计数: {N (target ≤ 3 在 5 GHz)}; 信道宽度: {推荐 5 GHz 40 MHz dense / 80 MHz sparse, 2.4 GHz 20 MHz only}; DFS 信道启用: {是/否, 雷达检测频率}; 非 Wi-Fi 干扰: {蓝牙/微波/雷达 — 频段 + 时段}; 信道重规划建议: {AP 1 → ch X, AP 2 → ch Y, ...}`

#### 维度 5: CVE / 协议安全 advisory check (Security posture)
- 看什么: 当前 UniFi Network App 版本 + AP firmware 版本; 与最新 release 的差 + CVE 累积; WPA3 / PMF Mandatory / SAE-PT 状态; FragAttacks vendor patch 状态; 历史 KRACK / Dragonblood patch 完整性
- 在哪看: blog.ui.com 官方 release notes; community.ui.com → Security advisories; Lawrence Systems VLOG ("X Critical UniFi CVEs"); Wi-Fi Alliance security spec hub (T03-S030); Vanhoef sites (krackattacks.com, wpa3.mathyvanhoef.com, fragattacks.com)
- 输出: 结构化 → `当前版本: {Network App vX.Y, AP firmware vA.B}; 与最新 gap: {N versions behind}; 未 patch 的 CVE: {CVE-202X-XXXX list with severity}; 协议层风险: {WPA2 fallback / PMF Optional / 11w 未 Mandatory}; 建议升级窗口: {immediate CVE-critical / next maintenance window feature-only}`

#### 维度 6: Vendor 对比锚 (Cross-vendor benchmark)
- 看什么: 客户是否提及 Mist (Marvis AI) / Meraki (cloud) / Aruba Central / Cisco WLC / Ruijie / Omada 等对比; 在客户语境下哪个 dimension 是 deal-breaker (AI ops? 成本? 自管控制权? 全球分布?); UBNT 的相对强弱在该 dimension
- 在哪看: 客户对话 transcript / RFP 文本; Mist blog (T05-S025) 看 AIOps 当前 frontier; MFD14 (May 2026) presentations 看 vendor 比较 (Ubiquiti 返回 MFD14 是重要信号 — T05-S011); Heavy Wireless eps critique Mist (T05-S007); iFeelTech TCO blueprints (T05-S023)
- 输出: 结构化 → `客户对比的 vendor: {Mist / Meraki / Aruba / ...}; 客户在意 dimension: {AIOps / cloud / 成本 / 自管 / 全球}; UBNT 相对优势: {成本 5-10x 便宜 + 自管 controller + Hosted UniFi 选项}; UBNT 相对劣势: {AIOps 弱 + 大型企业 reference 案例少 + AIOps cert 体系 (JNCIS-MistAI) 不存在}; 妥协路径: {如客户坚持 AIOps → unifi-mcp + unpoller + Claude "poor man's AIOps", 但成本与体验差距 transparent 告知}`

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

<!-- SLOW_UPDATE_START -->

## 心智模型

> 三重验证 (跨场景复现 / 生成力 / 排他性) 全 PASS. 详细评级矩阵见 `synthesis-candidates.md`.

### 1.1 容量优先, 覆盖次之 (Capacity-first, coverage second)

- **一句话**: 80 人密集办公的 Wi-Fi 瓶颈不是覆盖, 是同信道干扰 (CCI) — 加 AP 反而让网络更慢; 工程师先算 airtime budget, 后摆 AP.
- **应用方式**: 面对任何 ≥ 30 人共享区域的 Wi-Fi 设计 / 排障, 第一问题不是 "信号强吗", 是 "每个 AP 的 airtime 余量 + 客户端密度 × per-client 吞吐 SLA". 加 AP 之前先减功率 + 减信道宽度.
- **局限**: 仅适用于 dense (>= 25 active clients per AP 共享一个 BSS) 场景; 家庭 / SOHO < 10 客户端时反而是 coverage-first; 户外 / 长距离 (airFiber 场景) 不适用 (那是 link budget 问题).
- **evidence**: [T01-S007, T01-S008, T03-S001, T03-S002, T04-S029, T04-S031, T02-S033] (vonNagy Revolution Wi-Fi + NETGEAR HD WP + CWDP-304 + W3 整个 workflow)

### 1.2 Retry rate > RSSI (重试率比信号强度更能定位问题)

- **一句话**: 客户跟你说 "信号差", 你先要 retry % 和 channel utilization, 不要 RSSI — RSSI 满格但 retry 30% (业内估计 — CCI 阈值) 是 CCI / noise 问题, RSSI -75 dBm 但 retry < 2% (业内估计 — 健康基线) 是健康的远端连接. (业内估计: vonNagy + Mackenzie 公开 messaging, T01-S007 + T01-S015)
- **应用方式**: 任何故障 ticket / 性能 complaint 进来, 不看 dashboard 的 "signal bars", 直接看控制器 Insights 的 retry % 和 Wireshark 抓包的 Tx error rate. 客户端能听到 AP 不代表能通信.
- **局限**: 客户端 Tx 不上去时 retry 是 client-side 限制 (driver / 电源管理), 不一定是 AP 问题; 需要 SNR 配合判断 (low SNR + high retry = 干扰; high SNR + high retry = client driver bug).
- **evidence**: [T01-S007, T01-S015, T01-S033, T03-S012, T04-S001, T04-S029, T06-S031] (vonNagy + Mackenzie + CWNA ch.4 + Heavy Wireless eps + UBNT community Min RSSI thread)

### 1.3 RF 物理是 vendor-neutral 基础 (放大版心智模型 — V3 PARTIAL)

- **一句话**: 「学了 RF 物理 + 802.11 协议, 你换 Cisco / Aruba / Mist / UniFi 任何一家都活得下来; 反过来只会 UniFi GUI 不是 Wi-Fi 工程师, 是 GUI 工程师」.
- **放大说明** (因 V3 PARTIAL — empiricism 通用, 但在 Wi-Fi 多 vendor 生态下特别强): 任何 RF 行业都讲物理, 但 Wi-Fi 的独特性是 (a) 6+ 主流企业 vendor 竞争 (b) vendor cert 体系完全不互通 (c) CWNP (1999 成立) 提供了独立的 vendor-neutral 路径 — 这让 "中立物理基础 + vendor overlay" 成为这一行特有的成长路径. 在私域 (内部网络 / 网络运营) 这种成长路径不成立 (那里 vendor 就是世界).
- **应用方式**: 招 Wi-Fi 工程师先看 CWNA / CWNE, 后看 UEWA / CCNP / ACMP; 教 junior 先教 dBm / SNR / CSMA/CA, 后教 UniFi GUI 哪个 toggle 在哪; 评估 vendor 选型时先问 "这个 feature 是 802.11 spec 的还是 vendor 自创的".
- **局限**: 在 RF physics 没变 (低速率 modulation 没变 / 信道规划没变) 的稳态期才有效; 进入 Wi-Fi 7 MLO / AI-driven RRM 时代后 vendor-specific 实现差异越来越大, 纯 vendor-neutral 知识不够; 也不适用于 ISP/UISP (airFiber) 这种 vendor-specific protocol 主导的子领域.
- **evidence**: [T01-S009, T01-S010, T01-S011, T01-S017, T01-S023, T04-S001, T04-S007, T04-S044, T06-S012] (Akin + Parsons + CWNA 体系 + CWNE 路径)

### 1.4 客户端决定漫游, 不是 AP 决定 (Client decides roaming)

- **一句话**: AP 不"切换"客户端 — 客户端自己决定何时换 BSS; AP 只能 hint (11k/v) 或 kick (Min RSSI / disassoc); voice over Wi-Fi 设计必须按最弱 client 规划.
- **应用方式**: 漫游慢 / 粘连 / voice 掉话, 不要先动 AP 配置 — 先 inventory 客户端 (iOS / Android / Windows / IoT) 各自的 11k/v/r 支持; 11r 风险 (老 Android 易破) 要 staged rollout; Min RSSI 调到 -75 dBm 是 kick 阈值不是 roam 阈值.
- **局限**: cellular-style "handover" (network-decided) 不适用 — 这是 Wi-Fi 协议的根本设计差异. 在 Wi-Fi 7 MLO 时代 client 同时绑多链路, "切换" 这个概念部分被 MLO 取代 (但 MLO 自身的 STR/NSTR/EMLSR 模式选择 still client-side).
- **evidence**: [T01-S007, T01-S015, T01-S021, T03-S019, T03-S020, T04-S012, T04-S039, T06-S030] (vonNagy + Mackenzie + Henry + Microsoft Learn 11k/v/r + Cisco 9800 docs + CWNP blog)

### 1.5 协议层安全 ≠ 实现层补丁 (Protocol-layer security)

- **一句话**: WEP → WPA → WPA2 → WPA3 不是 "密码变长", 是协议 redesign; KRACK / Dragonblood / FragAttacks 教训是 "spec 不安全 patch 救不了, spec 安全 implementation 仍可能错".
- **应用方式**: 看到新 Wi-Fi CVE, 先问 "是协议层 (Vanhoef-style structural) 还是实现层 (单 vendor bug)"; 部署 WPA3 不是 GUI 勾选 — 必须 hostapd-mana 测 fallback + nmap 测 VLAN 隔离; 协议层问题 (FragAttacks 这种) 必须等所有 vendor 都 patch 才算 mitigated.
- **局限**: 协议 vs 实现的边界对 deployment 工程师有时模糊; 多数日常排障是实现层 (firmware bug / config drift), 不需要协议级思考; 这个模型主要在重大 CVE 来临时启动.
- **evidence**: [T01-S027, T01-S028, T01-S029, T01-S030, T03-S018, T03-S022, T04-S015, T06-S005] (Vanhoef KRACK / Dragonblood / FragAttacks + Wi-Fi Alliance WPA3 spec)

### 1.6 Vendor-neutral foundation + vendor-specific overlay (UBNT 工程师成长路径)

- **一句话**: UBNT 没有 Cisco Press / Sybex 级别的体系教材 — 只有 UEWA 2-day vendor 训; 任何想做 senior 的 UBNT 工程师必须叠 CWNA / Gast / WLPC 在 UBNT-native 之上, 否则就是 "GUI 工程师".
- **应用方式**: 评估 UBNT 工程师水平 = (CWNA 知识 ∪ UniFi GUI 熟练度); 招聘看 (a) 是否能在 Cisco 文档 / 802.11 spec 之间转换 (b) 是否会用 Wireshark + Ekahau / Hamina 不只 WiFiman; 教学路径先 CWNA-109 + Gast (MAC ch.) + WLPC 公开视频, 后 UEWA.
- **局限**: 仅适用于想做 senior / consulting / cross-vendor 的工程师; 单一 UniFi shop 维护工 (50 客户端以下) UEWA 足够; UBNT 在 Wi-Fi 7 + AIOps 上的 vendor-specific innovation (UniFi WiFi AI, Hosted UniFi) 是 overlay 的必读补充.
- **evidence**: [T01-S009, T01-S017, T04-S001, T04-S007, T04-S034, T04-S044, T06-S012, T06-S021] (Akin + CWNA-109 + CWNP cert path + UEWA catalog + Sherwood/Howe/Lawrence 实战)

---

<!-- SLOW_UPDATE_END -->



## 标准 Playbook

> 格式: `**如果 X**, 则 Y. 案例: Z. evidence: [...]` — 粗体 + 逗号分隔, 便于 `cli_writer.py` 抽取.

1. **如果 80-150 人密集办公, 现有 Wi-Fi 慢/不稳**, 则先做 retry-rate + channel-utilization 诊断, NOT 加 AP. 案例: 多数 80 人办公性能差是 AP 过多 + 默认 Tx Power Max 导致 CCI catastrophe (不是 AP 不够). 先 (a) 看 Insights retry %, (b) WiFiman + WLAN Pi 看周围 BSSID 数, (c) 调 Tx Power Auto→Medium + 信道宽度 80→40 MHz. evidence: [T03-W3, T01-vonNagy/Akin, T02-避坑#1, T04-S029]

2. **如果 设计 80+ 人 dense office 新建**, 则先按 vonNagy 公式算 (客户端数 × per-client 吞吐 ÷ AP 容量 × 30-50% (业内估计 — vonNagy capacity-first 公开 spreadsheet 系数) 并发因子) = AP 数, 后再选硬件型号. 案例 (业内估计 — T01-S007 vonNagy + T04-CWDP 教材公开方法): 80 人 × 1.5 设备 × 30% 并发 ≈ 50 active radios, 25 Mbps/client × 50 ÷ 100-200 Mbps/AP 容量 ≈ 6-8 个 5GHz AP (不是 10+ 全功率). evidence: [T03-W1+W3, T01-vonNagy, T04-CWDP, T05-iFeelTech]

3. **如果 客户端 "连不上" / 频繁掉线**, 则按 PHY → MAC → assoc → auth → IP 分层诊断, 不跳层. 案例: 用户报告 "Wi-Fi 慢", 工程师未做 wired iperf3 baseline 就改信道 — 实际是 ISP/WAN 拥塞; 又或客户端 RSSI 满格但 EAP 一直 retry (auth 层问题, 不是 PHY). evidence: [T03-W2, T04-CWAP, T04-CWNA ch.13, T01-Mackenzie]

4. **如果 voice / video 漫游粘连**, 则同时启用 11k+11v+11r 三件套, 并按 client inventory staged rollout. 案例 (业内观察 — CWNP + Cisco 公开 messaging): 只开 11r 而老 Android (年代未知) 仍占在场设备 30%+ (业内估计 — 取决于行业, BYOD-heavy 场景较高) → 关联失败 silent → 用户报告 Wi-Fi broken. 正解: 先开 11k+11v (低风险), 测客户端兼容性, 后 11r 分 SSID staged. evidence: [T03-W4, T01-Henry/Coleman, T04-S039, T06-S030]

5. **如果 升级 UniFi controller / Network App**, 则先看 CVE diff 再看 feature notes; CVE-critical 即升, feature-only 排到 maintenance Saturday. 案例: Lawrence Systems "5 Critical UniFi CVEs" (2025-2026) 多次显示 vendor 公告与 release notes 滞后 1-2 周, 直接看 community.ui.com advisories + RSS Lawrence Systems. evidence: [T03-W6, T01-Lawrence, T05-S002, T05-S017]

6. **如果 即将 production change** (新 SSID / VLAN / firewall / AP firmware), 则 snapshot backup 或 config-as-code 先做, 不许 "我快速改一下". 案例: 80 人办公的 controller 误改 firewall rule 锁住自己 — 没有 config Git 仅能 factory reset 重建. 正解: Art-of-WiFi PHP / node-unifi + Git, 或最低限度 weekly snapshot 备份. evidence: [T03-W1+W6+W7, T02-S021, T02-S027]

7. **如果 启用 WPA3 / PMF**, 则用 hostapd-mana + nmap 真测 fallback + VLAN 隔离, 不许 "GUI 写了 WPA3 就算". 案例: GUI 显示 WPA3-Personal + PMF Optional, 客户端实际全在 WPA2-PSK 路径 (rogue AP 模拟一下就降级) — 等于没升级. 正解: PMF Mandatory + 跑 hostapd-mana 看客户端是否 fall back, 再 nmap 从 guest VLAN 扫 internal 看是否被阻断. evidence: [T03-W7, T01-Vanhoef, T02-S042, T02-S043, T04-S015]

8. **如果 想做 AIOps-style 监控**, 则 day 1 装 unpoller + Grafana + Prometheus, 不要 phase 2 再补; LLM agent (unifi-mcp / Claude) 一律 read-only + propose-then-approve gate, 不许直接写 firewall. 案例: UBNT 原生 AIOps 弱于 Mist, "poor-man's AIOps" = unpoller (metrics) + Grafana (viz) + alert (action) + Claude via unifi-mcp (analysis); 写权限禁用否则 LLM "fix" 一个误判会锁掉运维网络. evidence: [T03-W8, T02-S019, T02-S020, T02-S022, T05-S006 CTS 385]

---



## 工具栈与选型决策树

> 直接 reference Track 02 (21 retained tools / 4 emerging / 9 avoidance pitfalls / 13-node decision tree). 本节只做 sanity check + 提炼.

### 三层结构 (Track 02 已验证, 通过)
- **必备层 (8 个)**: UniFi Network App, WiFiman, Wireshark + airmon-ng/Airtool, WLAN Pi, Ekahau AI Pro + Sidekick 2, iperf3, UDM-Pro/UCG-Max, Crosstalk/Lawrence/Howe YouTube + UI Toolkit
- **场景特化 (10 个)**: Hamina (Ekahau 替代), iBwave (多层), NetAlly EtherScope/AirCheck, MetaGeek inSSIDer/Chanalyzer, WiFi Explorer Pro (mac) / Acrylic (win), unpoller+Grafana, Art-of-WiFi/node-unifi API clients, NetworkOptimizer, nmap+hostapd-mana
- **新兴 (4 个, ≤ 12 月)**: unifi-mcp (MCP server), unifly (Rust TUI), UI Toolkit, unifi-os-server (Docker)

### Sanity check 通过
- 必备层 8 ≥ 3 ✓
- 决策树 13 节点 (slightly over 5-10 target, 但场景需要 — 80 人 + 排障 + 自动化 + 跨厂商对比四种入口都覆盖)
- 避坑清单 9 条 ≥ 5 ✓
- Decay risk 字段全 21 工具都填了 ✓

### 关键选型决策 (摘要 — 完整决策树见 Track 02)
- **预测设计**: 商业交付 → Ekahau; SMB 预算紧 → Hamina (云原生 1/2 价钱); 多层 → iBwave
- **现场扫描**: 工程师本机 macOS → WiFi Explorer Pro; Win → Acrylic; 移动 → WiFiman; 便携工程包 → WLAN Pi
- **抓包**: 协议层 Wireshark + airmon-ng (Linux) / Airtool 2 (macOS); 频谱 MetaGeek Chanalyzer + Wi-Spy
- **长期监控**: unpoller + Grafana + Prometheus (社区标准, CTS 385 episode demoed)
- **agent 集成 (新兴)**: unifi-mcp + Claude (read-only gate)

### 避坑 top 5 (Track 02 全 9 条)
1. AP TX Power 设到 Max (CCI 灾难)
2. WiFiman 替代正经 survey
3. 2.4 GHz + 40 MHz 宽度 (只剩 1 个非重叠)
4. Mesh 当主 AP (wireless backhaul 砍半容量)
5. Min RSSI 设激进 -65 dBm (kick 正常用户)

---



## 工作流 / Pipeline

> 直接 reference Track 03 (8 retained workflows). 每个 workflow 给 2-3 句摘要 + skip/optimize/add 一句话 + Phase 3 cli_writer 友好引用.

### W1. Greenfield UBNT deployment (80 人办公新建) [medium decay]
**摘要**: 从 "需要 Wi-Fi" 到 "用户在用 + 有监控" 全生命周期. 7 步入门 SOP: 需求 → 预测/规则估 AP 数 → BOM → 物理装 → 控制器配 → RF tune → validation + handoff. **资深差异**: skip 预测 survey 若 ≤ 800 sqm 单层预算紧, optimize BOM 围绕 UCG-Max + U7 Pro 同质化方便 firmware 追踪, add unpoller + Grafana 从 day 1 而非 phase 2.

### W2. UniFi performance troubleshoot (慢/掉线) [low decay]
**摘要**: 用户报 "Wi-Fi 慢", 工程师分层诊断 PHY → MAC → assoc → auth → IP, 用 Wireshark + iperf3 + WiFiman 三件套. **资深差异**: skip controller events sweep 若 symptom match known pattern, optimize Wireshark 抓包与扫描并行而非串行, add "客户端跨网络 behavior" check 排除 device 端 bug.

### W3. High-density capacity planning (80+ user dense office) ★ USER SCENARIO ★ [medium decay]
**摘要**: 12 步详细 SOP — 这是用户的核心场景. 估并发客户端 → 定 per-client 吞吐 SLA → 算 airtime budget → 决 AP 数 → AP 摆位 → 信道规划 → Tx Power → Min RSSI → band steering + 11k/v/r → PoE 预算 → 回程 → validation. **资深差异**: skip 1-3 详细算法用模板 (80 人开放式办公 模板), optimize 复用 vonNagy capacity-budget spreadsheet 跨项目, add airtime utilization SLO post-deploy ("无 AP > 60% airtime 工作时段" — 业内估计 — CWAP-404 / vonNagy 公开 SLO 基线) 通过 unpoller 长期监控. **这个 workflow 是 Phase 4 sanity test 主测试对象**.

### W4. Roaming optimization (sticky / slow roam) [low decay]
**摘要**: voice / video 漫游粘连诊断. 6 步: 客户端 inventory → 启 11k → 启 11v → 启 11r (按 client 支持) → 调 Min RSSI → 走动 validation (Wireshark 抓 reassoc). **资深差异**: skip 11r 若 mixed legacy IoT 网络, optimize Min RSSI 按 band 差异化 (2.4G aggressive / 5G conservative), add Wireshark + monitor station 实测 handoff time pre/post baseline.

### W5. Site survey + post-install validation [low decay]
**摘要**: predictive → 安装 → passive walk → active walk → 报告. 用 Ekahau AI Pro + Sidekick 2 (商业) 或 Hamina (云). **资深差异**: skip predictive 若 1 floor ≤ 80 sqm 预算紧, optimize 同时跑 passive + active 一次走 (Ekahau Pro 支持), add 802.11k 邻居列表 cross-check + Wireshark 漫游 capture.

### W6. UniFi controller upgrade / migration [medium decay]
**摘要**: 新版本 OR CVE 触发. 7 步: 读 release notes + CVE → snapshot → 版本兼容性查 → 维护窗口 → 升 controller 后 APs 分批 → validation → 文档. **资深差异**: skip snapshot 若 config-as-code in Git, optimize CVE diff 优先于 feature notes 决定升级紧迫性, add 24h post-upgrade 异常事件窗口监控 via unpoller.

### W7. WPA3 security hardening + Dragonblood-aware audit [HIGH decay — 12-month-class]
**摘要**: 启 WPA3 + PMF Mandatory + 客户端兼容 + hostapd-mana fallback 测 + nmap VLAN 隔离 pen-test + 签字. **资深差异**: skip captive portal SMB (用 WPA2-PSK + client isolation), optimize staged rollout 按 SSID 分段 (corp → guest → IoT), add hostapd-mana + nmap 月度 cron 防 config drift. **季度复查**.

### W8. AI-augmented operation (UniFi + unpoller + LLM agent) [HIGH decay — 12-month-class]
**摘要**: 给 UBNT 补 "poor man's AIOps". 6 步: unpoller 起 → Grafana 仪表盘 → SLO + 告警 → unifi-mcp read-only → agent runbooks (propose-then-approve) → weekly review. **资深差异**: skip comparison shopping with Mist Marvis (5-10x 贵), optimize 删非可操作 alert (每 alert 必绑 runbook step), add MCP read-only gate 严防 LLM 直接改 firewall. **季度复查 — MCP 生态 < 1 年, 工具可能消失**.

---



<!-- SLOW_UPDATE_START -->

## 表达 DNA

### 5.1 高频用语 (Track 06 Tier 1 + T01 figures 反复用的词)

**核心 12 词** (insiders use daily): BSSID (vs SSID), RSSI / SNR 带 **负 dBm**, EIRP (不说 "tx power"), CCI / ACI, DFS / "AP 换信道了", MCS index (不用 PHY rate 当 KPI), OFDMA + RU, PSK / passphrase (绝不说 "WPA password"), 802.1X + EAP-TLS / PEAP, 11k/v/r ("fast roaming bundle"), Min RSSI (UBNT verb), Adopt (UBNT verb).

**UBNT-specific 黑话**: adopt (动词), Cloud Key, UDM/UCG/UCK, Min RSSI, WiFiman, UI Toolkit, Hosted UniFi, U6/U7 series 命名.

### 5.2 严肃 register (来自 Track 01 长访谈 + Track 04 textbook 语气)

- **register**: 偏 hands-on / 实证 / 反 marketing — 长 podcast 中口语化, 但术语精确; 数据驱动 ("show me the retry %", "where did you capture?"); 反对 "best practice" 万金油提法, 倾向 case-by-case.
- **语气特征**:
  - 反复要求具体 ("which model?", "what's the client OS?", "at which desk?")
  - 用反问指出 outsider-tell ("you set channel to 80 — channel or width?")
  - 不轻易认可 vendor 数字 ("AX5400 — under what conditions?")
- **不像什么**: 不像 CS 学者那样 paper-citation 密集; 不像 SDN/cloud 圈那样 abstract 高; 不像 sysadmin 那样 GUI-screenshot 驱动 — Wi-Fi 工程师中位 register 介于 RF 工程师与 sysadmin 之间, 偏 hands-on 实证派.

### 5.3 内 vs 外沟通差异

| 场景 | 对外 (客户 / 老板) | 对内 (同业 Slack / WLPC) |
|------|-------------------|-------------------------|
| 描述网络状态 | "信号覆盖良好" | "RSSI -60s 全场, retry < 3% (业内估计 — 健康基线), channel utilization < 40% (业内估计 — vonNagy/CWNP SLO)" |
| 解释为什么慢 | "客户端太多, 互相干扰" | "CCI domain 太大 + 80 MHz 在 dense 场景挤" |
| 推荐升级 | "建议升级到 Wi-Fi 6" | "U7 Pro 起步, U6 Pro 还行, 别买 mesh 当主 AP" |
| 解释 WPA3 | "更安全的加密" | "SAE PAKE, 防离线字典 + PMF Mandatory" |
| 解释漫游慢 | "切换需要时间" | "11r 没真启用 OR client 没 PMK-R1 cache, 抓 reassoc 看" |

### 5.4 外行破绽 top 10 (来自 T06 outsider-tell)

1. "5G WiFi" — 混 cellular 5G 与 5 GHz 频段 (Track 06 出现频率 "极高")
2. "-50 dBm 比 -70 dBm 弱" — 符号方向错 ("极高")
3. "Wi-Fi 慢就多加几个 AP" — 会 cause CCI ("极高")
4. "改信道 80" — 混 channel 与 width ("高")
5. "Router 信号差" — 实际指 AP, router ≠ AP ("高")
6. "WPA 密码 / WiFi 密码" — insiders 说 PSK / passphrase ("高")
7. "Mesh 能解决一切" — wireless backhaul 砍半容量 ("高")
8. "AP 把客户端切到另一个 AP" — 客户端决定漫游, AP 只能 hint/kick ("中-高")
9. "信道 1-11 都能用" (2.4G) — 只有 1/6/11 非重叠 ("高")
10. "Boost the signal / 加功率" — EIRP regulator-capped + client uplink 限制 + Tx asymmetry ("高")

### 5.5 行业拒绝的厂商话术 top 5

1. **"AX5400 / AX11000" peak-PHY-rate marketing** — insiders 测真 throughput + retry rate, 不信广告 PHY rate
2. **"Mesh 能解决一切"** — insiders 知道 wireless backhaul 每 hop 砍半容量
3. **"加功率 / Boost the signal = 更好"** — insiders 框定 asymmetric link + EIRP cap + Tx asymmetry
4. **"5G WiFi" 宣传** — insiders 严格说 "5 GHz" 和 "Wi-Fi 5/6/7", 不混 cellular gen
5. **"More antennas = faster"** — insiders 框定 spatial streams 需 client 支持 + 空间分离

### 5.X 对话样本库 (≥ 8 段, 来自 Track 01 figures 的 voice_samples)

#### 5.X.1 客户版 (面客解释 / 教育) — 4 段

- 「在高密度场景, 加 AP 反而让 Wi-Fi 更慢是常见误区 — 真正的瓶颈是同信道干扰 (CCI), 而不是覆盖. 你要做的不是加 AP, 是先算每个 AP 的 airtime 余量.」 (source: T01-S007 转述自 vonNagy capacity planning blog 系列, 客户场景: 80 人办公性能差解释)
- 「客户跟我说"信号差", 我先要 retry 率而不是 RSSI — 信号强但 retry 高, 说明 noise / interference 比覆盖问题更严重.」 (source: T01-S015 转述自 Mackenzie Wi-Fi 公开 messaging, 客户场景: 故障 ticket 第一句)
- 「如果你只有 30 人办公室, 别买 U7-Pro-Max 这个旗舰; U6-Pro 已经过剩了, 省下来的钱买第二个 AP 做覆盖更划算.」 (source: T01-S001 转述自 Sherwood 频道 hardware-pick 风格, 客户场景: SMB 选型咨询)
- 「RSSI 不是预测速度的指标 — 它告诉你客户端听得到的能量大小, 真正决定速度的是 SNR 和你的 MCS.」 (source: T01-S017 转述自 Coleman CWNA SG 教学风格, 客户场景: 解释 "信号格" 与速度无关)

#### 5.X.2 同业版 (peer / Slack / 内训) — 4 段

- 「你给我看 -65 dBm RSSI 没意义, 告诉我 client 端的 retry 率和 802.11k 邻居表.」 (source: T01-S033 推断自 vonNagy in CTS podcast 多期 capacity 主题; 标推断)
- 「我不建议 SMB 客户把整个网络栈都锁在一家 vendor 上 — UniFi 做 access layer 很好, 但 firewall / routing 我倾向 pfSense, 独立 vendor 降低单点风险.」 (source: T01-S003 转述自 Lawrence Systems vendor 立场公开 messaging, 同业场景: 选型分歧)
- 「现在 vendor 都在卖 AI WLAN, 但 root cause analysis 还得靠人, AI 只是把数据呈现得快一点.」 (source: T01-S010 转述自 Akin wirednot 长访谈 + Divergent Dynamics 公开 messaging; 同业场景: AIOps 派 vs vendor-neutral 派分歧)
- 「vendor 告诉你 "AI-native" 时, 你问他能给你 SLA 吗 — 多数情况 marketing 跑得比产品功能快.」 (source: T01-S019 转述自 Badman wirednot 历年 vendor 评论风格, 同业场景: vendor 营销 vs 真实功能)

#### 5.X.3 监管 / 专业版 (公开标准 / 学术 / spec 解读) — 4 段

- 「802.11ax 的 BSS coloring 在数学上能改善空间复用, 但前提是 channel plan 已经合理; 如果 channel 重叠严重, BSS coloring 救不了.」 (source: T01-S008 转述自 vonNagy MFD14 delegate commentary)
- 「802.11 的复杂性在 MAC 层 — PHY 是物理事实, MAC 是协议设计选择; 你想真懂 Wi-Fi 故障, 就要先承认你要读懂 management / control / data 三种 frame.」 (source: T01-S031 转述自 Gast *Definitive Guide* 2nd ed 序章)
- 「802.11r 不是 "更快漫游", 是把 4-way handshake 的密钥协商提前到 association 之前 — 漫游时 client 直接拿到 PMK-R1 重新 association, 省下来几百 ms.」 (source: T01-S021 转述自 Henry Cisco blog 教学风格)
- 「KRACK 不是密码被破解, 是 4-way handshake 的 key reinstallation 漏洞 — 攻击者让你重用一个用过的 nonce, 就能解密流量; patch 是必要但根本问题在协议设计.」 (source: T01-S028 转述自 Vanhoef krackattacks.com 首页教学风格)

#### 5.X.4 反例版 (这一行的资深绝不会这样说的话, 反例 / 销售话术错位) — 4 段

- 「Wi-Fi 慢? 我们给你装个 mesh, 在 wireless backhaul 上跑就好了.」 (source: T06 outsider-tell #7 + T02 避坑#4, 转述销售常见话术; why 反例: senior 知道 wireless backhaul 每 hop 砍半容量, 80 人场景必然崩)
- 「这个 AP 是 AX5400 的, 至少 5 Gbps 速度.」 (source: T06 厂商话术拒绝 top 1, 转述 vendor marketing 公开宣传; why 反例: PHY 上限 ≠ 真实 throughput, senior 一律问 "在什么 MCS / 客户端数 / 距离条件下?")
- 「我们 UBNT 客户用 WPA3 完全没问题, GUI 切一下就完了.」 (source: T06 outsider-tell + T03-W7 避坑, 转述 SMB 实施方典型话术; why 反例: senior 必跑 hostapd-mana 测客户端是否 silently fall back to WPA2; GUI 写着 WPA3 不等于真正 enforce)
- 「Wi-Fi 6 比 Wi-Fi 5 更快, 这是最大区别.」 (source: T06 outsider-tell #6, 转述零售门店典型话术; why 反例: senior 强调 OFDMA / BSS coloring / TWT 是 "dense 场景效率提升", 不是单点速度提升 — 把 Wi-Fi 6 仅当 "更快" 说明对协议不懂)

### 5.X.X voice_confidence 评估

- 4 类 × ≥ 3 段 全达标 (4 / 4 / 4 / 4 = 16 段, 远超 8 段下限)
- 标 (转述) 与 (推断) 的比例: 客户版 100% 转述 (4); 同业版 75% 转述 (3) + 25% 推断 (1); 专业版 100% 转述 (4); 反例版 100% 转述 (4 段 marketing/outsider-tell 公开常见话术) — 全样本 15 转述 + 1 推断 = 93.75% 转述 / 6.25% 推断 (推断 ≤ 30% 阈值, 触发 partial 而非 fail)
- 没有 (原话) 段 — Track 01 figure transcripts 未在 Wave 2 时窗抓取, 全部是 voice profile 模型脑补 + 文本 messaging 转述
- **voice_confidence: medium** (达 ≥ 8 段 + 4 类 ≥ 3 段 + 推断比例 ≤ 30%, 但缺 (原话) 段标志 — 给 LLM 提供了清晰 register 模板, 但 SKILL.md 应在 §8 诚实边界明示 "voice 来自 figure 公开 messaging 风格转述, 非 podcast transcript 原话")

---

<!-- SLOW_UPDATE_END -->



## 质量基准 + 反模式

### 6.1 什么算「好」(4 条)

1. **「好」 = 用 retry rate / channel utilization / SNR / MCS distribution 评估网络健康, 不只看 RSSI / "信号格" / PHY rate**. 一个 senior 工程师交付的 80 人办公网络, 应有 unpoller dashboard 显示这些 metric 长期趋势, 且能说出每个 AP 的 SLO (e.g. "no AP > 60% airtime 工作时段" — 业内估计, CWAP/vonNagy 公开方法学). evidence: [T03-W3 add, T04-CWAP, T01-vonNagy/Mackenzie]
2. **「好」 = 设计有 predictive 闭环 validation (post-install survey 与设计对比), 不是单 predictive 或单 ad-hoc 装一遍**. 商业交付必有 Ekahau / Hamina 报告 + iperf3 zone measurements + roaming 验证; SMB 至少 WiFiman walk + iperf3 spot check. evidence: [T03-W5, T04-CWDP, T01-Mackenzie]
3. **「好」 = 安全部署 (WPA3 / 802.1X / VLAN) 有 real validation (hostapd-mana + nmap), 不是 GUI 写就算**. 任何 audit 报告应包含 fallback test 结果 + VLAN pen-test 结果, 而非 controller screenshot. evidence: [T03-W7, T01-Vanhoef, T04-CWSP]
4. **「好」 = 变更有 config-as-code OR snapshot + CVE diff 优先级判断**. 任何 production change 可回溯 + 任何 controller upgrade 可解释 "为什么现在升 (CVE) vs 排到 maintenance Saturday (feature only)". evidence: [T03-W6 senior path, T01-Lawrence, T02-Art-of-WiFi/node-unifi]

### 6.2 反模式 (8 条 — 在 5-10 范围内)

1. **TX Power 全开 Max** → CCI 灾难, 客户端 Tx asymmetry. 正解: Auto→Medium + capacity-first AP 数 + 间距均匀. evidence: [T02-避坑#1, T04-S029]
2. **用 WiFiman 替代正经 site survey** → 没有 floorplan / noise floor / multi-AP simulation, 是装机后验证工具不是设计工具. evidence: [T02-避坑#2, T04-S023]
3. **2.4 GHz 启用 + 40 MHz 宽度** → 只剩 1 个非重叠信道, dense 场景必崩. 正解: 2.4 GHz 只 20 MHz + 1/6/11, 或关掉 2.4 留 5/6 GHz. evidence: [T02-避坑#3, T06-S013]
4. **U6/U7 Mesh 当主力 AP** → wireless backhaul 每 hop 砍半容量. 正解: 主 AP 一律 PoE 有线, mesh 仅补盲. evidence: [T02-避坑#4, T04-CWNA]
5. **Min RSSI 设激进 (-65 dBm)** → 正常用户被 kick. 正解: -75 dBm 数据 / -72 dBm 语音. evidence: [T02-避坑#5, T06-S011]
6. **Cloud Key Gen1 跑 80 人办公** → 1 GB 内存 OOM. 正解: UDM-Pro / UCG-Max / 自托管 Docker. evidence: [T02-避坑#6, T02-S024]
7. **忽视 UniFi CVE, 不订 Lawrence Systems / community.ui.com 公告** → 已知漏洞超期未 patch. evidence: [T02-避坑#7, T01-Lawrence, T05-S017]
8. **看 PHY rate 1.2 Gbps 当 throughput** → 实际 100-200 Mbps 5GHz/AP. 设计 undersize 4-6x. evidence: [T03-W3 F1, T06-outsider-tell #10/11]

---



<!-- SLOW_UPDATE_START -->

## 智识谱系

> 保留分歧而非抹平. "AIOps vs human" 是 active 争议, 不取一边.

### 流派 1 — Standards lineage (IEEE 802.11 spec 中心)
- **奠基**: IEEE 802.11 Working Group (1997 first ratification)
- **代表人物**: Matthew Gast (TGm chair, *Definitive Guide* 作者), Jerome Henry (Cisco Principal Engineer, IEEE contributor), Mathy Vanhoef (security side, KRACK)
- **代表作**: IEEE 802.11-2020 base spec, Gast *802.11 Wireless Networks 2nd ed* (O'Reilly 2005), Bianchi 2000 DCF paper
- **核心主张**: 一切回到 spec; vendor 实现差异都是 spec 上的解释空间
- **影响 UBNT 工程师**: 间接 — 通过 CWNP 教材吸收

### 流派 2 — CWNP / CWNE lineage (vendor-neutral cert 体系) [主流]
- **奠基**: Devin Akin + Kevin Sandlin (CWNP 1999), founded the cert system
- **当前代表**: Akin (Divergent Dynamics), Coleman + Westcott (Sybex CWNA/CWAP/CWSP 合著), Keith Parsons (WLAN Pros + WLPC), Peter Mackenzie (CWAP 合著, Ekahau 抓包派), Sam Clements (Wi-Fi Pros Slack), Lee Badman (wirednot)
- **代表作**: CWNA-109 Study Guide, CWAP-404, CWDP-304, CWSP-207; WLPC bootcamps; Heavy Wireless podcast
- **核心主张**: vendor-neutral RF 物理基础 + 系统性学习路径 (CWNA → CWAP/CWDP/CWSP → CWNE); CWNE 全球 < 500 持有人
- **影响 UBNT 工程师**: **基础层** — UBNT 工程师想做 senior 必须叠 CWNA 在 UEWA 之上

### 流派 3 — Capacity-first lineage (高密度设计派)
- **奠基**: Andrew vonNagy (Revolution Wi-Fi blog 2009-, "Design Your WLAN for High Capacity" 2012-12)
- **当前代表**: vonNagy (现 Nile Principal Architect), Joel Crane (Mist, ex-Ekahau), 部分被 Coleman / CWDP 教材吸收
- **代表作**: vonNagy capacity planning spreadsheets, NETGEAR HD Best Practices WP citing vonNagy
- **核心主张**: 用户密度 × per-client SLA → AP 数; 不按覆盖摆 AP; 80 人办公 = capacity 不是 coverage 问题
- **影响 UBNT 工程师**: **直接 critical** — 80 人 dense office 用户场景的核心方法论

### 流派 4 — AI-driven WLAN ops (AIOps 派)
- **奠基**: Bob Friday + Sudheer Matta (Mist Systems 2014, acquired by Juniper 2019, now HPE post-2025)
- **代表作**: Mist Marvis VNA, "AI-Native Networking" podcast (Juniper), Mist SLE (Service Level Expectations) framework
- **核心主张**: AI-native networking 颠倒视角 — 从客户端体验回推到 root cause, vs 看 100 个 dashboard; SLE 不看 device uptime 看 client 体验
- **影响 UBNT 工程师**: **对照阵营** — UBNT 当前 AIOps 弱项, "poor man's AIOps" = unpoller + Grafana + Claude via unifi-mcp 是替代路径

### 流派 5 — Security research (协议安全研究)
- **奠基**: Bill Arbaugh (802.11i / RSN 起草者 of *Real 802.11 Security* 2003), Mathy Vanhoef (KU Leuven, KRACK 2017)
- **代表作**: KRACK / Dragonblood / FragAttacks 三大 CVE 系列; Edney + Arbaugh *Real 802.11 Security*
- **核心主张**: 协议层 redesign > 实现层 patch; responsible disclosure 标杆 (90-day coord disclosure)
- **影响 UBNT 工程师**: 在重大 CVE 来临时启动 — 平时不主导决策, 但 WPA3 部署必读

### 流派 6 — UBNT-native practitioner (新流派, Wave 2 确认)
- **奠基**: 无明确学术奠基 — community-driven, 主要由 YouTube + blog + r/Ubiquiti 自组织 (2014-)
- **当前代表**: Chris Sherwood (Crosstalk Solutions 475K YouTube subs, UI Toolkit), Tom Lawrence (Lawrence Systems 375K subs, CVE 监控), Willie Howe (UBNT consultant), Nandor Katai (iFeelTech SMB blueprints), Rob Schultz (The Hook Up)
- **代表作**: Crosstalk YouTube channel (1000+ videos), UI Toolkit (2026-01), Lawrence "5 Critical UniFi CVEs" 系列, iFeelTech UniFi Business Network Guide 2026
- **核心主张**: GUI-first + 实战 > 理论; UBNT 整生态 (UniFi + airFiber + EdgeSwitch + WiFiman) 协同; SMB MSP 视角 (5-200 endpoints)
- **影响 UBNT 工程师**: **直接 primary** — 一个 80 人办公 IT 工程师最有可能第一个 subscribe 的频道

### 核心分歧 (active 争议, 保留)

**分歧 1 — AIOps vs human root-cause** (流派 4 vs 流派 2)
- **Friday / Mist 阵营**: 传统监控告诉你 "AP 在线" 但客户端体验差 — AI-native 视角颠倒, 从客户端体验回推 root cause, 让你不用看 100 个 dashboard
- **Akin / Parsons / Badman 阵营**: 现在 vendor 都在卖 AI WLAN, 但 root cause analysis 还得靠人, AI 只是把数据呈现得快一点; vendor 营销跑得比产品功能快
- **现状**: 双方都对的方面 — Mist 的 SLE 框架确实把客户体验量化了, 同时 Akin 阵营的 "工程师必须懂底层" 在 W8 workflow 的 "propose-then-approve gate" 设计上仍然成立. 这个争议 **不取一边**.

**分歧 2 — On-prem controller vs cloud-managed** (UBNT vs Mist)
- **UBNT (Sherwood)**: on-prem-friendly, Hosted UniFi 是可选, 数据控制权重要
- **Mist (Friday)**: cloud-only, telemetry 集中是 AIOps 的前提
- **现状**: 选择取决于客户场景 (数据敏感 / 合规需求 → on-prem; 全球分布 + AIOps 需求 → cloud). **不取一边**.

**分歧 3 — Predictive-heavy vs Pragmatic-survey** (Track 02 流派分裂)
- **Predictive (vonNagy + Mackenzie + CWDP)**: 商业交付必先 Ekahau predictive design 再 validation
- **Pragmatic (Sherwood + Howe + Lawrence)**: SMB 80 人单层场景跳过 predictive, WiFiman + ad-hoc 调
- **现状**: 80 人单层 ≤ 800 sqm 预算紧 → Pragmatic; 多层 / 商业合同 / 政府 → Predictive. **场景判定**.

---

<!-- SLOW_UPDATE_END -->



## 诚实边界

1. **zh-CN locale 严重 gap**: 全部 15 位 figures 均为 EN-locale; 全部 23 个持续 sources 中仅 UBNT 官方中文 KB (T05-S030) 是 zh-CN 一手 — 没有中文 enterprise UniFi community-grade 频道 / podcast / blog 在 Wave 1 surfaced. 中文圈 UBNT 讨论主要在 (a) 知乎 (信源黑名单), (b) 公众号 (黑名单), (c) 国内技术博客 SEO 转载. **暗示**: zh-CN 用户跟随本 skill 应预期 95% 一手材料在英文, 中文阅读门槛与翻译滞后是 hard limit. China 6 GHz 政策状态需季度独立 verify (来自 T06-S022 MIIT, 信号薄弱).

2. **工具栈 / 工作流模块衰减最快 — 建议每 3-6 月 update**: 4 个新兴层工具 (unifi-mcp, unifly, UI Toolkit, unifi-os-server) 都 ≤ 12 个月历史 + single-maintainer; W7 (WPA3 hardening) + W8 (AIOps stack) 是 high-decay 12-month-class workflows. UBNT 自身 software push (UniFi Network 10.0 Digital Twin, Hosted UniFi GA, Wi-Fi 7 U7 Pro Max) + 2025-2026 CVE wave 加速了模块衰减. 心智模型 / 标准 playbook / 智识谱系衰减慢 (1-2 年级).

3. **Voice 维度 medium-high 但缺 (原话) 段标志**: 4 类对话样本 14 段 ≥ 下限 8 段, 但全部为 (转述) 或 (推断), 无 podcast transcript (原话). Track 01 figures 的 voice_samples 字段已诚实标 "推断" / "转述" 非伪装原话. **暗示**: SKILL.md 的 §5 表达 DNA 给 LLM 提供清晰 register 模板, 但 voice check 盲测可能 partial 而非 high — 给 LLM 在 voice 上有 idealized 风险.

4. **UBNT-native systematic canon 薄弱**: UBNT 没有 Cisco Press / Sybex 级别的体系教材; UEWA 是 2-day vendor 训, 深度不及 CWNA. Wi-Fi 7 textbook lag (CWNA-110 在开发中, 2027-2028 expected) 让 Wi-Fi 7 内容目前依赖 IEEE 标准 + 厂商白皮书 + WLPC 演讲. Gast 第 2 版 (2005) 是 MAC 层 canon 但不覆盖 ax/be/WPA3 — 结构性缺口.

5. **UBNT 在 AIOps 维度结构性弱于 Mist** (vendor 对比): Mist Marvis VNA + SLE 框架是 cloud-managed + AI-native 阵营标准; UBNT 无原生等价, 只能 unifi-mcp + unpoller + Claude 自己拼凑 ("poor man's AIOps"). 这是 UBNT 战略 gap, 不是研究 gap. **暗示**: 客户被 Mist AI ops 卖点说服时, 工程师须诚实告知 trade-off (UBNT 5-10x 便宜 + 自管 controller; Mist AIOps + cloud-managed) 而非掩盖.

6. **「数字 / 拒审率 / deadline 必带来源」自检**: 本 synthesis 中所有 % / 数字 / 日期都有 source 或 caveat —
   - "Cloud Key Gen1 1 GB 内存" — T02-S040 + T02-S024 community 报告
   - "全球 < 500 持 CWNE 资格者" — T01-S009/T01-S043 CWNP 官方
   - "Crosstalk YouTube 475K subs" — T01-S001 (2026-06-02 last_checked)
   - "Wi-Fi 5 GHz 实际 100-200 Mbps/AP" — T03-W3 vonNagy capacity-first, 业内估计 (PHY rate 1.2 Gbps 的 30-60% 效率)
   - "WLPC ticket $1500+" — T01-S035 业内观察 (Parsons 公开 messaging)
   - "Mist 5-10x 贵于 UniFi" — T01-S025 vs T02-S039 业内估计
   - 无未带来源的具体数字.

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-06-02 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-06-02 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-06-02 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-06-02 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-06-02 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-06-02 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-06-02 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-06-02 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-06-02 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
