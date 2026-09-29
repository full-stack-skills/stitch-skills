<div align="center">

# stitch-skills

**Stitch MCP UI design skills — screen generation, components, design systems**

[![GitHub](https://img.shields.io/badge/github-full--stack--skills%2Fstitch-skills-green.svg)](https://github.com/full-stack-skills/stitch-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-兼容-purple.svg)](https://agentskills.io)

[English](./README.md) | 简体中文

[简介](#-简介) ·
[安装](#-安装) ·
[技能列表](#-技能列表) ·
[支持的智能体](#-支持的智能体) ·
[生态](#-生态)

</div>

---

## 📖 简介

**Stitch MCP 技能** 是一组 AI 编码智能体技能，属于 [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) 生态，由 [PartMe.AI](https://github.com/partme-ai) 维护。

本包包含 **45 个技能**。每个技能是一个独立的 `SKILL.md` 文件，AI 智能体按需加载。本产品由 PartMe.AI 维护，在原有本地技能库上融合了 Google Labs `google-labs-code/stitch-skills` 固定快照 `0337446dadde6f8c94210444e2aa9d546126480f` 的部分材料；这不代表 Google 官方背书。来源与许可见 [NOTICE](NOTICE) 和[上游记录](docs/upstream/google-stitch-skills-0337446.md)。

## 📦 安装

```bash
npx skills add full-stack-skills/stitch-skills
```

或按需安装特定技能：

```bash
npx skills add full-stack-skills/stitch-skills --skill <skill-name>
```

### 远程 Stitch MCP

在 Stitch Settings 创建、吊销和轮换 API Key，仅通过运行环境变量注入，并在 MCP 配置中引用变量名。禁止把密钥明文提交到配置、日志、提示词或问题报告中。

```bash
export STITCH_API_KEY="<仅在本机设置>"
```

```json
{
  "mcpServers": {
    "stitch": {
      "url": "https://stitch.googleapis.com/mcp",
      "env_http_headers": {
        "X-Goog-Api-Key": "STITCH_API_KEY"
      }
    }
  }
}
```

设置变量后重启智能体运行时，并先用只读的项目列表调用验证连接，再使用写操作。


### 本地设计规格与提示词

使用 `stitch-design-spec` 统一编制页面合同与提示词。两个旧名称只保留兼容转交，不再各自维护规则。完整包、full-stack-doc 模块文档和 prompt-only 共用同一套规则；本地编写不执行认证检查。模板、来源与案例见 [技能入口](skills/stitch-design-spec/SKILL.md)。

## 🎯 技能列表 (45)

**43 个主要技能 + 2 个兼容入口。** 本地规格和提示词无需配置 Stitch 凭据。

命名约定：上层保留 `stitch-design-spec` / `stitch-design-harness`；具体界面能力使用 `stitch-ui-*`，框架约束使用 `stitch-ui-contract-*`，UI代码转换使用 `stitch-ui-<技术栈>-components`。底层工具保留 `stitch-mcp-*`；总路由、文档和专项操作保留明确的原名。

### 上层入口与交付编排

| Skill | 职责 |
| --- | --- |
| [stitch-design-use](skills/stitch-design-use/SKILL.md) | 总入口：识别任务并路由到具体技能。 |
| [stitch-design-spec](skills/stitch-design-spec/SKILL.md) | 页面合同、交互状态、Stitch 提示词及覆盖与任务映射。 |
| [stitch-design-harness](skills/stitch-design-harness/SKILL.md) | 管理可恢复的设计交付、证据、用户批准与归档。 |

### 具体 UI 设计能力

| Skill | 职责 |
| --- | --- |
| [stitch-ui-execute](skills/stitch-ui-execute/SKILL.md) | 执行 Stitch 屏幕的新建、编辑、导入后编辑与变体生成。 |
| [stitch-ui-style](skills/stitch-ui-style/SKILL.md) | 提出视觉风格、排版、色彩和动效方案，输出 DESIGN.md 提案。 |
| [stitch-ui-guide](skills/stitch-ui-guide/SKILL.md) | 设计表达、UI/UX 词汇和结构指导。 |
| [stitch-ui-preview](skills/stitch-ui-preview/SKILL.md) | 同步切页、主题切换与多设备预览对比，附完整可独立运行代码。 |
| [stitch-ui-variants](skills/stitch-ui-variants/SKILL.md) | 编写设计变体方案与提示词，不直接生成屏幕。 |
| [stitch-ui-loop](skills/stitch-ui-loop/SKILL.md) | 按授权 backlog 有限接力构建页面并交接进度。 |

### 框架设计契约：生成之前

| Skill | 职责 |
| --- | --- |
| [stitch-ui-contract-bootstrap](skills/stitch-ui-contract-bootstrap/SKILL.md) | Bootstrap/Vue 的组件、布局与状态约束。 |
| [stitch-ui-contract-element-plus](skills/stitch-ui-contract-element-plus/SKILL.md) | Element Plus 的组件、布局与状态约束。 |
| [stitch-ui-contract-layui](skills/stitch-ui-contract-layui/SKILL.md) | Layui-Vue 的组件、布局与状态约束。 |
| [stitch-ui-contract-uview2](skills/stitch-ui-contract-uview2/SKILL.md) | uni-app / Vue 2 / uView 2 的设计约束。 |
| [stitch-ui-contract-uviewpro](skills/stitch-ui-contract-uviewpro/SKILL.md) | uni-app / Vue 3 / uView Pro 的设计约束。 |
| [stitch-ui-contract-vant](skills/stitch-ui-contract-vant/SKILL.md) | Vant 4 的组件、布局与状态约束。 |

### 文档与设计系统

| Skill | 职责 |
| --- | --- |
| [stitch-design-md](skills/stitch-design-md/SKILL.md) | 从屏幕、HTML 或截图整理有来源的语义 DESIGN.md。 |
| [stitch-extract-design-md](skills/stitch-extract-design-md/SKILL.md) | 从前端源码、样式和主题提取 DESIGN.md。 |
| [stitch-site-md](skills/stitch-site-md/SKILL.md) | 整理供页面接力使用的 SITE.md、导航和 backlog。 |
| [stitch-manage-design-system](skills/stitch-manage-design-system/SKILL.md) | 查询、创建、更新和应用远程 Stitch 设计系统。 |

### 资产与项目操作

| Skill | 职责 |
| --- | --- |
| [stitch-code-to-design](skills/stitch-code-to-design/SKILL.md) | 将已有前端应用的页面和设计语言迁入 Stitch。 |
| [stitch-extract-static-html](skills/stitch-extract-static-html/SKILL.md) | 提取指定页面状态的静态 HTML 与可获取资产，不自动上传。 |
| [stitch-upload](skills/stitch-upload/SKILL.md) | 上传已授权的图片、HTML 或设计文档。 |
| [stitch-local-setup](skills/stitch-local-setup/SKILL.md) | 本地首次配置与认证故障恢复。 |
| [stitch-delete-project](skills/stitch-delete-project/SKILL.md) | 删除明确指定的远程项目并核对结果。 |

### MCP 底层工具适配

| Skill | 职责 |
| --- | --- |
| [stitch-mcp-create-project](skills/stitch-mcp-create-project/SKILL.md) | 创建 Stitch 项目容器。 |
| [stitch-mcp-generate-screen-from-text](skills/stitch-mcp-generate-screen-from-text/SKILL.md) | 将已准备的提示词提交给文本生成屏幕工具。 |
| [stitch-mcp-get-project](skills/stitch-mcp-get-project/SKILL.md) | 读取指定项目详情。 |
| [stitch-mcp-get-screen](skills/stitch-mcp-get-screen/SKILL.md) | 读取指定屏幕详情与资产。 |
| [stitch-mcp-list-projects](skills/stitch-mcp-list-projects/SKILL.md) | 列出可访问项目。 |
| [stitch-mcp-list-screens](skills/stitch-mcp-list-screens/SKILL.md) | 列出项目内的屏幕。 |

### 代码转换与演示制作：取得设计之后

| Skill | 职责 |
| --- | --- |
| [stitch-ui-react-components](skills/stitch-ui-react-components/SKILL.md) | 将 Stitch 设计转换或同步为 React/Vite 组件。 |
| [stitch-ui-react-native-components](skills/stitch-ui-react-native-components/SKILL.md) | 转换为 React Native 页面与原生组件。 |
| [stitch-ui-react-vite-dashboard](skills/stitch-ui-react-vite-dashboard/SKILL.md) | 实现含表格、筛选与异步状态的 React/Vite 看板。 |
| [stitch-ui-shadcn-components](skills/stitch-ui-shadcn-components/SKILL.md) | 选择、迁移和验证 shadcn/ui 组件与主题。 |
| [stitch-ui-uview2-components](skills/stitch-ui-uview2-components/SKILL.md) | 转换为 uni-app + Vue 2 + uView 2 页面与组件。 |
| [stitch-ui-uview-plus-components](skills/stitch-ui-uview-plus-components/SKILL.md) | 转换为 uni-app + Vue 3 + uview-plus 页面与组件。 |
| [stitch-ui-uviewpro-components](skills/stitch-ui-uviewpro-components/SKILL.md) | 转换为 uni-app + Vue 3 + uView Pro 页面与组件。 |
| [stitch-ui-vue-bootstrap-components](skills/stitch-ui-vue-bootstrap-components/SKILL.md) | 转换为 Vue/Bootstrap 组件，按工程核对具体实现版本。 |
| [stitch-ui-vue-element-plus-components](skills/stitch-ui-vue-element-plus-components/SKILL.md) | 转换为 Vue 3 / Element Plus 页面与组件。 |
| [stitch-ui-vue-layui-components](skills/stitch-ui-vue-layui-components/SKILL.md) | 转换为 Vue 3 / Layui-Vue 页面与组件。 |
| [stitch-ui-vue-vant-components](skills/stitch-ui-vue-vant-components/SKILL.md) | 转换为 Vue 3 / Vant 4 页面与组件。 |
| [stitch-remotion](skills/stitch-remotion/SKILL.md) | 将 Stitch 设计资产制作成 Remotion 走查视频。 |

### 技能开发

| Skill | 职责 |
| --- | --- |
| [stitch-scenario-skill-creator](skills/stitch-scenario-skill-creator/SKILL.md) | 创建指定业务场景的 Stitch 提示词技能。 |

### 旧名称兼容入口

| Skill | 行为 |
| --- | --- |
| [stitch-ui-design-spec-generator](skills/stitch-ui-design-spec-generator/SKILL.md) | 旧规格入口，转交 stitch-design-spec 的 spec-only 路径。 |
| [stitch-ui-prompt-architect](skills/stitch-ui-prompt-architect/SKILL.md) | 旧提示词入口，转交 stitch-design-spec。 |

新任务直接使用 `stitch-design-spec`。其余改名项目见[完整迁移表](docs/skill-name-migration.md)；源码改名不会自动升级已安装副本。

### 如何选择

- 不确定入口：`stitch-design-use`。
- 整理规格或提示词：`stitch-design-spec`。
- 真正生成或修改屏幕：`stitch-ui-execute`；需要完整交付闭环时使用 `stitch-design-harness`。
- 生成前采用 uView 2 约束：`stitch-ui-contract-uview2`；取得设计后生成 uView 2 代码：`stitch-ui-uview2-components`。
- 框架 contract 维护组件约束，最终提示词由 `stitch-design-spec` 编译。设计图符合框架风格不等于已生成可运行代码。

## 🤖 支持的智能体

适用于 [Claude Code](https://code.claude.com)、[Codex](https://developers.openai.com/codex)、[Cursor](https://cursor.com)、[OpenCode](https://opencode.ai)、[Gemini CLI](https://geminicli.com)、[GitHub Copilot](https://github.com/features/copilot)、[Windsurf](https://codeium.com/windsurf) 及 [70+ 其他智能体](https://agentskills.io/clients)。

### Claude Code 安装

**方式一：npx skills CLI（推荐）**

```bash
npx skills add full-stack-skills/stitch-skills
```

**方式二：手动安装**

```bash
git clone https://github.com/full-stack-skills/stitch-skills.git
cp -r stitch-skills/skills/* .claude/skills/
```

更多详情请参阅 [Claude Code 技能指南](https://code.claude.com/docs/en/skills) 和 [Agent Skills 规范](https://agentskills.io/)。

## 🌐 生态

| 资源 | 链接 |
|------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **全部技能组** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills 规范** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 许可证

Apache 2.0 — 详见 [LICENSE](LICENSE)。

来源归属见 [NOTICE](NOTICE)；原有第三方通知及许可正文完整保留于
[THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)，相关组件仍遵循各自许可。
