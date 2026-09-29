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

This package includes **44 skills**. Each skill is a self-contained `SKILL.md` file that AI agents load on-demand. It is a PartMe.AI-maintained local product that combines the existing library with selected material from Google Labs' `google-labs-code/stitch-skills` snapshot `0337446dadde6f8c94210444e2aa9d546126480f`; this does not imply Google endorsement. See [NOTICE](NOTICE) and the [source record](docs/upstream/google-stitch-skills-0337446.md).

## 📦 Install

```bash
npx skills add full-stack-skills/stitch-skills
```

Or install specific skills:

```bash
npx skills add full-stack-skills/stitch-skills --skill <skill-name>
```


### Local design specifications and prompts

Use `stitch-design-spec` as the single authoring entry. The two former names remain compatibility adapters only. Full packages, full-stack-doc module documents and prompt-only output share one contract. Local authoring skips authentication. See the [skill](skills/stitch-design-spec/SKILL.md) for templates, provenance and complete examples.

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

## 🎯 Skills (44)

**42 primary skills + 2 compatibility adapters.** Local specification and prompt authoring require no Stitch credentials.

Naming: keep `stitch-design-spec` / `stitch-design-harness` as upper-level entrypoints; use `stitch-ui-*` for concrete UI work, `stitch-ui-contract-*` for framework constraints, and `stitch-ui-<stack>-components` for UI code conversion. Keep `stitch-mcp-*` for tool adapters; retain explicit names for root routing, documents and specialized operations.

### Upper-level entrypoints and delivery

| Skill | Responsibility |
| --- | --- |
| [stitch-design-use](skills/stitch-design-use/SKILL.md) | Route a request to the appropriate skill. |
| [stitch-design-spec](skills/stitch-design-spec/SKILL.md) | Compile page contracts, states, Stitch prompts, coverage and task mappings. |
| [stitch-design-harness](skills/stitch-design-harness/SKILL.md) | Manage resumable design delivery, evidence, user approval and archival. |

### Concrete UI design capabilities

| Skill | Responsibility |
| --- | --- |
| [stitch-ui-execute](skills/stitch-ui-execute/SKILL.md) | Execute screen generation, editing, post-import editing and variants. |
| [stitch-ui-style](skills/stitch-ui-style/SKILL.md) | Propose visual style, typography, colors and motion in DESIGN.md. |
| [stitch-ui-guide](skills/stitch-ui-guide/SKILL.md) | Provide UI/UX vocabulary and guidance for design descriptions. |
| [stitch-ui-variants](skills/stitch-ui-variants/SKILL.md) | Prepare alternative design prompts without executing screen generation. |
| [stitch-ui-loop](skills/stitch-ui-loop/SKILL.md) | Build pages through a bounded, authorized backlog and hand off progress. |

### Framework design contracts: before generation

| Skill | Responsibility |
| --- | --- |
| [stitch-ui-contract-bootstrap](skills/stitch-ui-contract-bootstrap/SKILL.md) | Bootstrap/Vue component, layout and state constraints. |
| [stitch-ui-contract-element-plus](skills/stitch-ui-contract-element-plus/SKILL.md) | Element Plus component, layout and state constraints. |
| [stitch-ui-contract-layui](skills/stitch-ui-contract-layui/SKILL.md) | Layui-Vue component, layout and state constraints. |
| [stitch-ui-contract-uview2](skills/stitch-ui-contract-uview2/SKILL.md) | Design constraints for uni-app / Vue 2 / uView 2. |
| [stitch-ui-contract-uviewpro](skills/stitch-ui-contract-uviewpro/SKILL.md) | Design constraints for uni-app / Vue 3 / uView Pro. |
| [stitch-ui-contract-vant](skills/stitch-ui-contract-vant/SKILL.md) | Vant 4 component, layout and state constraints. |

### Documents and design systems

| Skill | Responsibility |
| --- | --- |
| [stitch-design-md](skills/stitch-design-md/SKILL.md) | Synthesize a source-backed semantic DESIGN.md from screens, HTML or images. |
| [stitch-extract-design-md](skills/stitch-extract-design-md/SKILL.md) | Extract DESIGN.md from frontend code, styles and themes. |
| [stitch-site-md](skills/stitch-site-md/SKILL.md) | Create SITE.md, navigation and backlog for page iteration. |
| [stitch-manage-design-system](skills/stitch-manage-design-system/SKILL.md) | Read, create, update and apply remote Stitch design systems. |

### Assets and project operations

