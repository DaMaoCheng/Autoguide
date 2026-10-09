# Project Track | Initiation Guide

**Keywords:** project; initiation; overall goal; first-phase goal; acceptance criteria; test specifications; acceptance methods; simulation of user operations; test results; operating boundaries; deployment location; platforms and servers; technology selection; code architecture; language; maintenance; requirement changes; phases; minimal validation; initiation record; version number; version rules; Git; version history; local repository; cloud work environment; handoff entry points

**Summary:** Starting with the problem the user wants to solve, gradually confirm the project's overall goal, first-phase scope, operating method, resources, and maintenance conditions. Research suitable implementation approaches online in real time against the deployment environment, decide which phase should include new requirements, and develop first-phase acceptance criteria and initial testing arrangements alongside these discussions. Refine them during task breakdown and design, and integrate them into an initiation record that can evolve with the discussion. Once the user confirms the current agreement, proceed to task breakdown and node design.

Use this guide for projects that organize multiple tasks, features, or long-term outcomes around an overall goal. Read [Home](index.md) first, and follow its shared principles of user leadership, plain communication, real-time online research, and consulting the knowledge base by stage. When adjusting just one feature, first assess whether project-level discussion is needed; do not mechanically apply every step.

Initiation clarifies what is currently being planned and establishes the basis for further work. Fill in the following information gradually as the discussion requires; do not ask the user to answer an entire table at once. Reuse information already established. Mark unknowns as pending confirmation; the AI must not fill them in with assumptions on the user's behalf.

## Clarify the Overall Goal and First-Phase Goal

Start with the user's actual work and views: understand how they work today, the problems they encounter, why change is needed, who will use the result, and what change they ultimately want to see. A tool, feature, or request for “full automation” is only a starting point; continue exploring its underlying purpose.

Distinguish the project's long-term overall goal from the outcome to deliver in the first phase. Set first-phase scope around the most pressing current problem, and state what is excluded for now, which ideas are deferred, and which still need discussion. If the user has not expressed views on these matters, help them describe their work and expectations first; the AI must not predefine a complete set of goals.

### Develop Acceptance Criteria and Test Specifications Alongside Initiation

During initiation, discuss how to determine whether the first phase meets requirements: who performs what work, under which circumstances, what result they should obtain, and what belongs in this phase. The user confirms the desired business outcomes, and the AI helps turn them into observable, checkable acceptance criteria in plain language. Avoid vague statements such as “runs normally” or “works well.” The AI must not invent unsupported speed, accuracy, or other numbers; mark them as pending confirmation when a baseline is missing.

Focus on current critical gaps to understand the outcomes the user finds least acceptable. Distinguish mandatory minimum requirements, improvements that are desired and need validation, and preferences that can be adjusted. When tradeoffs are needed, first explain the actual impact and feasible options in everyday business language, then help the user express their reasons for choosing. Do not ask a coding novice to rank abstract metrics first, or invent expectations for them. Reuse clear existing requirements and mark unknowns as pending confirmation; do not turn this guidance into another mandatory form to complete.

Record confirmed minimum requirements in the same initiation record and connect them to implementation requirements, corresponding checks, and actual results. Gradually clarify during breakdown and design how implementation will prevent unacceptable outcomes, which normal and exceptional situations must be checked, and what constitutes a pass. Record not implemented, not checked, and not passed as separate states. Questions and tests cannot guarantee zero errors, and desired business improvements must not be promised as already achieved.

For example, if the user explicitly requires that “no orders may be missed,” check the processing result of every order within the confirmed sources and processing scope. Preserve reasons and discoverable notifications for orders that could not be processed; do not silently treat everything as successful. Implement the requirements and check appropriate normal and failure cases. Passing sample checks establishes only the scope checked; it cannot prove every future case.

Acceptance criteria answer “what result is acceptable.” Test specifications answer “under what conditions, using what data and methods, and how is a pass determined.” Test results record the actual scope checked, passes and failures, and evidence. Describe these separately; do not present expected results as validated outcomes.

