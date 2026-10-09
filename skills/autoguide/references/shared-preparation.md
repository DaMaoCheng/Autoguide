# Shared Guide | Collaboration Preparation and Configuration

**Keywords:** Collaboration preparation; patience; platform identification; actual capabilities; client and model; account permissions; new conversation; workspace; AI configuration; AGENTS.md; CLAUDE.md; preserving existing settings; loading verification; guide access; accessible materials; authorized scope

**Summary:** Identify the platform and actual capabilities according to the current work's needs, choose a conversation and workspace, read existing settings before explaining and adding configuration, and verify loading and guide access. Configuration retains a short entry point and necessary stable requirements. If preparation is incomplete, explain the limitations honestly and continue independent work.

Read [Home](index.md) first. This document is for users and AI working with the guide. Complete preparation as actually needed, without requiring every tool to be set up at once or the user to supply all information first. Authorization for configuration changes must cover the current target and scope; do not ask again for authorization already given.

## Expectations before starting: patience and time

**Allow patience and time for early preparation.** Clarifying requirements, organizing experience, verifying materials, and breaking down tasks are part of the work itself. Depending on project complexity, producing even one initiation record agreed by both sides may take hours, days, or longer. This can be a normal investment in preparation. Discussion may span several sessions; save the current shared understanding each time and continue from it next time.

AI should help the user explain details gradually and describe why it asks follow-up questions, what is already clear, and what remains unresolved. Judge preparation by whether the goal is clear, key conditions are established, and the records support the next stage. Do not ask again about confirmed information. Hours or days are possible investments, not a fixed minimum duration; simple work may finish faster.

## Identify the platform and its current actual capabilities

Identify the AI's host platform from environment information explicitly supplied in the conversation, available tools, or client settings, for example Codex, Claude Code, WorkBuddy, or Doubao Work. Distinguish the client platform from the model it uses. If identification is not possible, ask for the product and how the user accesses it. Check or ask about the version or operating mode when it affects the judgment; mark unavailable information as unconfirmed.

Follow [Web Research and Evidence Assessment](shared-research.md) to consult the platform's current official documentation, release notes, and relevant practical materials, checking the version and environment. Focus on strengths, limitations, and permissions relevant to this work: guide access, online search, file reading and writing, script execution, external service connections, task execution, rule storage, and conversation management.

Distinguish “officially supported,” “available in this session,” and “unconfirmed.” Where needed, verify through read-only, low-risk operations. Marketing claims, model names, or other users' experiences cannot replace checks of current tools, connection status, and account authorization. The initial understanding may stay in context; save a short capability record when continuity across conversations is needed or it affects implementation choices. Include the environment, verification results, limitations, verification date, and sources. Proceed once the capabilities required for this work have been checked; do not expand permissions on your own.

## Choose a suitable conversation and workspace

Before starting, consider whether a new conversation or separate project is needed. Suggest switching when there is substantial unrelated content, a major change in goal or scope, a history too long to carry forward accurately, or configuration that requires a new session to take effect. Continue the current conversation when its context is clear and the work is brief.

A new conversation organizes discussion context; a separate project or workspace manages the work's files, rules, and long-term results. Choose each according to actual needs, then add configuration in the corresponding place. If creation and content transfer are available and the user has given the relevant authorization, carry them out; otherwise guide the user through the steps. Do not create multiple tasks, switch platforms, or incur additional costs by default. Prepare handover information when switching, using [Changes, Records, and Handover](shared-changes.md).

## Add configuration and verify the guide entry point

Verify the current platform's configuration mechanism, filenames, locations, scope, and loading conditions. Choose an entry point appropriate to this work, such as AGENTS.md, CLAUDE.md, project instructions, rules, or a Skill. Prefer configuration for the corresponding project or workspace by default. If global settings affecting all projects are needed, explain that scope explicitly and obtain authorization covering it.

**Before editing, tell the user the specific target, additions, and scope of impact; read the existing content before changing it.** Preserve the user's existing settings and integrate new requirements in appropriate places. Consolidate duplicates; explain substantive conflicts and resolve them according to applicable instructions. Do not overwrite files or remove existing rules without authorization. Authorization already given does not require another confirmation. Merely referring to this page, or requesting a read-only discussion, does not authorize configuration changes.

For the public edition, first establish the actual location of the current Skill and `references/index.md`, then write that real entry point into the applicable configuration. Do not assume the guide is in the business project's root directory. Configuration should retain a brief, stable entry point: [Home](index.md), the Home collaboration principles, the requirement to read the current stage as needed, and the triggers for consulting the guide again. Detailed rules come from the corresponding documents in the version actually installed. Do not copy the entire guide into configuration; respect the platform's instruction hierarchy and permission boundaries.

Add the stable requirements to the current project's applicable configuration, such as AGENTS.md, CLAUDE.md, or platform project instructions: report after completion; iterate from user feedback; retain existing frameworks and UI; maintain update logs and Bug logs by day; establish automatic project runtime logs; and search historical fixes before handling Bugs, using runtime logs to check the real process. For feature scenarios, also include actual ownership; preserving the original architecture when attached; modifying target behavior as authorized for this phase while protecting existing features outside the scope; verifying affected behavior and related workflows; archiving documentation and logs with the feature; and checking relevant existing features during acceptance. Read the existing settings first, integrate the requirements appropriately, and retain other valid content. Tell the user the specific changes and their scope as required above. This document provides configuration requirements and examples; it does not mean any user's project configuration has already been changed.

