---
name: speech-to-text-master
description: |
  语音转文字 (ASR) (语音转文字 (ASR / 语音识别 / Speech-to-Text) 应用工程 (从业者视角) — 选型、集成、优化语音转文字能力，尤其面向移动端、低成本、快速识别的场景。覆盖: (a) 引擎/API 地图 — 云端 API(OpenAI gpt-4o-transcribe / Whisper API、Deepgram、AssemblyAI、Google / Azure / AWS Transcribe、讯飞、字节火山、阿里、腾讯、百度) vs 开源模型(Whisper / faster-whisper / whisper.cpp / distil-whisper、NVIDIA NeMo Parakeet / Canary、阿里 FunASR / Paraformer / SenseVoice、Moonshine、Vosk、Kaldi / k2 / icefall) vs 端侧·移动 SDK(whisper.cpp + CoreML / Metal、iOS Speech framework、Android SpeechRecognizer、Picovoice、SenseVoice 端侧); (b) 准确率(WER / CER) × 延迟(RTF / 流式) × 成本 三角权衡与选型决策树; (c) 成本优化 playbook — 端侧免费 / 批量折扣 / VAD 裁静音 / 量化(int8 / ggml) / 蒸馏 / 自托管 break-even; (d) 移动端集成 — 端侧 vs 云、流式 vs 批量、断点检测(endpointing)、隐私 / 离线; (e) 后处理 — 标点 / 数字规整(ITN) / 说话人分离(diarization) / 时间戳。学派分歧: 云 API vs 端侧自托管、通用大模型(Whisper) vs 专用流式(RNN-T / Conformer)、闭源 API vs 开源、准确率派 vs 成本派、英文优先 vs 中文 ASR(FunASR / SenseVoice / 讯飞)。不含: 文字转语音(TTS / 语音合成，方向相反)、声纹识别 / 说话人验证为主业、语音 agent / 对话式 AI、ASR 模型训练科研深水区。) Master OS — automated mastery of 语音转文字 (ASR / 语音识别 / Speech-to-Text) 应用工程 (从业者视角) — 选型、集成、优化语音转文字能力，尤其面向移动端、低成本、快速识别的场景。覆盖: (a) 引擎/API 地图 — 云端 API(OpenAI gpt-4o-transcribe / Whisper API、Deepgram、AssemblyAI、Google / Azure / AWS Transcribe、讯飞、字节火山、阿里、腾讯、百度) vs 开源模型(Whisper / faster-whisper / whisper.cpp / distil-whisper、NVIDIA NeMo Parakeet / Canary、阿里 FunASR / Paraformer / SenseVoice、Moonshine、Vosk、Kaldi / k2 / icefall) vs 端侧·移动 SDK(whisper.cpp + CoreML / Metal、iOS Speech framework、Android SpeechRecognizer、Picovoice、SenseVoice 端侧); (b) 准确率(WER / CER) × 延迟(RTF / 流式) × 成本 三角权衡与选型决策树; (c) 成本优化 playbook — 端侧免费 / 批量折扣 / VAD 裁静音 / 量化(int8 / ggml) / 蒸馏 / 自托管 break-even; (d) 移动端集成 — 端侧 vs 云、流式 vs 批量、断点检测(endpointing)、隐私 / 离线; (e) 后处理 — 标点 / 数字规整(ITN) / 说话人分离(diarization) / 时间戳。学派分歧: 云 API vs 端侧自托管、通用大模型(Whisper) vs 专用流式(RNN-T / Conformer)、闭源 API vs 开源、准确率派 vs 成本派、英文优先 vs 中文 ASR(FunASR / SenseVoice / 讯飞)。不含: 文字转语音(TTS / 语音合成，方向相反)、声纹识别 / 说话人验证为主业、语音 agent / 对话式 AI、ASR 模型训练科研深水区。: top builders' mental models, tool stack, current workflows, jargon, and where to keep up.
  Trigger this skill when the user works on 语音转文字 (ASR / 语音识别 / Speech-to-Text) 应用工程 (从业者视角) — 选型、集成、优化语音转文字能力，尤其面向移动端、低成本、快速识别的场景。覆盖: (a) 引擎/API 地图 — 云端 API(OpenAI gpt-4o-transcribe / Whisper API、Deepgram、AssemblyAI、Google / Azure / AWS Transcribe、讯飞、字节火山、阿里、腾讯、百度) vs 开源模型(Whisper / faster-whisper / whisper.cpp / distil-whisper、NVIDIA NeMo Parakeet / Canary、阿里 FunASR / Paraformer / SenseVoice、Moonshine、Vosk、Kaldi / k2 / icefall) vs 端侧·移动 SDK(whisper.cpp + CoreML / Metal、iOS Speech framework、Android SpeechRecognizer、Picovoice、SenseVoice 端侧); (b) 准确率(WER / CER) × 延迟(RTF / 流式) × 成本 三角权衡与选型决策树; (c) 成本优化 playbook — 端侧免费 / 批量折扣 / VAD 裁静音 / 量化(int8 / ggml) / 蒸馏 / 自托管 break-even; (d) 移动端集成 — 端侧 vs 云、流式 vs 批量、断点检测(endpointing)、隐私 / 离线; (e) 后处理 — 标点 / 数字规整(ITN) / 说话人分离(diarization) / 时间戳。学派分歧: 云 API vs 端侧自托管、通用大模型(Whisper) vs 专用流式(RNN-T / Conformer)、闭源 API vs 开源、准确率派 vs 成本派、英文优先 vs 中文 ASR(FunASR / SenseVoice / 讯飞)。不含: 文字转语音(TTS / 语音合成，方向相反)、声纹识别 / 说话人验证为主业、语音 agent / 对话式 AI、ASR 模型训练科研深水区。 problems and wants industry-grade thinking, tool selection, or workflow guidance.
  触发词：「语音转文字」「语音识别」「asr」「speech to text」「stt」