At initiation, establish overall criteria and known checking methods first. Refine them into features, rules, and workflows during task breakdown and node design. Before advancing a part, complete its required acceptance conditions and checking methods; after completing it, perform self-checks against them, and finally check whether the entire workflow meets the first-phase goal. Initiation does not require every testing detail to be worked out at once. Update affected criteria and test specifications when requirements, rules, or the implementation environment change.

Choose checking methods according to the feature and actual use scenario. Test scripts can check calculations, filtering, scoring, and data processing. Interactions such as buttons, forms, uploads, and navigation require simulated real user operations and checks of feedback and final results. Workflows spanning several parts require checking connections and final delivery from the actual entry point. Methods can be combined, and user-operation simulation can be automated. Do not impose “passing scripts means completion” universally, or treat “a click succeeded” as proof that the business result is correct.

For each check, specify the corresponding requirement, test environment, inputs or operation steps, expected results, pass conditions, and result evidence as needed. Cover relevant normal, exceptional, boundary, and repeated-operation cases, with checking depth proportionate to actual impact. The AI must actually execute applicable checks. Honestly mark checks that were not executed, could not be executed, or used simulated validation only; reading the code once does not justify declaring a pass.

By default, integrate acceptance criteria, test specifications, and actual results into the “Validation and Acceptance” section of the current initiation and design document, linked to features. Split detailed testing into a separate document only when project complexity warrants it, keeping an entry point in the main document to avoid duplicate maintenance. See the [Design Document Guide](project-design.md) for writing guidance.

The AI restates its current understanding using existing information, and continues asking about ambiguities, contradictions, or omissions that affect current decisions, establishing user-confirmed goals and boundaries. Once goals and authorization are clear, proceed in the current direction without asking again about the output format every round. Handle new requirements by phase under this guide. Confirmation establishes agreement for this stage; it can still be adjusted later based on actual conditions.

## Understand How the Project Operates as a Whole

Based on the goals, map overall operating boundaries: who uses it, what materials come from where, what must be produced, who receives it or where it is stored, what triggers a run, how often it runs, and approximate workload. Ask the user to describe one real task and understand it step by step from start to completion.

Also understand which parts should be automated, which currently need human involvement, and common exceptions. During initiation, clarify the overall process and boundaries first. Do not demand all node rules immediately or expand the discussion straight into designing an entire production pipeline.

## Understand Resources and Maintenance Conditions

Gradually establish the expected delivery time, acceptable construction and ongoing operating costs, existing platforms or servers, company tools and materials, and who will use and maintain the project, as needed for current decisions. Verify whether existing resources can actually be used against real permissions and conditions.

Maintenance conditions include who can later adjust rules, diagnose problems, or take over the code or service. Discuss choices based on the maintenance the user can support; do not assume the user can program or equate insufficient resources directly with project infeasibility. If budget, timing, or a maintainer is not yet known, record it as undecided and continue discussions that do not depend on those answers.

## Determine Deployment Location and Operating Conditions

First establish whether the user already has a platform, server, or company environment for the project. If established, research official documentation, current versions, and practical material for that environment in real time to verify available capabilities, limitations, and maintenance methods. If undecided, compare relevant candidates against the user's goals and resources, and let the user choose.

Explain each option's practical effects: whether it can connect to required systems, how materials are accessed and stored, whether continuous operation is needed, how permissions are obtained, how costs arise, who handles problems, and whether migration or handoff will be possible later. Discuss only differences relevant to the current project, rather than listing every platform.

Label “officially supported,” “actually available in the current environment,” and “not yet confirmed” separately. Perform read-only or low-risk checks as needed. Product marketing and others' success stories cannot replace confirmation of the current account, version, and connection conditions. Actual configuration, paid actions, and production operations still follow the current task's authorization.

### Agree on Version Records and Handoff During Initiation