Project documentation must retain actual paths or links to the current code, update logs, Bug logs, and runtime logs, and project configuration must be able to locate those entry points. If locations are unclear, first inspect existing documentation, directories, and records; do not invent paths. Where an entry point is missing, add it according to current project conventions or explain the limitation. Fill in the examples below with the real project's entry points, then verify that they take effect after configuration loads.

### A brief entry point in configuration

```text
## Collaboration guide entry point
- Before starting work, locate references/index.md relative to the directory containing the autoguide/SKILL.md actually loaded in this session. Record its real path in project documentation or configuration, and read the corresponding guide for the current stage.
- Check the latest relevant rules when entering a new stage, after important changes, or during handover. Reuse confirmed records that remain valid as needed.
- If access fails, explain the missing content and its impact; do not claim to have followed rules you could not read.
```

### Stable requirements to integrate into applicable configuration

Use the stable requirements below together with the brief entry point. Add actual project paths and integrate them into existing settings. Equivalent rules may be consolidated, but applicable core rules from this guide must not be marked optional and omitted, especially the requirement to search historical logs before fixing Bugs.

```text
## Collaboration and issue handling in this project
- AI assists around the user's business viewpoint and goals; all suggestions and judgments about external facts require live online verification. Before initiation and during the work, explain practical effects, benefits, costs, and uncertainty in business language so the user can understand and decide important tradeoffs. Handle ordinary implementation details within authorization. When the goal is clear, proceed directly without routinely asking for each round's output or format.
- Read the existing implementation before changing it. Retain existing frameworks, UI, modules, and shared rules, and prioritize reuse.
- Carry confirmed nonnegotiable requirements through implementation requirements, corresponding checks, and actual evidence. If necessary checks fail, continue repairs within authorization or explain limitations truthfully. Do not silently change those requirements or promise unverified effects as achieved results. Report truthfully after completing the currently authorized task and necessary self-checks. Make later changes from user feedback; handle new requirements under the rules for this phase or later phases.
- Record ordinary changes in daily update logs; record fault investigations, repairs, and verification in Bug logs. Obtain the actual entry points from current documentation.
- Establish automatic runtime logging: automatically create an empty file for each day and append events automatically, recording the run identifier and actual process without requiring user or AI intervention each time. Verify it in the actual environment.
- Before handling a Bug, search for the same or similar historical Bugs, then use runtime logs to check the current version, environment, and actual process. If no applicable record exists, continue investigating from real evidence.
- Verify repairs in practice, complete searchable Bug records, and link runtime evidence. Do not rewrite original runtime records or mark an unverified issue as resolved.
- When a feature is attached to an existing host, preserve the original architecture. Modify target behavior as explicitly authorized for this phase; keep existing features outside the scope and related workflows operating normally. Acceptance checks cover the target change and affected workflows. Archive documentation and logs with the feature.
- Keep current documentation consistent with the actual state. Maintain Git and versions at established delivery milestones; uploading to GitHub is not required.
- Do not request confirmation again when authorization already covers the target, scope, and consequences. Before deletion, publication, paid actions, external sending, production operations, or configuration changes outside that authorization, explain the action and obtain corresponding authorization.
```

After editing, check what was written, whether the configuration actually loads, and whether the guide is accessible. Reload or start a new session according to the platform mechanism where needed; “written” does not mean “effective.” If there is no configuration entry point or permission to edit it, explain the limitation and provide brief guidance the user can place in settings or a new conversation. Once feasible preparation is complete and actual limitations are explained, enter the requirements discussion; do not pretend to have completed configuration that could not be performed.

## Preparation outcome and subsequent reading

The platform and permissions required for the current work have been verified, or their limitations and effects are clear. Applicable configuration has been added and checked, with truthful explanations for anything that could not be done. Necessary guide entry points have been confirmed readable, or accessible materials needed now have been obtained with limitations recorded. Once discussion is possible, clarify requirements according to Home; do not make unrelated missing information a prerequisite for starting.

## Shared methods and platform references

Follow [Web Research and Evidence Assessment](shared-research.md) for capability checks and verification of all suggestions. Follow [Changes, Records, and Handover](shared-changes.md) for switching conversations, record entry points, and restricted reading access. For installation, creation, or adaptation of the companion Skill, consult [Companion Skill \| Installation and Adaptation Guide](installation.md), which covers packages, complete source, platform differences, and reading verification. Whether installation is needed depends on the actual environment.

Configuration mechanisms: [Codex: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md); [Claude Code: Project Instructions and Memory](https://code.claude.com/docs/en/memory); [WorkBuddy: Plugins and Rules](https://www.workbuddy.cn/docs/workbuddy/Plugins). These explain mechanisms; actual use still requires checking the current version and environment.
