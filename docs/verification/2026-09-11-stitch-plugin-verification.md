# Stitch 个人插件安装与只读连接验收

日期：2026-09-11。

## 结论

文件与安装交付完成。`stitch@personal` 已安装并启用；正常配置下，新的非交互 `codex exec --ephemeral` 进程可发现 Stitch Skill 与 `mcp__stitch__list_projects`。当前调用进程未设置 `STITCH_API_KEY`，因此按验收台账将真实 `list_projects` 标记为 `BLOCKED_ONLY_BY_MISSING_USER_ENV`，不将在线连接或 MCP 来源表述为已通过验证。

## 初次安装验收证据（Task 8 历史记录）

| 门禁 | 结果 |
| --- | --- |
| 验收前本地 HEAD | `22d1e6fb60c5aa3e113bff68ec59d111b0f12132` |
| 本地 Skill 库存 | 39；`verify_skill_inventory.py` 输出 `validated 39 skills` |
| 未分类能力 | 0 |
| quick validation | 39/39 退出码为 0；失败 0 |
| TRACE | Task 5 严格 checker 覆盖 17 个新增或修改入口，17/17 PASS；失败 0。该结论是已完成的内容门禁，不等同于远程运行可用性 |
| 插件 validator | PASS：`Plugin validation passed: /Users/wandl/plugins/stitch` |
| 明文密钥模式扫描 | 0 个匹配；扫描过程未输出凭据值 |
| marketplace 名称 | `personal` |
| 插件安装 | `stitch@personal`，`installed, enabled`，版本 `0.1.0` |
| Skill 发现 | PASS；正常配置的新进程读取了个人插件缓存中的 `stitch-mcp-list-projects` |
| MCP 工具发现 | PASS；新进程产生 `server=stitch`、`tool=list_projects` 的工具调用事件 |
| 插件 MCP 来源 | `UNVERIFIED`；`--ignore-user-config` 同时禁用了个人插件，无法以该模式证明正常配置下工具来自 `stitch@personal` |
| 缺失环境变量错误路径 | `NOT_OBSERVED`；忽略用户配置时工具不可用，正常配置时 unset/空字符串调用仍成功 |
| `list_projects` | `BLOCKED_ONLY_BY_MISSING_USER_ENV` |

## 在线验证边界

控制端和本任务 shell 均确认 `STITCH_API_KEY` 未设置。验证使用新的非交互、ephemeral `codex exec`，没有创建用户 owned Codex task，也没有读取、搜索、复制或打印任何现有 Codex/其他客户端配置或密钥。

隔离进程分别执行 `env -u STITCH_API_KEY` 和显式 `STITCH_API_KEY=''` 后，`mcp__stitch__list_projects` 仍返回成功。这证明工具可发现并可被调用，但不能证明鉴权来自新插件的环境变量映射，也无法得到预期的“缺少 `STITCH_API_KEY`”可操作错误。由于使用旧全局配置或其他不可见注入来源不算通过，本记录不采信返回内容，不记录项目数量、名称、ID、标题、URL、缩略图或其他私有字段。

补充执行 `env -u STITCH_API_KEY codex exec --ignore-user-config --ephemeral ...`：进程报告 `plugin_loaded=false`、`tool_discovered=false`、`call_succeeded=false`、`error_category=tool_unavailable`，没有执行 Stitch 调用。该模式排除了用户配置，但也禁用了个人插件，所以不能用于证明插件 MCP 来源或环境变量负路径。

后续需要同时满足两类证据：一是在明确受控的 Codex 启动环境中配置 `STITCH_API_KEY` 后，从全新任务或进程验证只读调用；二是使用能够保留 `stitch@personal`、同时隔离其他 MCP/凭据来源的受支持方式验证缺失变量提示。当前 CLI 观察不到满足第二项的隔离模式，因此本次不猜测替代配置。

## 最终审查修复（本轮离线证据）

最终修复说明沿用已批准设计与计划。四项 finding 已修复：远程静态资源在每次连接/重定向前校验字面 IP 与全部 DNS 答案，并绑定到已验证地址；文本和 JSON 诊断去掉 URL 用户信息、查询与片段，停止转发任意浏览器日志/异常；JSX 文本、属性和 CSS raw-text 上下文分别转义；依赖预检和实际执行统一在获准应用 cwd，通过 `scripts/run.mjs` 解析已安装的 tsx/Puppeteer/Babel，缺失时明确停止且不安装。

四项 finding 均记录了 RED 后 GREEN。附加兼容性验证覆盖签名图片 URL、带引号的 inline CSS 与标题中的替换元字符。修复测试只伪造 DNS/网络传输和浏览器 API 边界，未访问公网、未启动浏览器、未调用 Stitch。真实隔离依赖参与 TypeScript 检查，未添加 `any` 模块桩、忽略检查或安装依赖。39 个 Skill 入口和三份许可文件保持不变，39 quick validators、库存与 412 条相对 Markdown 引用通过。