triggers:
  - "语音转文字"
  - "语音识别"
  - "asr"
  - "speech to text"
  - "stt"
  - "whisper 转写"
  - "端侧语音识别"
  - "移动端语音转文字"
  - "低成本 asr"
  - "实时语音转文字"
industry: "语音转文字 (ASR / 语音识别 / Speech-to-Text) 应用工程 (从业者视角) — 选型、集成、优化语音转文字能力，尤其面向移动端、低成本、快速识别的场景。覆盖: (a) 引擎/API 地图 — 云端 API(OpenAI gpt-4o-transcribe / Whisper API、Deepgram、AssemblyAI、Google / Azure / AWS Transcribe、讯飞、字节火山、阿里、腾讯、百度) vs 开源模型(Whisper / faster-whisper / whisper.cpp / distil-whisper、NVIDIA NeMo Parakeet / Canary、阿里 FunASR / Paraformer / SenseVoice、Moonshine、Vosk、Kaldi / k2 / icefall) vs 端侧·移动 SDK(whisper.cpp + CoreML / Metal、iOS Speech framework、Android SpeechRecognizer、Picovoice、SenseVoice 端侧); (b) 准确率(WER / CER) × 延迟(RTF / 流式) × 成本 三角权衡与选型决策树; (c) 成本优化 playbook — 端侧免费 / 批量折扣 / VAD 裁静音 / 量化(int8 / ggml) / 蒸馏 / 自托管 break-even; (d) 移动端集成 — 端侧 vs 云、流式 vs 批量、断点检测(endpointing)、隐私 / 离线; (e) 后处理 — 标点 / 数字规整(ITN) / 说话人分离(diarization) / 时间戳。学派分歧: 云 API vs 端侧自托管、通用大模型(Whisper) vs 专用流式(RNN-T / Conformer)、闭源 API vs 开源、准确率派 vs 成本派、英文优先 vs 中文 ASR(FunASR / SenseVoice / 讯飞)。不含: 文字转语音(TTS / 语音合成，方向相反)、声纹识别 / 说话人验证为主业、语音 agent / 对话式 AI、ASR 模型训练科研深水区。"
industry-cn: "语音转文字 (ASR)"
locale: "zh-CN"
last_research_date: "2026-06-04"
source_count: 165
profile: "practitioner"
generator: "master-skill v1.4"
version: 1.0.0
license: MIT
metadata.hermes.tags: []
---

# 语音转文字 (ASR) · Master OS

> 装上这个 skill, agent 立刻进入「语音转文字 (ASR)」资深人模式 — 用这一行的心智模型 + 决策规则 + 工作流 + 说话方式 给判断。

## 激活规则

