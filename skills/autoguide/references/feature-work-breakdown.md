# Feature Track | Task Breakdown Guide

**Keywords:** Feature Track; task breakdown; fine detail; user guidance; real operations; tacit experience; actions; decision criteria; prerequisites; inputs and outputs; waiting; repetition; exception paths; nested features; feature hierarchy; execution paths; project integration; standalone scripts; complete walkthrough

**Summary:** With the feature goals, ownership, and scope for this phase established, gradually help the user explain the real work in enough detail to implement and verify it. Describe multiple levels of subfeatures, decisions and exception paths, and the direction of integration or standalone operation. Review the work in a walkthrough and create a breakdown record.

This is the guide for the current stage of the Feature Track. First read [Home](index.md) and the current records from completed stages, and retain the principles of user leadership, plain communication, live online verification, and reading as needed. Build integrated features within the original project's architecture. Change target behaviors explicitly authorized for this phase as required, keep existing features and related workflows outside the scope functioning normally, and verify affected behaviors. Advance standalone features in the confirmed implementation environment. Archive documentation and the three types of logs alongside the feature.

## Start a gradual discussion from confirmed goals

Before starting, check this feature's goals, scope for this phase, ownership, existing foundations, and initial acceptance criteria. Keep unconfirmed business rules as open questions rather than filling the solution with AI guesses. Use one actual operation by the user as the main thread, then explore different cases. Focus each round on the key questions currently affecting understanding rather than handing all technical questions to the user to complete.

## Break down features and execution paths in detail

Start with one instance of the user's real work and expand it section by section into actions, tacit experience, decision criteria, prerequisites, inputs, outputs, waiting, repetition, and exceptional cases. Refine it until it can be implemented and verified. AI helps ask follow-up questions and organize information rather than filling gaps in business rules by guessing. Use a complete walkthrough for the user to correct omissions and misunderstandings. Read the [Task Breakdown Guide](project-work-breakdown.md) for specific guidance methods.

When there are nested subfeatures, specify their hierarchy, upstream and downstream relationships, conditional paths, and failure handling. For integration, explain how the feature is entered from the original project, which existing capabilities it calls, and how results return to the original workflow. For standalone operation, explain how it starts, how inputs enter, how execution ends, and where results go.

Example: The following conceptual ownership tree for an integrated feature helps explore hierarchy and direction. It does not require restructuring existing directories to match it.

```plaintext
Original project
└─ Order management
   └─ New in this phase: bulk export
      ├─ Get orders selected by the user
      ├─ Check export conditions
      │  ├─ No orders selected: return a notification
      │  ├─ Missing order information: handle under confirmed rules
      │  └─ Conditions met: proceed to file generation
      ├─ Generate the export file
      │  ├─ Call the verified order-reading capability
      │  ├─ Transform data under confirmed rules
      │  └─ Save the file
      └─ Return the processing result
         ├─ Success: provide the result location or download entry point
         └─ Failure: identify the failed step and automatically write to the runtime log
```

## Specify actions, decisions, and results for each step

Record step by step who or which tool executes it, which inputs or prerequisites it needs, what it actually does, the basis for decisions, where outputs go, and how completion is known. For vague expressions such as “process it,” “filter suitable ones,” or “retry on failure,” continue asking for the actual rules, conditions, number of attempts, or basis for waiting. If no definite answer is available, mark it as unconfirmed and continue discussing independent parts.

Distinguish user operations, system execution, and steps requiring human judgment. Expand normal cases, unmet conditions, missing inputs, failures, waiting, repeated triggers, and other cases as actually needed, and explain which step follows or how execution ends. For integration, describe the relationship between the original entry point, this feature's processing, and the return to the original workflow. Do not treat a conceptual hierarchy tree as an instruction to refactor directories.

## Review the complete walkthrough and save the current breakdown

Walk through the starting point, all steps, conditional branches, and ending point in full, inviting the user to correct omissions and misunderstandings. Produce the current list of actions, hierarchy, normal and exception paths, decision criteria, and unconfirmed items, and save them in the corresponding sections of this feature's documentation. Update the relevant sections when requirements change rather than continually appending patches.

For shared methods of detailed follow-up questions, walkthroughs, and breakdowns, read the [Shared Task Breakdown Standards (Project Track)](project-work-breakdown.md) as needed. Apply them within this feature's scope without expanding project goals. Integration architecture constraints and record ownership requirements remain in effect.

## Results of this stage and next steps

- Actual work is refined into reproducible actions, decision criteria, prerequisites, inputs and outputs, and exceptional cases expanded as needed.
- Multiple levels of subfeatures, upstream and downstream relationships, and conditional paths can be located. The feature scenario explains integration with and return to the original project, or the starting point, ending point, and result destination for standalone operation.
- A complete walkthrough has been reviewed and the user has corrected the current business record. Key questions and their impact are clear. The records are sufficient to proceed to feature or project documentation.

Check these conditions against the current scope and impact without adding a process that waits for approval after each chapter. Verify unconfirmed key conditions before dependent work, and continue other authorized work whose prerequisites are met. Shared methods: [Shared Guide | Web Research and Evidence Assessment](shared-research.md); [Shared Guide | Collaboration Preparation and Configuration](shared-preparation.md); [Shared Guide | Changes, Records, and Handover](shared-changes.md).

Save this stage's current results and unconfirmed items, then proceed to the corresponding stage using the [Feature Track | Initiation and Design Document Guide](feature-design.md). Reuse confirmed information that remains valid. When a necessary condition is not met, explain its specific impact and continue authorized work that does not depend on it.
