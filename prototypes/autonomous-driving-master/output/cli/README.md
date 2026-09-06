# 自动驾驶 CLI

把 自动驾驶 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/workflow-1.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 安全 决策树 (3 条规则) |
| `decision/topic-2.sh` | 案例 决策树 (5 条规则) |
| `decision/topic-3.sh` | 数字 决策树 (1 条规则) |
| `decision/topic-4.sh` | 口径 决策树 (1 条规则) |
| `workflow/workflow-1.sh` | 功能定义与运行设计域（ODD）划定 (Decay risk: medium) SOP 走查 |
| `workflow/workflow-2.sh` | 危害分析与风险评估到安全目标与 ASIL 分解 (Decay risk: low) SOP 走查 |
| `workflow/workflow-3.sh` | 预期功能安全（SOTIF）分析与危险场景收敛 (Decay risk: medium) SOP 走查 |
| `workflow/workflow-4.sh` | 数据采集与合规处理（中国：测绘资质 / 数据出境 / 脱敏） (Decay risk: high) SOP 走查 |
| `workflow/workflow-5.sh` | 标注与数据集构建（自动标注与人工审核的分工） (Decay risk: high) SOP 走查 |
| `workflow/workflow-6.sh` | 感知模型训练与评测 (Decay risk: high) SOP 走查 |
| `workflow/workflow-7.sh` | 预测与规划模块开发（含规则兜底层设计） (Decay risk: high) SOP 走查 |
| `workflow/workflow-8.sh` | 闭环仿真与场景回归（场景库构建、参数化、覆盖度） (Decay risk: medium) SOP 走查 |
| `workflow/workflow-9.sh` | 实车路测与影子模式验证 (Decay risk: medium) SOP 走查 |
| `workflow/workflow-10.sh` | 长尾问题挖掘与数据闭环 (Decay risk: high) SOP 走查 |
| `workflow/workflow-11.sh` | 版本发布与整车 OTA（中国备案与准入许可的分流） (Decay risk: high) SOP 走查 |
| `workflow/workflow-12.sh` | 事故与接管的复盘调查（含向监管报送） (Decay risk: high) SOP 走查 |
| `workflow/workflow-13.sh` | 量产准入与型式认证材料准备 (Decay risk: high) SOP 走查 |
| `workflow/workflow-14.sh` | 示范运营与远程协助值守 (Decay risk: medium) SOP 走查 |
| `workflow/safety-case.sh` | 安全案例（safety case）的持续维护 (Decay risk: medium) SOP 走查 |

## 设计与生成

CLI 子树由 `tools/cli_writer.py` 自动从 `references/synthesis.md` (Section 2 Playbook + Section 9 Agentic Protocol) 和 `references/research/03-workflows.md` 生成。

完整 spec 在 master-skill 仓库 `references/cli-spec.md`。

## 重新生成

如果 synthesis.md 或 03-workflows.md 更新了, 重跑:

```bash
python3 <master-skill>/tools/cli_writer.py emit \
  --skill-dir <this-skill-dir> \
  --synthesis references/synthesis.md \
  --workflows references/research/03-workflows.md \
  --industry-cn "自动驾驶"
```
