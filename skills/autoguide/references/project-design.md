# Project Track | Design Document Guide

**Keywords:** project description; project initiation and design description; DESIGN.md; document structure; feature hierarchy; nested features; hierarchy tree; usage paths; execution paths; information flow; directory structure; code organization; construction standards; module responsibilities; call relationships; file splitting; large-file assessment; permitted long files; structural checks; feature descriptions; state transitions; interruption recovery; duplicate prevention; requirement mapping; acceptance criteria; test specifications; acceptance methods; simulation of user operations; test environment; test results; acceptance cases; examples; document maintenance; version number; Git; repository location; version tags; delivery status; log entry points; runtime logs; automatic recording; daily empty files; run identifiers; log acceptance; handoff

**Summary:** Guide the AI in organizing user-confirmed initiation and task breakdown into one complete, continuously maintained project description. Explain goals, feature hierarchy, different paths, specific features, runtime states, and acceptance mappings. Distinguish acceptance criteria, test specifications, and actual results. Choose script checks, user-operation simulation, and complete-workflow validation by feature, using hierarchy trees, execution paths, and feature examples to illustrate the writing. Record actual directories, code responsibilities, call relationships, and maintenance conventions. Assess long files according to actual needs and explain reasons for retaining them. Record entry points for automatic runtime logs, daily empty-file creation and event appending, run identifiers, and acceptance arrangements, distinguishing them from update logs and Bug logs. Preserve the status of undecided designs and fill them in through later discussion and actual implementation.

For users and collaborating AI assistants who need to organize current project agreements to support implementation and handoff. Read [Home](index.md), the [Initiation Guide](project-initiation.md), and the [Task Breakdown Guide](project-work-breakdown.md) first. Follow user leadership, plain communication, real-time online research, patience, and realistic time expectations. Do not ask users to produce technical designs themselves.

## Organize Current Agreements into a Continuously Maintained Project Description

The document may be titled “Project Initiation and Design Description,” saved as DESIGN.md in the project, or placed somewhere appropriate on the current platform. Extend and integrate existing documentation when it can serve this purpose. No particular filename is mandatory, and user content must not be overwritten.

Create an initial version during initiation, then add complete feature hierarchy and workflows during task breakdown. Once later designs have been discussed and confirmed, add execution methods, data, file directories, and deployment arrangements. Mark undecided technology plans, models, and specific nodes as pending discussion; do not invent plans to fill a table of contents. Technology stacks and directories in illustrations belong only to their example projects, not a fixed template for all projects.

The AI organizes the main text using the user's experience and confirmed requirements; the user checks critical business meaning. Verify technical recommendations online in real time under Home, explaining applicability conditions, tradeoff reasons, and what still needs validation. Details may be refined over several rounds. Unconfirmed content must not be written as settled rules.

## Organize the Main Text with a Complete Structure

The following is a basic structure for project documentation; add, remove, and expand sections as appropriate. Section titles can change, but do not omit critical content affecting understanding, implementation, or acceptance. Explain why a part is inapplicable; keep unknowns pending confirmation.

| Section | Required Content |
|-|-|
| Project overview | Current problem, why the project is needed, users, and the ultimate desired outcome. |
| Goals and phases | Overall goal, first-phase goal, included and excluded content, later requirements, and important constraints. |
| Usage scenarios and roles | Who uses it under which circumstances, what each role does, and relevant operation permissions. |
| Complete feature hierarchy | Ownership and responsibilities across the project, modules, features, subfeatures, and specific actions. |
| Core business workflow | Overall workflow and progressively expanded steps, decisions, conditional branches, waiting, repetition, and ending conditions. |
| Overall architecture and execution methods | How parts collaborate, which use rules, scripts, tools, or models, and why. |
| Data and external connections | Data sources, critical fields, storage locations, transfer direction, external systems, and connection constraints. |
| Project directory structure | Purposes of directories and files and their mapping to modules and features; distinguish unimplemented designs from actual paths. |
| Deployment, operation, and maintenance | Deployment location, startup and configuration, maintenance responsibilities, fault diagnosis, and recovery. |
| Validation and acceptance | How first-phase requirements map to features and workflows, acceptance criteria, checking environments, data or user operations, expected results, and pass conditions; record actual results, evidence, and unvalidated parts. |
| Matters pending confirmation or validation | Undecided issues, missing materials, critical assumptions, affected scope, and validation arrangements. |
| Important decisions and changes | What was decided or changed, why, and its impact; update related main text together and retain a brief change history. |

