# Feature Track | Initiation and Design Document Guide

**Keywords:** Feature Track; feature documentation; initiation and design document; DESIGN.md; scope for this phase; hierarchy tree; nested features; direction; execution paths; inputs and outputs; specific rules; status; exception handling; acceptance criteria; testing standards; existing feature checks; record entry points; handoff; body text maintenance

**Summary:** Organize the consensus from feature initiation and task breakdown into complete documentation, describing responsibilities, paths, rules, connections, acceptance, and actual status at each level. For integration, accurately identify connections to and reuse of the original project. Archive documentation and logs alongside the feature, and keep the body text describing the complete current solution.

This is the guide for the current stage of the Feature Track. First read [Home](index.md) and the current records from completed stages, and retain the principles of user leadership, plain communication, live online verification, and reading as needed. Build integrated features within the original project's architecture. Change target behaviors explicitly authorized for this phase as required, keep existing features and related workflows outside the scope functioning normally, and verify affected behaviors. Advance standalone features in the confirmed implementation environment. Archive documentation and the three types of logs alongside the feature.

## Create complete feature documentation

Organize confirmed content into complete documentation that is maintained over time. Save goals, ownership, scope for this phase, hierarchy and execution paths, specific rules, reused content, operating methods, exception handling, acceptance and testing, actual status, and entry points for code and records. Read the [Initiation and Design Document Guide](project-design.md) for specific ways to document hierarchies, paths, lowest-level features, and their corresponding acceptance criteria. Scale the project scope down to this feature rather than copying the entire project documentation.

Wherever the feature resides, archive its documentation, changelog, Bug log, and runtime logs there too. This applies to both integrated and standalone operation. Specify entry points according to actual directories or cloud locations rather than inventing paths. For integration, keep the feature entry point and related relationships in the original project's relevant documentation, while detailed feature records remain alongside the feature. For standalone scripts, explain how to start them, where to place inputs, and where to view results.

Documentation for a simple script may be concise, but must still be sufficient for use, checks, and handoff. When discussions or implementation change, update the corresponding sections so the body text describes the complete current solution. Distinguish planned, implemented, tested, deployed, and unconfirmed content rather than continuously appending patches at the end.

## Structure of complete documentation

Organize the body text around confirmed content. If information is incomplete, create an initial version and supplement it during breakdown and node design. Do not force a large document on a simple script, or omit key content needed for use, verification, and handoff.

| Section | What to explain |
|-|-|
| Goals, scope, and ownership | Current problems, expected outcomes, content and boundaries for this phase, the project to integrate with or standalone operating environment, and verified and unconfirmed conditions. |
| Hierarchy, responsibilities, and paths | Relationships between this feature and all levels of subfeatures; each part's inputs and outputs, rules, conditions, upstream and downstream relationships, and completion criteria; clear normal and exception directions. |
| Implementation and integration | The original project's entry points, verified reusable modules, new parts, and how to return to the original workflow; startup, inputs, and result locations for standalone features. Add node methods and the reasons for choosing them later. |
| Acceptance and testing | Passing conditions for goals, features, and paths, using scripts, simulations of actual user operations, or a combination; include affected existing behaviors when integrating. |
| Records, versions, and handoff | Actual code, current documentation, changelog, Bug log, runtime logs, and Git entry points, together with the current version and completed and incomplete states. |

## Write enough to understand and build along the paths

Describe the ownership and responsibilities of multiple levels of subfeatures level by level rather than listing module names alone. For lowest-level steps, explain how they are entered, what they read, which rules they execute, which results they produce, and where they go after success or failure. Integrated features need both internal paths and their boundaries with the original project. Describe conceptual relationships separately from actual code directories, and preserve the original architecture.

Using the hierarchy example from task breakdown, record actual directions such as “original project entry point → this feature's validation → call a verified capability → generate results → return to the original workflow.” This is only an example of how to write the documentation. Verify actual entry points, rules, failure destinations, and code paths in the current project rather than treating the example as a predetermined implementation.

For more detailed ways to document hierarchy trees, lowest-level features, status, and corresponding acceptance criteria, read the [Shared Documentation Standards (Project Track)](project-design.md) as needed and scale them to the current feature. Describe only the actual structure and integration constraints of existing architecture. Do not use documentation design to arrange an architecture migration.

## Maintain initial acceptance criteria alongside the current body text

Map the acceptance criteria and test plans from initiation to specific features and paths, and save the scope of checks for normal, exceptional, boundary, and connection cases. For integration, separately list target behaviors authorized to change, existing features outside the scope that must remain functioning normally, and the check scope for affected workflows. Record planned checks separately from actual test results, and accurately state anything untested, undeployed, or dependent on unconfirmed conditions. Link confirmed mandatory limits to specific implementation requirements, corresponding checks, and actual results, explaining how unacceptable outcomes are avoided. Mark not implemented, not verified, and checks not passed separately rather than merely repeating the user's words. Explain important tradeoffs and impacts on existing work in business language.

Return to the relevant sections to update them after node plans are confirmed or implementation changes. Keep the body text complete and current. The changelog records what changed, the Bug log preserves actual problems and their handling, and runtime logs preserve the actual execution process. Do not replace body text maintenance with accumulated version patch sections.

## Results of this stage and next steps

- The current body text provides locatable goals, scope, hierarchy, responsibilities, rules, inputs and outputs, and normal and exception paths. The user has checked key business meanings.
- Acceptance criteria, test plans, ownership, and record entry points match the current scope. Confirmed, awaiting discussion, and awaiting verification content are clearly distinguished. Locations not yet created are marked as planned or awaiting verification.
- The documentation is sufficient to discuss node selection without AI guessing rules on the spot. Preserve actual status when node methods, code, or deployment are not yet determined or implemented.

Check these conditions against the current scope and impact without adding a process that waits for approval after each chapter. Verify unconfirmed key conditions before dependent work, and continue other authorized work whose prerequisites are met. Shared methods: [Shared Guide | Web Research and Evidence Assessment](shared-research.md); [Shared Guide | Collaboration Preparation and Configuration](shared-preparation.md); [Shared Guide | Changes, Records, and Handover](shared-changes.md).

Save this stage's current results and unconfirmed items, then proceed to the corresponding stage using the [Feature Track | Node Design and Execution Methods Guide](feature-node-design.md). Reuse confirmed information that remains valid. When a necessary condition is not met, explain its specific impact and continue authorized work that does not depend on it.
