# Stitch Skills Union and Codex Plugin Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将本地 Stitch 技能库扩展为本地与 Google 官方能力并集，并基于该技能快照交付可通过 `STITCH_API_KEY` 连接远程 Stitch MCP 的个人 Codex 插件 `stitch`。

**Architecture:** 本地仓库继续作为技能事实源：保留 29 个现有 Skill，引入 10 个官方独有 Skill，并把 6 组重叠能力融合进现有规范入口，最终形成 39 个无重复入口的 Skills。个人插件复制该仓库的已验证快照，通过 `.mcp.json` 的 `env_http_headers` 将 `STITCH_API_KEY` 映射为 `X-Goog-Api-Key`，不包含 SDK 代理层或明文密钥。

**Tech Stack:** Agent Skills (`SKILL.md`)、Markdown、Shell/Python/TypeScript 辅助脚本、Codex plugin manifest、远程 HTTP MCP、Google Stitch MCP、Apache-2.0。

**Spec:** `docs/superpowers/specs/2026-09-11-stitch-skills-union-and-codex-plugin-design.md`

## Global Constraints

- 本地仓库 `/Users/wandl/workspaces/workspace-agent-skills/full-stack-skills-repositories/stitch-skills` 是合并主干。
- Google 官方上游固定为 `google-labs-code/stitch-skills@0337446dadde6f8c94210444e2aa9d546126480f`。
- 保留现有 29 个 Skill，不删除本地独有能力；最终规范入口数为 39。
- 插件名称、目录名和 marketplace 名称均为 lower-case `stitch`。
- Stitch MCP URL 固定为 `https://stitch.googleapis.com/mcp`。
- `X-Goog-Api-Key` 只能来自环境变量 `STITCH_API_KEY`，不得写入仓库、插件、日志或示例。
- 不执行 `specify init`、`openspec init`、第三方包静默安装、项目删除或自建 SDK 网关。
- 所有新增或修改 Skill 必须通过 quick validation 与 TRACE 检查后才能进入插件快照。

---

### Task 1: 固化上游快照与能力矩阵

**Files:**
- Create: `docs/upstream/google-stitch-skills-0337446.md`
- Create: `docs/upstream/stitch-skills-capability-matrix.md`
- Create: `scripts/verify_skill_inventory.py`
- Test: `scripts/verify_skill_inventory.py`

**Interfaces:**
- Consumes: 本地 `skills/*/SKILL.md`；官方提交 `0337446dadde6f8c94210444e2aa9d546126480f`。
- Produces: `verify_skill_inventory.py --root PATH --expected-count N`，成功返回 0，目录缺失、frontmatter 名称不一致或数量错误时返回非 0；能力矩阵为后续合并的唯一映射表。

- [ ] **Step 1: 写入会失败的库存验证测试脚本**

创建 `scripts/verify_skill_inventory.py`，使用以下接口和断言：

```python
#!/usr/bin/env python3
import argparse
import pathlib
import re
import sys


def skill_name(skill_file: pathlib.Path) -> str:
    text = skill_file.read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*[\"']?([^\n\"']+)", text)
    if match is None:
        raise ValueError(f"missing name: {skill_file}")
    return match.group(1).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--expected-count", required=True, type=int)
    args = parser.parse_args()
    root = pathlib.Path(args.root)
    entries = sorted(path for path in root.iterdir() if path.is_dir())
    errors = []
    for entry in entries:
        skill_file = entry / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {entry.name}")
            continue
        if skill_name(skill_file) != entry.name:
            errors.append(f"name mismatch: {entry.name}")
    if len(entries) != args.expected_count:
        errors.append(f"expected {args.expected_count}, found {len(entries)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"validated {len(entries)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 2: 运行库存验证并确认目标计数尚未满足**

Run:

```bash
python3 scripts/verify_skill_inventory.py --root skills --expected-count 39
```

Expected: FAIL，输出 `expected 39, found 29`；若同时发现既有 frontmatter 名称问题，将其逐项记录到能力矩阵。

- [ ] **Step 3: 获取并核验只读官方快照**

Run:

```bash
upstream_snapshot=/tmp/stitch-skills-upstream-0337446
if [ ! -d "$upstream_snapshot/.git" ]; then
  test ! -e "$upstream_snapshot"
  git clone --quiet https://github.com/google-labs-code/stitch-skills.git "$upstream_snapshot"
