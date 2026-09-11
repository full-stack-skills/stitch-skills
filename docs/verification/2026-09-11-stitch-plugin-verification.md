# Stitch 个人插件安装与只读连接验收

日期：2026-09-11。

## 结论

文件与安装交付完成。`stitch@personal` 已安装并启用，插件 Skills 与 `mcp__stitch__list_projects` 在新的非交互 `codex exec --ephemeral` 进程中可发现。当前调用进程未设置 `STITCH_API_KEY`，因此按验收台账将真实 `list_projects` 标记为 `BLOCKED_ONLY_BY_MISSING_USER_ENV`，不将在线连接表述为已通过。

## 验收证据

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
| Skill 发现 | PASS；新进程从已安装插件缓存加载 `stitch-mcp-list-projects` |
| MCP 工具发现 | PASS；新进程产生 `server=stitch`、`tool=list_projects` 的工具调用事件 |
| `list_projects` | `BLOCKED_ONLY_BY_MISSING_USER_ENV` |

## 在线验证边界

控制端和本任务 shell 均确认 `STITCH_API_KEY` 未设置。验证使用新的非交互、ephemeral `codex exec`，没有创建用户 owned Codex task，也没有读取、搜索、复制或打印任何现有 Codex/其他客户端配置或密钥。

隔离进程分别执行 `env -u STITCH_API_KEY` 和显式 `STITCH_API_KEY=''` 后，`mcp__stitch__list_projects` 仍返回成功。这证明工具可发现并可被调用，但不能证明鉴权来自新插件的环境变量映射，也无法得到预期的“缺少 `STITCH_API_KEY`”可操作错误。由于使用旧全局配置或其他不可见注入来源不算通过，本记录不采信返回内容，不记录项目数量、名称、ID、标题、URL、缩略图或其他私有字段。

用户在 Codex 启动环境中显式配置 `STITCH_API_KEY` 并重启后，应再次从全新任务或进程执行只读 `list_projects`，届时才能把该项改为 PASS。缺失变量错误路径还需要一个能隔离所有非环境凭据注入、同时保留 Codex 登录授权的受支持 CLI/桌面加载方式；当前 CLI 未提供可证明这一点的开关，因此本次不猜测替代配置。

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
list_projects = BLOCKED_ONLY_BY_MISSING_USER_ENV
```
