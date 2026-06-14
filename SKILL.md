---
name: "master-skill"
description: "Use when \u5927\u5e08.skill \u2014 \u8f93\u5165\u300c\u6211\u505a\u7684\u7ec6\u5206\u884c\u4e1a\u300d\uff0c\u81ea\u52a8\u5b8c\u6210\u884c\u4e1a\u5927\u4f6c\u8c03\u7814 / \u5de5\u5177\u5730\u56fe / \u5de5\u4f5c\u6d41 / \u77e5\u8bc6\u6b63\u5178 / \u4fe1\u606f\u6e90 / \u672f\u8bed\u6807\u51c6 \u516d\u8f68\u6df1\u5ea6\u8c03\u7814\uff0c\u63d0\u70bc\u4e3a\u53ef\u8fd0\u884c\u7684\u300c\u884c\u4e1a Master OS\u300dskill\u3002\n\u751f\u6210\u7684 {industry}.master skill \u662f\u81ea\u5305\u542b\u76ee\u5f55\uff0c\u6240\u6709 hermit agent / Claude Code agent / OpenClaw / Codex \u90fd\u80fd\u5b89\u88c5\uff0c\u8ba9 AI \u7acb\u523b\u8fdb\u5165\u300c\u8fd9\u884c\u7684\u8d44\u6df1\u4eba\u300d\u6a21\u5f0f\u3002\n\u89e6\u53d1\u8bcd\uff1a\u300c\u9020\u5927\u5e08\u300d\u300c\u505a\u4e2a X \u7684 master skill\u300d\u300c\u6211\u662f X \u884c\u4e1a\u300d\u300c\u8ba9 agent \u53d8\u6210 X \u5927\u5e08\u300d\u300cupdate \u5927\u5e08 X\u300d\u300c\u5927\u5e08 X\u300d\u300c\u6211\u505a X\uff0c\u5e2e\u6211\u84b8\u4e00\u4e2a\u300d\u3002\n"
allowed-tools: "Read, Write, Edit, Bash, WebSearch, WebFetch"
----

# 大师 · 行业蒸馏术

> 「同事.skill 蒸馏一个人，女娲.skill 蒸馏一种思维方式，大师.skill 蒸馏一整个行业的 OS。」

## 核心理念

一个好的行业 master skill **不是行业百科**，是**可运行的行业认知操作系统**：

- 这行的人用什么**心智模型**看问题？（镜片）
- 这行的标准**playbook** 是什么？（决策启发式）
- 这行的人怎么**沟通**？（行业表达 DNA）
- 什么算**好工作**？（质量基准）
- 外行才会犯什么错？（反模式）
- 这行的工具栈和工作流今年怎么变的？（时效层）

**关键区分**：捕捉的是 HOW the field thinks，不是 WHAT happens to be in the news this week。

---

## 范围约束（重要）

- **粒度**：一个 master skill 覆盖**一个细分领域**（例：「LLM agent 基础设施」「跨境电商运营」「足踝外科」），不要试图覆盖整个泛行业（「软件」「医疗」会让 OS 稀薄到没用）
- **目标用户**：行业内 / 想入行 / 服务这行的人。不是给完全外行做扫盲
- **不替代实操工具**：master skill 是「思维顾问」，不是 RPA。不要在里面塞「自动操作 X 后台」之类
- **版权安全**：不存全本书 / 完整字幕 / 长段原文。只保留结构化摘要 + 来源元数据 + 极短引用

---

## 路径占位符 (iter 24 重要)

prompts 里两个不同的目录占位符:

| 占位符 | 含义 | 例子 |
|--------|------|------|
| `{master_skill_dir}` | master-skill 仓库 (本仓库) 的 `skill/` 目录, 工具脚本住在这里 | `~/master-skill/skill/` 或 `/Users/foo/master-skill/skill/` |
| `{skill_dir}` | 当前正在生成 / 更新 的**行业** skill 目录, 调研笔记 / SKILL.md / sub-skills 都写到这里 | `~/.claude/skills/llm-agent-infra-master/` |

工具脚本 (source_verifier.py / cold_detector.py / quality_check.py / collectors / ingest / transcribe) **不复制**到生成的行业 skill 目录, agent 直接调 `{master_skill_dir}/tools/...`. 行业 skill 只装载 prompts + research notes + SKILL.md + sub-skills + cli/.

如果运行环境的 master-skill 路径变了, agent 替换占位符即可; 不需要改任何工具源代码.

---

## 执行流程

### Phase 0: 入口分流

收到用户输入后判断路径：

| 用户输入 | 路径 | 示例 |
|---------|------|------|
| 明确的细分行业 | **直接路径** → Phase 0A | 「我做跨境电商，给我做一个 master skill」 |
| 模糊的需求 | **诊断路径** → Phase 0B | 「我想转 AI 行业，但不知道哪个细分」 |
| 已存在的 skill | **更新路径** → Phase 0C | 「update 大师 LLM-agent-infra」 |

