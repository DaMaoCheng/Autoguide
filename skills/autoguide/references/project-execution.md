# Project Track | Execution and Progress Guide

**Keywords:** execution; progress; implementing the plan; dependency order; sections; modules; tasks; existing implementation; GitHub repository research; open-source reuse; repository maintenance; source version; licenses; reuse; unified rules; construction standards; code organization; code quality; module responsibilities; decoupling; file splitting; large files; 500 lines; 1000 lines; permitted long files; circular dependencies; complexity; structural self-checks; self-checks; acceptance criteria; test specifications; script checks; simulation of user operations; upstream and downstream connections; complete workflows; problem diagnosis; fixes; critical conditions; scope changes; real-time online research; progress records; Git; local repository; version number; commits; version tags; version history; handoff entry points; update logs; Bug logs; runtime logs; automatic recording; daily empty files; run identifiers; actual execution process; daily rollover; historical issue searches; similar issues; historical solutions; fix validation; user feedback; completion reports; framework and UI reuse; daily records; local logs; cloud logs; actual status; context management; handoff; switching chats

**Summary:** Work from current initiation and design documentation, task breakdown, and the node execution plan. Before substantial construction, read the entire current initiation and design description, then research GitHub in real time for relatively recent, maintained repositories fitting requirements and the implementation environment; confirm reusable parts, then adapt them. Prepare or retain Git records according to the actual environment, without requiring GitHub uploads, and advance parts by actual dependencies. Check existing implementation before each part and prioritize reuse. Clarify directories, responsibilities, and call relationships, controlling mixed responsibilities, duplicate logic, and complexity under code-organization standards. Use 500 and 1000 lines to trigger assessment, permitting more than 1000 lines when actually needed. Implement and actually self-check against acceptance criteria. When Bugs occur, search historical logs first and check solution applicability; validate fixes before continuing. Handle critical gaps and important changes, check complete workflows, record progress by day in update logs and actual faults and handling results in Bug logs. During construction, implement automatic runtime logs: create an empty file every day and append run events, linking actual steps and results by run identifier without user or AI intervention each time. Logs may reside locally or in the cloud. Maintain version numbers, corresponding code, and Git tags at delivery milestones and support continuity of progress. Continue within authorization after self-checks pass without requiring confirmation after each chapter. Report actual results after current work, and follow user feedback for subsequent modifications and operating adjustments, retaining the existing framework and UI, prioritizing reuse, and recording actual changes.

For users and collaborating AI assistants with current project goals, first-phase scope, node execution methods, and corresponding acceptance bases who are ready to start or continue implementation. Read [Home](index.md), the [Design Document Guide](project-design.md), and the [Node Design and Execution Methods Guide](project-node-design.md), then check actual project documents, implementation, and progress. Retain user leadership, plain communication, real-time online research, and continued consultation; do not invent a different business plan during execution.

## Follow the Current Plan and Advance by Actual Dependencies

The execution sequence is: read current plan → determine current task by dependencies → inspect and reuse existing content → implement → self-check against criteria and fix → update progress → continue. When critical plans and acceptance conditions are clear, proceed directly without adding a complex startup process or duplicate documentation.

Whenever beginning work, entering a new part, or switching chats, check current goals, first-phase boundaries, feature hierarchy, paths, node execution methods, acceptance criteria, test specifications, and unresolved matters. Confirm actual directories, operating environment, and relevant outcomes. Do not rely solely on early chats, old document versions, or remembered code state.

### Find Reusable GitHub Repositories Before Substantial Work

Before initial substantial construction, read the entire current initiation and design description to understand first-phase goals, overall functionality, deployment, and maintenance conditions. Then search GitHub in real time for repositories to reuse or learn from. Search using user requirements, critical features, implementation conditions, and relevant Chinese and foreign-language keywords. Do not decide to write from scratch solely from AI memory, or rely only on rankings and search snippets.

Focus on relatively recent, maintained implementations. Read README files, runnable examples, necessary code, Releases, recent commits, and Issues. Check current versions, completeness, deployment requirements, dependencies, known problems, and actual adaptation effort. Recent maintenance is an important signal, but publication date, latest tag, or Stars alone does not establish reliability. Choose a version fitting current goals, the deployment environment, and maintenance conditions.

