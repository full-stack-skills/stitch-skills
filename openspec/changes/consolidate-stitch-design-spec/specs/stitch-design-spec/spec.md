## ADDED Requirements

### Requirement: Single canonical owner
The package SHALL expose stitch-design-spec as the canonical local specification and prompt workflow and retain the two former names only as compatibility routes.

#### Scenario: Legacy caller
- **WHEN** a caller requests either former skill
- **THEN** the adapter forwards original inputs and expected output to the canonical skill, or reports the missing dependency without installing it

### Requirement: Traceable design package
The skill SHALL produce page contracts, navigation, states, flows, prompts and dependency-ordered acceptance tasks with stable source references, or an explicitly scoped module/prompt-only view.

#### Scenario: Multi-page PRD
- **WHEN** a PRD requests multiple pages
- **THEN** every in-scope page and state is mapped to a prompt or a reasoned deferral, including entry, return, failure and recovery behavior

### Requirement: Prompt mode preservation
The skill SHALL preserve vague-input enhancement, spec compilation, six framework contracts and Context/Layout/Components formatting.

#### Scenario: Applied design system
- **WHEN** an executor supplies evidence of an applied project design system for a new screen
- **THEN** the prompt excludes visual tokens and color roles and carries the system reference in separate handoff metadata

#### Scenario: Local design document only
- **WHEN** only DESIGN.md is supplied
- **THEN** the prompt uses inline mode and does not claim remote system application

#### Scenario: Targeted edit
- **WHEN** the request changes only one control
- **THEN** the prompt describes only that delta, preserving its explicitly requested visual value

### Requirement: Local boundary and reproducible verification
The workflow SHALL run without credentials, include self-contained examples and templates, and distinguish structural checks, semantic review and actual remote generation.

#### Scenario: Offline authoring
- **WHEN** the user requests only specifications or prompts
- **THEN** the root router dispatches without setup, authentication or remote writes

#### Scenario: Incomplete package
- **WHEN** a referenced prompt is missing or a required page-state has no mapping
- **THEN** local validation fails and the delivery is not marked ready

### Requirement: Canonical Stitch harness name
Active delivery handoffs SHALL use stitch-design-harness. Existing run identities, evidence formats and persisted dispatch packets SHALL remain unchanged.

#### Scenario: Historical dispatch
- **WHEN** a persisted dispatch names stitch-delivery-harness
- **THEN** it resolves to stitch-design-harness with the same scope and packet identity, without rewriting history or starting another run

#### Scenario: New profile run
- **WHEN** ui-design-harness starts a new stitch-high-fidelity-delivery version 4 run
- **THEN** its candidate handler is stitch-design-harness with unchanged stage semantics

### Requirement: Consistent discoverable skill names
The package SHALL use the documented canonical naming map in docs/skill-name-migration.md. Plugin registration, skill metadata, active references and both READMEs SHALL agree. The two existing spec compatibility adapters SHALL be documented separately from primary skills.

#### Scenario: Framework contract versus code conversion
- **WHEN** a user selects stitch-design-contract-uview2 or stitch-uview2-components
- **THEN** the former supplies design constraints and the latter produces uni-app/Vue 2/uView 2 code, without claiming identical responsibilities

#### Scenario: Scenario creation after rename
- **WHEN** the scenario creator is installed without sibling skills and generates a new scenario
- **THEN** its output references canonical skill names and includes its license, preserving existing target files on repeated creation

### Requirement: UI namespace under design entrypoints
The package SHALL preserve stitch-design-spec and stitch-design-harness as upper-level entrypoints. Concrete UI execution, style, guidance, variants, page loops, framework contracts and UI code conversion SHALL use the stitch-ui- prefix. Root routing, document artifacts, MCP adapters and non-UI specialized operations SHALL retain their documented names.

#### Scenario: Selecting UI versus upper-level responsibilities
- **WHEN** a caller requests uView 2 constraints, uView 2 code, screen execution or complete design delivery
- **THEN** the respective entries are stitch-ui-contract-uview2, stitch-ui-uview2-components, stitch-ui-execute and stitch-design-harness

#### Scenario: Generated scenario handoff
- **WHEN** a scenario prompt skill is created
- **THEN** it references stitch-ui-execute and stitch-ui-guide while preserving stitch-design-spec as the prompt-contract owner
