# 更新日志

本文件自 v1.3.1 起维护；更早版本的发布说明见仓库 git tag 注释（`git tag -n8`）。

## v1.3.1

stitch-design-harness 并入 MCP 代理调用规范。

- `stitch-design-harness` 新增「本地 MCP 代理调用规范」一节：本地 stdio MCP 代理（插件根 `scripts/stitch_mcp_proxy.py`）执行通道、Python 3.11+ 硬要求、`__file__` 脚本路径解析、凭据托管边界、`probe` 就绪探针、无 Playwright/浏览器兜底、付费一次性提交与 `stitch-design-use` 路由纪律。
- 凭据首次配置沿用 `stitch-local-setup` 既有流程，按技能名引用，不重复其正文。
- `.claude-plugin/plugin.json` 版本同步至 1.3.1（v1.2.0、v1.3.0 发版时未同步该字段，本次一并校正）。
- 配套消费方 `stitch-design-plugin` 双 harness 合并：其 plugin-local 的 `stitch-harness` 调用规范技能已删除，有效内容由本版本带回；本版本合并发版后消费方需将 skills 锁定升级至 v1.3.1。