Reuse a suitable overall project foundation or only relevant modules, scripts, and components. Once suitable, permitted content is found, obtain the code, understand it, and check compatibility with the existing project before adapting, integrating, and validating it against confirmed requirements. Do not require indiscriminately importing the whole repository. If no suitable repository exists, explain the research outcome, then use existing tools or implement the needed work. Do not change user goals merely to enable reuse.

Before adoption, check the repository's LICENSE and usage conditions for required parts, preserving required copyright and license notices. Public visibility does not grant unrestricted copying and modification. If licensing is unclear, do not describe reuse as authorized; continue checking or select an explicitly permitted alternative. Preserve the repository link, adopted version or commit, research date, reuse scope, adaptation reasons, and main modifications for later diagnosis, upgrades, and handoff.

Integrate confirmed reuse into current project documentation and record introductions or adaptations in that day's update log. If a candidate repository changes a critical plan, discuss it with the user under the important-change rules. Routine adaptation proceeds under existing authorization. Research again as needed for new independent requirements or environment changes; do not search repositories afresh at every small step.

### Prepare Git Records and Maintain Versions at Delivery Milestones

Before substantive code changes, check whether a Git repository exists, the actual code location, and initiation agreements. Retain existing repositories and history. If none exists, establish version records in a project location appropriate to the current environment, avoiding initialization in the wrong directory, generated-artifact directories, or inside an existing repository. Storage may be a local project directory, cloud work environment, or deployment target machine. Designate one primary record location so relevant code and history are preserved and accessible to authorized successors.

Git preserves code changes and traceable versions. Uploading to GitHub, registering a code-hosting account, creating a remote repository, and learning Git commands are not required. Choose arrangements suited to local, cloud, or target-machine conditions without maintaining duplicate records in all three. If the deployment platform cannot persist Git history, maintain it in a local or cloud work directory that can preserve the complete project, and document its mapping to deployed versions. Verify specific platform capabilities and configuration methods in real time against the current environment.

The AI prepares the repository, commits changes, and maintains version numbers and tags, explaining current progress, version, and storage location to the user. Include actual code, necessary configuration templates, project documentation, and applicable tests. Retain existing ignore rules and inspect actual content; exclude credentials, real business data, and large volumes of regenerable files. Match record detail to project size and keep simple projects simple.

After each relatively complete change with a clear purpose, self-check against corresponding criteria and save a Git commit stating which feature or part it concerns, what changed, and why; retain relevant validation results in logs. Limit the commit to current changes and protect existing user and collaborator modifications. If unfinished work needs an interim save, record progress but explicitly mark unfinished, unvalidated, or failed status and remaining items. Do not present a progress commit as an accepted delivery.

Follow version rules agreed during initiation; see examples in the [Initiation Guide](project-initiation.md). One delivery version may contain multiple commits. Update its number only after corresponding acceptance conditions are met, then create an annotated version tag, such as v1.1.0, on the exact corresponding Git commit. Preserve delivered code and tags; subsequent modifications produce new versions. Daily commits and log updates do not automatically increment versions.

Use the project's existing version file or configuration as the primary source for its current version number. If none exists, explicitly record it in an appropriate location and reference it in project documentation. When forming a version, check consistency among its number, code, Git tag, and update log. Separately record actual states such as in development, accepted, and deployed, along with the actual deployed version. The latest development version is not automatically the deployed version. Before another AI or technical colleague resumes work, check these records, actual directories and code, and uncommitted changes.

Sections locate responsibilities and tasks; implementation follows dependencies. If a later section provides the foundation for an earlier one, complete the foundation first instead of mechanically following contents order. Proceed directly with confirmed simple parts. Fill critical conditions for parts with gaps first; all later details need not be settled before any work can begin.

## Inspect Actual Existing Implementation Before Starting Each Part

Review relevant existing functions, components, scripts, rules, configuration, interfaces, and data processing, understanding their responsibilities, inputs and outputs, consumers, applicability, and current status. Actually read or check earlier outcomes. Do not assume from memory that a capability exists, or treat “exists in code” as “validated.”

Directly reuse content matching current needs under applicable conditions. Keep fields, naming, data formats, decision rules, and handling consistent to reduce duplicate implementation and divergent rule versions. Follow existing design when adjustments are needed, inspecting consumers and affected behavior. Do not force unsuitable reuse or rewrite existing outcomes without evidence.

