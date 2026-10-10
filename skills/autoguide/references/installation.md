# Companion Skill | Installation and Adaptation Guide

**Keywords:** Skill; installation; creation; autoguide; SKILL.md; Codex; Claude Code; platform adaptation; local guide; loading verification; AGENTS.md; CLAUDE.md; updates and handover

**Summary:** Install the Skill with its complete bundled rules, or adapt it to your AI platform using the source. Verify that the current session can actually read Home and its supporting documents. Read the specific collaboration rules in [Home](index.md) and the corresponding stage documents.

The current compiled version is **1.2.2**, dated **2026-10-10**. The guide text can be read locally without a Feishu account; all AI suggestions and judgments about external facts still require live online tools provided by the platform. The Skill does not include business service accounts, online tools, or authorization to operate on other projects.

## Use the existing Skill directly

Locate `skills/autoguide` in the repository source you obtained, or extract the Skill package for the corresponding version. During installation, copy the entire `autoguide` folder, preserving every document in `references`. Do not copy only `SKILL.md` or add another enclosing folder with the same name.

```text
autoguide/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── index.md
    ├── shared-preparation.md
    ├── shared-research.md
    ├── shared-changes.md
    ├── project-*.md
    ├── feature-*.md
    └── installation.md
```

Here, `project-*.md` and `feature-*.md` represent the five complete stage documents for each track. Use the Home index for the specific entry points.

Give your AI the Skill folder or archive, then send:

```text
Install the autoguide Skill I have supplied into the current project.
First identify my platform, operating mode, and the mechanisms it actually supports; check the current official installation method online.
Tell me the installation location and its scope, and check for an existing Skill with the same name. Preserve other settings. Compare any existing custom content before changing it; do not overwrite it directly.
Copy the entire folder, including the full documents in references; do not install only SKILL.md.
After installation, verify in read-only mode: actually read references/index.md and at least one stage document needed now, then report the loading location, version, and reading results.
Do not also change global rules, AGENTS.md, or CLAUDE.md. If using the guide requires configuration additions, first explain the specific target, content, and scope, then act according to existing authorization.
```

Use the current project's scope by default. If you want to use the Skill across multiple projects, explicitly tell the AI to install it at the personal scope. A Skill being installed, loaded by the current session, and able to expose readable guide text are three different states.

## Choose an installation location for the actual platform

The following locations and invocation methods are compiled from official documentation consulted on 2026-10-09. `~` means the current user's home directory. Before installation, check the actual client, version, organization settings, and operating mode. Personal scope affects multiple projects and requires an explicit user choice.

| Platform and scenario | Current project | Personal scope | Invocation |
| --- | --- | --- | --- |
| Codex local Skill | `.agents/skills/autoguide/` | `~/.agents/skills/autoguide/` | Reference `$autoguide` in the CLI or IDE; in the desktop app, use the actual Skill selection entry point. |
| Claude Code local session | `.claude/skills/autoguide/` | `~/.claude/skills/autoguide/` | Reference `/autoguide`; the platform may also recognize requests matching the description automatically. |
| Other platforms, cloud, or managed environments | Verify the current official entry point and loading scope | Verify the supported mechanism | Do not copy local directory assumptions or claim that an untested platform is definitely compatible. |

The full path ends in `SKILL.md` inside one of the directories above. `agents/openai.yaml` provides only Codex interface information and a default prompt; other platforms need not depend on it. Cloud or account-level sessions may not read a local personal directory; handle them according to the current platform mechanism.

For products such as WorkBuddy and Doubao Work, check current capabilities first. If there is no native Skill entry point but project instructions or rules are supported, adapt a brief guide entry point within authorization. If persistent settings are unavailable, provide the currently needed documents and usage instructions in a new conversation and state the limitations on continued loading.

Follow [Collaboration Preparation and Configuration](shared-preparation.md) for configuration changes, preservation of existing settings, and permission boundaries. Record the actual installation entry point in project configuration; do not mistake a source repository's relative path for a path that applies to every business project.

## Verify loading and reading