Version management enables tracing what the project changed, recovering the corresponding code, and handing work to other AI assistants or technical colleagues. Existing projects retain their version rules and Git repository. For new projects, record version-number rules, proposed locations for code and version history, maintenance arrangements, and future handoff entry points in the initiation record. Choose a local project directory, cloud work environment, or target deployment machine according to the actual environment. Uploading to GitHub, registering a code-hosting account, and learning Git commands are not required. The AI implements and maintains this arrangement and explains it in plain language.

New projects may use the three-part “major.minor.patch” format, referring to Semantic Versioning and documenting which usage patterns, interfaces, or data must remain compatible in the actual business context. Early 0.x.x versions indicate construction is ongoing and the project is not stable yet. Once the first-phase goal passes acceptance and is ready for formal delivery and use, it may become 1.0.0. The following examples are project conventions for this workflow; directly retain explicit rules in existing projects.

| Version Example | Applicable Situation |
|-|-|
| 0.1.0 → 0.2.0 | A new set of verifiable features emerges during early construction; save development versions by actual stage. This does not mean stability or deployment. |
| 0.x.x → 1.0.0 | The first-phase goal passes acceptance, producing a formal delivery version. Record deployment separately. |
| 1.0.0 → 1.0.1 | A fix preserves compatibility with existing usage patterns, interfaces, and data. |
| 1.0.1 → 1.1.0 | Added features preserve compatibility with existing usage patterns, interfaces, and data. |
| 1.x.x → 2.0.0 | Incompatible changes require adjustments to existing usage patterns, interfaces, or data for continued use. A large number of changes alone does not justify a major-version increase. |

Agree on rules and intended storage during initiation, verify actual directories and repository conditions during execution preparation, and then have the AI implement them. Each Git commit saves a relatively complete change. Update version numbers at actual delivery milestones, rather than every workday, conversation, or commit. See the [Execution and Progress Guide](project-execution.md) for maintenance, log connections, and handoff checks.

## Choose an Implementation Approach Based on Goals, Deployment, and Maintenance

Using confirmed goals, deployment location, and maintenance conditions, the AI researches suitable code organization, languages, frameworks, and required tools online in real time. Check current official support, version compatibility, and maintenance status first, then relevant community practice, failure cases, and limitations, using Home's evidence-evaluation method. Do not decide solely from existing knowledge, preferences, or past project experience.

“Broadly applicable and easy to maintain” must mean something concrete for this project: whether the ecosystem and documentation are mature, dependencies are maintained, deployment and migration are convenient, others can take over, and how much existing content a feature change would affect. A suitable choice considers implementation cost, ongoing fees, reliability, and maintenance difficulty together; do not pursue architectural complexity or tool count.

Explain how candidate approaches differ for the user, such as initial investment, later modifications, deployment, and maintenance, instead of asking them to pick an architecture or language first. Once the user chooses the tradeoffs, record the choice and reasons. Recheck affected choices when deployment location, first-phase scope, or maintenance conditions change.

A project-wide approach does not mean every node uses the same tool. During subsequent node breakdown, continue selecting rules, configuration, scripts, existing services, or suitable models by task. Use models where judgment is needed, prioritize fixed implementation of stable deterministic logic, and verify quality, cost, and efficiency with real tasks.

## Decide Whether New Requirements Belong in the First Phase or Later

When the user proposes new features or goals during discussion or implementation, first understand why they are being added and how they relate to the overall and first-phase goals. Then explain the impact on existing work, including workload, delivery time, cost, technology choices, and stability. Do not silently expand first-phase scope simply because the user mentioned something.

| New Requirement Situation | Discussion and Handling |
|-|-|
| Necessary for the first-phase goal, or essential content previously omitted | Discuss inclusion in the first phase with the user in light of the impact. If included, update scope, acceptance criteria, and affected arrangements together. |
| Can be implemented independently, or deferral does not affect the first-phase goal | May be assigned to a later phase. Record its purpose and dependencies; do not promise delivery dates that have not been discussed. |
| Changes the overall goal or a critical premise | Return to goal clarification, reconfirm scope and approach, and check whether the existing plan still applies. |