**Example:** If earlier work implemented unified account-field validation and scoring rules, later group-assignment or summary features should use the same confirmed logic. When fields or weights change, update the unified source and related descriptions rather than copying and modifying a separate version in another section. This example illustrates reuse; it does not mean any particular project already has the implementation.

### Code Organization and Ongoing Maintenance Standards

Keep code and files understandable, modifiable, verifiable, and transferable throughout progress. Do not accumulate unrelated business responsibilities indefinitely in one giant file or keep adding mixed responsibilities to “get it running first.” Assess responsibilities, dependencies, duplicate logic, and real maintenance cost; line counts prompt inspection. The AI handles technical details according to current requirements, language, framework, project scale, and deployment environment, explaining arrangements and impact in language the user understands.

#### Clarify Directories, Module Responsibilities, and Call Relationships First

Before substantive construction, translate the initiation document's feature hierarchy into suitable code organization, describing main directory purposes, module responsibilities, inputs and outputs, and dependency direction. Prefer appropriate conventions in existing projects. Use simple structures for simple scripts rather than imposing a layered architecture or fixed directory template universally. Verify recommendations for new structure, languages, or tools online in real time using official sources and relevant practice, and choose against the actual environment rather than solely from AI memory.

#### Organize Files Around Clear Primary Responsibilities

Entry points initialize, connect, or organize workflows, while business details belong in relevant modules. Distinguish user interaction, business decisions, data reading and storage, conversion, configuration, and other content by actual responsibilities, splitting only when needed. One responsibility may include several related functions or files; do not impose one feature or one function per file. Function names describe purpose. Break complex decisions into understandable steps, and use comments to explain necessary business reasons, constraints, or exceptions.

Example: organize order processing by the following responsibilities. This is a conceptual ownership tree; actual directories, filenames, and depth of splitting depend on the project environment. Separately explain inputs, outputs, and failure results between obtaining, filtering, matching, and exporting orders.

```plaintext
Order processing
├─ Workflow entry point
├─ Obtain orders
│  ├─ File import
│  └─ API retrieval
├─ Filtering rules
├─ Product matching
└─ Information export
```

#### Use File Length to Trigger Assessment and Allow Reasonable Long Files

If the project has no explicit rules, initially use the following assessment reminders, adjusting for language, file type, business characteristics, and existing conventions. 500 and 1000 lines are starting reminder thresholds for this workflow, not universal industry limits. Assessments may exclude blank lines and comment-only lines, but must not evade checks by compressing code, removing necessary comments, or mechanically fragmenting files.

| Situation | Required AI Action |
|-|-|
| Maintained business-code file approaches or exceeds 500 lines | Inspect primary responsibilities, duplicate logic, complex decisions, dependencies, and change impact; assess whether appropriate splitting is needed. |
| Exceeds 1000 lines | Assess maintainability and benefits of splitting. Exceeding this length is allowed when actually needed. Retain files whose responsibilities are clear, whose splitting offers no practical benefit, and which remain understandable, modifiable, and verifiable. Briefly record reasons in project documentation and reassess when adding content. |
| Mixed responsibilities, confused dependencies, or small changes affecting unrelated features | Assess and resolve structural issues involved in the current change even if the file is short. Being below the line-count threshold does not justify continued accumulation. |
| Build or code-generation artifacts, third-party code, large static data | Classify separately and record sources and generation or update methods. Check under applicable rules rather than mechanically splitting as business files. AI-written business code remains maintained code and does not qualify for this exception merely because AI generated it. |

Exceeding 1000 lines alone does not automatically mean failure, require user approval, or halt the whole project. After inspection, the AI chooses suitable handling within existing authorization. If actual mixed responsibilities, continued accumulation, or difficulty making safe changes exist, perform the smallest relevant split for current requirements first, then continue dependent work.

#### Give Shared Behavior a Unified Source and Check Reuse Before Adding

Actually read existing implementation first. Maintain the same business rule, calculation, validation, or conversion in a clear location wherever practical, and have relevant features call it to avoid inconsistent copies. Share similar fragments only when their business meaning and reasons for change align; superficial resemblance does not justify merging different rules. Shared directories contain genuinely shared content rather than miscellaneous clutter. Do not prebuild extensive extension layers, interfaces, or general frameworks for hypothetical requirements.

#### Have Modules Collaborate Through Explicit Contracts