个人插件需使用本轮提交快照同步、验证并按 plugin-creator 的 cachebuster/reinstall 流程刷新；完整提交、版本和最终验证记录保存在本地 SDD `final-fix-report.md`。以上源码和离线测试证据不改变在线验收边界：`plugin_mcp_provenance=UNVERIFIED`、`missing_env_error_path=NOT_OBSERVED`、`list_projects=BLOCKED_ONLY_BY_MISSING_USER_ENV`。

## 完成门禁

```text
local_skill_count = 39
unclassified_capabilities = 0
quick_validation_failures = 0
trace_failures = 0
plugin_validation = PASS
plaintext_secret_matches = 0
marketplace_plugin = stitch@personal
mcp_tool_discovery = PASS
plugin_mcp_provenance = UNVERIFIED
missing_env_error_path = NOT_OBSERVED
list_projects = BLOCKED_ONLY_BY_MISSING_USER_ENV
```

## 2026-09-12 复核附录

本节是事后复核，不修改上面的历史结论，只补充新查明的原因和复验结果。记录中不含任何凭据值。

### 两个未决门禁的根因已查明

`plugin_mcp_provenance=UNVERIFIED` 和 `missing_env_error_path=NOT_OBSERVED` 不是"无法验证"，而是**有效 MCP 定义被同名用户级配置遮蔽**。`codex mcp get stitch` 显示生效定义带有字面 `http_headers: X-Goog-Api-Key=<value>`，且 `env_http_headers: -`；插件的 `.mcp.json` 用的是 `env_http_headers` 且不含 `http_headers`。两者同名 `stitch`，用户级定义胜出。

因此：无论 `STITCH_API_KEY` 是否设置，鉴权都由该字面请求头提供。这同时解释了隔离进程取消环境变量后调用仍成功，以及缺少变量的可操作提示始终观察不到。

无凭据直连验证（只读探测，未使用任何凭据）：`tools/list` 无需凭据即可返回；`tools/call list_projects` 无凭据时返回 `isError: true` 及"Request is missing required authentication credential"。即工具调用确实需要凭据，而当前生效的凭据来自用户级配置而非插件映射。

该字面凭据位于用户自己的 Codex 配置中，属于凭据治理事项：把它改为环境变量后，插件的 `STITCH_API_KEY` 映射才会真正生效。此项需要用户决定，本轮未改动该配置。

### 插件交付形态的变更

方案 Task 6/7 的目标路径 `/Users/wandl/plugins/stitch` 已不存在；实现迁移到公开仓库 `partme-ai/codex-stitch-plugin`（标识 `stitch-design`，v0.3.0，本地目录 `codex-stitch-design-plugin`）。因此个人 marketplace 条目原先指向一个不存在的路径，已修正为实际仓库路径。刷新后 `stitch-design@personal` 的安装缓存已与仓库 HEAD `86bd667` 逐文件一致。

### 离线门禁复验（2026-09-12）

| 门禁 | 结果 |
| --- | --- |
| 本地 Skill 库存 | `validated 39 skills` |
| 上游表行数 | 16 行 |
| 能力矩阵 | UPSTREAM_ONLY 10 + OVERLAP_MERGED 6 + LOCAL_ONLY 23 = 39，无未分类行，融合行均含验证命令 |
| README 索引 | 英文 39 行、中文 39 行；无旧计数残留 |
| quick validation | 39/39 退出码 0 |
| Markdown 相对引用 | 398 条全部可解析，0 死链（本记录原先写作 412 条，计数方法不同，检查本身通过） |
| 脚本语法 | `bash -n`、`py_compile`、`node --check` 全部通过 |
| TypeScript 检查 | 未复现。本机无全局 `tsc`，技能目录未附带类型依赖，`tsc` 仅报缺少 `@types/node` 与 `@babel/*` 声明（TS2307/TS2580）。按方案要求不静默安装依赖，此项标记为工具缺失 |
| 明文密钥扫描 | 0 匹配（仓库内） |
| 插件 validator / 测试 | PASS；`validated 39 skills and compatibility distribution 0.3.0`；5 项测试通过 |
| 技能快照一致性 | 插件 `skills/` 与技能库工作树 `62ef818` 逐文件一致；39 个目录、无符号链接 |

### 本轮新增的阻塞与待决项

- 在线 `list_projects` 复验被账号用量额度挡下（错误类型为用量限额），非鉴权问题；需在额度恢复后重跑。
- 探针 stderr 出现 `rmcp::transport::worker: worker quit with fatal: Unexpected content-type`，无法归因到 `stitch`：直连该端点时 `notifications/initialized` 返回 202 且带 `content-type: application/json`，与其他本地 MCP server 的失败特征不符。
- 技能库分支 `feat/stitch-skills-union-plugin`（`62ef818`）与 `main`（`c46f497`）双向分叉（各 15 / 4 个提交），仅能真实合并，不能快进；是否合并入 main 与是否推送 origin 待用户决定，本轮未动。
