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

本包包含 **43 个技能**。每个技能是一个独立的 `SKILL.md` 文件，AI 智能体按需加载。本产品由 PartMe.AI 维护，在原有本地技能库上融合了 Google Labs `google-labs-code/stitch-skills` 固定快照 `0337446dadde6f8c94210444e2aa9d546126480f` 的部分材料；这不代表 Google 官方背书。来源与许可见 [NOTICE](NOTICE) 和[上游记录](docs/upstream/google-stitch-skills-0337446.md)。

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

## 🎯 技能列表 (43)

| 技能 | 描述 |
|------|------|
| `stitch-code-to-design` | 通过静态页面提取、设计系统提取和上传，将现有前端应用或组件转换为 Stitch 设计。 |
| `stitch-delete-project` | 安全删除一个明确指定的 Stitch 项目；先预览完整资源名并再次取得批准，删除后只读对账。 |
| `stitch-delivery-harness` | 把 Stitch 屏幕变成完整高保真交付：可编辑 HTML、视觉增强、验证、用户批准与可追溯归档。 |
| `stitch-design-md` | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md. Uses Stitch MCP list_projects list_sc... |
| `stitch-design-use` | Stitch Design 根路由：按最窄下游 Skill 分发认证、读取、生成、设计系统、资产处理与交付请求。 |
| `stitch-extract-design-md` | 从前端源码、样式、主题和令牌中提取 DESIGN.md 设计系统。 |
| `stitch-extract-static-html` | 提取可分享或上传至 Stitch 的自包含静态 HTML。 |
| `stitch-loop` | 使用接力循环模式通过 Stitch 迭代构建网站。 |
| `stitch-local-setup` | 本地首次设置 Stitch（获取 STITCH_API_KEY、一次性配置、认证失败恢复）。 |
| `stitch-manage-design-system` | 检索、创建、更新并应用 Stitch 设计系统。 |
| `stitch-mcp-create-project` | Creates a new Stitch project container. Use this when starting a new design task, app idea, or fresh workspace. |
| `stitch-mcp-generate-screen-from-text` | Generates high-fidelity UI screens or wireframes from text descriptions. The core Text-to-UI engine. |
| `stitch-mcp-get-project` | Retrieves the detailed metadata of a specific Stitch project. |
| `stitch-mcp-get-screen` | Retrieves the full details of a specific screen, including HTML code. |
| `stitch-mcp-list-projects` | Lists all Stitch projects accessible to the user. |
| `stitch-mcp-list-screens` | Lists all screens contained within a specific project. |
| `stitch-react-components` | Convert Stitch designs into modular Vite/React components with validation and design token consistency. Uses Stitch M... |
| `stitch-react-native` | 将 Stitch HTML 设计转换为 React Native 组件，或同步已有原生组件。 |
| `stitch-react-vite-dashboard` | 将 Stitch 设计转换为生产级 React 与 Vite 仪表盘。 |
| `stitch-remotion` | Generate walkthrough videos from Stitch projects using Remotion. Retrieves screens via Stitch MCP list_projects list_... |
| `stitch-shadcn-ui` | Expert guidance for integrating and building applications with shadcn/ui. Component discovery, installation npx shadc... |
| `stitch-site-md` | 将项目需求整理为 Stitch 构建循环使用的 SITE.md 项目约章。 |
| `stitch-skill-creator` | "A factory skill for creating new Stitch Scenario Skills. It enforces the \"Design First, Execute Last\" SOP and stan... |
| `stitch-taste-design` | 生成指导高品质、非模板化 UI 决策的语义化 DESIGN.md。 |
| `stitch-ued-guide` | UED guidelines, visual vocabulary, and prompt structure for Stitch. Use when the user asks about layout/style terms, ... |
| `stitch-ui-design-spec-bootstrap` | Bootstrap-Vue design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt. |
| `stitch-ui-design-spec-element-plus` | Element Plus design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt. |
| `stitch-ui-design-spec-generator` | Translates user requirements into structured Design Specs for Theme, Color, and Typography. |
| `stitch-ui-design-spec-layui` | Layui-Vue design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt. |
| `stitch-ui-design-spec-uview` | uView 2 design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt. |
| `stitch-ui-design-spec-uviewpro` | uView Pro design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt. |
| `stitch-ui-design-spec-vant` | Vant 4 design spec for Stitch. Outputs hard-constraints prefix or selector JSON and assembled prompt. |
| `stitch-ui-design-variants` | Logic skill that generates prompts for alternative design variants e.g. A B testing options. |
| `stitch-ui-designer` | The Master Orchestrator. Handles the end-to-end flow of designing and generating UI screens. Use this for all "Design... |
| `stitch-ui-prompt-architect` | Builds Stitch-ready prompts from vague UI ideas or from Design Spec and User Request. Outputs sectioned Context, Layo... |
| `stitch-upload-to-stitch` | 将本地视觉资产、HTML 页面或设计文档上传到 Stitch 项目。 |
| `stitch-uview-components` | Convert Stitch designs into uni-app and Vue 2 and uView 2.0 pages and components. Uses Stitch MCP get_screen for retr... |
| `stitch-uview-plus-components` | 将 Stitch 设计转换为 uni-app、Vue 3 和 uview-plus 页面与组件。 |
| `stitch-uviewpro-components` | Convert Stitch designs into uni-app and Vue 3 and uView Pro pages and components. Uses Stitch MCP get_screen for retr... |
| `stitch-vue-bootstrap-components` | Convert Stitch designs into modular Vite/Vue 3 and BootstrapVue or BootstrapVueNext components. Uses [BootstrapVue Vu... |
| `stitch-vue-element-components` | Convert Stitch designs into modular Vite/Vue 3 and Element Plus components. Uses Stitch MCP get_screen to retrieve de... |
| `stitch-vue-layui-components` | Convert Stitch designs into modular Vite/Vue 3 and Layui-Vue components. Uses Stitch MCP get_screen for retrieval; hi... |
| `stitch-vue-vant-components` | Convert Stitch designs into modular Vite/Vue 3 and Vant 4 mobile components. Uses Stitch MCP get_screen for retrieval... |

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