State required inputs, produced outputs, states, and failure results so dependencies are traceable. Avoid circular dependencies, secretly changing another module's internal data, duplicated maintenance of the same state, and hard-to-discover global state. Use simple implementation methods suited to the current technology stack. The goal is to limit effects on other modules when one changes, not to require separately deploying modules as multiple services.

#### Keep File Purposes and Active Implementations Clear

Names reflect actual purpose, and related business content is grouped around the same feature. Distinguish configuration, static data, tests, and generated artifacts as needed. Avoid long-term coexistence of active implementations with the same responsibility named final2, new3, backup-latest, and similar variants; preserve history through Git. After splitting or replacing, check all consumers, references, and configuration. Remove old implementation only when confirmed unnecessary and permitted by authorization, protecting existing user changes and necessary records. Update actual directories, responsibilities, and paths in project documentation, distinguishing planned from implemented structure.

#### Check Functionality and Structure After Each Part

Actually check functionality against existing acceptance criteria, then inspect whether the change introduces mixed responsibilities, duplicate rules, circular dependencies, hidden state, hard-to-understand long functions, or unnecessary abstractions. Prefer existing project tools for formatting, syntax, types, complexity, or dependencies. If no suitable tool exists, use small helper scripts or targeted reading without requiring a large tool system for simple projects. Verify tools, rules, and numbers against the current language and environment. Automated checks find problems but do not replace responsibility assessment or actual business validation.

#### Advance Structural Changes in Steps, Validating Before Continuing

Before splitting, establish original entry points, outputs, state, consumers, and critical validation points, retaining a suitable Git checkpoint. Extract a small part involved in current requirements by responsibility or call relationship, preserve original behavior, and validate relevant features, interactions, and upstream and downstream relationships before continuing. Resolve validation failures first. If needed, return to a suitable checkpoint while protecting existing modifications instead of layering on further splitting. Record structural changes, reasons, validation results, and actual remaining items in the existing update log and update project documentation. Do not create a new version for every file split.

Structural governance serves current requirements. Avoid renovating the whole project simply because old code looks untidy, splitting into many files that only forward calls, or introducing layers without practical benefit. Follow existing change rules for major plans, scope, or dependency changes. The AI handles routine reversible splitting within authorization; coding novices need not decide professional design details.

## Implement the Current Part, Actually Self-Check, Then Continue

Complete implementation around the current task and confirmed node plan, preserving user content and other outcomes within scope. Execute explicit rules through code, configuration, or existing capabilities. Implement model nodes according to the confirmed plan; do not silently turn fixed logic into free model judgment during execution.

After each part, actually check it against acceptance criteria and test specifications in project documentation. Under “Code Organization and Ongoing Maintenance Standards,” check responsibilities, duplicate logic, dependencies, and file organization, resolving actual structural issues introduced by the current change. Check affected behavior for simple changes and relevant consumers and connections for shared rules and core parts. Match depth to actual impact rather than mechanically running the whole suite for every small step.

Select checking methods by feature. Check actual inputs and outputs for calculations and data processing, simulate user clicks and data entry and check final results for interactions, and check consistent data formats, rules, and states across upstream and downstream parts. Refer to “Validation and Acceptance” in the design document guide rather than maintaining another standard.

Self-checks require actual execution results and pass evidence. Reading the code, completing an operation, or seeing no error does not justify declaring a pass. Accurately record scope and limitations for unexecuted, unavailable, or simulated-only checks. Resolve issues affecting current completion or downstream dependencies and perform targeted rechecks before continuing dependent work.

After necessary checks pass, continue to the next part within authorization without requiring user confirmation after every chapter or passing check. Repeat or expand checks only when new changes, failures, or unresolved impact warrant it, rather than mechanically revalidating steps that already passed.

When critical minimum requirements or necessary acceptance checks fail, continue diagnosis, fixes, and revalidation within existing authorization, following the historical Bug and runtime-log process. If objective conditions or the existing plan cannot meet them, explain the failure, impact on the user's work, and feasible options in business language, preserving an honest incomplete status. Do not advance dependent parts until the condition is met; other authorized work whose conditions are met may continue. Do not silently lower minimum requirements or acceptance expectations, or promise unvalidated effects to report completion. The user decides important tradeoffs that change confirmed goals or minimum requirements after understanding them.