---

### Phase 0A: 行业澄清（直接路径）

确认 6 个维度（用户没主动提的字段就问，主动给的就不要重问）：

1. **行业 / 细分领域**（必填）— 例：`LLM agent infra`，不是 `AI`；`跨境电商运营`，不是 `电商`
2. **聚焦方向**（可选）— 全景画像 vs 某个角度优先（例：技术视角 vs 商业视角）
3. **地域 / 语言区**（可选）— global / 中文圈 / 美国 / 欧洲。影响信源选择
4. **用户身份**（可选）— 从业者 / 学习者 / 投资人 / 咨询。影响 master skill 的语气与决策视角
5. **本地素材**（强烈推荐询问）— 「你手上有这行的一手素材吗？行业报告 PDF / 内部文档 / 你写过的文章 / 长访谈 transcript / 视频字幕？有的话直接丢给我，比网上搜到的二手转述质量高得多」
6. **新建 or 更新**（可选）— 检查 `~/.claude/skills/{slug}-master/` 是否已存在

用户没主动给 → 默认全景 + global + 从业者视角 + 无本地素材，确认后推进。
用户提供了本地素材 → 标记为**本地语料模式**，Phase 1 采集策略相应调整。

确认后 → Phase 0.5。

---

### Phase 0B: 需求诊断（模糊路径）

用户不确定要蒸哪个细分时，反推合适的范围。

#### Step 1: 锚定核心目标

最多 1-2 轮追问，定位用户真正的需求维度：

| 维度 | 典型表达 | 反推方向 |
|------|---------|---------|
| 谋生 / 转行 | 「想入行 X」「做这个能赚钱吗」 | 商业生态视角的 master skill |
| 提效 | 「这行的工作流我搞不清」「文档堆成山」 | 工作流视角的 master skill |
| 决策 | 「不知道该选 A 还是 B」 | 工具选型 + 标准 playbook |
| 学习 | 「想系统学这行」 | 知识正典视角 |
| 创业 | 「想做 X 方向的产品」 | 行业 OS + 信息源（找未被满足的需求） |

#### Step 2: 反推候选

基于用户表达，提议 2-3 个具体的细分领域。每个候选要回答：

- 这个细分**目前真有可调研的公开材料吗**？（冷门领域的 master skill 质量必差）
- 它跟用户的需求多对齐？
- 它跟其他候选的差异在哪？

用户选定后 → Phase 0A 补全 6 个维度 → Phase 0.5。

---

### Phase 0C: 更新路径

读取已存在的 `{slug}-master/SKILL.md`，从 frontmatter 找到 `last_research_date`。基于距今多久决定刷新强度：

| 距今 | 刷新策略 |
|------|---------|
| < 1 月 | 拒绝刷新，告知用户最近刚更新过 |
| 1-3 月 | 仅 Track B（工具）+ Track C（工作流）+ Track E 中的「最新动态」节 |
| 3-6 月 | 加上 Track A（看 top figures 是否有大动作）+ Track F（标准是否有新版） |
| > 6 月 | 全部 6 轨重跑，但保留旧版 archive |

不要每次都重写整个 skill — 行业的**核心 OS** 通常 1-2 年才动一次，**工具 / 工作流**才是高频变量。

---

### Phase 0.5: 创建 Skill 目录

在调研开始之前完成：

```
{HOST_SKILLS_ROOT}/{slug}-master/
├── SKILL.md                          # 最终产物
├── meta.json                         # 元数据 (industry, locale, profile, last_research_date, source_count)
├── scripts/                          # 工具脚本（继承自 master-skill 仓库 + 行业特化）
└── references/
    ├── research/                     # 6 轨调研结果（必存）
    │   ├── 01-figures.md             # 行业大佬
    │   ├── 02-tools.md               # 工具地图
    │   ├── 03-workflows.md           # 工作流 / SOP
    │   ├── 04-canon.md               # 知识正典（书 / 论文 / 课）
    │   ├── 05-sources.md             # 信息源（newsletter / podcast / 会议 / 社区）
    │   └── 06-glossary.md            # 术语 + 标准 + 法规
    ├── synthesis.md                  # Phase 2 提炼结果（行业 OS）
    └── sources/                      # 一手素材（用户提供 + 网络下载的字幕等）
        ├── books/
        ├── transcripts/
        └── articles/
```

**HOST_SKILLS_ROOT 解析**：
- Claude Code: `~/.claude/skills`
- OpenClaw: `~/.openclaw/skills`
- Codex: `~/.codex/skills`
- Hermes: `~/.hermes/skills`
- 其他 / 不确定：在当前 cwd 下创建 `./{slug}-master/`，最后让用户决定装到哪

