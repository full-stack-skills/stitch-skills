<div align="center">

# stitch-skills

**Stitch MCP UI design skills — screen generation, components, design systems**

[![GitHub](https://img.shields.io/badge/github-full--stack--skills%2Fstitch-skills-green.svg)](https://github.com/full-stack-skills/stitch-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io)

English | [简体中文](./README.zh-CN.md)

[Introduction](#-introduction) ·
[Install](#-install) ·
[Skills](#-skills) ·
[Supported Agents](#-supported-agents) ·
[Ecosystem](#-ecosystem)

</div>

---

## 📖 Introduction

**Stitch MCP Skills** is a curated collection of Agent Skills for AI coding agents, part of the [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) ecosystem maintained by [PartMe.AI](https://github.com/partme-ai).

This package includes **39 skills**. Each skill is a self-contained `SKILL.md` file that AI agents load on-demand. It is a PartMe.AI-maintained local product that combines the existing library with selected material from Google Labs' `google-labs-code/stitch-skills` snapshot `0337446dadde6f8c94210444e2aa9d546126480f`; this does not imply Google endorsement. See [NOTICE](NOTICE) and the [source record](docs/upstream/google-stitch-skills-0337446.md).

## 📦 Install

```bash
npx skills add full-stack-skills/stitch-skills
```

Or install specific skills:

```bash
npx skills add full-stack-skills/stitch-skills --skill <skill-name>
```

### Remote Stitch MCP

Create and rotate an API key in Stitch Settings, export it only in your runtime environment, and reference the variable from the MCP configuration. Never commit or paste the key into configuration, logs, prompts, or issue reports.

```bash
export STITCH_API_KEY="<set-locally>"
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

Restart the agent runtime after setting the variable. Verify connectivity with a read-only project listing before using write tools.

## 🎯 Skills (39)

| Skill | Description |
|-------|-------------|
| `stitch-code-to-design` | Convert an existing frontend application or component into a Stitch design through static extraction, design-system capture, and upload. |
| `stitch-design-md` | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md. Uses Stitch MCP list_projects list_sc... |
| `stitch-extract-design-md` | Extract a DESIGN.md design system from frontend source, styles, themes, and tokens. |
| `stitch-extract-static-html` | Capture a self-contained static HTML representation for sharing or Stitch upload. |
| `stitch-loop` | Iteratively build websites with Stitch using a baton-passing loop. |
| `stitch-manage-design-system` | Retrieve, create, update, and apply Stitch design systems. |
| `stitch-mcp-create-project` | Creates a new Stitch project container. Use this when starting a new design task, app idea, or fresh workspace. |
| `stitch-mcp-generate-screen-from-text` | Generates high-fidelity UI screens or wireframes from text descriptions. The core Text-to-UI engine. |
| `stitch-mcp-get-project` | Retrieves the detailed metadata of a specific Stitch project. |
| `stitch-mcp-get-screen` | Retrieves the full details of a specific screen, including HTML code. |
| `stitch-mcp-list-projects` | Lists all Stitch projects accessible to the user. |
| `stitch-mcp-list-screens` | Lists all screens contained within a specific project. |
| `stitch-react-components` | Convert Stitch designs into modular Vite/React components with validation and design token consistency. Uses Stitch M... |
| `stitch-react-native` | Convert Stitch HTML designs to React Native components or synchronize existing native components. |
| `stitch-react-vite-dashboard` | Convert Stitch designs into production React and Vite dashboards. |
| `stitch-remotion` | Generate walkthrough videos from Stitch projects using Remotion. Retrieves screens via Stitch MCP list_projects list_... |
| `stitch-shadcn-ui` | Expert guidance for integrating and building applications with shadcn/ui. Component discovery, installation npx shadc... |
| `stitch-site-md` | Synthesize project requirements into a SITE.md constitution for the Stitch build loop. |
| `stitch-skill-creator` | "A factory skill for creating new Stitch Scenario Skills. It enforces the \"Design First, Execute Last\" SOP and stan... |
| `stitch-taste-design` | Generate a semantic DESIGN.md that guides premium, non-generic UI decisions. |
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
| `stitch-upload-to-stitch` | Upload local visual assets, HTML pages, or design documents to a Stitch project. |
| `stitch-uview-components` | Convert Stitch designs into uni-app and Vue 2 and uView 2.0 pages and components. Uses Stitch MCP get_screen for retr... |
| `stitch-uview-plus-components` | Convert Stitch designs into uni-app, Vue 3, and uview-plus pages and components. |
| `stitch-uviewpro-components` | Convert Stitch designs into uni-app and Vue 3 and uView Pro pages and components. Uses Stitch MCP get_screen for retr... |
| `stitch-vue-bootstrap-components` | Convert Stitch designs into modular Vite/Vue 3 and BootstrapVue or BootstrapVueNext components. Uses [BootstrapVue Vu... |
| `stitch-vue-element-components` | Convert Stitch designs into modular Vite/Vue 3 and Element Plus components. Uses Stitch MCP get_screen to retrieve de... |
| `stitch-vue-layui-components` | Convert Stitch designs into modular Vite/Vue 3 and Layui-Vue components. Uses Stitch MCP get_screen for retrieval; hi... |
| `stitch-vue-vant-components` | Convert Stitch designs into modular Vite/Vue 3 and Vant 4 mobile components. Uses Stitch MCP get_screen for retrieval... |

## 🤖 Supported Agents

Works with [Claude Code](https://code.claude.com), [Codex](https://developers.openai.com/codex), [Cursor](https://cursor.com), [OpenCode](https://opencode.ai), [Gemini CLI](https://geminicli.com), [GitHub Copilot](https://github.com/features/copilot), [Windsurf](https://codeium.com/windsurf), and [70+ others](https://agentskills.io/clients).

### Claude Code Installation

**Option 1: npx skills CLI (Recommended)**

```bash
npx skills add full-stack-skills/stitch-skills
```

**Option 2: Manual Installation**

```bash
git clone https://github.com/full-stack-skills/stitch-skills.git
cp -r stitch-skills/skills/* .claude/skills/
```

For more details, see the [Claude Code Skills Guide](https://code.claude.com/docs/en/skills) and [Agent Skills Spec](https://agentskills.io/).

## 🌐 Ecosystem

| Resource | Link |
|----------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **All Skill Groups** | [github.com/full-stack-skills](https://github.com/full-stack-skills) |
| **Agent Skills Spec** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE).