## Investigate Problems First and Handle Critical Gaps by Dependency

### Search Historical Logs Before Fixing Bugs, Then Check the Actual Problem

When faults occur during new-project construction or later maintenance, first obtain the Bug-log entry point from project documentation or configuration. Search identical and similar issues as one would consult a dictionary, then read corresponding automatic runtime logs by current time, run identifier, feature, or error. Check actual steps, results, versions, and environment before selecting a fix. If records are absent or incomplete, explain the limitation and continue examining other real evidence; do not assume missing steps succeeded. Historical records are reusable diagnostic clues, not proof that similarly named symptoms have the same cause.

1. Search Bug logs using actual errors, abnormal behavior, affected features, relevant interfaces, or input conditions, looking first for identical issues and then similar ones. Review existing investigations, causes, solutions, failed attempts, validation results, and the environment and version at the time.
2. Compare current environment, version, triggers, and implementation to assess applicability. Prefer a validated historical solution when applicable, making necessary adjustments for current requirements. Do not copy based only on similar titles or treat an unvalidated or failed old approach as a successful answer.
3. If logs are missing, inaccessible, or contain no applicable record, explain the actual situation and continue diagnosing from errors, logs, inputs and outputs, environment, and existing implementation, distinguishing facts from hypotheses. Verify uncertain external capabilities and technical conclusions online in real time. Missing historical answers must not stop feasible investigation.
4. After a fix, actually validate against relevant acceptance criteria and test specifications, checking affected upstream and downstream behavior and user operations as needed. Continue investigation within current authorization if validation fails. Do not record resolution before validation passes or treat a test-tool failure as a business-feature pass.
5. Record current symptoms, conditions, causes or uncertainties, adopted solution, validation method and results, actual status, and known versions in the Bug log using searchable descriptions. Reuse the existing issue identifier for the same problem, adding daily progress or recurrence conditions. Create a new record only for a genuinely different issue. Briefly link the corresponding Bug record in the update log without duplicating all fault details.

For uncertain external tools, platform capabilities, or implementation methods, research current Chinese and international material online in real time under Home and the node design guide, verifying against the actual environment. Do not keep repeating failed attempts without new evidence. Explain reasons and impact when changing the plan, distinguishing routine implementation details from important business or plan changes.

When necessary materials, permissions, credentials, or critical decisions are missing, record what is missing, which step is affected, attempts made, and the current assessment, and request the specific information needed. Pause dependent parts; other authorized work that does not depend on the condition can continue. Do not invent data, capabilities, or results to maintain apparent progress.

## Return Important Changes to Discussion and Update Relevant Main Text

When execution reveals new requirements, changed business rules, or a critical plan needing adjustment, understand the reasons first. Explain in business language how daily operations, outcomes, delivery arrangements, and later maintenance will change, then the impact on first-phase scope, existing implementation, deployment environment, and acceptance. Continue discussing important tradeoffs from the user's views. Verify new tool selections and external-capability judgments online in real time before recommending them from existing knowledge alone.

The user confirms business rules, critical scope, and important plan changes. Handle reversible, low-risk routine implementation details within authorization according to project conventions rather than turning each detail into repeated confirmation. See the [Initiation Guide](project-initiation.md) for requirement phasing; do not silently expand first-phase goals.

Once a change is settled, update corresponding project-description sections, node plans, acceptance criteria, and test specifications, checking related implementation and references. Briefly record reasons and impact for important changes, keeping the main text a complete current plan rather than only appending patches at the end. Reuse verified, still-applicable external material as needed; do not mechanically search again for every line of implementation.

## Check Complete Connections and Preserve Progress That Others Can Continue

After relevant parts are complete, check critical full workflows according to actual dependencies. From the user's or system's actual entry point through final delivery, check upstream and downstream connections, state transitions, data storage, and business results. Passing individual parts does not establish that the whole workflow is usable. Overall checks still follow current acceptance criteria and actual impact.

### Maintain Change Logs and Bug Logs by Day

The project retains three log types with distinct purposes. Update logs and Bug logs cover progress and maintenance, organized by actual work date. Runtime logs are automatically generated and appended by the project during actual operation, organized by event date; see the automatic-runtime-log section below. Store them locally or in the cloud, retaining existing locations. If no arrangement exists, choose storage appropriate to the environment and document entry points and primary record locations so the user and later AI assistants can find them.