Start with read-only verification, without creating a business project, performing production operations, or changing other configuration:

```text
Use autoguide only to verify reading access.
Locate and read references/index.md relative to the directory containing the SKILL.md actually loaded in this session.
Tell me the title you actually read, the current version, how the Project Track and Feature Track are selected, and each track's initiation entry point after confirmation.
Then actually read one initiation guide, explain its key requirements and completion criteria, and give the real file location you used.
If a file is missing, reading permission is unavailable, or you can only see a directory listing, explain where access failed and its impact. Do not fill in content from filenames or your own knowledge.
Do not modify configuration or create a business project yet.
```

Confirm the following:

- The intended Skill name, location, and version are loaded; merely copying files does not prove successful loading. If an update does not appear, reload or start a new session according to the current platform mechanism.
- Home and the needed supporting documents are actually readable. Resolve relative paths from the current `SKILL.md` location; do not guess from the directory of the business project being worked on.
- AI can explain that it reads Home first, the corresponding document before each stage, and reuses valid records when taking over existing work instead of repeating initiation in full each time.
- Configuration changes are explained before editing and preserve existing content; Bugs are handled by checking historical logs first. Before modifying existing code, the AI follows the [Existing-Code Review and Change Plan](shared-changes.md#review-existing-code-and-form-a-change-plan-before-editing), assessing related effects and defining acceptance checks before implementation. Once the goal and authorization are clear, the AI self-reviews its plan and continues without routine approval for the plan or each chapter.
- Record local rule access separately from the online tool status. If online tools are unavailable, local rules can still be read and existing facts organized, but model memory must not be presented as suggestions verified online.

Verifying installation structure and entry-point reading does not prove that business automation runs successfully or guarantee that every client supports the same loading mechanism. Actual projects must still be checked against their own acceptance criteria.

## Create or adapt your own version

The complete core source is [SKILL.md](../SKILL.md); the optional Codex interface file is [agents/openai.yaml](../agents/openai.yaml). Keep the source aligned with the bundled rules; there is no need to duplicate the source in this document and maintain it separately over time.

You can send your AI:

```text
Use this installation guide and the complete adjacent SKILL.md to create an adapted version for my current platform.
First identify the platform, operating mode, and scope of this use. Verify the current official Skill, rule, or project-instruction mechanism online; ask me if you cannot identify it.
Preserve the complete current references directory and Home index. Read the actual documents by relative path without depending on the original author's private knowledge base.
Retain user direction, live online verification of suggestions, reading by stage, preservation of existing configuration, review and planning before existing-code changes with related-effect and acceptance checks and no routine user approval, checking Bug history first, the three log types, and actual-state requirements.
Generate files that can be saved or downloaded and installation instructions. Verify file structure and document reading; do not assume every platform supports the same import format.
Explain file creation, installation, and changes to other configuration separately. Continue within the authorized scope without automatically expanding to global settings for all projects.
```

## Updates, handover, and maintenance

Detailed rules are maintained in the corresponding documents of the currently installed version; Home retains the index. Read the relevant documents when entering a new stage. If a newer version is known to exist, the user supplies an update, or important rules change, check version differences and their impact on current work before updating copies and applicable configuration within authorization.

A local copy is not automatically replaced when the upstream repository or someone else's knowledge base changes. Preserve existing custom content before updating. Afterward, confirm that `SKILL.md`, `references`, and interface metadata come from the same version, and verify loading and reading again. Do not describe local files as always up to date.

When switching conversations or AI, hand over the goal, scope, track, stage, actual outputs, log locations, guides already read, and unresolved issues. The new AI checks relevant guides from the real installation entry point and continues the work. When maintainers update general rules, they also check the related tracks, index, and configuration examples and record version changes.

Technical mechanism references: [OpenAI: Build Skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code: Extend Claude with Skills](https://code.claude.com/docs/en/skills), and [Agent Skills Specification](https://agentskills.io/specification). These sources are used to verify installation and file mechanisms; business collaboration rules follow the current guide and user authorization.