**目录创建后立即检查**：
- [ ] 目录已创建
- [ ] 如果 locale 是中文圈：信源策略切换为 B 站原始视频 / 小宇宙播客 / 36氪 / 极客公园 / 晚点 / 财新优先（**永远排除知乎、微信公众号、百度百科**）
- [ ] 如果 locale 是英文圈：默认 Twitter/X / YouTube / Substack / arXiv / 行业 podcast 优先
- [ ] 如果是更新模式：已读取现有 `SKILL.md` 和 `references/research/*.md`，标注哪些信息要刷
- [ ] 如果用户提供了本地素材：复制到 `sources/` 对应子目录，标记为**本地语料模式**

**关键规则（开源分发的核心）**：
- 所有调研文件必须存在 skill 目录内部 `references/research/`，**绝不存到外部目录**
- skill 必须自包含：clone 整个目录就能用
- 每个 subagent 必须把调研写入对应文件。不存文件的调研等于没做

---

### Phase 1: 多源信息采集（六轨 Agent Swarm，wave 结构）

#### 模式判断

| 模式 | 触发 | 策略 |
|------|------|------|
| **纯网络搜索**（默认） | 用户没给本地素材 | 6 个 Agent 全部走网络 |
| **本地语料优先** | 用户提供了 PDF / 行业报告 / transcript | 先按 6 轨分类本地素材，识别缺口，定向网络补充 |
| **纯本地语料** | 用户明确说「只用我给的」 | 只分析本地，不联网 |

#### Wave 结构（重要 — 不是纯并行）

iter 4 figures 跑通后发现：6 轨之间互相是 bootstrap 输入。Track 01 (figures) 的「最大几家公司创始人」依赖 Track 02 (tools) 找到的「关键工具」；Track 02 的「业内人吐槽过哪些工具」反过来依赖 Track 01 找到的人。强行纯并行 → 各轨都凭空猜起点。

执行结构：

**Wave 1（并行）— 「广撒网」轨**：
- Track 04 (canon) — 必读书 / 论文 / 课，搜索路径最独立（看 Goodreads / arXiv / 大学课程页就行）
- Track 05 (sources) — newsletter / podcast / 会议，搜索路径独立（搜「{industry} podcast」「{industry} newsletter」）
- Track 06 (glossary) — 术语 + 标准，从行业入门书 / 维基 / 标准化机构 page 抓

**Wave 1 加速器：先跑 collectors 拉机械 seed (iter 24)**

Wave 1 启动前 2 分钟跑这 4 个 collector, 拉到结构化 seeds.jsonl, 让 web search 不再凭空猜:

```bash
mkdir -p {skill_dir}/references/research/seeds
# 用户主 industry slug 对应的 GitHub topic / arXiv 类目 / 行业核心 RSS
python3 {master_skill_dir}/tools/collectors/github_topics.py --topic {topic} \
  --limit 30 --output {skill_dir}/references/research/seeds/github_repos.jsonl
python3 {master_skill_dir}/tools/collectors/arxiv_collect.py --query "cat:cs.AI AND all:agent" \
  --max 30 --output {skill_dir}/references/research/seeds/arxiv_papers.jsonl
python3 {master_skill_dir}/tools/collectors/rss_collect.py --feed-list {skill_dir}/intake.feeds.txt \
  --max 20 --output {skill_dir}/references/research/seeds/rss_items.jsonl
python3 {master_skill_dir}/tools/collectors/podcast_rss.py --apple-id {N} \
  --max 30 --output {skill_dir}/references/research/seeds/podcast_episodes.jsonl
```

Wave 1 subagent 必须**先 cat 这些 jsonl** 再启动 web search. 例如 Track 05 (sources) 看 podcast_episodes.jsonl 里反复出现的 host / show 直接进 retain 候选; Track 04 (canon) 看 arxiv_papers.jsonl 的 author 网络. 这把「凭直觉撒网」换成「从机械 seed 撒网」, 漏掉的高密度一手少很多.

**Seeds JSONL 通用 schema** (collectors 都遵守):
- `type`: `github_repo` / `arxiv_paper` / `rss_item` / `podcast_episode` (必填, agent 根据它路由)
- `name` / `title`: 实体名
- `url`: 一手 URL (跑 source_verifier classify 取 bucket)
- `author` / `host` / `show_host`: 主创
- `published` / `pushed_at` / `last_activity`: ISO 时间戳 (用于 freshness)
- 类型特有字段: stars/forks (github), authors/abstract (arxiv), guests/duration_sec (podcast), summary (rss)
- 任何 collector 输出都可作 seed; agent 在合并时用 `url` 去重

