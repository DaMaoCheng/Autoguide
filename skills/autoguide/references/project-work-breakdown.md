# Project Track | Task Breakdown Guide

**Keywords:** task breakdown; workflow mapping; user guidance; gradual follow-up questions; fine detail; tacit experience; actions; decision basis; prerequisites; inputs and outputs; completion criteria; exception branches; waiting; repetition; full replay; reproduction; node design

**Summary:** Start with the user's actual work and business experience. Through descriptions of each segment, detailed follow-up questions, and replay checks, break work within first-phase scope into reproducible actions, decisions, and exception branches. Record starting conditions, specific operations, results, and completion criteria, marking unconfirmed details. Discuss nodes and execution methods after the user corrects and confirms the record.

Read [Home](index.md) and the [Project Track | Initiation Guide](project-initiation.md) first to check current goals, first-phase scope, and confirmed conditions. This guide retains user leadership, plain communication, real-time online research, patience, and realistic time expectations. Task breakdown may span several sessions; save confirmed content and missing details each time, and continue next time.

## Start with One Real Instance of the User's Work

Ask the user to choose a task within first-phase scope and describe how they completed a recent instance: what triggered it, what materials were available, what they did first, how they proceeded, and what result they ultimately produced. Follow the actual process step by step, avoiding only generalized descriptions such as “usually check it, then submit when done.”

First establish the task's start and end points, organize the main stages the user has described, and then expand each stage. Stage names serve as navigation, not substitutes for the specific process. Do not claim task breakdown is complete merely because several stages have been named.

For new work that has not yet been performed, discuss the intended actual process using the user's existing experience. Mark ideas separately from facts that have already occurred. The AI must not present a process it supplied itself as the user's existing practice or confirmed requirement.

## Expand Each Segment into Specific Actions

Guide the user to describe habitual details that are easy to omit when explaining their work. If one action contains several others, keep breaking it down level by level. For example, “export orders” may involve entering the system, finding the entry point, selecting conditions, determining fields, starting the export, waiting for the result, finding the file, and checking its contents. This illustrates granularity; it does not mean every user follows the same method.

Do not treat phrases such as “check it,” “organize materials,” “decide if suitable,” “handle exceptions,” or “do it as usual” as fully specified steps. Continue exploring where they check, what information they examine, how they actually operate, which rules guide choices, and how completion is confirmed.

Follow the order of the current description, focusing each round on one action or short segment instead of presenting every question at once. The AI organizes information as it listens and restates it in language the user understands. Update the record when the user corrects it, so misunderstandings do not accumulate.

## Clarify the Judgment and Experience Behind Actions

Beyond visible operations such as clicking, entering information, copying, and saving, understand what information the user obtained, why they chose one option over another, what makes them continue or return, and when they must wait, repeat, or communicate with others. Do not summarize mental judgment as merely “decide from experience.”

When the user says “it looks wrong,” “I think it is fine,” or “I usually handle it this way,” explore a concrete example: what they saw, which details affected the decision, how normal and exceptional cases differed, and whether there are counterexamples. If the user cannot yet express a rule, record examples and unresolved points first. Do not demand immediate thresholds or have the AI invent decision criteria.

The AI may research relevant approaches online in real time around the user's views to help explore alternatives. Verify sources and evidence under Home. Record external methods separately from the user's actual experience. Candidate improvements must not become established steps in the existing workflow without user confirmation.

## Complete Each Step's Conditions, Results, and Variations

The following table helps the AI identify gaps and ask gradually as needed. Reuse existing answers. Do not require the user to complete the entire table for each step or mechanically ask every question.

| What to Clarify | How to Help the User Explain It |
|-|-|
| Starting conditions and required information | Under what circumstances does this step begin? What materials, pages, or someone else's completed work must be available first? |
| Specific operations and objects | Where do you open, what do you select, and what do you enter? How do you find the target object? What smaller actions are contained in this action? |
| Decision basis and next steps | What must you see before continuing? How do you choose among multiple options? Which step follows each possible result? |
| Outputs and completion criteria | What do you obtain, where is it placed, or who receives it? What confirms success? |
| Waiting, repetition, and order | What result must you wait for, and how do you know you can continue? Which objects are processed repeatedly, and when does repetition end? Which steps must occur in order? |
| Exceptions and human involvement | What actually happens when materials are missing, results are wrong, or operations fail? When do you redo, return, pause, or ask someone to confirm? |

Describe normal and alternative situations separately, retaining the conditions for returning to the main flow or ending. Mark exception handling that has never occurred and has not been confirmed by the user as pending discussion; do not portray it as an existing mechanism.

