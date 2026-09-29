# 技能命名规范与迁移

当前注册44个名称：42个主要技能、2个旧规格兼容入口。本轮修正的是源码包命名，不是宿主安装更新或发布；包版本未变。

## 最终命名规范

| 层级 | 规则 | 例子 |
| --- | --- | --- |
| 上层设计 | 保留已确认入口 | stitch-design-spec、stitch-design-harness |
| 具体界面能力 | stitch-ui-* | stitch-ui-execute、stitch-ui-style、stitch-ui-guide、stitch-ui-variants、stitch-ui-loop |
| 框架设计约束 | stitch-ui-contract-<框架> | stitch-ui-contract-uview2 |
| UI代码转换 | stitch-ui-<技术栈>-components | stitch-ui-uview2-components、stitch-ui-react-native-components |
| UI专项实现 | stitch-ui-<技术栈>-<场景> | stitch-ui-react-vite-dashboard |
| 底层工具 | stitch-mcp-* | stitch-mcp-get-screen |
| 总路由与专项操作 | 保留明确的操作/产物名称 | stitch-design-use、stitch-design-md、stitch-upload、stitch-local-setup |

contract 约束生成前的设计；components 实现生成后的代码。Remotion走查视频属于演示制作，保留 stitch-remotion。文档提取、设计系统管理、场景技能生成等专项入口也保持原名。

## 原名称到最终名称

中间名指上一轮按职责分组时使用的名称；当前只注册最终名，不新增同能力副本。

| 原名称 | 中间名 | 最终名称 |
| --- | --- | --- |
| `stitch-ui-designer` | `stitch-design-execute` | `stitch-ui-execute` |
| `stitch-ui-design-variants` | `stitch-design-variants` | `stitch-ui-variants` |
| `stitch-loop` | `stitch-design-loop` | `stitch-ui-loop` |
| `stitch-taste-design` | `stitch-design-style` | `stitch-ui-style` |
| `stitch-ued-guide` | `stitch-design-guide` | `stitch-ui-guide` |
| `stitch-ui-design-spec-bootstrap` | `stitch-design-contract-bootstrap` | `stitch-ui-contract-bootstrap` |
| `stitch-ui-design-spec-element-plus` | `stitch-design-contract-element-plus` | `stitch-ui-contract-element-plus` |
| `stitch-ui-design-spec-layui` | `stitch-design-contract-layui` | `stitch-ui-contract-layui` |
| `stitch-ui-design-spec-uview` | `stitch-design-contract-uview2` | `stitch-ui-contract-uview2` |
| `stitch-ui-design-spec-uviewpro` | `stitch-design-contract-uviewpro` | `stitch-ui-contract-uviewpro` |
| `stitch-ui-design-spec-vant` | `stitch-design-contract-vant` | `stitch-ui-contract-vant` |
| `stitch-vue-element-components` | `stitch-vue-element-plus-components` | `stitch-ui-vue-element-plus-components` |
| `stitch-uview-components` | `stitch-uview2-components` | `stitch-ui-uview2-components` |
| `stitch-upload-to-stitch` | — | `stitch-upload` |
| `stitch-skill-creator` | — | `stitch-scenario-skill-creator` |
| `stitch-react-components` | — | `stitch-ui-react-components` |
| `stitch-react-native` | — | `stitch-ui-react-native-components` |
| `stitch-react-vite-dashboard` | — | `stitch-ui-react-vite-dashboard` |
| `stitch-shadcn-ui` | — | `stitch-ui-shadcn-components` |
| `stitch-uview-plus-components` | — | `stitch-ui-uview-plus-components` |
| `stitch-uviewpro-components` | — | `stitch-ui-uviewpro-components` |
| `stitch-vue-bootstrap-components` | — | `stitch-ui-vue-bootstrap-components` |
| `stitch-vue-layui-components` | — | `stitch-ui-vue-layui-components` |
| `stitch-vue-vant-components` | — | `stitch-ui-vue-vant-components` |

此前 stitch-delivery-harness 已更名为 stitch-design-harness，历史派发兼容规则继续有效。原资源、运行时脚本、框架标识、组件前缀、CONTRACT_SELECTION_JSON_V1 及远程MCP工具名不会因技能命名变化而更名。

## 兼容与安装边界

- stitch-ui-design-spec-generator 与 stitch-ui-prompt-architect 仍是两个显式旧名适配器，仅转交 stitch-design-spec；不作为新的UI专业技能推荐。
- 场景生成器仍产出 stitch-ui-<scenario>-designer，属于UI领域命名，保留现有调用兼容。
- 上述其他旧名和中间名不再注册；外部调用、插件分发与已安装副本需在发布升级时同步，源码修改不会自动更新它们。
- 历史快照及既往验证记录保留当时名称；当前有效清单以中英文README和插件manifest为准。