**Wave 2（并行，用 Wave 1 的产出做 seed）— 「人 + 工具」轨**：
- Track 01 (figures) — 用 Wave 1 的 canon 作者 + sources 嘉宾名单作为初始候选
- Track 02 (tools) — 用 Wave 1 的 sources 中频繁讨论的工具 + canon 中点名的工具作为初始候选

**Wave 3（用前两 wave 的产出做 seed）— 「整合」轨**：
- Track 03 (workflows) — 综合 figures 怎么干活 + tools 怎么用 + canon 中描述的流程，提炼当前 SOP

每个 wave 内可并行启动 subagent。Wave 之间串行，但每 wave 跑完不阻塞用户 —— 模型并行 swarm 的内部时间预算 ≤ 3 min / wave，整体 Phase 1 应在 10-15 min 内拿到完整 6 个 research note 文件。

**Wave seed fallback 统一规则**（findings iter 7+8 unified）：

| 上 wave 总产出 seed 数 | 下 wave 启动策略 |
|---------------------|----------------|
| ≥ 8 seeds | 正常启动，按 seed 撒大网 |
| 5-7 seeds | 警告但启动，subagent 模板被指示「seed 偏少，加权 web search 兜底」 |
| 1-4 seeds | 启动前先回头检查上 wave subagent 是否还在跑 / 是否失败；如确定失败 → 启动当前 wave 但**降级**为「半 seeded 半 web search」 |
| 0 seeds | **STOP**，向用户报告：「上 wave 信号 0，可能行业极冷僻 / 闭源主导 / 输入有误。要继续吗？」用户决定 (a) 等待重试 (b) 切纯 web search 模式 (c) 收回 industry 重新选 |

如果某 wave 内某 track 失败（5 min 没产出有效 source），不阻塞下一 wave，但 seed 总数减少。子 wave 自动按上表表行降级。

启动 wave 1 的 3 个 subagent；Wave 1 完成后启动 wave 2 的 2 个；Wave 2 完成后启动 Wave 3 的 1 个。每个 subagent 任务模板（以 Track A 为例）：

```
你的任务：调研「{industry}」行业的 {track_topic}。

{track-specific 搜索方向}

强制约束：
- 调研结果必须写入 {skill_dir}/references/research/{NN-track}.md
- 每条信息标注来源 URL 和可信度（一手 > 二手 > 推测）
- 区分一手（行业人自己说的）vs 二手（别人转述的）vs 推断（你的判断）
- 发现矛盾保留，不和稀泥
- 不要存全本书 / 长字幕 / 大段原文 — 只存结构化摘要 + 来源
- 信源黑名单：{locale-specific blacklist}
- 信源优先级：用户本地一手素材 > 行业人本人输出 > 长访谈 > 行业经典著作 > 权威媒体长稿 > 社交媒体短稿 > 二手转述
```

#### 6 个 Agent 的任务分配

| Agent | Track | 搜索目标 | 提取重点 | 输出 |
|-------|-------|---------|---------|------|
| 1 | **Figures** | top 10-15 thought leaders | 各自的「核心一句话」、代表作品、值得读 / 听 / 看的 3 件事、争议、最近 12 个月动态 | `01-figures.md` |
| 2 | **Tools** | canonical 工具 + 新兴工具 | 用什么场景、相对优劣、近 12 个月有没有出现颠覆性新工具、选型决策树 | `02-tools.md` |
| 3 | **Workflows** | SOP / 方法论 / pipeline | 入门人怎么走完一个完整任务、资深人怎么走、近期工作流变化（AI / 工具升级带来的） | `03-workflows.md` |
| 4 | **Canon** | 必读书 / 论文 / 课 / 核心概念 | 「这行的人都读过」的清单（≥3 个独立来源都点过）、核心 20-30 个概念 | `04-canon.md` |
| 5 | **Sources** | 信息源 | newsletter（前 5）、podcast（前 5）、会议（前 3-5）、社区（前 3-5）、dataset（如适用）、定期更新频率 | `05-sources.md` |
| 6 | **Glossary** | 术语 + 标准 | 高频黑话 / 缩写、合规框架、认证、最近一次行业标准更新 | `06-glossary.md` |

#### 音视频转文本（必备能力）

行业素材大量是访谈、conference talk、podcast。优先级：

1. **YouTube / B 站官方字幕**：`yt-dlp --write-subs --skip-download`，优先人工字幕 → 中文 → 英文 → 自动字幕
2. **podcast transcript 网站**：podcastnotes.org、transcriber.io 等，搜「{podcast name} transcript」
3. **本地 whisper fallback**：仅当用户明确提供音频文件且没有公开 transcript 时使用
4. **转写后存** `sources/transcripts/{slug}.txt`

注意：调研笔记中**不要 paste 完整 transcript**，只提取观点 + 引用极短句子。

#### 信源黑名单（按 locale）