## Explain Hierarchy and Different Paths Clearly

Expand as many levels as actually exist. At each level, explain its parent, responsibilities, contents, and relationships with other parts; do not stop at a name such as “module X.” Use continuous numbering, contents, and section links to move from overview to detailed rules. Expand complex parts separately when needed, retaining parent and child-document links.

Distinguish containment from operation: the hierarchy tree shows which parts contain which content, while workflows show execution order, conditions, and transitions. Expand multiple branches within actual features, without forcing every decision result into a separate code module.

| Path Type | Description Requirements |
|-|-|
| Usage paths | Through which entry point the user or system enters which feature, required conditions, and the destination after the operation. |
| Execution paths | Step order, conditional branches, loops, waiting, returns, and endings; where failures go. |
| Information flow | What information one part passes to another, what is returned after processing, and where it is ultimately saved or delivered. |
| File and code paths | Which directory or file carries each part and its responsibilities; add real paths once the design is settled or implemented. |

### Example: Expanding Nested Features and Workflows

**The following is an illustrative project showing how to write the description; it does not represent actual order or foreign-exchange settlement rules.** Retain readable textual examples of this kind to help the AI understand the required granularity. Rewrite them around the user's actual business; do not copy them with only the project name changed.

```plaintext
Order processing project
└─ Foreign-exchange settlement management
   └─ Generate settlement materials
      ├─ Obtain orders
      │  ├─ Upload files
      │  └─ Retrieve through an API
      ├─ Filter usable orders
      │  ├─ Check delivery receipt status
      │  ├─ Check whether already used
      │  └─ Handle missing information
      └─ Generate platform files
         ├─ Select platform template
         ├─ Match product information
         │  ├─ Successful match
         │  └─ Handle failed match
         └─ Export and record
```

“Successful match” and “Handle failed match” expand possible results and handling within the feature. They do not require separate modules, files, or automation nodes. Real projects still need responsibilities, conditions, specific steps, and results for the relevant parts.

### Example: Execution Direction and Conditional Paths

```plaintext
Obtain orders → Check delivery receipt status → Check whether already used → Match product information
Successful match → Generate platform files → Export and record → Current workflow complete
Failed match → Review missing or conflicting information → Add and confirm information → Match again
Information still insufficient → Pause this order → Record reason and wait for additions → Return to matching when conditions are met
```

This example shows only one segment of transitions. The real document must also explain how other results, such as delivery not received or already used, are handled, and the conditions and information transferred along every arrow. A diagram showing only the normal path cannot replace the full workflow. Rules involving actual business judgment require user confirmation.

## Write Complete Descriptions for Lowest-Level Features

Use a consistent sequence for each concrete feature: name and ownership, purpose and corresponding requirement, user or triggering actor, starting conditions and inputs, detailed steps, decision rules, outputs and completion criteria, exceptions and recovery, relationships and dependencies, execution method and reasons, and acceptance cases. Reuse existing answers; do not require the user to fill in each field. Inapplicable fields need not be forced in.

### Example: Expanding “Match Product Information”

**This is a hypothetical example; real projects must separately confirm its rules, fields, and handling methods.** It shows that even lowest-level features need concrete explanations; adding their names to a contents list does not complete the work.

| Description Item | Example Content |
|-|-|
| Name and ownership | Match product information; belongs to Order processing project / Foreign-exchange settlement management / Generate settlement materials / Generate platform files. |
| Purpose and entry point | Obtain the corresponding product information for orders needing files; enter this step from the usable-order list. |
| Starting conditions and inputs | Usable orders and a product-information table are available. This example assumes both have product identifiers; missing identifiers enter a branch awaiting additional information. |
| Detailed steps | Read the order's product identifier → Find the same identifier in the information table → Check the number of matches → Handle under confirmed rules → Pass results to file generation. |
| Decision rules | Example assumption: exactly one match with all required fields is successful. With no match or multiple candidates, do not select automatically; record the issue and await confirmation. |
| Outputs and completion criteria | Output confirmed matching information or an explicit reason for pending handling. Only successfully matched orders with complete required information enter generation. |
| Exceptions and recovery | Save issues when information is missing or conflicting; return to matching after additions and confirmation. Check existing results and records before processing again to avoid duplicate generation. |
| Relationships, implementation, and status | Depends on the usable-order list and product information; file generation is downstream. Tool or code choices remain pending discussion. This example has not been implemented or validated. |