## Help the User Add Detail and Preserve Actual Status

If the user cannot explain something yet, ask whether they can conveniently provide an actual example, screenshot, demonstration, or explain while performing the task next time. These materials support understanding. If unavailable, record the gap and explain whether it affects later breakdown; do not demand materials or invent details.

Maintain a current breakdown record as discussion progresses: steps and substeps, order and branches, conditions and operations for each step, decision basis, outputs and completion criteria, known exceptions, and unconfirmed details. Use a list or table appropriate to the existing project, preferably integrating existing records rather than repeatedly creating files with identical content.

Clearly distinguish facts described by the user, ideas the user has confirmed, the AI's understanding pending confirmation, and content requiring additions or validation. When saving stage progress, state which segment has been clarified and where to resume. Follow Home's guidance on patience and do not repeatedly ask for confirmed information.

## Check the Breakdown Through a Full Replay

After organizing the record, walk through it from start to finish and ask the user to check for skipped steps, incorrect order, implicit preparation, omitted decisions, or missing exception branches. Use a real example for demonstration or checking when conditions permit. If only restating text, identify this as a record check; do not claim an actual trial run.

### Completion Conditions for the Current Stage

- Actual work is detailed into reproducible actions, decision bases, prerequisites, inputs and outputs, and exceptions expanded as needed.
- Nested subfeatures, upstream and downstream relationships, and conditional paths can be located. Feature scenarios explain entry into and return to the original project, or the start, end, and destination of results for independent operation.
- A full replay is complete, and the user has corrected the current business record. Critical questions and their impact are clear, and the record supports organizing feature or project documentation.

Check these conditions against the current scope and impact without adding a process of waiting for approval after every chapter. Verify unconfirmed critical conditions before progressing dependent parts; continue other work whose conditions are met and which is authorized. Shared methods: [Shared Guide | Web Research and Evidence Assessment](shared-research.md); [Shared Guide | Collaboration Preparation and Configuration](shared-preparation.md); [Shared Guide | Changes, Records, and Handover](shared-changes.md).

Ask the user to correct and confirm the current record. If the first-phase goal or scope needs to change, return to the initiation guide to discuss tradeoffs and update affected parts. Do not silently expand the project by continuously adding steps.

## Connect Task Breakdown to Documentation and Node Design

Clarify the user's actual work first, then discuss which steps to retain, merge, replace, or automate. Each recorded action does not need its own automation node, and existing manual operations do not automatically determine the final implementation method.

Use the [Design Document Guide](project-design.md) to organize confirmed initiation and breakdown content into a complete current project description, stating feature hierarchy, different paths, and specific rules. Refer to its hierarchy tree, execution paths, and lowest-level feature examples. Update documentation with the discussion. Keep undecided node designs and implementation methods pending discussion rather than inventing them to fill the structure.

Next, based on the confirmed breakdown record, read the [Project Track | Node Design and Execution Methods Guide](project-node-design.md) first, and select appropriate rules, scripts, tools, or models according to the actual task and completion criteria. Prioritize correctness, stability, speed, and maintainability. Use real-time technical research from Chinese and international sources and actual sample validation to clarify connections and failure handling. Integrate confirmed content into project documentation, then proceed to construction. Once an execution plan exists, continue under the execution and progress guide. Report actual results upon completion; handle subsequent modifications, operating adjustments, and iteration through that guide's user-feedback process, retaining the existing framework and UI and reusing outcomes. For faults, search historical Bug logs first, then complete records after validation.

Execution-stage entry point: [Project Track | Execution and Progress Guide](project-execution.md). Follow the current plan and dependencies, inspect existing outcomes first, reuse them directly when appropriate, and actually perform self-checks against acceptance criteria after completion.

### Reference Entry Points

[HSE: Understanding the Task](https://www.hse.gov.uk/humanfactors/assets/docs/understanding-the-task.pdf) describes step-by-step demonstration and explanation by people familiar with the work, recording small actions, information gathering, and decisions, then organizing them into hierarchical tasks, sequences, and prerequisites. This guide draws on its task-interview method. The source concerns safety; do not directly apply its domain rules to business automation. [UiPath: Build Diagram](https://docs.uipath.com/task-capture/standalone/2022.4/user-guide/build-diagram) provides a practical reference for organizing the main workflow before adding actions and branches. The link is to 2022.4 documentation; it does not establish current product capabilities or require installation. Verify specific tool recommendations in real time under Home.