| Locale | 永远排除 |
|--------|---------|
| zh-CN | 知乎、微信公众号、百度百科、百度知道、CSDN（除非是作者本人原文） |
| en | Quora answers（除非作者认证）、ChatGPT-generated blog spam、内容农场 |
| 通用 | AI summaries 站（无原文链接的）、SEO 农场 |

#### 利用已安装的辅助 skill

Phase 1 启动前扫描 `~/.claude/skills/`（或宿主对应路径），如果有以下 skill 可调用，告知 subagent：

| Skill | 用途 |
|------|------|
| `agent-reach` | 多平台信息获取（X / Reddit / YouTube / Bilibili / 小红书等） |
| `web-article-reader` | 精读网页全文 |
| `pdf` | 读 PDF 行业报告 |
| `gemini-video` | 用户提供本地视频文件无字幕时转写 |
| `nuwa-skill` | **关键**：Phase 3 时调用它生成 top 3 figures 的 sub-skill |

#### Agent 失败 / 信息不足处理

- 单 Agent 跑 5 分钟无有价值结果 → 不等，继续推进，在诚实边界中标注
- 总来源 < 30 条 → 冷门领域协议：
  - 心智模型限制为 2-3 个
  - 工作流模块标注「基于有限信息」
  - 扩大诚实边界
  - 告知用户：「这个细分目前公开材料偏少，{N} 条来源。如果你能提供以下材料质量会显著提升：[列出关键缺口]」

---

### Phase 1.5: 调研 Review 检查点

所有 Agent 完成后**强制暂停**，向用户展示结构化摘要：

```
┌──────────────────┬──────────┬─────────────────────────────────┐
│ Track            │ 来源数    │ 关键发现                         │
├──────────────────┼──────────┼─────────────────────────────────┤
│ 1 Figures        │ N        │ top: A / B / C；最近动态: ...    │
│ 2 Tools          │ N        │ canonical: X / Y；新出: Z        │
│ 3 Workflows      │ N        │ 当前 SOP: ...；近期变化: ...     │
│ 4 Canon          │ N        │ 必读 top 3: ...                  │
│ 5 Sources        │ N        │ newsletter / podcast / 社区     │
│ 6 Glossary       │ N        │ 关键术语 N 个                    │
├──────────────────┼──────────┼─────────────────────────────────┤
│ 矛盾点            │ N 处      │ Track1 说 X, Track4 说 Y         │
│ 信息不足维度       │ [列表]   │ 补充计划: ...                    │
│ 一手 / 二手比例    │ a:b      │ 一手占比 X%                     │
│ 冷门领域?         │ 是 / 否   │                                  │
└──────────────────┴──────────┴─────────────────────────────────┘
```

用户确认 OK → Phase 2。
用户觉得某轨不够 → 补完再继续，不能跳过。

**这一关挡住的是**：调研垃圾导致后续提炼全部失真。垃圾进垃圾出，在这里返工成本最低。

---

### Phase 2: 框架提炼（Synthesis）

读取 6 轨 research 笔记，提炼行业 OS。

#### 2.1 行业心智模型（3-7 个）

= 这行的人看问题的独特镜片。

**三重验证筛选**：
- **跨场景复现**：在 ≥ 2 个不同案例 / 子领域 / 经典著作中出现？
- **生成力**：能用它推断这行人对一个新问题的立场？
- **排他性**：不是所有聪明人都会这样想？只有这行的人这样想？

三重通过 → 心智模型；仅 1-2 重 → 降级为决策启发式；0 重 → 丢弃。

每个模型记录：名称、一句话描述、≥ 2 处来源证据、应用方式、局限。

#### 2.2 标准 playbook（5-10 条决策启发式）

= 这行的人面对 X 类问题时的快速规则。表述为「如果 {场景}，则 {决策方向}」，每条配 1-2 个具体案例。

#### 2.3 工具栈与选型决策树

从 Track 02 提炼：
- **必备工具**（≥ 80% 从业者用）
- **场景特化**（不同子方向用不同的）
- **新兴 / 实验**（近 12 个月出现，未必稳定）
- **避坑清单**（外行容易选错的）

#### 2.4 工作流 / pipeline

从 Track 03 提炼：
- **入门 SOP**：完成一个最小完整任务的最少步骤
- **资深路径**：跳过 / 优化哪些步骤
- **近期变化**：AI / 新工具 / 法规变化带来的工作流改写

#### 2.5 行业表达 DNA

从 Track 01 / 03 / 06 提炼：
- 这行人的高频用语 / 黑话
- 严肃讨论 vs 轻松吐槽的 register 差别
- 内部 vs 外部沟通时的差异
- 一个外行读起来「不像这行的」的常见破绽

#### 2.6 质量基准 + 反模式

- **什么算「好」**：3-5 条具体可验证的基准
- **什么是反模式**：外行 / 入门常犯的 5-10 条错误