For example, two acceptance cases could be designed: unique, complete matching information should proceed to file generation; multiple candidates should record a conflict and pause automatic selection. These cases express only expected example behavior, not test results that have already passed.

## Describe Runtime States, Interruption Recovery, and Duplicate Prevention

Define runtime states such as “pending,” “processing,” “waiting for information,” “failed,” and “complete” according to the actual business, along with conditions allowing transitions. Do not mechanically impose the same states on every feature. State descriptions must correspond to waiting, branches, returns, and endings in the workflow.

For interruptions, retries, or repeated triggers, specify whether completed work is retained, where recovery resumes, which operations can be retried, which require pausing or manual handling, and how duplicate creation, submission, sending, or charging is prevented. Establish rules from actual operations and verified results; do not write a vague “retry on failure.” If technical mechanisms are undecided, record them as awaiting design instead of pretending protections exist.

Record business runtime states separately from document-confirmation states. Throughout the description, distinguish confirmed, pending discussion, pending validation, implemented, and validated. For example, “the user confirmed the approach” does not mean implemented, and “the code is written” does not mean actual validation passed.

## Connect Goals, Acceptance Criteria, and Test Specifications

Each first-phase requirement must have corresponding features, execution paths, acceptance criteria, and checking methods. Connect them by names, identifiers, and section links: requirement → feature and its hierarchy → workflow and rules → acceptance criteria → test method or case → actual result. For small projects, existing documentation suffices; no extra complex matrix is needed. Include unacceptable outcomes and other confirmed minimum requirements in this chain: record how implementation prevents them, corresponding checks, and actual results, rather than merely copying user requirements. Explain business tradeoffs and reasons for unmet criteria in language the user understands.

Distinguish the following three types of content in “Validation and Acceptance.” Begin with overall requirements during initiation and refine them during breakdown and design. Complete the standards and checking methods needed for a part before advancing it. The user confirms business expectations, while the AI organizes checking conditions. Do not ask the user to complete professional testing tables or invent precise metrics.

| Content | Required Description |
|-|-|
| Acceptance criteria | Which business result counts as complete or acceptable within the agreed scope and conditions. Make expectations explicit; implementation methods are not results. |
| Test specifications | How criteria are checked: corresponding requirement or feature, environment and prerequisites, input data or operation steps, expected results, pass conditions, and result evidence. |
| Test results | Actual environment and conditions, checks executed, results and evidence, problems discovered, unvalidated parts, and limitations. |

### Choose Acceptance Methods According to Actual Features

| Feature and Scenario | Checking Method and Basis for Completion |
|-|-|
| Calculations, filtering, scoring, data conversion | Use test scripts or appropriate result checks to inspect inputs, outputs, and exception handling; results must match confirmed rules. |
| Buttons, forms, uploads, navigation, and other interactions | Simulate user clicks, entry, and operations from the actual entry point; check UI feedback and resulting business outcomes. Passing an API check cannot substitute for unchecked interactions. |
| Complete workflows spanning several parts | Follow the entire critical workflow from its actual entry point, checking upstream and downstream connections, data storage, and final delivery. Separate passing parts do not establish overall usability. |

These methods can be combined, and automated scripts can simulate user operations. Choose according to the deployment environment, current tool capabilities, and usage scenarios, rather than requiring one test tool for all projects. Explain validation boundaries when the test environment differs from actual operation. If interfaces serve different devices or clients, specify applicable clients and checking scope under project requirements.

### Make Test Cases and Actual Results Concrete

For important features, specify concrete inputs or operations and expected results, including relevant normal, exceptional, boundary, repeated-operation, interruption, and recovery situations. Match checking depth to actual impact, without mechanically adding a full suite to every small feature. The AI's self-checks must actually execute applicable checks. Honestly mark unexecuted, unavailable, or simulated-only validation; do not treat code reading, completed clicks, or expected outcomes as actual passes.

