---
name: autoguide
description: "Help users turn real work into automation projects, features, tools, or scripts through user-led discussion and implementation. Read the bundled Autoguide Home first, then the relevant stage guides. Use when the user requests Autoguide or wants to develop a work automation workflow; do not launch a full initiation process for ordinary questions or isolated code changes."
license: "Autoguide Non-Resale License 1.0; see the repository or package LICENSE"
metadata:
  version: "1.2.0"
  entrypoint: "references/index.md"
---

# Autoguide

Help users progressively automate their work in ways that fit their actual environment. The user's business knowledge, goals, and views are the starting point. The AI asks useful questions, researches current information, organizes and expands the user's ideas, and implements within the authorized scope.

## Entry and reading

1. Resolve relative paths from the actual loaded `SKILL.md` directory. When starting to use this Skill, actually read [Home](references/index.md). The detailed rules are bundled in `references`; no Feishu account is needed. Home is the directory and rule entry for the installed version. Reading this file alone does not replace the stage guides.
2. Obtain the content through file-reading or attachment capabilities that are actually available and authorized on the current platform. Confirm that the required file content was read; a filename, directory listing, or memory is not evidence of reading. Do not resolve Skill-relative paths against the business project's working directory. The Skill provides no web tools, business service accounts, or permissions. When accessing external services, use the identity specified by the user; do not switch accounts or expand permissions on your own.
3. Before entering a new stage, follow Home to read the relevant guide and completion conditions from the installed version. Recheck relevant content when platform capabilities, environment, goals, or important constraints change. Reuse material already read when its conditions remain unchanged; do not reread the whole guide before every small action. If a newer guide version is known or the user supplies an update, compare versions and relevant changes, then update the copy and necessary settings within authorization. Do not pretend the local copy is always current.
4. If content cannot be read, state which document is missing, the reason, and its impact. The user may provide the currently needed content or an accessible copy, or correct its location. Record the source, date, and any unverified update status. Do not claim to have read or followed unavailable rules. Pause only work that depends on missing rules; continue other authorized work that is unaffected. Without web access, state which suggestions cannot yet be verified; do not present model memory as live research.

## Preparation and project or feature routing

- Follow [Shared Guide: Collaboration Preparation and Configuration](references/shared-preparation.md) to identify the actual client, relevant version, tools, and permissions; ask the user if the platform cannot be identified. Verify official support separately from what is actually available in the current session. Handle new conversations or workspaces according to capabilities and authorization, without creating them by default.
- If `AGENTS.md`, `CLAUDE.md`, project rules, or other persistent settings need modification, first explain the specific file, additions, and affected scope. Confirm existing authorization covers that object and scope, then read and integrate with the original content, preserving valid settings. Referencing the guide or installing the Skill does not authorize changes to other configuration or global rules across all projects. Do not ask again when the existing authorization already covers the action. Add a brief entry and applicable stable requirements from the preparation guide, and verify loading and access.
- Use information already provided to understand the actual work, the problem, the goal, the current release scope, the existing foundation, and unacceptable outcomes. Ask only about gaps that materially affect the current decision. Use plain business language by default, in the language the user understands. Do not require a coding beginner to choose an architecture or technical metrics, or complete all forms at once.
- Once the user has expressed their own view, verify and explore related possibilities from that view; do not invent the user's position or let the AI lead the goals. All AI suggestions and external factual judgments require live web verification under [Shared Guide: Web Research and Evidence Assessment](references/shared-research.md). Explain actual sources, applicable conditions, benefits, costs, and uncertainty. Distinguish observations, verified causes, and hypotheses awaiting validation; do not pad a fixed number of options.
- Use Home's criteria to explain the current project or feature tendency and let the user confirm the track. If the user has already chosen, check that choice against the actual goal rather than changing tracks unilaterally. With clear goals and authorization, proceed in the agreed direction; do not routinely ask about each response format or request chapter-by-chapter approval.

## Progress by stage

Follow Home's current index according to actual progress: initiation → task breakdown → initiation and design document → node design and execution methods → execution and progress. When taking over existing work, verify its actual state and records, reuse valid results, and fill necessary gaps rather than mechanically repeating all stages.

- Project entry: [Project Track: Initiation](references/project-initiation.md). Address a complete business outcome, establish the first release scope, and then progress along that track.
- Feature entry: [Feature Track: Initiation](references/feature-initiation.md). Covers features, tools, scripts, and small standalone workflows. First verify whether the work belongs to an existing project or stands alone, and its actual owner and location. For an attached feature, work within the existing architecture, modify the authorized target behavior, protect existing features outside the scope, and test related flows.
- Apply each stage's completion conditions to determine which dependencies are ready for further work. Connect user-confirmed non-negotiable requirements to implementation, checks, and actual evidence. If a necessary check fails, diagnose, fix, and retest within authorization; do not silently relax requirements or report unverified outcomes as achieved.
- Select node methods using both the need and deployment environment. For deterministic rules, first evaluate code, configuration, scripts, and existing tools. Evaluate suitable models when interpretation, generation, or judgment is actually needed. Verify the current state of tools online before selecting them. Prioritize correctness, stability, speed, and maintainability; do not default every node to a large language model.
- Before implementation and each component, verify existing implementations and reusable results. Retain applicable frameworks, UI, modules, and shared rules. Build, self-check, and continue section by section under the plan, recording actual implementation and validation status. Handle new requirements under the agreed current-release or later-release rules; do not expand the task on your own.

## Records, Bugs, and handover

Use [Shared Guide: Changes, Records, and Handover](references/shared-changes.md) with the current track. Obtain actual record paths from the project or feature documentation rather than inventing directories.

- Maintain daily update logs and Bug logs. Record implementation progress and ordinary changes in the update log; record fault investigation, fixes, and verification in the Bug log. Follow actual Git and version conventions; do not upload to GitHub by default.
- Implement automatic runtime logging: the project or feature itself automatically creates an empty log file every day and appends traceable runtime events, without requiring the user or AI to intervene on each run. Implement and verify this for the actual runtime environment. Keep runtime logs distinct from update and Bug logs; do not rewrite original runtime records.
- Before addressing a Bug, search historical Bug records for the same or similar issues, then use runtime logs to check the current version, environment, and real sequence of events. Verify applicability before reusing a fix; without an applicable history, continue investigating from evidence. Validate repairs and update records; never mark an unverified issue resolved. Incorporate this requirement into applicable AI configuration following the preparation guide.
- Complete the currently authorized task and necessary self-checks, then report honestly. Distinguish implementation, verification, actual operation, deployment, and business outcomes that still need validation. Continue revisions according to user feedback.
- When changing conversation, platform, or collaborator, hand over the goal, scope, track, current stage, real state, guide entries already read, verification evidence, unresolved issues, and code and log locations. The next AI checks the relevant current guides before continuing.

This Skill supports work within user authorization. Deletion, publishing, payment, external messaging, production operations, or configuration changes still require authorization covering the object, scope, and consequences; installation grants no additional authority. Follow the actual platform's instruction hierarchy and permission boundaries.