fi
git -C "$upstream_snapshot" checkout --quiet 0337446dadde6f8c94210444e2aa9d546126480f
test "$(git -C "$upstream_snapshot" rev-parse HEAD)" = "0337446dadde6f8c94210444e2aa9d546126480f"
find "$upstream_snapshot/plugins" -path '*/skills/*/SKILL.md' -print | sort
```

Expected: PASS，并列出 16 个官方 `SKILL.md`。

- [ ] **Step 4: 写入上游记录与完整能力矩阵**

`docs/upstream/google-stitch-skills-0337446.md` 必须记录仓库 URL、完整 SHA、Apache-2.0、抓取日期和 16 个路径。`docs/upstream/stitch-skills-capability-matrix.md` 必须包含本地 29 项与官方 16 项，并采用以下确定映射：

```text
UPSTREAM_ONLY -> stitch-code-to-design
UPSTREAM_ONLY -> stitch-extract-design-md
UPSTREAM_ONLY -> stitch-extract-static-html
UPSTREAM_ONLY -> stitch-manage-design-system
UPSTREAM_ONLY -> stitch-upload-to-stitch
UPSTREAM_ONLY -> stitch-react-native
UPSTREAM_ONLY -> stitch-react-vite-dashboard
UPSTREAM_ONLY -> stitch-site-md
UPSTREAM_ONLY -> stitch-loop
UPSTREAM_ONLY -> stitch-taste-design
OVERLAP_MERGED react-components -> stitch-react-components
OVERLAP_MERGED remotion -> stitch-remotion
OVERLAP_MERGED shadcn-ui -> stitch-shadcn-ui
OVERLAP_MERGED generate-design -> stitch-ui-designer + stitch-ui-prompt-architect
OVERLAP_MERGED design-md -> stitch-design-md
OVERLAP_MERGED enhance-prompt -> stitch-ui-prompt-architect
```

本地其余 23 个 Skill 标为 `LOCAL_ONLY`，矩阵不得出现未分类行。

- [ ] **Step 5: 验证文档记录与官方计数**

Run:

```bash
test "$(rg -c '^\| `plugins/.+/SKILL.md` \|' docs/upstream/google-stitch-skills-0337446.md)" -eq 16
rg -n 'LOCAL_ONLY|UPSTREAM_ONLY|OVERLAP_MERGED' docs/upstream/stitch-skills-capability-matrix.md
git diff --check
```

Expected: PASS；官方表 16 行，能力矩阵无空状态。

- [ ] **Step 6: 提交能力基线**

```bash
git add docs/upstream scripts/verify_skill_inventory.py
git commit -m "docs: establish Stitch skills union baseline"
```

---

### Task 2: 引入 10 个官方独有 Skills

**Files:**
- Create: `skills/stitch-code-to-design/**`
- Create: `skills/stitch-extract-design-md/**`
- Create: `skills/stitch-extract-static-html/**`
- Create: `skills/stitch-manage-design-system/**`
- Create: `skills/stitch-upload-to-stitch/**`
- Create: `skills/stitch-react-native/**`
- Create: `skills/stitch-react-vite-dashboard/**`
- Create: `skills/stitch-site-md/**`
- Create: `skills/stitch-loop/**`
- Create: `skills/stitch-taste-design/**`
- Create: `NOTICE`
- Test: `scripts/verify_skill_inventory.py`

**Interfaces:**
- Consumes: Task 1 的官方只读快照和能力矩阵。
- Produces: 10 个使用 `stitch-*` 规范名称的独立 Skills；`NOTICE` 记录 Google 上游来源与 SHA。

- [ ] **Step 1: 复制官方独有能力及其完整伴随资源**

重新绑定并核验 Task 1 的只读快照，然后执行明确映射；不复制三个上游插件 manifest：

```bash
upstream_snapshot=/tmp/stitch-skills-upstream-0337446
test "$(git -C "$upstream_snapshot" rev-parse HEAD)" = "0337446dadde6f8c94210444e2aa9d546126480f"
cp -R "$upstream_snapshot/plugins/stitch-design/skills/code-to-design" skills/stitch-code-to-design
cp -R "$upstream_snapshot/plugins/stitch-design/skills/extract-design-md" skills/stitch-extract-design-md
cp -R "$upstream_snapshot/plugins/stitch-design/skills/extract-static-html" skills/stitch-extract-static-html
cp -R "$upstream_snapshot/plugins/stitch-design/skills/manage-design-system" skills/stitch-manage-design-system
cp -R "$upstream_snapshot/plugins/stitch-design/skills/upload-to-stitch" skills/stitch-upload-to-stitch
cp -R "$upstream_snapshot/plugins/stitch-build/skills/react-native" skills/stitch-react-native
cp -R "$upstream_snapshot/plugins/stitch-build/skills/react-vite-dashboard" skills/stitch-react-vite-dashboard
cp -R "$upstream_snapshot/plugins/stitch-utilities/skills/site-md" skills/stitch-site-md
cp -R "$upstream_snapshot/plugins/stitch-utilities/skills/stitch-loop" skills/stitch-loop
cp -R "$upstream_snapshot/plugins/stitch-utilities/skills/taste-design" skills/stitch-taste-design
```

- [ ] **Step 2: 先运行名称验证并确认复制后的 frontmatter 不合格**

Run:

```bash
python3 scripts/verify_skill_inventory.py --root skills --expected-count 39
```

Expected: FAIL，列出官方原名与 `stitch-*` 目录名不一致的项。

- [ ] **Step 3: 规范化新 Skill 名称与依赖引用**

逐个将 `SKILL.md` frontmatter `name` 改为目录名，并把内部依赖改成最终规范名称：

```text
code-to-design -> stitch-code-to-design
extract-design-md -> stitch-extract-design-md
extract-static-html -> stitch-extract-static-html
manage-design-system -> stitch-manage-design-system
upload-to-stitch -> stitch-upload-to-stitch
react-native -> stitch-react-native
react-vite-dashboard -> stitch-react-vite-dashboard
site-md -> stitch-site-md
stitch-loop -> stitch-loop
taste-design -> stitch-taste-design
```

引用既有能力时使用 `stitch-ui-prompt-architect`、`stitch-design-md`、`stitch-react-components` 等本地规范名称，不保留不可发现的官方短名依赖。

- [ ] **Step 4: 写入许可证归属**

`NOTICE` 使用以下内容并保留根 `LICENSE`：

```text
This distribution includes material adapted from google-labs-code/stitch-skills,
commit 0337446dadde6f8c94210444e2aa9d546126480f.
Copyright Google LLC. Licensed under the Apache License, Version 2.0.

Original and additional Stitch skills are maintained by Full Stack Skills / PartMe.AI.
See LICENSE for the complete Apache License, Version 2.0 text.
```

- [ ] **Step 5: 运行库存验证**

Run:

```bash
python3 scripts/verify_skill_inventory.py --root skills --expected-count 39
git diff --check
```

Expected: PASS，输出 `validated 39 skills`。

- [ ] **Step 6: 提交官方独有能力**

```bash
git add NOTICE skills/stitch-code-to-design skills/stitch-extract-design-md skills/stitch-extract-static-html skills/stitch-manage-design-system skills/stitch-upload-to-stitch skills/stitch-react-native skills/stitch-react-vite-dashboard skills/stitch-site-md skills/stitch-loop skills/stitch-taste-design
git commit -m "feat: add official-only Stitch skills"
```

---

### Task 3: 融合 6 组重叠能力并消除触发冲突

**Files:**
- Modify: `skills/stitch-react-components/**`
- Modify: `skills/stitch-remotion/**`
- Modify: `skills/stitch-shadcn-ui/**`
- Modify: `skills/stitch-design-md/**`
- Modify: `skills/stitch-ui-designer/**`
- Modify: `skills/stitch-ui-prompt-architect/**`
- Modify: `docs/upstream/stitch-skills-capability-matrix.md`
- Test: all six canonical `SKILL.md` files and their referenced resources

**Interfaces:**
- Consumes: 官方 `react-components`、`remotion`、`shadcn-ui`、`generate-design`、`design-md`、`enhance-prompt`。
- Produces: 六个本地规范入口；每个入口包含双方非重复流程，并在矩阵中列出吸收的官方文件。

- [ ] **Step 1: 生成逐文件差异证据**

Run:

```bash
upstream_snapshot=/tmp/stitch-skills-upstream-0337446
test "$(git -C "$upstream_snapshot" rev-parse HEAD)" = "0337446dadde6f8c94210444e2aa9d546126480f"
diff -ru skills/stitch-react-components "$upstream_snapshot/plugins/stitch-build/skills/react-components" || true
diff -ru skills/stitch-remotion "$upstream_snapshot/plugins/stitch-build/skills/remotion" || true
diff -ru skills/stitch-shadcn-ui "$upstream_snapshot/plugins/stitch-build/skills/shadcn-ui" || true
diff -ru skills/stitch-design-md "$upstream_snapshot/plugins/stitch-utilities/skills/design-md" || true
diff -u skills/stitch-ui-designer/SKILL.md "$upstream_snapshot/plugins/stitch-design/skills/generate-design/SKILL.md" || true
diff -u skills/stitch-ui-prompt-architect/SKILL.md "$upstream_snapshot/plugins/stitch-utilities/skills/enhance-prompt/SKILL.md" || true
```

Expected: 每组都产生可审阅差异；差异只作为合并输入，不直接覆盖本地文件。

- [ ] **Step 2: 为融合后的触发边界写失败检查**

Run:

```bash
rg -n '^name: (react-components|remotion|shadcn-ui|generate-design|design-md|enhance-prompt)$' skills
```

Expected: 当前新增目录已经规范化，因此无输出；随后人工检查六个本地 description，若同一用户意图同时出现在两个入口中，将该意图记录为待修复的冲突。

- [ ] **Step 3: 融合构建类资源**

将官方独有的验证脚本、模板、API 参考和示例分别放入对应本地目录；同名文件内容不同时，以本地文件为主文件，并把官方新增规则合入同一文件。三个规范入口必须保持如下职责：

```text
stitch-react-components: Stitch HTML -> Vite/React 组件与验证
stitch-remotion: Stitch 屏幕资产 -> Remotion walkthrough
stitch-shadcn-ui: Stitch/shadcn 组件选择、迁移与验证
```

所有 `SKILL.md` 必须明确使用 Stitch MCP `get_screen`/`list_screens` 获取资产，禁止假定本地已有 HTML。

- [ ] **Step 4: 融合设计类流程**

规范入口职责固定为：

```text
stitch-design-md: 从现有设计或代码提取和校验 DESIGN.md
stitch-ui-prompt-architect: 把模糊需求增强为含 Context/Layout/Components 的生成提示
stitch-ui-designer: 端到端设计编排，调用 prompt architect 后再调用 Stitch MCP
```

从官方 `generate-design` 吸收设备、设计系统、生成和结果验证规则；从官方 `enhance-prompt` 吸收平台、编号区块、颜色角色和具体 UI 文案规则；从官方 `design-md` 吸收 DESIGN.md 结构与 lint 约束。不得创建新的重叠入口。

- [ ] **Step 5: 更新能力矩阵的融合证据**

每个 `OVERLAP_MERGED` 行增加：规范入口、吸收的官方目录、保留的脚本/资源、触发边界和验证命令。六行均不得使用“同上”等省略描述。

- [ ] **Step 6: 验证重叠入口与引用**

Run:

```bash
python3 scripts/verify_skill_inventory.py --root skills --expected-count 39
rg -n '^name: (react-components|remotion|shadcn-ui|generate-design|design-md|enhance-prompt)$' skills && exit 1 || true
rg -n 'code-to-design|extract-design-md|extract-static-html|manage-design-system|upload-to-stitch|react-native|react-vite-dashboard|site-md|taste-design' skills --glob 'SKILL.md'
git diff --check
```

Expected: 库存 PASS；不存在官方短名 frontmatter；所有依赖指向可发现的最终名称。

- [ ] **Step 7: 提交重叠能力融合**

```bash
git add skills/stitch-react-components skills/stitch-remotion skills/stitch-shadcn-ui skills/stitch-design-md skills/stitch-ui-designer skills/stitch-ui-prompt-architect docs/upstream/stitch-skills-capability-matrix.md
git commit -m "feat: merge upstream Stitch workflows"
```

---

### Task 4: 补齐远程 MCP 操作边界与库文档

**Files:**
- Modify: `skills/stitch-ui-designer/SKILL.md`
- Modify: `skills/stitch-mcp-generate-screen-from-text/SKILL.md`
- Modify: `README.md`
- Modify: `README.zh-CN.md`
- Modify: `stitch-skills.md`
- Test: documentation inventory and unsafe retry scan

**Interfaces:**
- Consumes: 39 个最终 Skills 和官方 Stitch MCP 写操作语义。
- Produces: 单一端到端入口、无重复写重试规则、准确的 39 项索引。

- [ ] **Step 1: 写入文档失败断言**

Run:

```bash
rg -n '28 skills|28 个技能|Skills \(28\)|技能列表 \(28\)' README.md README.zh-CN.md stitch-skills.md
```

Expected: FAIL，命中旧计数。

- [ ] **Step 2: 固化写操作恢复规则**

在 `stitch-ui-designer` 和 `stitch-mcp-generate-screen-from-text` 中明确：`generate_screen_from_text`、`edit_screens`、`generate_variants` 超时或连接中断后，不再次提交同一写调用；先调用 `get_project`、`list_screens`、`get_screen` 查询实际状态。删除项目必须在动作发生前获得用户明确确认。

- [ ] **Step 3: 更新三个索引到 39 项**

README 英文、中文和 `stitch-skills.md` 均列出 39 个规范名称；新增官方来源、固定 SHA、NOTICE、远程 MCP 配置和 `STITCH_API_KEY` 安全说明。README 中的安装示例继续指向本地仓库产品，不声称 Google 官方背书。

- [ ] **Step 4: 验证索引与安全文案**

Run:

```bash
python3 scripts/verify_skill_inventory.py --root skills --expected-count 39
test "$(rg -c '^\| `stitch-[^`]+` \|' README.zh-CN.md)" -eq 39
test "$(rg -c '^\| `stitch-[^`]+` \|' README.md)" -eq 39
rg -n 'STITCH_API_KEY|X-Goog-Api-Key|0337446dadde6f8c94210444e2aa9d546126480f' README.md README.zh-CN.md
git diff --check
```

Expected: PASS；两个 README 各有 39 个 Skill 表格行。

- [ ] **Step 5: 提交远程 MCP 边界与文档**

```bash
git add skills/stitch-ui-designer/SKILL.md skills/stitch-mcp-generate-screen-from-text/SKILL.md README.md README.zh-CN.md stitch-skills.md
git commit -m "docs: align Stitch skill inventory and MCP safety"
```

---

### Task 5: 执行 Skill 规范、脚本和 TRACE 门禁

**Files:**
- Modify: only files identified by validation failures under `skills/`
- Test: every `skills/*/SKILL.md`, referenced local paths, `.sh`, `.py`, `.js`, `.mjs`, `.ts`

**Interfaces:**
- Consumes: Task 4 的 39 个 Skills。
- Produces: 全量 quick validation、路径检查、脚本语法检查和逐 Skill TRACE 结果。

- [ ] **Step 1: 对 39 个 Skills 运行 quick validation**

Run:

```bash
for skill_dir in skills/*; do
  python3 /Users/wandl/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_dir"
done
```

Expected: 全部退出码为 0；任何失败先按错误修正，再重新运行全量循环。

- [ ] **Step 2: 校验所有 Markdown 相对引用**

运行一个只读 Python 检查，从每个 `SKILL.md` 提取 Markdown 相对链接，忽略 `http://`、`https://` 和锚点，确认目标存在；任何缺失路径都必须修正为真实文件或删除无效引用。随后再次运行 quick validation。

- [ ] **Step 3: 校验伴随脚本语法**

Run:

```bash
find skills -type f -name '*.sh' -print0 | xargs -0 -n1 bash -n
find skills -type f -name '*.py' -print0 | xargs -0 -n1 python3 -m py_compile
find skills -type f \( -name '*.js' -o -name '*.mjs' \) -print0 | xargs -0 -n1 node --check
if find skills -type f -name '*.ts' -print -quit | grep -q .; then
  command -v tsc
  tsc --noEmit --allowJs false --skipLibCheck --target ES2022 $(find skills -type f -name '*.ts' -print)
fi
```

Expected: 所有实际存在的脚本通过。若没有 `.ts` 文件则跳过 TypeScript 检查；若存在 `.ts` 但本机没有 `tsc`，明确记录工具缺失并停止该门禁，不得静默安装编译器或项目依赖。

- [ ] **Step 4: 对新增和修改 Skills 执行 TRACE 检查**

逐个调用 `skill-trace-checker`，至少覆盖 Task 2 的 10 个新 Skill和 Task 3/4 修改的 6 个规范入口。每个结果必须达到该 Skill 定义的通过门槛；失败项按 T/R/A/C/E 反馈修复并重新评测。

- [ ] **Step 5: 运行仓库级最终门禁**

Run:

```bash
python3 scripts/verify_skill_inventory.py --root skills --expected-count 39
rg -n 'AIza[0-9A-Za-z_-]{20,}' . --hidden --glob '!.git/**' && exit 1 || true
git diff --check
git status --short
```

Expected: 39 个 Skills 通过；密钥扫描无结果；只有当前任务文件发生变化。

- [ ] **Step 6: 提交验证修正**

```bash
git add skills README.md README.zh-CN.md stitch-skills.md docs scripts NOTICE
git commit -m "test: validate unified Stitch skill library"
```

---

### Task 6: 创建个人 Codex 插件骨架与 marketplace 条目

**Files:**
- Create: `/Users/wandl/plugins/stitch/.codex-plugin/plugin.json`
- Create: `/Users/wandl/plugins/stitch/.mcp.json`
- Create: `/Users/wandl/plugins/stitch/skills/`
- Create: `/Users/wandl/plugins/stitch/assets/`
- Modify or Create: `/Users/wandl/.agents/plugins/marketplace.json`
- Test: `/Users/wandl/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py`

**Interfaces:**
- Consumes: plugin-creator scaffold；Task 5 的已验证技能库。
- Produces: marketplace 可发现的 `/Users/wandl/plugins/stitch` 插件骨架。

- [ ] **Step 1: 检查目标与 marketplace，确认不会覆盖**

Run:

```bash
test ! -e /Users/wandl/plugins/stitch
python3 /Users/wandl/.codex/skills/.system/plugin-creator/scripts/read_marketplace_name.py
```

Expected: 插件路径不存在；marketplace 名称输出 `personal`。如果路径已存在，停止新建流程并改用 plugin-creator 的既有插件更新流程，不使用 `--force`。

- [ ] **Step 2: 使用官方脚手架创建所需结构和 marketplace 条目**

Run:

```bash
cd /Users/wandl/.codex/skills/.system/plugin-creator
python3 scripts/create_basic_plugin.py stitch --with-skills --with-assets --with-mcp --with-marketplace
```

Expected: 创建 `/Users/wandl/plugins/stitch`；marketplace 追加 `stitch`，策略包含 `AVAILABLE`、`ON_INSTALL` 和 `Productivity`。

- [ ] **Step 3: 验证未定制骨架可被解析**

Run:

```bash
python3 /Users/wandl/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/wandl/plugins/stitch
```

Expected: PASS；这是骨架基线，不代表功能交付完成。

---

### Task 7: 配置 MCP、复制技能快照并完善插件元数据

**Files:**
- Modify: `/Users/wandl/plugins/stitch/.codex-plugin/plugin.json`
- Modify: `/Users/wandl/plugins/stitch/.mcp.json`
- Create: `/Users/wandl/plugins/stitch/README.md`
- Create: `/Users/wandl/plugins/stitch/LICENSE`
- Create: `/Users/wandl/plugins/stitch/NOTICE`
- Create: `/Users/wandl/plugins/stitch/skills/**`
- Test: plugin validator and skill validators

**Interfaces:**
- Consumes: Task 5 的 39 个 Skills；Task 6 插件骨架。
- Produces: 可安装、可分享、无明文密钥的 `stitch` v0.1.0 插件。

- [ ] **Step 1: 写入远程 MCP 配置**

`.mcp.json` 使用 Codex 远程 MCP 环境请求头映射：

```json
{
  "mcpServers": {
    "stitch": {
      "type": "http",
      "url": "https://stitch.googleapis.com/mcp",
      "env_http_headers": {
        "X-Goog-Api-Key": "STITCH_API_KEY"
      }
    }
  }
}
```

该结构必须由当前 plugin validator 和安装后的 Codex MCP 加载共同验证；不得回退到把真实值放入 `http_headers`。

- [ ] **Step 2: 复制已验证技能快照**

Run:

```bash
cp -R /Users/wandl/workspaces/workspace-agent-skills/full-stack-skills-repositories/stitch-skills/skills/. /Users/wandl/plugins/stitch/skills/
cp /Users/wandl/workspaces/workspace-agent-skills/full-stack-skills-repositories/stitch-skills/LICENSE /Users/wandl/plugins/stitch/LICENSE
cp /Users/wandl/workspaces/workspace-agent-skills/full-stack-skills-repositories/stitch-skills/NOTICE /Users/wandl/plugins/stitch/NOTICE
```

Expected: 插件包含 39 个独立 Skill 目录，没有符号链接。

- [ ] **Step 3: 完善插件 manifest**

`plugin.json` 使用以下确定元数据；不声明不存在的 `.app.json`、hooks、logo 或 screenshots：

```json
{
  "name": "stitch",
  "version": "0.1.0",
  "description": "Google Stitch design and design-to-code workflows powered by the remote Stitch MCP server.",
  "author": {
    "name": "Full Stack Skills / PartMe.AI",
    "url": "https://github.com/full-stack-skills/stitch-skills"
  },
  "homepage": "https://github.com/full-stack-skills/stitch-skills",
  "repository": "https://github.com/full-stack-skills/stitch-skills",
  "license": "Apache-2.0",
  "keywords": ["stitch", "design", "mcp", "design-to-code", "ui-generation"],
  "skills": "./skills/",
  "mcpServers": "./.mcp.json",
  "interface": {
    "displayName": "Stitch",
    "shortDescription": "Design and build with Google Stitch",
    "longDescription": "Operate Google Stitch from Codex: generate and edit screens, manage design systems, run code-to-design workflows, and turn Stitch artifacts into frontend components.",
    "developerName": "Full Stack Skills / PartMe.AI",
    "category": "Creativity",
    "capabilities": ["Interactive", "Read", "Write"],
    "websiteURL": "https://stitch.withgoogle.com",
    "defaultPrompt": [
      "Create a responsive product screen in Stitch",
      "Edit my Stitch screen and preserve its design system",
      "Turn this Stitch design into production components"
    ],
    "brandColor": "#1A73E8",
    "screenshots": []
  }
}
```

- [ ] **Step 4: 编写插件 README**

README 必须包含：设置 `STITCH_API_KEY`、在 Stitch Settings 创建和吊销密钥、重启 Codex/新建任务、只读连接验证、39 个 Skills 的来源、官方 SHA、超时后查询而非重试写操作，以及不回显密钥的故障排查命令：

```bash
test -n "$STITCH_API_KEY" && echo "STITCH_API_KEY is set" || echo "STITCH_API_KEY is not set"
```

- [ ] **Step 5: 运行插件与 Skill 全量验证**

Run:

```bash
python3 /Users/wandl/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/wandl/plugins/stitch
python3 /Users/wandl/workspaces/workspace-agent-skills/full-stack-skills-repositories/stitch-skills/scripts/verify_skill_inventory.py --root /Users/wandl/plugins/stitch/skills --expected-count 39
for skill_dir in /Users/wandl/plugins/stitch/skills/*; do
  python3 /Users/wandl/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill_dir"
done
rg -n 'AIza[0-9A-Za-z_-]{20,}' /Users/wandl/plugins/stitch --hidden && exit 1 || true
jq -e '.mcpServers.stitch.env_http_headers["X-Goog-Api-Key"] == "STITCH_API_KEY"' /Users/wandl/plugins/stitch/.mcp.json
```

Expected: plugin validator、39 项库存和全部 Skill 均 PASS；密钥扫描无结果。

---

### Task 8: 安装插件并验证只读 MCP 连接

**Files:**
- Modify: Codex 本地插件安装缓存（由 `codex plugin add` 管理）
- Test: `codex plugin list` and Stitch MCP `list_projects`

**Interfaces:**
- Consumes: marketplace `personal` 中的 `stitch` 条目和用户环境变量 `STITCH_API_KEY`。
- Produces: Codex 中可发现的 Stitch Skills 与 `mcp__stitch__*` 工具。

- [ ] **Step 1: 安装个人 marketplace 插件**

Run:

```bash
marketplace_name=$(python3 /Users/wandl/.codex/skills/.system/plugin-creator/scripts/read_marketplace_name.py)
test "$marketplace_name" = "personal"
codex plugin add "stitch@$marketplace_name"
codex plugin list
```

Expected: `stitch@personal` 显示为已安装。默认个人 marketplace 不执行 `codex plugin marketplace add`。

- [ ] **Step 2: 检查环境变量而不读取其值**

Run:

```bash
test -n "$STITCH_API_KEY"
```

Expected: 用户已配置时返回 0；未配置时停止真实连接验证并报告唯一剩余步骤，不读取或打印密钥。

- [ ] **Step 3: 在新的 Codex 任务中验证 MCP 工具发现**

新建任务后请求“列出我的 Stitch 项目”，确认实际调用 `mcp__stitch__list_projects`。成功结果可以是项目列表或空列表；`Unauthenticated`、工具不可发现或使用了旧全局配置均不算通过。

- [ ] **Step 4: 验证无密钥错误路径**

在不暴露真实值的隔离进程中临时取消 `STITCH_API_KEY`，确认插件给出缺少环境变量的可操作提示，且错误文本不包含其他凭据或现有 Codex 配置内容。

- [ ] **Step 5: 最终验收记录**

在本地技能仓库新增 `docs/verification/2026-09-11-stitch-plugin-verification.md`，记录以下证据：本地 HEAD、39 项库存、quick validation、TRACE 汇总、插件 validator、marketplace 名称、插件版本、MCP 工具发现以及 `list_projects` 的成功/阻塞状态。不得记录项目私有内容或 API Key。

- [ ] **Step 6: 提交验收记录**

```bash
git add docs/verification/2026-09-11-stitch-plugin-verification.md
git commit -m "docs: record Stitch plugin verification"
```

---

## Completion Gate

只有同时满足以下条件才能宣称完成：

```text
local_skill_count = 39
unclassified_capabilities = 0
quick_validation_failures = 0
trace_failures = 0
plugin_validation = PASS
plaintext_secret_matches = 0
marketplace_plugin = stitch@personal
mcp_tool_discovery = PASS
list_projects = PASS or BLOCKED_ONLY_BY_MISSING_USER_ENV
```

如果仅缺少用户尚未配置的 `STITCH_API_KEY`，可以声明文件与安装交付完成，但必须将在线连接验收标记为阻塞，不得表述为已验证可用。