**Example: account classification.** If the user has confirmed fields, weights, and grouping conditions, write “input samples with confirmed expected classifications → run classification → check individual scores and final groups.” Check missing fields and classification boundaries separately under confirmed rules; check repeated runs for duplicate records. Results should be consistent with the same rule version and data. Actual business requirements must confirm specific fields, samples, handling methods, and metrics; this example is not an executed test result.

**Example: form submission.** Write “enter through the actual page → complete agreed fields → click submit → check page feedback and saved business data.” Add cases for relevant failures as requirements dictate. “The button can be clicked” is insufficient evidence that “the form was correctly submitted and saved.” Verify actual automated-operation methods and pass conditions against the current environment.

By default, save acceptance criteria, test specifications, and results in the same project description, linked to corresponding features. Complex projects may separate detailed testing documents while retaining a summary and links in the main document, avoiding duplicate main text. Update affected descriptions and checking cases when goals, rules, environments, or implementations change, recording actual validation scope and remaining issues.

## Maintain Complete Current Text to Support Handoff

When goals, rules, paths, structure, or actual implementation change, edit corresponding sections and related references so the main text describes the complete current plan. Briefly record reasons, tradeoffs, and impact for important decisions and changes. Follow user feedback for later modifications, retaining the existing framework, UI, and reusable implementation so relevant sections continuously reflect current status. Do not merely append patches at the end, forcing readers to piece together multiple versions to understand the current plan.

### Record Actual Code Organization and Maintenance Conventions

Translate feature hierarchy into actual directories and files. Explain main module responsibilities, entry points, inputs and outputs, and call relationships so a feature's location, callers, and affected parts can be found. Retain appropriate existing conventions and keep simple projects simple. Distinguish planned from implemented paths. The AI organizes technical information; the user need not produce a professional architecture.

Keep the adopted structural-checking method, file-length assessment conventions, and reasons for exceptions needed at handoff in project documentation. Use 500 and 1000 lines as assessment reminders when no convention exists. Files may exceed 1000 lines when actually needed; state why they are retained and reassess when adding content. Do not mechanically split files or classify AI-written business code as generated-artifact exceptions. Update actual paths, call relationships, and related validation descriptions when shared-rule locations, dependencies, or structure change. Refer consistently to “Code Organization and Ongoing Maintenance Standards” in the [Execution and Progress Guide](project-execution.md) for detailed execution standards instead of maintaining a duplicate rule set here.

Record work, progress, and changes by day in update logs; record actual faults and investigation, fixes, and validation in Bug logs. Initial construction primarily uses update logs. These two types may reside locally or in the cloud. Preserve actual paths or links in project documentation, and have the project AI configure how to locate them. Before fixing a Bug, search identical and similar historical records and check applicability; complete logs after fixing and validation. Refer to the [Execution and Progress Guide](project-execution.md) for detailed rules rather than maintaining another duplicate logging policy. Logs retain the process, while corresponding sections retain the complete current plan.

### Describe Automatic Runtime Log Design and Acceptance

Alongside update logs and Bug logs, project documentation must record runtime logs automatically generated by the project during actual operation. Implement automatic recording during construction, so users and AI assistants do not need manual actions for every run. State the definition of a run, run identifiers, critical steps, results and exceptions to record, actual log storage entry points, time zone, daily rollover mechanism, retention arrangements, and necessary read permissions.

Explicitly require automatic creation of an empty file each day, automatic appending when events occur, and an empty file when no events occur. Startup and recovery reuse the current day's file without overwriting history. Include normal and failure records, run-identifier correlation, file creation on event-free days, daily rollover, and restart appending in the corresponding acceptance criteria and test specifications, preserving actual validation results. Runtime logs retain real processes and must not be mixed with update logs or Bug logs. Fault records reference the corresponding date or run identifier to support later AI verification. Refer consistently to the automatic-runtime-log section in the [Execution and Progress Guide](project-execution.md) for specific fields, environment limitations, and implementation standards.

### State Version Records and Handoff Entry Points

Retain code location, Git repository and primary record location, version-number rules and primary source, current development or delivery version, corresponding tag or commit, actual deployed version and status, log entry points, validation status, and unfinished work in current project documentation. Complete fields according to the actual stage. If no repository, delivery version, or deployment exists yet, state that truthfully; do not invent paths, version tags, or acceptance results.

