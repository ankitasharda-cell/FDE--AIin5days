# Day 5 — Capstone and Evaluation

## Outcome

Present a small AI application with a clearly scoped purpose, a tested workflow, and an evaluation plan that considers usefulness, reliability, and safety.

## Capstone steps

1. **Define the user and task.** State the problem, intended users, and what the application will not do.
2. **Choose the simplest design.** Use prompting first; add retrieval, tools, or multiple agents only when they address a demonstrated need.
3. **Map the flow.** Show where instructions, context, model calls, tools, and outputs fit. Mark trust boundaries and any human approval.
4. **Build a small prototype.** Use synthetic or public data. Keep credentials out of prompts and source files.
5. **Test representative cases.** Include a normal case, ambiguous input, missing information, an attempted out-of-scope request, and a tool or retrieval failure.
6. **Evaluate and revise.** Compare outputs against explicit criteria, inspect errors, and document known limitations.

## Evaluation checklist

- **Usefulness:** Does the result address the stated user task?
- **Grounding:** Are factual claims supported by the provided source or tool result?
- **Reliability:** How does the application handle malformed input, missing data, and unavailable tools?
- **Safety and privacy:** Are sensitive data and consequential actions appropriately constrained?
- **Clarity:** Does the application communicate uncertainty and limitations?
- **Repeatability:** Can another person understand the expected behavior and reproduce the tests?

## Presentation

Ask the learner to demonstrate the happy path and one failure case, describe an evaluation result that changed the design, and name one known limitation and next improvement. Do not treat a successful demo as proof of general reliability.

## Checkpoint

Have the learner explain why each component is present, how they tested an unsupported or failed case, and what evidence would be needed before using the application with real users or data.