Use either two documents with YYYY-MM-DD sections or date-named files in two log directories. One arrangement suitable for the project suffices; filenames are not fixed, and duplicate local and cloud recording is not required. Update corresponding logs on days with actual progress, changes, or issue handling. Do not create empty records when there is no work content.

| Log Type | Recorded Content |
|-|-|
| Update log | Which section or feature advanced that day, what was completed or adjusted, outcome locations, actual self-check or validation status, unfinished work, and next steps. Include source and adoption scope for introduced or adapted repositories. Record actual versions when formal versions exist; do not create version numbers for every small step. |
| Bug log | Discovery date of an actual fault, affected feature, symptoms and occurrence conditions, relevant evidence, cause or assessment pending investigation, actions taken, validation results, and current status. Record unresolved or unfixed faults truthfully, without describing them as resolved. |

Initial construction mainly records progress and work in update logs; do not list every planned, unimplemented feature as a Bug. Use Bug logs for actual faults. When one issue spans days, preserve its identifier or record entry point and add investigation, fix, and validation progress under corresponding dates instead of recreating it as a new issue daily.

If a Bug fix also changes the project, briefly record the fix in that day's update log and link its Bug record. Keep fault detail in the Bug log without duplicating whole passages. Acceptance criteria and the current plan stay in project documentation; logs record real changes and handling history, not a replacement for current text or evidence of validated outcomes by themselves.

When a version is formed, record its number, main changes, actual validation results, and Git tag or commit entry point in the corresponding day's update log. Associate ordinary progress with commits as appropriate without creating a version for every entry. Bug logs record affected versions when known and the fix version after actual delivery; do not prewrite resolution for unfixed issues. Dates archive daily work; versions locate corresponding outcomes. Continue using update logs and Bug logs for version changes and fault handling, while storing raw automatically generated execution processes separately in runtime logs, without copying them into project-change text.

### Build Automatic Runtime Logs to Preserve Actual Execution

Runtime logging is a capability of the project itself, designed and implemented during construction. Programs, scripts, or existing environment logging tools write it automatically during actual runs. It requires no manual user entries, daily user actions, AI intervention for every run, or model-generated logs. It records what actually happened. Update logs record project changes; Bug logs record investigation, solutions, and validation. Maintain all three separately and connect them as needed.

#### Automatically Create Empty Files Daily and Append Events

Specify the project time zone, daily rollover time, and log directory or cloud storage location in project documentation. Automatically create a new empty log file every agreed day, for example runtime/2026-10-08.log. Append each run or relevant execution event to that day's file. Leave it empty when no runtime events occur; do not write fabricated results or “completed normally” placeholders. The example path is not a universal directory requirement.

Selection and implementation must meet “automatically create the day's empty file even without runtime events.” A method that creates or rolls over files only on first output is insufficient. Reuse existing daily-rollover capability appropriate to the environment, or automate it through programs, scripts, and the runtime environment's scheduler. Automatically check the day's file on startup or recovery and append if it exists; never overwrite or clear it. Automatic log-file creation requires neither daily user wakeups nor AI operations. If the whole environment is down or storage unavailable, record confirmable gaps and recovery without fabricating runtime records for downtime. Timely daily creation depends on an environment that can actually run.

#### Correlate Each Run and Trace Critical Steps and Results

Define one run as a workflow, task, request, or business operation according to actual execution. Do not record a continuously available service only as one undiagnosable “running” entry. Assign or reuse a distinct run identifier so start, nodes, calls, retries, and end can be connected. Different runs must not share an indistinguishable identifier. For runs spanning days, write each event to its occurrence-date file, retaining the same run identifier to connect the whole process.

Use fixed searchable, parseable fields, selecting format according to existing tools and environment. Record event time and time zone, run identifier, project version and necessary environment details, executing module or step, event type or level, key conditions and processed-count summaries, result status, and necessary elapsed time. Automatically record failed nodes, actual error or exception details, retry counts, and follow-up handling when problems occur. Record input and output summaries or safe references needed for diagnosis rather than dumping all business data.

Actually write entries at startup, critical-step progress, external calls, and completion or failure, distinguishing normal, warning, and error events. End records state actual outcomes such as success, failure, partial success, skipped, or interrupted. Without an end record, a start record alone cannot establish success. Do not directly log passwords, keys, login credentials, or sensitive personal information. Redact necessary content first, retaining nonsensitive diagnostic information.