#### 2.7 智识谱系

这个行业的几个主要流派 / 学派 → 各自的奠基人 → 当前代表人物 → 核心分歧。

#### 2.8 诚实边界

必须明确写出的局限：
- 信息截止 `{research_date}`，工具 / 工作流模块衰减最快
- master skill 不能替代行业实操经验
- 公开信息有偏差（成功者发声多，失败者沉默）
- 这次调研的薄弱维度（如有）

#### 2.9 Agentic Protocol 种子

为 Phase 3 准备：从 2.1 / 2.3 / 2.4 推导出「这行人面对一个新问题时，会按什么维度去做功课」。例如：

- 「跨境电商运营」 master 拿到「我要在德国上线一个新品类」 → 默认会研究：竞品定价（看 Helium 10）、目标市场习惯、税务（VAT / 一站式申报）、物流（FBA / 海外仓选型）、合规（CE / GS / 包装法）

写下 **3-10 个**（按行业复杂度调整）**这行人面对新问题时的标准研究维度**，每个维度配 1-2 个具体的搜索 / 查询动作。简单行业（窄 + 工具少）3-5 个；标准行业 5-7 个；复杂行业（宽 + 工具栈多 + 流派多）7-10 个。

---

### Phase 2.5: 提炼确认检查点

向用户展示提炼摘要：

```
{industry} Master OS 提炼结果
─────────────────────────────────
心智模型：N 个
  1. {名称} - {一句话}
  2. ...

标准 playbook：N 条
工具栈：必备 N / 场景化 N / 新兴 N
工作流：入门 / 资深 / 近期变化
表达 DNA：{3-4 个关键特征}
质量基准：N 条
反模式：N 条
智识谱系：{N 个流派}
诚实边界：N 条

Agentic Protocol：N 个研究维度
─────────────────────────────────
确认进入 Skill 构建？还是某项要调？
```

用户确认 OK → Phase 3。
用户觉得某项不准 → 回到 Phase 2 调整。

---

### Phase 3: Skill 构建

将 Phase 2 提炼组装为可运行的 `SKILL.md`。

#### Step 1: 读取生成模板

读取 `references/skill-template.md`（master-skill 仓库自带）获取标准结构。模板定义：
- frontmatter（name / description / triggers / industry / locale / last_research_date）
- 角色扮演规则
- **Agentic Protocol**（按行业研究维度做功课再答）
- 行业 OS 模块（心智模型 / playbook / 表达 DNA / 质量基准 / 反模式 / 智识谱系 / 诚实边界）
- 知识模块（figures / tools / workflows / canon / sources / glossary）
- 调研来源汇总

#### Step 2: 填充

按模板逐 section 填入 Phase 2 结果。

| 模板 Section | 填充来源 |
|------------|---------|
| frontmatter | meta.json + research summary |
| 角色扮演规则 | 直接用模板 default |
| Agentic Protocol | Phase 2.9 推导的研究维度 |
| 心智模型 | Phase 2.1 |
| 标准 playbook | Phase 2.2 |
| 工具栈 | Phase 2.3 |
| 工作流 | Phase 2.4 |
| 表达 DNA | Phase 2.5 |
| 质量基准 + 反模式 | Phase 2.6 |
| 智识谱系 | Phase 2.7 |
| 诚实边界 | Phase 2.8 |
| Figures / Tools / Workflows / Canon / Sources / Glossary | Track 01-06 整理后摘要 + 链接到 `references/research/` |
| 调研来源 | 6 轨引用汇总 |

#### Step 3: Top Figures Sub-skill — cross-skill composition (v1.x)

> 大师.skill 调女娲.skill 蒸馏 top figures, 生成的 person sub-skill 嵌入 `sub-skills/`. 这是 cross-skill composition 的核心 — 大师不重新发明 person 蒸馏, 它委托给女娲.

#### 3.0 先决条件

- 用户在 Phase 0A 选了「全景画像」或明确要求 sub-skill
- Track 01 (figures) 至少有 3 个 figures 已被多源认可（≥ 2 endorsement-evidence per figure）
- nuwa-skill 已安装 (`~/.claude/skills/nuwa-skill/` 或 `~/.openclaw/skills/nuwa-skill/`); 没有则告知用户「装一下女娲.skill 才能展开 sub-skill 步骤」

如果用户选了「聚焦」或时间紧 → 跳过本步, 只在主 skill 中保留 figures 摘要 (Track 01 输出已足够).

#### 3.1 选 Top 3 figures

读 `references/research/01-figures.md`, 按以下排序选 top 3:

| 优先级 | 标准 |
|------|------|
| 1 | endorsement count (≥ 3 个独立来源点过为优先) |
| 2 | long-form material 量 (有 ≥ 2 hour podcast / multiple book chapters / ≥ 5 long-form blog) |
| 3 | 思维方式独特度 (figures 之间观点重叠度低, 同一行业 3 个一样的 figure 没意义) |
| 4 | 当前活跃度 (最近 12 月有公开发声) |