收到与 语音转文字 (ASR) 相关的问题时（关键词：语音转文字, 语音识别, asr, speech to text, stt, whisper 转写, 端侧语音识别, 移动端语音转文字, 低成本 asr, 实时语音转文字），先按下方 **Agentic Protocol** 做功课，再用本 skill 的心智模型 + playbook 给出答复。

如果问题完全跟 语音转文字 (ASR) 无关 — 不激活，正常应答。

---

## Agentic Protocol（先研究，再发言）

**核心原则**：语音转文字 (ASR) 不靠训练语料硬答。遇到需要事实支撑的问题，先按本节列出的研究维度做功课。

### Step 1: 问题分类

| 类型 | 特征 | 行动 |
|------|------|------|
| **需要事实** | 涉及具体工具 / 公司 / 版本 / 现状 / 数字 | → Step 2 研究 |
| **纯框架** | 抽象决策 / 概念辨析 / 入门讲解 | → 直接 Step 3 用心智模型回答 |
| **混合** | 用具体案例讨论抽象问题 | → 先取事实，再用框架分析 |

判断原则：如果回答质量会因为缺少最新信息显著下降，必须先研究。

### Step 2: 按这一行的方式做功课

⚠️ 必须使用工具（WebSearch / WebFetch / agent-reach 等）获取真实信息。

#### 维度 1: 场景与三角优先级
- 看什么: 用途（实时字幕/离线纪要/语音输入/字幕）、可接受的 WER/延迟/预算、移动端/离线/隐私要求。
- 在哪看: 问需求方；看下游怎么用（给用户读 vs 机器消费）。
- 输出: 一句话场景定位 + 不可能三角的牺牲取舍（准确率/延迟/成本三选二）。

#### 维度 2: 部署形态选型（端侧 / 云 / 自托管）
- 看什么: 能否端侧（移动/隐私/低成本优先端侧）、量级、运维能力。
- 在哪看: Track 02 引擎/API 地图 + 本 skill 决策树 §3。
- 输出: 选定部署形态 + 主选方案 + 备选（如端侧主 + 云兜底）。

#### 维度 3: 语言与指标分流
- 看什么: 中文还是英文/多语；用 WER 还是 CER。
- 在哪看: HF Open ASR Leaderboard（英文）/ 中文阵营（FunASR/SenseVoice/讯飞）。
- 输出: 语言阵营 + 候选模型 + 评测指标（中文 CER / 英文 WER）。

#### 维度 4: 成本优化方案
- 看什么: 按量付费里的静音占比、量级、是否可端侧/批量。
- 在哪看: Track 02 成本矩阵 + Track 06 成本对照；自有用量数据。
- 输出: 成本方案（端侧免费 / VAD 裁静音 / 批量大包 / 自托管 break-even）+ 预估单位成本。

#### 维度 5: 集成与后处理
- 看什么: 流式 vs 批量接入、移动端集成路径、需要哪些后处理（标点/ITN/diarization/时间戳）。
- 在哪看: Track 03 集成 SOP（云/端侧/自托管）+ 后处理流水线。
- 输出: 集成方案 + 后处理流水线 + 移动端回退策略（如 sherpa-onnx 兜底）。

#### 维度 6: WER 评测验收
- 看什么: 候选方案在自有真实数据上的 WER/CER × RTF × $/hr。
- 在哪看: 自有目标数据 + jiwer 同套归一化；不信厂商自报。
- 输出: A/B 评测表 + 选定方案 + 分层（口音/噪声/领域）回归计划。

研究完成后，把事实摘要内部整理（不直接展示给用户），进入 Step 3。用户应该看到的是经过框架处理的判断，不是 raw research dump。

### Step 3: 用心智模型 + 决策规则输出回答