#### Have the AI Read Logs as Diagnostic Evidence When Problems Occur

For later Bug handling, still search historical solutions for identical or similar problems in Bug logs first. Then read corresponding runtime logs using user-reported time, affected feature, run identifier, or error, and check causes against the version, environment, input conditions, and execution path at the time. Runtime logs establish what actually happened, where failure occurred, and whether retries took place. Compare historical solutions with that evidence rather than applying them solely from identical symptoms. An empty file shows only that no events were recorded; it does not prove operational health or business-execution success.

Actually validate fixes and record investigation, cause, solution, results, and corresponding runtime-log date, run identifier, or entry point in the Bug log, reusing existing identifiers for the same issue. Record ordinary changes in the update log. Retain raw runtime logs as actual history; do not rewrite them into fix conclusions or have AI backfill nonexistent events. New runs after fixes automatically generate new records for later comparison.

#### Arrange Storage and Validation for the Deployment Environment

Storage may be local or cloud-based. Prefer existing logging capability, specify read permissions, retention periods, and necessary automatic archiving according to volume and environment, and prevent unbounded growth. Do not default to adding paid services or a new tool system. If logging fails, retain clues through fallback error output or status notifications permitted by the environment. Do not silently claim logs are complete or let routine logging errors repeatedly cause cascading failures. Verify implementation capabilities of the current language, tools, and runtime environment in real time.

Include runtime logging in project acceptance criteria and test specifications. Actually check records for normal runs, faults, and retries, verifying that run identifiers, steps, times, and results can be correlated. Check automatic empty-file creation on an event-free day, rollover across days, and restart appending without clearing existing content. Check necessary concurrent writing, permissions, redaction, and retention policies according to project scale. State test conditions when validating rollover with a controlled clock or test scheduler. Configuration changes alone or generated example logs do not constitute actual automatic-runtime validation.