The user decides phase tradeoffs according to actual circumstances; the AI provides verified evidence and impact explanations. Once a change is settled, update the current initiation record so new requirements do not remain only in chat while work continues against the old scope. Goals can evolve; do not make the initial initiation record an unchangeable constraint.

## Resolve Critical Uncertainties and Create the Initiation Record

Identify critical premises that affect whether the project can proceed, such as access to required systems, the platform's ability to run necessary tasks, and availability of materials. State what has been verified, what has external documentation only, and what remains an assumption to validate. If needed, perform minimal validation first, using the least work needed to check the critical issue.

Validation must specify what is to be established, the conditions used to check it, and what counts as a pass. One working interface or demonstration does not mean the full project is usable. Record actual test scope, results, and remaining limitations. Operations involving permissions, costs, or real data must follow their corresponding authorization; initiation discussion does not automatically authorize all implementation.

Save the current agreement in a location suitable for the project as an initiation record that can be updated continuously. Integrate it into existing project documentation when that can carry the information. Save a concise document when continuity across chats is needed, without mechanically adding duplicate files. Include the following as actually needed:

- **Goals and boundaries:** The overall goal, current first-phase goal, included and temporarily excluded content, checkable acceptance criteria, and arrangements for gradual refinement. Add test specifications and actual results during design and validation.
- **Operation and resources:** Users, inputs and outputs, triggers and frequency, boundaries of automation and human involvement, time and budget, and maintenance conditions.
- **Environment and choices:** Deployment location, actually available capabilities, selected implementation approach and tradeoff reasons. Preserve sources, verification dates, and applicability conditions for critical external evidence.
- **Later work and pending items:** Deferred requirements, undecided matters, key assumptions, and necessary validation arrangements.
- **Actual status:** What the user has confirmed, what has actually been validated, and what still needs discussion or validation. Update corresponding content for important changes.

### Completion Conditions for the Current Stage

- The user has confirmed current goals, phase scope, boundaries, and initial acceptance criteria. New requirements and those still under discussion are accurately marked.
- Main usage, inputs and outputs, operating conditions, and maintenance conditions are described. Critical premises are verified or have clear validation arrangements. The project hosting location and constraints are checked; when an existing project or attached feature is involved, verify its actual ownership and integration constraints.
- Current agreements and unconfirmed items are saved and can support task breakdown. Code, Git, or log locations not yet created may be recorded as proposed arrangements; do not pretend they exist.

Check these conditions against the current scope and impact without adding a process of waiting for approval after every chapter. Verify unconfirmed critical conditions before progressing dependent parts; continue other work whose conditions are met and which is authorized. Shared methods: [Shared Guide | Web Research and Evidence Assessment](shared-research.md); [Shared Guide | Collaboration Preparation and Configuration](shared-preparation.md); [Shared Guide | Changes, Records, and Handover](shared-changes.md).

After reaching the current initiation agreement, read the [Project Track | Task Breakdown Guide](project-work-breakdown.md) first, guide the user to explain actual work in detail, and replay it for verification. Then organize the complete current description using the [Project Track | Design Document Guide](project-design.md) before discussing node design.

### Reference Entry Points

Requirement changes and scope management: [Atlassian: Scope Changes and Their Impact](https://www.atlassian.com/work-management/project-management/scope-creep). Technology and environment tradeoffs: [Microsoft: Architecture Choices and Operating Conditions](https://learn.microsoft.com/en-us/azure/architecture/guide/). Critical-assumption validation: [Microsoft: Collaboration and Proofs of Concept](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/collaboration). These entry points aid verification. Each project must still check current information and applicability online in real time, without directly applying a particular product's solution.

Validation and acceptance methods: [Microsoft: Design and Continually Adjust Testing to Business Requirements](https://learn.microsoft.com/en-us/azure/well-architected/design-guides/testing); [Playwright: Simulate Browser User Operations](https://playwright.dev/docs/input). The method and example entry points were checked on 2026-10-08. Actual tools and environments still require real-time verification; no particular platform is mandatory.