This information helps other AI assistants or technical colleagues find actual outcomes and continue work. The AI maintains it and explains it plainly to the user. Keep code and Git history locally, in a cloud work environment, or on the deployment target machine according to the environment. Uploading to GitHub, account registration, and mastery of Git commands are not required. Update entry points and mappings when locations change. Refer consistently to the [Execution and Progress Guide](project-execution.md) for commit, version, and tag maintenance. This description references current status; logs retain the changes over time.

Long documents may split out detailed subdocuments. The main document retains complete hierarchy, summaries, and links; subdocuments state their ownership and parent entry point for reading as needed. Avoid maintaining the same rule in multiple copies of main text; link to the current description.

When another AI takes over or a new stage begins, read current project documentation and relevant knowledge-base guides first, then open details as needed. After edits, check consistency among contents, hierarchy, workflows, paths, and acceptance, and whether unconfirmed items were accidentally stated as settled conclusions. After implementation, check that descriptions match outcomes and accurately record validation scope.

## Check Whether the Current Description Supports the Next Stage

- Current text makes goals, scope, hierarchy, responsibilities, rules, inputs and outputs, and normal and exception paths locatable. The user has checked critical business meaning.
- Acceptance criteria, testing arrangements, ownership, and record entry points correspond to current scope. Confirmed content, matters pending discussion, and matters pending validation are distinct. Locations not yet created are marked as arrangements or awaiting verification.
- The description supports discussion of node choices without the AI guessing rules on the spot. Preserve actual status where node methods, code, or deployment remain undecided or unimplemented.

Check these conditions against the current scope and impact without adding a process of waiting for approval after every chapter. Verify unconfirmed critical conditions before progressing dependent parts; continue other work whose conditions are met and which is authorized. Shared methods: [Shared Guide | Web Research and Evidence Assessment](shared-research.md); [Shared Guide | Collaboration Preparation and Configuration](shared-preparation.md); [Shared Guide | Changes, Records, and Handover](shared-changes.md).

Ask the user to check project goals, first-phase boundaries, business hierarchy, and rules. Check whether any important feature's ownership, entry point, operations, decisions, dependencies, result destinations, and acceptance methods can be located. Clearly mark critical gaps and arrangements to fill them; do not rely on the AI guessing during execution.

Creating the current description does not require every later design to be settled. Save confirmed content and actual status at this stage, then read the [Project Track | Node Design and Execution Methods Guide](project-node-design.md). Discuss rules, tools, or models one by one, use real-time technical research and sample validation to form an execution plan, and integrate it into project documentation before construction. Once a plan exists, implement, reuse, and self-check each part under the execution and progress guide. Report actual results upon completion. Handle later modifications, operating adjustments, and iteration through that guide's user-feedback process, retaining the existing framework, UI, and reusable implementation, maintaining the current plan, update logs, and Bug logs, and ensuring project runtime logs continue recording actual processes through the agreed mechanism.

Construction and continued implementation entry point: [Project Track | Execution and Progress Guide](project-execution.md). That stage uses the acceptance criteria and test specifications confirmed here, records actual results, and maintains the complete current project description alongside the work.

### Reference Entry Points

[C4: Structural Hierarchy](https://c4model.com/abstractions) and [C4: Runtime Interactions](https://c4model.com/diagrams/dynamic) help distinguish ownership from operating relationships, without requiring fixed technical layers. [Google: Maintain Architecture Documentation as Systems Change](https://docs.cloud.google.com/architecture/framework#document_your_architecture) and [AWS: Decision Context and Impact](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) support recording and maintenance. [AWS: Retries and Duplicate Prevention](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_prevent_interaction_failure_idempotent.html) and [Microsoft: Mapping Requirements to Tests](https://learn.microsoft.com/en-us/azure/well-architected/design-guides/testing) provide further verification entry points. Specific recommendations still require real-time verification of current environments and applicability; do not directly apply cloud-platform implementations.

Interaction-validation examples: [Playwright: Clicking, Filling, and Uploading](https://playwright.dev/docs/input) and [Playwright: Checking Actual Results](https://playwright.dev/docs/test-assertions). The testing sources above were checked on 2026-10-08 and provide further verification entry points; example tools are not mandatory project choices.