**反模式**: 选「业内最有名」(可能只是 PR 强), 而忽略「思维最锐利」.

#### 3.2 准备每个 figure 的素材包

为每个 top figure 准备:
- **基础事实**: 姓名 / 公司 / 角色 / 主要观点 (从 01-figures.md 的「核心一句话」字段)
- **长素材**: ≥ 2 个 long-form material 的 transcript / 长文 (优先用 `tools/transcribe/youtube.sh` 处理 podcast / talk)
- **代表作品**: 文章 / 演讲题目 / 书 (URL 可)
- **争议立场**: figure 的非 mainstream 观点 (这部分通常最能体现思维方式)

把这些写到一个临时 prompt blob, 用 [`prompts/sub-skill-figures.md`](prompts/sub-skill-figures.md) 模板填充.

#### 3.3 spawn subagent 调用 nuwa-skill

```
spawn subagent (general-purpose):
prompt: 「{prompts/sub-skill-figures.md 填充后的内容}」
working_directory: {slug}-master/sub-skills/{figure-slug}/
```

subagent 拿到任务后:
1. 读 `~/.claude/skills/nuwa-skill/SKILL.md` (或者其他 host 的 nuwa 安装路径)
2. 走 nuwa-skill 的 5 步流程 (intake → 思维素材采集 → 三轨提炼 → 生成 → 验证)
3. 把生成的 person sub-skill 写到 `{slug}-master/sub-skills/{figure-slug}/`
4. subagent 完成后回主 agent, 报告写入文件清单

主 agent 跑 3 个 subagent **并行** (3 个 figures 互不依赖, 可并发).

#### 3.4 在主 SKILL.md 中绑定 sub-skill

主 SKILL.md 「智识谱系」节末尾自动插入:

```markdown
### Sub-skills (女娲蒸馏的 top figures)

需要某位 figure 的视角时, 加载对应 sub-skill:

| Figure | Sub-skill 路径 | 何时调用 |
|--------|--------------|---------|
| {figure-1} | `sub-skills/{slug-1}/SKILL.md` | 当问题涉及 {topic-1} 时 |
| {figure-2} | `sub-skills/{slug-2}/SKILL.md` | 当问题涉及 {topic-2} 时 |
| {figure-3} | `sub-skills/{slug-3}/SKILL.md` | 当问题涉及 {topic-3} 时 |
```

`skill_writer.py` 的 `meta.json` 同步更新 `sub_skills` 字段 (slug + path 列表).

#### 3.5 失败模式

| 失败场景 | 应对 |
|---------|------|
| nuwa-skill 没装 | 告知用户安装 + 暂时跳过 sub-skill 步骤, 完整大师 skill 仍能交付 |
| figure 的 long-form material 不够 | 跳过这个 figure, 选第 4 名顶上, 或降级为只在 01-figures.md 中保留摘要 |
| nuwa-skill subagent 超时 | 30 min 没完成单个 figure → 标记 timeout, 主 agent 决定是否等; 不阻塞 Step 4 写入主 skill |
| 三个 figures 思维高度重叠 | 选 2 个差异大的, 第 3 个换成持反对立场的 figure (即使排名靠后) |

#### Step 4: 写入

调 `tools/skill_writer.py create`（v0.3+），它会：
- 写 `{skill_dir}/SKILL.md`（自动注入 synthesis body）
- 写 `{skill_dir}/meta.json`（自动算 source ratio + decay registry）
- 复制 6 个 `references/research/0X-*.md` 到 skill 内部
- 复制 `references/synthesis.md`（自包含）

```bash
python3 tools/skill_writer.py create \
  --skill-dir <output> \
  --intake <intake.json> \
  --synthesis <synthesis.md> \
  --template references/skill-template.md \
  --research-dir <research/>
```

#### Step 5: CLI 工具流子树 (v0.6+)

`skill_writer.py` 在写完 SKILL.md / meta.json 后，**自动调** `tools/cli_writer.py emit` 生成 `cli/` 子树：

| 脚本类别 | 来源 | 输出 |
|---------|------|------|
| `cli/protocol/agentic.sh` | synthesis Section 9 (Agentic Protocol) | 拿到新问题时按 N 维度做功课的交互脚本 |
| `cli/decision/{cluster}.sh` | synthesis Section 2 (Playbook 规则聚类) | 决策树（每个聚类 ≥ 1 条规则） |
| `cli/workflow/{wf-slug}.sh` | research/03-workflows.md | SOP 走查 + 失败模式自检 |

每个生成脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 标准接口。完整 spec: [references/cli-spec.md](references/cli-spec.md)。

