# 验证记录

## 实现范围

统一入口、两类模板、固定产物合同、模糊输入/规格编译/精确编辑、六框架映射和三种设计系统模式已整合。旧名称及历史资源路径保留兼容转交，活跃调用者改为新入口；注册44个名称，其中2个为旧名适配器。本地规格路由不执行 setup。full-stack-doc 自身和其他仓库未修改。

## 本地证据

- `python3 -m unittest discover -s tests -p "test_design_spec_package.py"`：19项通过。覆盖文件缺失、漏状态、延期说明、错误引用、依赖环、模式证据、三段顺序、模板残留、路径越界、畸形输入和插件注册。
- 校验器最初缺失时测试失败；补充畸形输入用例曾暴露 TypeError，修复后全通过。
- `python3 scripts/lint_skills.py`：44 skills，0 errors。
- `python3 scripts/verify_skill_package.py`：44 skills，0 errors。
- `python3 scripts/verify_skill_inventory.py --root skills --expected-count 44`：通过。
- 完整实例中心夹具：结构校验0错误，2页/14个页面状态/2份提示/3项依赖任务。
- TRACE 使用相邻 agent-skills 仓库评测器，其脚本与 CI 固定提交 91cd3e8e2aafd73d73fc037ce75dee7b6b663ffb 的 diff 为空；44项均达4.5门槛，平均4.600，最低4.54。未改门槛或评测器。
- `OPENSPEC_TELEMETRY=0 openspec validate consolidate-stitch-design-spec --strict --no-interactive`：通过。
- `git diff --check`：通过；新增文档无作者机器绝对路径。示例 manifest 已在 ignore 规则中明确放行，避免只在本机存在。

## 语义审阅

- 实例中心保留字段与70/30结构，增加的状态/返回/跨端规则标为教学建议；危险操作因缺业务合同列为范围外，未冒充完整实例管理功能。
- Agent Browser 保留 J03→G03→P11/P12 与结果未知核对；G03是全局面；仅展开确认提示，其他提示明确待补，不声称24页全覆盖。
- 本地 DESIGN.md 不等于远端已应用；系统模式正文与token分离；编辑只写差值。
- 兼容适配器仅转交，spec-only 与 prompt-only 范围保留；依赖缺失时说明，不自动安装。

## 完成边界

完成本地实现和等价 verify；当前变更保持可审阅，尚未同步至 openspec/specs 或归档。没有执行真实模型多次评测、Stitch生成或视觉验收，不能保证所有模型永远一致。没有安装到任何宿主、没有提交/推送/发布；独立的 harden-skill-release-dispatch 变更未修改。后续如需发布，先按仓库发布流程处理规格同步与版本。

## 后续命名调整验证

用户明确要求后，将技能目录、frontmatter、插件注册、README 和活跃引用改名为 stitch-design-harness；44个技能名称总数不变。design-skills 的提供方 profile 更新为版本4，新运行使用新 handler；历史派发的旧名称仅在文档中明确映射到新入口，不修改运行账本或脚本。该 profile 原被通用 *.json 规则忽略，现单独放行以便提交；其余已忽略文件不在本次修改范围。

验证：Stitch 19项测试、44项 lint/资源校验和 TRACE 门槛通过；design-skills 15项 lint、10项 profile 测试、24项 dispatch 测试通过；新 handler/版本和旧目录消失断言通过；两个仓库 diff --check 通过；OpenSpec 严格验证通过。旧名仅在明确兼容说明中保留。历史任务到真实 Stitch 的执行未实测，没有提交、推送或更新宿主安装副本。

本补充涉及 design-skills 的4项合同/profile文件及定向 ignore 规则，取代上文初始实现记录中的“其他仓库未修改”边界；不改变既有产品需求或提供方交付门禁。

## 全库命名与索引优化验证

- 按 docs/skill-name-migration.md 执行15项目录/frontmatter迁移；既有Harness更名继续有效，两个旧规格入口仍仅为兼容转交。
- 插件 `.claude-plugin/plugin.json`、中英文README和44个实际技能目录一致：42个主要技能+2个兼容入口，每份README各列出44个唯一入口。
- 框架设计契约与代码转换职责在README和契约入口中分开说明；框架token、selector schema、MCP工具名及已存在的场景技能名称规则不变。
- 场景生成器使用新下游名称，并从自身目录复制LICENSE，独立安装无需依赖相邻执行技能。生成到临时目录的真实测试验证了新引用、许可、拒绝覆盖和非法名称无写入。
- 22项测试通过；lint和资源校验均为44项/0错误，inventory通过，TRACE平均4.600、最低4.54（门槛4.5），OpenSpec严格验证和diff --check通过。
- 逐项核对所有迁移目录内原受版本控制的资源：目标文件存在且不被ignore规则排除；扫描活跃技能/脚本/模板无15项旧名残留。两份README与manifest逐项比对无缺漏。
- CI 已更新为执行全部 `test_*.py`；以上仅是本地运行证据，未声称GitHub CI、宿主安装或真实Stitch生成已通过。
- 历史上游快照和既往验证文档保留当时名称；源码包当前名称以README/manifest为准。未增加15个兼容副本，未更新插件缓存、外部消费者或全局技能目录，未提交、推送、发布。

## UI领域前缀修正验证（当前有效命名）

- 保留stitch-design-spec、stitch-design-harness上层入口；22个具体界面能力统一stitch-ui-*。总路由stitch-design-use、文档产物、MCP、上传/设置/视频/技能生成保持现有名字。
- 同步44项插件注册、中英文README、当前库索引、活跃技能及脚本引用、生成器模板。两个旧规格适配器继续单列；迁移文档同时记录最初名称、中间名称和最终名称。
- 迁移前记录的327项资源移动后全部存在。相对于原Git索引检查351项受迁移影响的资源均存在且可被版本控制；React相关5个原有JSON因目录迁移触发ignore，已按文件逐项放行。
- 场景生成器预期改为UI前缀时，先出现预期失败；更新模板后22项测试全通过。lint/资源校验44项0错误，注册44项与两份README逐项一致，文档链接检查0错误，TRACE平均4.600/最低4.54，OpenSpec严格验证和diff --check通过。
- 当前技能中无本轮22个中间名称的活跃引用；历史文档保留原发生时名称，不作为当前路由依据。
- 未修改运行时MCP接口、框架组件标识或提供方协议；未提交/推送/安装/发布，未运行真实Stitch生成或跨模型验收。本节当前命名取代此前分阶段记录，不回写历史验证结果。