| Skill | Responsibility |
| --- | --- |
| [stitch-code-to-design](skills/stitch-code-to-design/SKILL.md) | Bring existing frontend pages and design language into Stitch. |
| [stitch-extract-static-html](skills/stitch-extract-static-html/SKILL.md) | Extract static HTML and available assets without automatic upload. |
| [stitch-upload](skills/stitch-upload/SKILL.md) | Upload authorized images, HTML or design documents. |
| [stitch-local-setup](skills/stitch-local-setup/SKILL.md) | Configure local access and recover from authentication failures. |
| [stitch-delete-project](skills/stitch-delete-project/SKILL.md) | Delete an explicitly identified remote project and reconcile the result. |

### MCP tool adapters

| Skill | Responsibility |
| --- | --- |
| [stitch-mcp-create-project](skills/stitch-mcp-create-project/SKILL.md) | Create a Stitch project container. |
| [stitch-mcp-generate-screen-from-text](skills/stitch-mcp-generate-screen-from-text/SKILL.md) | Submit a prepared prompt to text-to-screen generation. |
| [stitch-mcp-get-project](skills/stitch-mcp-get-project/SKILL.md) | Read a specified project. |
| [stitch-mcp-get-screen](skills/stitch-mcp-get-screen/SKILL.md) | Read a specified screen and its assets. |
| [stitch-mcp-list-projects](skills/stitch-mcp-list-projects/SKILL.md) | List accessible projects. |
| [stitch-mcp-list-screens](skills/stitch-mcp-list-screens/SKILL.md) | List screens within a project. |

### Code conversion and presentations: after design

| Skill | Responsibility |
| --- | --- |
| [stitch-ui-react-components](skills/stitch-ui-react-components/SKILL.md) | Convert or synchronize Stitch designs into React/Vite components. |
| [stitch-ui-react-native-components](skills/stitch-ui-react-native-components/SKILL.md) | Convert designs into React Native screens and native components. |
| [stitch-ui-react-vite-dashboard](skills/stitch-ui-react-vite-dashboard/SKILL.md) | Implement React/Vite dashboards with tables, filters and async states. |
| [stitch-ui-shadcn-components](skills/stitch-ui-shadcn-components/SKILL.md) | Select, migrate and verify shadcn/ui primitives and themes. |
| [stitch-ui-uview2-components](skills/stitch-ui-uview2-components/SKILL.md) | Convert into uni-app + Vue 2 + uView 2 pages and components. |
| [stitch-ui-uview-plus-components](skills/stitch-ui-uview-plus-components/SKILL.md) | Convert into uni-app + Vue 3 + uview-plus pages and components. |
| [stitch-ui-uviewpro-components](skills/stitch-ui-uviewpro-components/SKILL.md) | Convert into uni-app + Vue 3 + uView Pro pages and components. |
| [stitch-ui-vue-bootstrap-components](skills/stitch-ui-vue-bootstrap-components/SKILL.md) | Convert into Vue/Bootstrap components, checking the target implementation version. |
| [stitch-ui-vue-element-plus-components](skills/stitch-ui-vue-element-plus-components/SKILL.md) | Convert into Vue 3 / Element Plus pages and components. |
| [stitch-ui-vue-layui-components](skills/stitch-ui-vue-layui-components/SKILL.md) | Convert into Vue 3 / Layui-Vue pages and components. |
| [stitch-ui-vue-vant-components](skills/stitch-ui-vue-vant-components/SKILL.md) | Convert into Vue 3 / Vant 4 pages and components. |
| [stitch-remotion](skills/stitch-remotion/SKILL.md) | Produce Remotion walkthrough videos from Stitch design assets. |

### Skill authoring

| Skill | Responsibility |
| --- | --- |
| [stitch-scenario-skill-creator](skills/stitch-scenario-skill-creator/SKILL.md) | Create Stitch prompt skills for a specific business scenario. |

### Legacy compatibility adapters

| Skill | Behavior |
| --- | --- |
| [stitch-ui-design-spec-generator](skills/stitch-ui-design-spec-generator/SKILL.md) | Legacy specification entry; forwards spec-only requests to stitch-design-spec. |
| [stitch-ui-prompt-architect](skills/stitch-ui-prompt-architect/SKILL.md) | Legacy prompt entry; forwards requests to stitch-design-spec. |

Use `stitch-design-spec` for new requests. See the [complete rename map](docs/skill-name-migration.md); source changes do not automatically update installed copies.

### Choosing an entry

- Unsure where to start: `stitch-design-use`.
- Specifications or prompts: `stitch-design-spec`.
- Actual screen generation or editing: `stitch-ui-execute`; complete delivery: `stitch-design-harness`.
- Before generation, use `stitch-ui-contract-uview2` for framework constraints; after design, use `stitch-ui-uview2-components` for implementation.
- Framework contracts own component constraints; `stitch-design-spec` compiles the final prompt. Framework-style visuals do not prove runnable framework code.

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

Third-party attribution is recorded in [NOTICE](NOTICE); the preserved third-party notices and
license texts are in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md); those components retain
their respective licenses.
