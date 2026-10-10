# Autoguide

**User-led guidance for turning real work into reliable automation.**

Guide version: **1.2.1**

Autoguide helps a user and an AI develop projects, features, tools, scripts, and automated workflows from actual business needs. It connects goal clarification, task breakdown, design, implementation, verification, and iteration. The installable `autoguide` Skill guides the AI to read the rules needed for the current stage.

It is for people who understand their work and want to reduce repetitive actions or improve their workflows. Describe your needs in ordinary language; you do not need to learn coding, architecture, or prompt engineering first. The AI should organize what you have already provided and ask only about gaps that affect the next meaningful decision. Developers can also use the guide to clarify business constraints, acceptance criteria, and handover records.

All rules are included as local Markdown files. **No Feishu account or access to the original private knowledge base is required.** Web research, file operations, script execution, and service connections depend on the capabilities and permissions actually available on the user's platform.

## How collaboration works

- **The user leads goals and important trade-offs.** Start from how the work is done, what is wrong, and the desired outcome. The AI asks useful questions, researches, organizes, explores, and implements. It explains practical consequences in understandable business language and does not turn unconfirmed assumptions into requirements.
- **Verify suggestions and external facts online.** Before recommending a method or judging an external fact, the AI uses available web tools to check current evidence, applicability, and counterexamples. Recently checked evidence can be reused while its conditions remain unchanged. Without web access, the AI states the limitation instead of presenting model memory as current evidence.
- **Read by stage and need.** Begin with Home, read the relevant guide before entering a stage, and recheck affected rules at significant changes or handover. Reuse valid records; do not reread the entire collection before every small action.
- **Review and plan before modifying existing code.** The AI reads the actual implementation, identifies where and how to change it, checks related effects, and defines acceptance checks. It records and self-reviews a proportionate plan, then implements within authorization without routine user approval. See the [change-planning process](skills/autoguide/references/shared-changes.md#review-existing-code-and-form-a-change-plan-before-editing).
- **Choose the right method for each node.** Explicit validation, calculations, mappings, and state transitions should first be evaluated as code, configuration, or existing tools. Evaluate model calls when interpretation, generation, or judgment is needed. Do not assign every node to an LLM.
- **Keep progressing within authorization and report honestly.** The AI handles ordinary implementation details using existing conventions. The user decides changes that materially affect the business. Deletion, publication, spending, external messages, production operations, and configuration changes need authorization that covers their objects, scope, and consequences.

Preparation and initiation are real work. A complex need may take several discussions, hours, or days to clarify. There is no minimum duration, no requirement to configure every tool first, and no demand to fill every field at once.

## Start here

1. Read [Home](skills/autoguide/references/index.md) for the principles and project or feature routing criteria.
2. Use [Collaboration Preparation and Configuration](skills/autoguide/references/shared-preparation.md) as needed to verify platform capabilities, workspace, existing rules, and relevant permissions.
3. Describe one real task. Build a current understanding of the goal, release scope, constraints, acceptance conditions, confirmed facts, and hypotheses to verify.
4. Confirm the project or feature track with the AI and continue from its initiation guide.

For an AI that can read local files, provide the repository and a request such as:

```text
Use Autoguide to help me progress with this work.
First read skills/autoguide/SKILL.md and its Home entry.
Verify the web, file, and action capabilities available in this session.

My current work is: ...
The problem is: ...
The result I want is: ...
My existing materials or tools are: ...

Organize what you understand from this information.
Discuss key gaps progressively, explain important trade-offs in business terms,
and help me confirm the project or feature track.
```

Use the actual directory you provide to the AI. With a clear goal and authorization, the AI should continue from the current agreement. The repository is in English; collaboration should use language the user understands.

## Two tracks, five stages

A **project** addresses an overall business outcome and how several capabilities work together. A **feature** addresses a specific capability with identifiable inputs, results, and boundaries; it may stand alone or belong to an existing project. Size, lines of code, UI, or a server do not decide the track on their own. Projects can contain multiple features. The user confirms the track based on the actual goal and scope.

| Stage | Result | Project entry | Feature entry |
| --- | --- | --- | --- |
| Initiation | Current goals, release scope, runtime conditions, and initial acceptance criteria | [Project initiation](skills/autoguide/references/project-initiation.md) | [Feature initiation](skills/autoguide/references/feature-initiation.md) |
| Task breakdown | Real actions, conditions, implicit judgments, exceptions, and complete paths | [Project task breakdown](skills/autoguide/references/project-work-breakdown.md) | [Feature task breakdown](skills/autoguide/references/feature-work-breakdown.md) |
| Initiation and design document | A maintained complete description of hierarchy, rules, and acceptance arrangements | [Project design document](skills/autoguide/references/project-design.md) | [Feature design document](skills/autoguide/references/feature-design.md) |
| Node design and execution methods | Verified reuse, node methods, integration, and failure handling | [Project node design](skills/autoguide/references/project-node-design.md) | [Feature node design](skills/autoguide/references/feature-node-design.md) |
| Execution and progress | Incremental implementation, necessary checks, records, and feedback-driven iteration | [Project execution](skills/autoguide/references/project-execution.md) | [Feature execution](skills/autoguide/references/feature-execution.md) |

Completion conditions identify which dependencies are ready; they do not add chapter-by-chapter approval. Verify work affected by a critical gap while continuing independent authorized work. An attached feature stays within the original architecture, states the target changes and protected behavior, and tests affected flows. Existing valid work is reused rather than forced through initiation again.

## Install and use the Skill

The guides can be read directly. Install the Skill when you want the AI to use stage-specific guidance in later collaboration.

The complete source is in [skills/autoguide](skills/autoguide), with [SKILL.md](skills/autoguide/SKILL.md) as the entry. Keep the entire Skill directory and all `references/` files. See [Installation and Adaptation](skills/autoguide/references/installation.md) for platform-specific locations and loading checks.

You can provide the directory to your AI and say:

```text
Install the provided autoguide Skill for the current project.
Identify my platform and runtime, verify its current official installation method,
and explain the target location and scope. Check for an existing Skill of that name.
Preserve existing settings; compare custom content instead of overwriting it.
After installation, verify loading and read Home and the required stage document.
Report the actual result and any limitation.
```

Default to the current project scope. Request a personal installation explicitly if that is what you want. Installing a Skill supplies neither web tools, service credentials, nor additional authority. It does not start a background automation process.

Directory structure, installation scope, and invocation depend on current official documentation: [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) and [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills). Actual support must still be checked in the user's client, account, and runtime environment.

## Records and iteration

Keep requirements, implementation, and observed results distinct. At delivery, distinguish implemented, tested, locally running, deployed, and verified in the actual environment. State known limitations; do not report expected business benefits as achieved outcomes.

Maintain three types of records according to the real environment: an update log for changes and verification results, a Bug log for symptoms, evidence, causes, fixes, and status, and automatic runtime logs for real execution events. Daily runtime files and automatic event appending must be implemented and verified in the actual project. Installing this Skill does not create that mechanism.

Before fixing a Bug, search the same or similar historical issues and compare the current environment, version, and runtime evidence. Verify the repair, update its record, and preserve original runtime evidence. At conversation changes or important condition changes, save a concise handover and continue the current stage. See [Changes, Records, and Handover](skills/autoguide/references/shared-changes.md) and [Web Research and Evidence Assessment](skills/autoguide/references/shared-research.md).

## Repository layout

```text
.
├── README.md
├── VERSION
├── CHANGELOG.md
├── LICENSE
├── skills/
│   └── autoguide/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
│           ├── index.md
│           ├── shared-preparation.md
│           ├── shared-research.md
│           ├── shared-changes.md
│           ├── project-initiation.md
│           ├── project-work-breakdown.md
│           ├── project-design.md
│           ├── project-node-design.md
│           ├── project-execution.md
│           ├── feature-initiation.md
│           ├── feature-work-breakdown.md
│           ├── feature-design.md
│           ├── feature-node-design.md
│           ├── feature-execution.md
│           └── installation.md
└── scripts/
    ├── check_links.py
    └── build_package.py
```

`SKILL.md` handles discovery and stage routing. The 15 files in `references` contain the complete guides. `agents/openai.yaml` supplies optional Codex interface metadata.

From the repository root, check local links and build a standalone package:

```sh
python3 scripts/check_links.py
python3 scripts/build_package.py
```

The ZIP is created in `dist/` and contains the entire Skill and its guide documents. Use `python3 scripts/build_package.py --release` before publishing to check the release prerequisites and include the license in the package. Original exports and private backups are stored separately and are not part of this repository or package.

## Maintenance and contributions

Use Issues for real usage problems, environment details, and evidence. Use Pull Requests for corrections, examples, or platform adaptations.

- Describe the actual scenario, current workflow, problem, and desired outcome. Remove credentials, personal information, and sensitive business data.
- State the conditions, verification date, sources, and actual validation results of examples. Do not promote a single unverified experience into a universal rule.
- When changing detailed rules, check the Home index, stage entries, keywords, and Skill navigation. Link to one maintained source rather than maintaining duplicate versions of the same rule.
- Run the link check before submitting. For installation or packaging changes, verify package structure and actual loading results, and state environments not covered by testing.
- When platform capabilities or installation facts change, update the relevant official sources and verification notes. Separate official support from what was actually tested in the current environment.

## Licensing

Copyright © 2026 DaMaoCheng. Autoguide is publicly available under the [Autoguide Non-Resale License 1.0](LICENSE), a project-specific source-available license.

- Personal use and internal organizational use, including internal work at commercial companies, are permitted.
- You may modify and share copies free of charge, retaining the license and attribution and identifying material changes.
- Selling Autoguide or modified copies, charging for access to it, or including it in paid Skill packages, bundles, subscriptions, or courses requires separate written permission.
- Independently created projects and business outputs are not required to be published and may be commercialized; copied or substantially adapted Autoguide content still follows the license.

The license covers this repository's original guide content, Skill, metadata, examples, and helper scripts. External works retain their own terms. This is not MIT and is not represented as an OSI-approved open-source license. Read the full license for the governing terms.

The guide preserves credit to Huang Jincheng's day-to-day collaboration with AI, as recorded in [Home](skills/autoguide/references/index.md).