如果用户不要 CLI（例如纯演示）：`skill_writer.py create --no-cli`.

---

### Phase 4: 质量验证

生成后**用子 agent 独立测试**（避免自评偏差）：

#### 4.1 已知测试（Sanity Check）

挑 3 个这行有共识答案的问题，spawn 子 agent 带着新 skill 回答。对比业内共识：
- 方向一致 → PASS
- 偏离 → 回 Phase 2 调整

#### 4.2 边缘测试（Edge Case）

挑 1 个这行人没特别讨论过但相关的问题，让 skill 推断。
- 期望：「基于 {心智模型 X} 和 {playbook Y} 推断，可能 ...; 但需要 {具体来源} 确认」
- 不应该斩钉截铁

#### 4.3 风格测试（Voice Check）

让 skill 写 100 字行业短评。盲测能否被识别为「这行的人写的」。

#### 4.4 通过标准

| 检查项 | 通过 | 不通过 |
|------|------|--------|
| 心智模型数 | 3-7 | < 3 或 > 10 |
| 每个模型有局限 | ✓ | 只写优点 |
| 表达 DNA 辨识度 | ✓ | 像通用 ChatGPT |
| 诚实边界 | ≥ 3 条具体 | 只有「不能替代真人」 |
| 一手来源占比 | ≥ 50% | 主要二手转述 |
| Agentic Protocol | ≥ 5 个研究维度 | < 3 |
| 时效性标注 | ≥ 1 处 last_updated | 无 |

不通过 → 标注薄弱维度回 Phase 2 迭代。**最多 2 轮**，仍不通过则在诚实边界中明确标注，交付当前最优版本。

---

### Phase 5: 双 Agent 精炼（标准后置）

Phase 4 通过后，并行启动两个评审 agent：

**Agent A（auto-skill-optimizer 视角）**：
- 评 SKILL.md 的工作流清晰度、边界条件、检查点设计、指令具体性
- 干跑 3 个典型 prompt，评估有效性
- 输出最弱 2 个维度的具体改进建议（带改后文本示例）

**Agent B（skill-creator 视角）**：
- 评激活触发条件是否覆盖真实场景
- 评角色扮演规则的可操作性
- 识别缺失的关键信息
- 输出 2-3 处具体改动建议（带改后文本示例）

主 agent 综合两份报告，应用不冲突的改进，向用户展示变更摘要请求确认。

精炼标准：让 skill「激活即执行」，不是「内容更多」。

---

## 更新已有 Skill

走 Phase 0C 路径。重点：

1. 读 `meta.json` 中 `last_research_date`
2. 按距今时长决定哪几轨重跑
3. 旧的 `references/research/` 文件移到 `references/research/archive/{date}/`
4. 重跑选定的 track，但保留旧版本可参考
5. Phase 2 重新提炼时，明确对比新 vs 旧：
   - 新信息加强现有模型 → 补充案例
   - 新信息与旧模型矛盾 → 标记 changed，更新模型，在诚实边界写「{date} 起 {模型 X} 改为 ...」
   - 出现新模型 → 加入
   - 旧模型彻底过时 → 标记 deprecated，移到「历史模型」节
6. 写 `CHANGELOG.md` 记录这次更新动了什么
7. 不重写整个 skill，只增量更新

---

## 品味守则（速查）

| 原则 | 一句话 |
|------|--------|
| 长访谈 > 金句 | 1 小时 podcast 比 50 条推文更揭示行业 OS |
| 争议 > 共识 | 流派分歧最能揭示行业的真问题 |
| 工具栈年更 vs OS 年更 | Phase 3 的工具 / 工作流模块每 3-6 月可衰减；心智模型 1-2 年才动 |
| 一手 > 二手 | 行业人本人发的内容 > 别人写他的 |
| 本地素材 > 网络搜索 | 用户手上的行业报告 PDF / 内部文档 > 任何网络爬来的 |

### 绝不做的事

- 编造行业 figures 没说过的话 / 没写过的书
- 把通用商业道理包装成「{X 行业的} 独特见解」
- 忽略行业的真实争议、骗局、黑历史
- 在公开材料 < 30 条时强行生成「全维度 master skill」

---

## 与其他 skill 的关系

| Skill | 用途 |
|------|------|
| [同事.skill (dot-skill)](https://github.com/titanwings/colleague-skill) | 蒸馏一个具体的人（同事 / 合作方） |
| [女娲.skill](https://github.com/alchaincyf/nuwa-skill) | 蒸馏一种思维方式 / 名人 OS。**大师.skill 在 Phase 3 调用它生成 top figures 的 sub-skill** |
| 大师.skill（本 repo） | 蒸馏一个细分行业的 OS |

层级：dot < nuwa < master，覆盖范围一层比一层大，调研深度逐层下降。
