# Shared Guide | Changes, Records, and Handover

**Keywords:** handling changes; requirement changes; current consensus; actual status; recording responsibilities; Git; versions; changelog; Bug log; runtime logs; historical issue search; handoff; new conversations; record entry points; accessible copies

**Summary:** Check relevant rules and carry current work forward when stages, goals, environments, or conversations change. Distinguish requirements, capabilities, evidence, and actual delivery status. Clarify the responsibilities of Git and the three types of logs, and use concise handoff and Bug templates. Continue referring to existing stage standards for detailed implementation and verification.

First read [Home](index.md). This guide applies to changes, records, and handoff in both the Project Track and Feature Track. Retain current authorization, align important business changes with the user, and reuse confirmed information that remains valid as needed.

## Return to the knowledge base at each stage

When starting work or a new conversation, first read Home and the existing overall index. When entering the next stage, read its corresponding guide first. Recheck affected content when goals change, rules conflict, a new method is adopted, or the knowledge base is updated. Reuse existing materials that remain valid as needed rather than rereading the entire knowledge base before every tiny action. If access is unavailable, explain the missing content and its impact. Do not claim to have followed rules that were not read.

## Realign when goals or environments change

Discussion, trial runs, practical experience, or business changes may alter requirements. Update the current statement of requirements, ask the user to confirm important changes, and realign affected workflows, nodes, and passing criteria. Do not let old plans constrain new requirements. When changing platforms, versions, accounts, or tool configuration, verify affected capabilities through Home's collaboration preparation and research entry points rather than mechanically repeating all preparation.

## Hand off the current state when switching conversations

When a switch is needed, prepare a concise handoff: current goals and scope; the user's views, experience, and key constraints; confirmed matters and adopted methods; questions awaiting discussion and assumptions awaiting verification; current stage, completed work, and actual verification results; related file or result locations; knowledge base entry points and content to read next. Explicitly mark goals that have not been determined rather than filling them with guesses presented as consensus.

Save the handoff in a location suited to the platform, or provide text that can be copied into the new conversation. The new conversation first reads the handoff and knowledge base, checks key goals, and continues the current stage rather than assuming it automatically inherits all history. Subsequently maintain only necessary progress and decisions, avoiding important information being left solely in lengthy chat histories.

## Handoff template and continuity checks

```text
Current goals and scope for this phase:
User views, experience, and key constraints:
Confirmed matters and adopted methods:
Questions awaiting discussion, assumptions awaiting verification, and their impact:
Current stage, completed work, and actual check results:
Entry points for code, documentation, changelog, Bug log, runtime logs, and Git:
Current code version, actual implementation status, and incomplete items:
Knowledge base entry points and guides to read next:
```

Fill in the template as actually needed and reference materials already provided directly. Mark uncertain information as unconfirmed. Do not require the user to complete all fields before discussion, or describe expected results as actual completion.

## Describe status by dimension

| Dimension | Standard terms and usage |
|-|-|
| Requirements and items | Confirmed, awaiting discussion, awaiting verification: current consensus, content awaiting a decision, and assumptions requiring actual verification, respectively. |
| Platform capabilities | Record separately whether officially supported, available in the current session, and dependent on unconfirmed conditions. Official support and current availability can both be true; do not treat them as mutually exclusive levels. |
| Evidence use | Supports a conclusion, practical reference for verification, or unproven lead; assess against the specific claim and current applicability conditions. |
| Implementation and delivery | Separately state not started, in progress, implemented, tested, running locally, deployed, acceptance in the actual environment, and known limitations. Passing tests cannot replace deployment or external acceptance. |

## What Git and each of the three log types record

| Record | Content and maintenance |
|-|-|
| Git commits and version tags | Preserve relatively complete actual code changes. At established delivery milestones, link versions to corresponding commits, tags, and records. Existing projects retain their original conventions; uploading to GitHub is not required. |
| Changelog | AI records what was done, why, how far work progressed, and actual verification results by the actual work date. Use summaries to link code or Bug records and avoid duplicate copying. |
| Bug log | AI records actual symptoms, investigation evidence, causes or unresolved questions, solutions, verification results, status, and linked runtime records. Retain the identifier for the same issue; the log can serve as a lookup dictionary for later searches. |
| Runtime logs | The program or existing tools automatically record actual events. Automatically create an empty file each day in the agreed time zone, append events when they occur, and leave it empty when no events occur. People and AI do not rewrite raw execution records. |

Archive feature documentation and the three types of logs alongside the feature. For integration, overall project documentation may reference the entry points. Follow the [Automatic Runtime Logging Standards](project-execution.md#build-automatic-runtime-logs-to-preserve-actual-execution) and relevant execution guide sections for log fields, day rollover, storage, exception handling, and verification details. For version examples, see [Version Conventions During Initiation](project-initiation.md#agree-on-version-records-and-handoff-during-initiation). Specify paths, formats, and storage conditions according to the actual environment rather than requiring every project to use one directory or log format. Daily empty files remain a requirement of this knowledge base. If the environment cannot support them, explain the actual limitations and discuss them rather than silently changing to file creation on the first run.

## Check historical records before fixing bugs

First search for the same or similar bugs. Then use corresponding runtime logs to check time, version, environment, steps, and actual execution, and determine whether historical solutions apply. If no usable records exist, investigate based on actual evidence. After a repair, verify it in practice and update the cause, solution, results, and related information in the Bug log. Do not mark it resolved without verification. See the [Historical Bug Search and Investigation Standards](project-execution.md#search-historical-logs-before-fixing-bugs-then-check-the-actual-problem) for the detailed process.

```text
Issue identifier, date, and actual status:
Feature or step, environment, and version:
Symptoms, expected results, and actual results:
Similar historical records and their applicability:
Corresponding run date, run ID, or safe evidence entry point:
Investigation process, verified cause, or judgment awaiting verification:
Solution and actual changes:
Actual checks, results, and remaining limitations:
```

## Accessible materials when reading is restricted

First verify the current file location, reading tools, and access permissions, and explain the missing content and its specific impact on the work. Ask the user for the currently needed body text, complete installation package, or an accessible copy if appropriate. Record the actual entry point, version, acquisition date, and update status, and use the installed version actually read as the basis for this task's rules. When a newer upstream version is known or the user provides an update, check version differences and their impact, then update the copy and necessary configuration as authorized. If differences cannot be checked, state the limitations. Do not claim the local copy is always current. Do not require Feishu access or assume the user's project materials, accounts, or logs should be made public.

If copy content or key rules cannot be obtained, do not pretend they have been followed. Continue organizing available materials and doing authorized work that does not depend on missing content. External recommendations requiring online verification still follow this knowledge base's requirements.