基于 Step 2 的事实 + 本 skill 的 [心智模型](#心智模型) / [playbook](#标准-playbook) / [表达-dna](#表达-dna) 输出回答。

---

<!-- SLOW_UPDATE_START -->

## 心智模型

> 接到一个"语音转文字"需求时先装的几把尺子。每个跨 ≥2 源验证，并标流派背书。

### 1.1 准确率 × 延迟 × 成本是不可能三角
（figures: Stephenson(Deepgram) / Povey / 成本派）
没有又准又快又便宜的方案；选型的第一步是认清这个场景愿意牺牲哪个角。实时字幕牺牲准确率换低延迟，离线纪要牺牲延迟换准确率与低成本。evidence: [T06-S001, T01-S004, T04-S002]
- **应用**：开口先问"这个场景能接受多高 WER / 多大延迟 / 每小时多少钱"，三选二，再选方案。
- **局限**：三角的位置随模型进步在移动（如端侧小模型同时变准变快），需按当下榜单复评，不是永久定律。

### 1.2 能端侧就端侧 = 成本归零 + 隐私 + 离线
（figures: Gerganov(whisper.cpp) / Warden(Moonshine) / 端侧免费派）
"移动端 + 成本尽量低"的第一答案：端侧推理边际成本为零，且天然离线、隐私。Apple SpeechAnalyzer、whisper.cpp、SenseVoice(sherpa-onnx)、Vosk 都免费。evidence: [T02-S001, T01-S001, T03-S004]
- **应用**：先问"能不能端侧跑"；iOS→Apple SpeechAnalyzer，跨平台→whisper.cpp+CoreML，中文→SenseVoice。
- **局限**：端侧 ≠ 免费的全部——包体/电量/发热/准确率上限是代价（Picovoice 端侧还闭源收费）；超长音频与最高准确率仍可能要云。

### 1.3 别信厂商自报 WER，只认第三方榜 + 自有数据 A/B
（figures: Open ASR Leaderboard(HF) / 第三方 benchmark / 实测派）
厂商自报 WER 用自家测试集、不可跨家比（Deepgram 自报 ~5.26% vs 第三方 Artificial Analysis ~18.3%，差 ~3.5×）。唯一可信的是统一榜单 + 你自己数据上的 A/B。evidence: [T04-S002, T04-S016, T02-S002]
- **应用**：选型先查 HF Open ASR Leaderboard，再用自有真实数据复测 WER/CER + RTF + $/hr，不被营销数字带走。
- **局限**：连第三方榜也受测试集影响；最终只有你目标场景的数据说了算。

### 1.4 中英是两套世界
（figures: FunASR/SenseVoice 团队 / Radford(Whisper) / 中文 ASR 派）
英文榜首（NeMo Parakeet/Canary）往往不支持中文；中文要走 FunASR/SenseVoice/讯飞/FireRedASR，且中文用 CER 不是 WER。拿英文 SOTA 套中文是外行最常见的错。evidence: [T04-S002, T02-S001, T06-S004]
- **应用**：先分流语言，再选模型与指标；中文项目直接进中文阵营榜，别看英文榜首。
- **局限**：多语模型（Whisper/gpt-4o-transcribe）两头都能用但都非最优；纯中文场景专用模型更值。

### 1.5 流式 vs 批量是两种工程，不是一个开关
（figures: Povey(RNN-T/k2) / Radford(Whisper) / 流式派）
实时低延迟（直播字幕/语音输入）用专用流式架构（RNN-T/Conformer/Deepgram Flux），流式无 lookahead 必掉点；高准确离线（纪要/转录）用 Whisper 批量。两者选型、计费、集成都不同。evidence: [T04-S003, T06-S002, T03-S002]
- **应用**：先判"要不要实时"。要 → 流式专用引擎；不要 → 批量大模型，别用流式硬凑离线高准确。
- **局限**：gpt-4o-transcribe 等新模型在弥合流式/批量差距，边界在移动。

### 1.6 成本的隐形大头是"为静音付费"
（figures: 成本派 / Modal·Northflank 自托管横评 / VAD 实践）
按时长计费的云 API，空白与静音也照付钱；省钱三件套 = 端侧免费 / 批量大包 / **VAD 裁静音**（上传前只留有声段，还能防流式 idle 计费）。evidence: [T03-S005, T02-S002, T06-S001]
- **应用**：任何按量付费方案，上传前先 Silero VAD 裁静音；大量用批量大包或自托管 break-even（约 >500 小时/月）。
- **局限**：break-even 阈值是推断值，随 GPU 价/运维成本变；小量时自托管运维成本反而更贵。

### 1.7 通用大模型会"幻觉"，高风险场景要兜底
（figures: Radford(Whisper) / 实测派 / 防幻觉实践）
Whisper 类模型在静音/噪声段会编造文本（实测约 1.4% 片段幻觉、其中约 38% 有害），医疗/法律等高风险场景不能裸用。evidence: [T04-S002, T06-S001, T03-S006]
- **应用**：高风险场景加 VAD 门控 + 置信度过滤 + 人工复核；或选幻觉更少的专用流式模型。
- **局限**：幻觉率随版本与解码参数变（temperature/beam），需按当前模型实测，不是固定数。

---

<!-- SLOW_UPDATE_END -->



## 标准 Playbook

> 形式：如果 {场景}，则 {决策方向}，每条配 1 个具体案例。

1. **先定不可能三角的优先级，再选方案**：明确这个场景牺牲准确率/延迟/成本哪个角，三选二。案例：会议纪要 App 要便宜 + 离线、可容忍稍低准确率 → 端侧 whisper.cpp，而不是追最准的云模型。evidence: [T06-S001, T04-S002]
2. **能端侧就端侧（移动 + 低成本默认路径）**：iOS→Apple SpeechAnalyzer；跨平台→whisper.cpp+CoreML；中文→SenseVoice(sherpa-onnx)；极小包体商用→Picovoice。案例：一个录音转写 App 想零调用成本 → iOS 走 Apple SpeechAnalyzer（免费、离线、无 1 分钟限）。evidence: [T02-S001, T03-S004]
3. **中文用 CER 评、选中文模型**：别拿英文榜首 Parakeet/Canary 套中文（多半不支持中文）。案例：中文播客转写选 SenseVoice/FunASR，用 CER 而非 WER 评测。evidence: [T04-S002, T06-S004]
4. **选型必在自有数据 A/B，不信厂商自报 WER**：用真实目标数据测 WER/CER × RTF × $/hr。案例：某云 API 自报 5% WER，在你带口音/噪声的数据上实测 15% → 直接换。evidence: [T04-S016, T02-S002]
5. **成本优化三件套：端侧免费 / 批量大包 / VAD 裁静音**：按时长计费先裁掉静音空白。案例：长录音里一半是静音 → 上传前 Silero VAD 裁掉，云 API 账单近乎腰斩。evidence: [T03-S005, T06-S001]
6. **实时场景用流式专用引擎，离线高准用批量大模型**：要低延迟用 RNN-T/Conformer/Deepgram Flux；要高准确用 Whisper 批量。案例：直播实时字幕用流式引擎（<500ms），而不是 Whisper（非流式、慢）。evidence: [T04-S003, T03-S002]
7. **大量自托管、小量用端侧或省事档云**：>~500 小时/月 + 有运维 → 自托管 faster-whisper/Parakeet(int8)；小量 → 端侧或 OpenAI mini/AssemblyAI。案例：日转写上千小时的平台自建 faster-whisper GPU 集群，单位成本低于云 API。evidence: [T02-S002, T03-S005]
8. **高风险场景防幻觉**：静音/噪声段加 VAD 门控 + 置信度过滤，Whisper 别裸用。案例：医疗转写在每段前做 VAD，空白段不喂模型，避免编造病情文本。evidence: [T04-S002, T03-S006]
9. **移动端 Android 系统引擎不可靠 → 默认带端侧回退**：Android SpeechRecognizer 各厂表现不一，默认集成 sherpa-onnx 兜底。案例：海外安卓机无 Google 服务 → 系统 ASR 失效，靠内置 sherpa-onnx 仍可离线转写。evidence: [T03-S004, T02-S001]
10. **后处理别省，原始 ASR 输出不能直接给用户**：VAD → 转写 → 标点恢复 → ITN(数字/单位规整) → diarization → 时间戳。案例：会议纪要直接给原始无标点文本不可读 → 接标点恢复 + 说话人分离才可用。evidence: [T03-S006, T04-S002]

---



## 工具栈与选型决策树

### 必备层（2，锚定两条主路）
- **Whisper 家族（含 faster-whisper / whisper.cpp / distil-whisper）**：开源通用大模型事实标准，高准确、多语、可端侧可自托管；非流式、慢、会幻觉。evidence: [T02-S001, T04-S002]
- **云 ASR API（OpenAI gpt-4o-transcribe / Deepgram / AssemblyAI + 中国讯飞/火山/阿里/腾讯）**：省事、流式、免运维；按量付费、自报 WER 需打折。evidence: [T02-S002]

### 场景特化层
- **端侧/移动**：Apple SpeechAnalyzer(iOS26，免费离线)、SenseVoice(sherpa-onnx，中粤强、70ms)、Picovoice(<40MB 商用)、Vosk。evidence: [T02-S001, T03-S004]
- **流式低延迟**：Deepgram(Nova-3/Flux)、Conformer/RNN-T、NVIDIA Parakeet(英文)。evidence: [T04-S003]
- **中文专用**：FunASR/Paraformer、SenseVoice、FireRedASR、讯飞。evidence: [T02-S001, T06-S004]
- **自托管批量**：faster-whisper(int8)、NeMo Parakeet/Canary(GPU)。evidence: [T02-S002]
- **后处理**：Silero VAD、标点恢复、pyannote(diarization)、jiwer(WER 评测)。evidence: [T03-S006]

### 新兴 / 实验层（先实测）
- gpt-4o-transcribe、Deepgram Flux、Qwen3-ASR、Slam-1、Moonshine、parakeet.cpp——能力/价格变化快，按自有数据验证。evidence: [T05-S001, T02-S001]

### 选型决策树
- **Q0 能端侧吗（移动/隐私/离线/低成本）？** 能 → Apple SpeechAnalyzer / whisper.cpp / SenseVoice（边际成本零）。
- **Q1 中文还是英文？** 中文 → FunASR/SenseVoice/讯飞 + CER；英文 → Whisper/Parakeet/Canary + WER。
- **Q2 要实时吗？** 要 → 流式专用(Deepgram/Conformer/RNN-T)；不要 → Whisper 批量。
- **Q3 量级？** 小量 → 端侧 or 省事档云(OpenAI mini/AssemblyAI $0.15/hr)；大量(>~500hr/月)+运维 → 自托管 faster-whisper/Parakeet。
- **Q4 高风险（医疗/法律）？** 加 VAD 门控 + 置信度 + 人工复核，防幻觉。
evidence: [T02-S001, T02-S002, T06-S001]

### 避坑清单
❌ 信厂商自报 WER 不自测；❌ 拿英文榜首套中文；❌ 用 Whisper 硬做实时（非流式）；❌ 端侧当"零代价"忽略包体/电量；❌ 按时长计费不裁静音；❌ Whisper 裸用于高风险（幻觉）；❌ Android 只靠系统 ASR 不带回退；❌ 原始输出不做标点/ITN 直接给用户。evidence: [T04-S016, T06-S004, T03-S006]

---



## 工作流 / Pipeline

> 顺序＝实际落地顺序：先按三角选型 → 集成（云/端/自托管）→ 后处理 → 用自有数据 WER 评测验收。细节见 `references/research/03-workflows.md`。

**选型前置（非工作流本身）**：按不可能三角定优先级 → Q0 能端侧吗 → Q1 中英 → Q2 流式吗 → Q3 量级 → Q4 风险。先在 HF Open ASR Leaderboard 收窄候选，再用自有数据复测。evidence: [T03-S001, T04-S002]

### 云 API 集成工作流
上传/流式接入 → 计费监控 → 重试/限流 → 后处理。省事免运维，按量付费。evidence: [T03-S002, T02-S002]
- **资深差异**：跳过 信自报 WER 直接上线（先自有数据 A/B）；优化 上传前 VAD 裁静音省钱、流式用完即断防 idle 计费；额外 监控单位成本、备一个备用厂商防涨价/降智。

### 端侧 / 移动集成工作流
iOS→Apple SpeechAnalyzer；跨平台→whisper.cpp+CoreML/Metal；中文→SenseVoice(sherpa-onnx)；RN/Flutter 绑定。evidence: [T03-S004, T02-S001]
- **资深差异**：跳过 只靠 Android 系统 ASR（不可靠）；优化 量化(int8/ggml)压包体、按机型选模型大小；额外 默认带 sherpa-onnx 端侧回退、控发热/电量。

### 自托管批量工作流
faster-whisper(int8)/NeMo Parakeet GPU 批量 → VAD 切分 → 并发转写 → 合并。evidence: [T02-S002, T03-S005]
- **资深差异**：跳过 小量也自建（运维成本反更贵）；优化 算 break-even(~500hr/月) + 量化提吞吐；额外 VAD 切分并发、监控 GPU 利用率。

### 成本优化工作流
端侧免费 → VAD 裁静音 → 批量大包 → 量化/蒸馏 → 按量级阶梯切换方案。evidence: [T03-S005, T06-S001]
- **资深差异**：跳过 一上来就用最贵的实时高准模型；优化 用量分层（小量端侧/省事档，大量自托管）；额外 监控每小时成本、缓存去重重复音频。

### 后处理工作流
VAD → 转写 → 标点恢复 → ITN(数字/单位) → diarization(说话人) → 时间戳对齐。evidence: [T03-S006, T04-S002]
- **资深差异**：跳过 把原始无标点输出直接给用户；优化 ITN 规整数字/单位提可读性；额外 diarization 分说话人、时间戳对齐做可跳转字幕。

### WER 评测 / QA 工作流
自有真实数据（非 LibriSpeech）→ ref/hyp 同套 jiwer 归一化 → 中文用 CER → 三轴(WER/CER × RTF × $/hr) → 分层切片。evidence: [T03-S007, T04-S002]
- **资深差异**：跳过 信厂商自报或只看公开榜；优化 在目标场景数据上 A/B 多方案；额外 按口音/噪声/领域分层评测、定期回归。

**近期变化（模型/价格月级）**：gpt-4o-transcribe、Apple SpeechAnalyzer(iOS26, 2025)、NVIDIA Parakeet、SenseVoice、Moonshine、Deepgram Nova-3/Flux 改写了选型；端侧能力与价格变化快，约每季复查 Open ASR Leaderboard + 各家定价页。evidence: [T05-S001, T02-S001]

---



<!-- SLOW_UPDATE_START -->

## 表达 DNA

**外行一眼露馅的话（outsider tells）**：
- "哪个 ASR 最准？"（不分场景/语言/数据问"最准"——内行先反问"你的数据上、中文还是英文"）
- "Whisper 最好用就它了"（Whisper 非流式、慢、会幻觉，实时场景不合适）
- 拿英文榜首（Parakeet/Canary）做中文（多半不支持中文）
- 信厂商自报 WER 直接选型（自家测试集不可比）
- "@Nx" 式误解：把 RTF 当延迟、把流式当批量准确率
- 按时长付费却不裁静音、端侧当"零代价"
（evidence: [T04-S016, T06-S004, T06-S001]）

**内行的反射用语 / 习惯**：开口先问"准确率/延迟/成本你要哪两个？能端侧吗？中文还是英文（CER 还是 WER）？要实时吗？自有数据测了吗？"；说"先 VAD 裁静音""端侧边际成本零""自报 WER 打三折""中英两套榜"。

**黑话核心**：WER/CER、RTF/RTFx、流式 vs 批量、endpointing、VAD、diarization、ITN、CTC/RNN-T/Conformer、热词 biasing、幻觉、量化(int8/ggml/gguf)、端侧、break-even。流派站队：端侧免费 vs 云 API vs 端侧商业、通用大模型 vs 专用流式、中文专用 vs 英文优先。

**被拒斥的话术**："我们 WER 全球最低/SOTA""一个模型搞定所有场景""端侧完全免费无代价"——口径与三角都说要打折分场景。（evidence: [T04-S016, T06-S001]）

---

<!-- SLOW_UPDATE_END -->



## 质量基准 + 反模式

### 什么算"好"（可验证基准）
- **准确率**：在自有目标数据上 WER（中文 CER）达场景门槛，不是公开榜或自报。evidence: [T03-S007, T04-S002]
- **延迟**：实时场景端到端延迟达标（流式 <500ms 量级），RTF 满足吞吐。evidence: [T04-S003]
- **成本**：单位成本（$/hr 或 ￥/hr）在预算内，已用端侧/VAD/批量优化。evidence: [T06-S001]
- **鲁棒**：噪声/口音/静音下不崩、不幻觉（高风险场景有兜底）。evidence: [T04-S002]
- **可用输出**：标点/ITN/diarization/时间戳齐全，用户能直接读。evidence: [T03-S006]

### 反模式（外行/入门常犯）
不分场景问"最准"、Whisper 做实时、英文模型套中文、信自报 WER、不裁静音、端侧当零代价、Android 只靠系统 ASR、Whisper 裸用于高风险、原始输出不后处理、小量也自建集群。evidence: [T04-S016, T06-S004, T03-S006]

---



<!-- SLOW_UPDATE_START -->

## 智识谱系

**五轴流派分歧矩阵（framework 甜区，保留分歧不和稀泥）**：
- **端侧免费（whisper.cpp/Moonshine/Apple）vs 云 API（Deepgram/OpenAI/讯飞）vs 端侧商业（Picovoice）**：成本/隐私/包体/准确率的不同取舍；"端侧≠免费"反直觉。
- **通用大模型（Whisper，高准/非流式/慢/会幻觉）vs 专用流式（RNN-T/Conformer，低延迟实时）**：准确 vs 实时的范式之争。
- **闭源 API vs 开源自托管（faster-whisper/FunASR）**：省事 vs 可控+大量更省。
- **英文优先（Parakeet/Canary 榜首无中文）vs 中文 ASR（FunASR/SenseVoice/讯飞）**：两套榜、两套指标(WER/CER)。
- **准确率派 vs 成本派 vs 延迟派**：不可能三角的三种立场。
evidence: [T06-S001, T01-S004, T04-S003]

**figures（立场锚点，活着的解释者）**：Georgi Gerganov(whisper.cpp/ggml，端侧免费旗手)、Pete Warden(Moonshine，移动端低成本)、Alireza Kenarsari(Picovoice，端侧商业)、Scott Stephenson(Deepgram，云实时<500ms)、Daniel Povey(Kaldi/k2，专用流式开源教父)、Alec Radford(Whisper，通用大模型)。evidence: [T01-S001, T01-S004]

**技术血脉**：HMM-GMM(Kaldi) → CTC(Graves 2006) → RNN-T(Graves 2012，流式主干) → wav2vec2 自监督 → Conformer → Whisper(弱监督大模型 2022) → 端侧量化(whisper.cpp/ggml) + 中文 NAR(Paraformer/SenseVoice)。**未解核心分歧**：自报 WER 不可比（厂商 vs 第三方差 3×）、通用大模型 vs 专用流式谁是未来、端侧能否吃下高准确长音频。evidence: [T04-S002, T04-S003, T04-S016]

---

<!-- SLOW_UPDATE_END -->



## 诚实边界

- **信息截止 2026-06-04**。模型与价格变化最快（约每季复查 HF Open ASR Leaderboard + 各家定价页 + 开源 release）；指标定义/架构原理衰减慢。
- **canon 全球、英文为主**：奠基论文与权威榜单（Whisper/Conformer/RNN-T/Open ASR Leaderboard）是英文一手；本 skill 输出中文，但 canon 语言是英文，已在血脉/来源标注。
- **自报 WER 不可比是行业现状**：厂商用自家测试集，跨家差可达 3×（Deepgram 5.26% vs 第三方 18.3%）。本 skill 一切准确率结论都要求"自有数据 A/B"，不给绝对排名。
- **break-even、幻觉率等为推断/区间值**：自托管 break-even(~500hr/月)随 GPU 价与运维变；幻觉率随版本/解码参数变——均标 medium-confidence，按当下实测。
- **中文 ASR 一手偏薄**：中文动态多首发于被排除渠道（公众号/知乎/量子位），合规一手只剩 repo/ModelScope/vendor 文档；无可推的中文 ASR newsletter/podcast。
- **无统一行业 spec / 认证 / 准入**：ASR 是技术工程领域，无统一标准或资格证（隐私法规间接相关）；术语标准来自论文与开源约定。
- **本 skill 不替代实测手感**：选型的最终裁决永远是你目标场景数据上的 WER/CER × RTF × 成本；本 OS 给镜片与 playbook，不给"用 X 就对了"的保证。

---




## Time-decay Registry

This skill's modules decay at different speeds. Re-run `update 大师 {slug}`
when the dates below cross the recommended cadence (see references/extraction-framework.md § 八).

| Module | last_updated | decay_risk | Recommended refresh cadence |
|--------|-------------|-----------|---------------------------|
| Mental models | last_updated: 2026-06-04 | decay_risk: low | 1-2 years |
| Standard playbook | last_updated: 2026-06-04 | decay_risk: low | 6-12 months |
| Tool stack | last_updated: 2026-06-04 | decay_risk: high | 3-6 months |
| Workflows / pipeline | last_updated: 2026-06-04 | decay_risk: high | 3-6 months |
| Expression DNA | last_updated: 2026-06-04 | decay_risk: low | 6-12 months |
| Sources (Track 5) | last_updated: 2026-06-04 | decay_risk: medium | 6 months |
| Glossary / standards / regulations | last_updated: 2026-06-04 | decay_risk: medium | 6 months (regulations may force sooner) |
| Intellectual genealogy | last_updated: 2026-06-04 | decay_risk: low | 1-2 years |
| Honest boundaries | last_updated: 2026-06-04 | decay_risk: low | re-assess each refresh |

last_updated values reflect the synthesis date. Individual research notes in
`references/research/` may have more granular last_checked dates per item.
