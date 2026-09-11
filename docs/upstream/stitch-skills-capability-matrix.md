# Stitch Skills 能力矩阵

本矩阵是本地 29 项 Skill 与官方快照 16 项 Skill 后续合并的唯一映射表。`UPSTREAM_ONLY` 行给出拟新增的本地 Skill 名，`OVERLAP_MERGED` 行给出承接官方能力的既有本地 Skill；所有未与官方重叠的既有 Skill 均标为 `LOCAL_ONLY`。

| 状态 | 官方 Skill | 本地 Skill / 规范入口 | 吸收的官方目录（快照 0337446） | 保留/融合的脚本与资源 | 触发边界 | 验证命令 |
| --- | --- | --- | --- | --- | --- | --- |
| `UPSTREAM_ONLY` | `code-to-design` | `stitch-code-to-design` |
| `UPSTREAM_ONLY` | `extract-design-md` | `stitch-extract-design-md` |
| `UPSTREAM_ONLY` | `extract-static-html` | `stitch-extract-static-html` |
| `UPSTREAM_ONLY` | `manage-design-system` | `stitch-manage-design-system` |
| `UPSTREAM_ONLY` | `upload-to-stitch` | `stitch-upload-to-stitch` |
| `UPSTREAM_ONLY` | `react-native` | `stitch-react-native` |
| `UPSTREAM_ONLY` | `react-vite-dashboard` | `stitch-react-vite-dashboard` |
| `UPSTREAM_ONLY` | `site-md` | `stitch-site-md` |
| `UPSTREAM_ONLY` | `stitch-loop` | `stitch-loop` |
| `UPSTREAM_ONLY` | `taste-design` | `stitch-taste-design` |
| `OVERLAP_MERGED` | `react-components` | `stitch-react-components` | `plugins/stitch-build/skills/react-components` | 新增 `scripts/validate.js`、package/lock、`resources/stitch-api-reference.md`、`resources/style-guide.json`、`examples/gold-standard-card.tsx`；保留本地 `fetch-stitch.sh`、component-template、architecture-checklist、tailwind-to-react；融合当前 tokens、MCP 同步与路由规则 | Stitch HTML → Vite/React 组件与验证；shadcn 迁移交专门入口，视频交 Remotion | `node skills/stitch-react-components/scripts/validate.js skills/stitch-react-components/examples/gold-standard-card.tsx` |
| `OVERLAP_MERGED` | `remotion` | `stitch-remotion` | `plugins/stitch-build/skills/remotion` | 新增 `scripts/download-stitch-asset.sh`、`resources/screen-slide-template.tsx`、`resources/composition-checklist.md`、`examples/WalkthroughComposition.tsx`；保留本地 screens.json、usage；适配原子下载、转场 siblings/timing/重叠帧与 staticFile | Stitch 屏幕资产 → walkthrough 视频；先 list_screens/get_screen，不承接应用组件构建 | `bash -n skills/stitch-remotion/scripts/download-stitch-asset.sh`；按 SKILL.md 示例核对总帧数并运行目标 Remotion 渲染 |
| `OVERLAP_MERGED` | `shadcn-ui` | `stitch-shadcn-ui` | `plugins/stitch-build/skills/shadcn-ui` | 新增 `scripts/verify-setup.sh`，setup-guide/component-catalog/customization-guide/migration-guide 四份 resources，auth-layout/data-table/form-pattern 三份 TSX examples；保留本地 tailwind-to-shadcn 和 usage | Stitch/shadcn 组件选择、迁移与验证；先 MCP 获取资产，React 初始转换交 stitch-react-components | `bash -n skills/stitch-shadcn-ui/scripts/verify-setup.sh`；在目标 app 运行 `bash <skill-dir>/scripts/verify-setup.sh` 并执行实际 type/lint/视觉检查 |
| `OVERLAP_MERGED` | `generate-design` | `stitch-ui-designer` | `plugins/stitch-design/skills/generate-design` | 新增 `references/design-mappings.md`、`references/prompt-keywords.md`、`examples/enhanced-prompt.md`；保留本地 spec/框架 contract、workflows 和中英文例子；融合设备、项目 designSystem、text/image/edit/variants、outputComponents 与资产验证 | 端到端设计执行；先调用 stitch-ui-prompt-architect 再调用 MCP；prompt-only 请求不直接生成 | `python3 scripts/verify_skill_inventory.py --root skills --expected-count 39`；核对实际工具响应、屏幕资产与模式分流（离线检索不冒充 live MCP） |
| `OVERLAP_MERGED` | `design-md` | `stitch-design-md` | `plugins/stitch-utilities/skills/design-md` | 融合官方 SKILL.md 的五段语义结构及 examples/DESIGN.md 的导航/产品卡模式；保留本地第六段生成契约、URL 解析与 usage；新增本地来源/语义 lint 约束（官方无 lint 脚本） | 从现有设计或代码提取和校验 DESIGN.md；精确 CSS 提取交 stitch-extract-design-md，远程系统维护交 stitch-manage-design-system | `python3 scripts/verify_skill_inventory.py --root skills --expected-count 39`；执行 SKILL.md 的五项人工 lint 并逐条对照来源 |
| `OVERLAP_MERGED` | `enhance-prompt` | `stitch-ui-prompt-architect` | `plugins/stitch-utilities/skills/enhance-prompt` | 保留已包含官方 KEYWORDS 全内容的本地 `references/KEYWORDS.md`；融合 SKILL.md 的平台/编号区块/颜色角色/具体文案与 targeted edit；保留 spec→prompt、六框架 contract、三段统一结构 | 模糊需求或 Design Spec → Context/Layout/Components 提示文本；项目级系统的新屏提示不重复 tokens，精确 edit 可带请求的颜色值 | `python3 scripts/verify_skill_inventory.py --root skills --expected-count 39`；按 SKILL.md output validation 检查两个输入路径与系统/inline/edit 三种模式 |
| `LOCAL_ONLY` | — | `stitch-mcp-create-project` |
| `LOCAL_ONLY` | — | `stitch-mcp-generate-screen-from-text` |
| `LOCAL_ONLY` | — | `stitch-mcp-get-project` |
| `LOCAL_ONLY` | — | `stitch-mcp-get-screen` |
| `LOCAL_ONLY` | — | `stitch-mcp-list-projects` |
| `LOCAL_ONLY` | — | `stitch-mcp-list-screens` |
| `LOCAL_ONLY` | — | `stitch-skill-creator` |
| `LOCAL_ONLY` | — | `stitch-ued-guide` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-bootstrap` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-element-plus` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-generator` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-layui` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-uview` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-uviewpro` |
| `LOCAL_ONLY` | — | `stitch-ui-design-spec-vant` |
| `LOCAL_ONLY` | — | `stitch-ui-design-variants` |
| `LOCAL_ONLY` | — | `stitch-uview-components` |
| `LOCAL_ONLY` | — | `stitch-uview-plus-components` |
| `LOCAL_ONLY` | — | `stitch-uviewpro-components` |
| `LOCAL_ONLY` | — | `stitch-vue-bootstrap-components` |
| `LOCAL_ONLY` | — | `stitch-vue-element-components` |
| `LOCAL_ONLY` | — | `stitch-vue-layui-components` |
| `LOCAL_ONLY` | — | `stitch-vue-vant-components` |