Runtime-log verification entry points: [OpenTelemetry: Times, Correlation Identifiers, and Log Fields](https://opentelemetry.io/docs/specs/otel/logs/data-model/), [Tencent Cloud: Request Start, End, Exceptions, and Run Identifiers](https://cloud.tencent.com/document/product/583/60336), [Microsoft: Structured Logging, Time Zones, Retries, and Sensitive Information](https://learn.microsoft.com/zh-cn/azure/architecture/best-practices/monitoring), [Python: Time-Based Log Rollover and Its Output-Triggered Conditions](https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler). Checked on 2026-10-08, these provide Chinese and international official references without fixing a technology stack or cloud platform. Daily empty files are an explicit requirement of this workflow. Verify that adopted tools meet it; “daily rollover” does not automatically mean “create a file every day even without events.”

Match log detail to project scale, prioritizing outcomes, reasons, and remaining items useful for continuity. Do not transcribe entire conversations, every command, or every small action, and never record credentials. Ensure relevant logs match actual current progress before switching chats.

| Status or Record | Description Requirements |
|-|-|
| Implemented | Relevant code, configuration, or outcomes are complete. State their locations; this does not automatically mean tests passed. |
| Validated | State checking methods, environment, scope, actual results, and necessary evidence; do not extend claims to unchecked parts. |
| Unvalidated or insufficient conditions | Explain reasons, impact, required conditions, and independent work that can continue. |
| Remaining issues and next steps | Locate issues in relevant parts and clarify the next task and dependencies so a successor can continue. |

When switching chats or handing off to another AI, first read Home, the current-stage guide, project documentation, update logs, relevant Bug logs, and actual progress. Check documented code and Git locations, current version and corresponding tag or commit, actual deployed version, validation status, and unfinished work. Then inspect relevant implementation and uncommitted changes as needed before continuing. If a new chat or project is needed, follow Home's context-management method and current authorization instead of relying solely on verbal chat summaries.

### Report After Self-Checks and Follow User Feedback for Later Changes

After completing current authorized work and necessary self-checks, report what was done, what was actually checked, the results, current version or delivery status, known limitations, and unfinished checks. Accurately distinguish implemented, tested, running locally, deployed, and accepted in the actual environment. Passing tests does not automatically mean deployment or online acceptance. Reporting communicates actual results; it does not replace acceptance criteria, test specifications, or actual self-checks. Do not introduce a process of awaiting user review after each chapter.

Subsequent changes, adjustments during continuous operation, outcome recording, and iteration follow user feedback or requirements. Understand the behavior the user wants to change, complete authorized modifications, necessary validation, and related fixes, then report results. Execute clear feedback directly; ask only about gaps that cannot be verified and materially affect results or risk. Completion of the current task does not authorize adding features, expanding scope, or starting monitoring or scheduled tasks independently. When the user explicitly requests continuous operation, complete corresponding setup and validation, then follow that authorization and feedback.

Actually read current implementation before modifications, retaining the existing framework, UI, components, modules, scripts, and unified rules. Directly reuse what can serve the need, making necessary changes for current requirements. Do not create a separate UI, duplicate existing features, or rewrite the whole project solely from AI preference. If the original plan genuinely cannot meet requirements, explain specific limitations, the adjustment, and its impact, then proceed under existing important-change rules.

Record ordinary modifications and additions by day in update logs, and fault investigation, fixes, and validation in Bug logs. Follow this guide's historical-log search process before fixing Bugs. Maintain current project-description text, related paths, and actual status together, following established delivery-milestone rules for versions and Git records. Report actual results after each feedback request is handled; later user feedback continues to determine what changes next.

### Completion Conditions for the Current Stage

- Authorized scope reported as complete is actually implemented and checked under corresponding acceptance and testing requirements. Results for critical paths and affected existing features are clear.
- Current documentation, update logs, Bug logs, and agreed version records match actual changes. Automatic runtime logging, daily rollover, and appending are validated against the actual environment, with limitations recorded honestly.
- Usage, code, and record entry points can be located, and delivery status and unfinished matters have been reported truthfully. Tested does not mean deployed or accepted in the actual environment; subsequent work follows user feedback.

Check these conditions against the current scope and impact without adding a process of waiting for approval after every chapter. Verify unconfirmed critical conditions before progressing dependent parts; continue other work whose conditions are met and which is authorized. Shared methods: [Shared Guide | Web Research and Evidence Assessment](shared-research.md); [Shared Guide | Collaboration Preparation and Configuration](shared-preparation.md); [Shared Guide | Changes, Records, and Handover](shared-changes.md).

### References and Verification Entry Points

[Microsoft: Appropriate Testing Levels and Result Analysis for Business Requirements](https://learn.microsoft.com/en-us/azure/well-architected/design-guides/testing) and [Google: Maintain Current Project Documentation as Implementation Changes](https://docs.cloud.google.com/architecture/framework#document_your_architecture) aid verification. [Playwright: Simulate Browser Operations](https://playwright.dev/docs/input) and [Playwright: Check Actual Results](https://playwright.dev/docs/test-assertions) provide interaction-validation examples. Sources were checked on 2026-10-08. They do not imply implementation or testing in the current project, nor require these platforms. New technical recommendations still need real-time online verification for the current task.

Repository-reuse verification entry points: [GitHub: Recent Repository Activity](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity), [GitHub: Releases and Versions](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), [GitHub: Licenses and Usage Conditions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). Checked on 2026-10-08. Actual repositories still require real-time research and inspection against current needs; these entry points do not mean a repository has been selected for any project.

Version and Git verification entry points: [Semantic Versioning](https://semver.org/lang/zh-CN/spec/v2.0.0.html), [Git: Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository), [Git: Version Tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging.html). Checked on 2026-10-08, they provide reference rules. Verify actual storage locations, platform capabilities, and implementation methods in real time for the project; no code-hosting platform is fixed.

Code-organization verification entry points: [Microsoft: Separation of Responsibilities, Explicit Dependencies, and Reuse](https://learn.microsoft.com/zh-cn/dotnet/architecture/modern-web-apps-azure/architectural-principles), [Google: Reviewing Design, Complexity, Testing, and Maintenance](https://google.github.io/eng-practices/review/reviewer/looking-for.html), [ESLint: File-Length Rules and Configurable Options](https://eslint.org/docs/latest/rules/max-lines). Checked on 2026-10-08. Adopt applicable principles without making .NET or JavaScript tools mandatory for every project. This workflow's 500- and 1000-line reminder thresholds are project conventions; actual languages, tool capabilities, and exceptions still require real-time verification against the environment.
