# Day 3 — Context Engineering and Reusable Skills

## Outcome

Select relevant information for a model request and turn a repeatable task into a clear, reusable workflow.

## Concepts

- Context is the information available to the model for a particular request, including instructions, conversation history, retrieved material, and tool results.
- More context is not always better. Irrelevant, stale, or conflicting content can consume a context window and make results worse.
- Context engineering is the deliberate selection, organization, and updating of information provided to a model.
- A reusable skill captures a task's purpose, procedure, constraints, and expected output so it can be applied consistently.
- Persistent memory, when used, should be limited to information that is useful, appropriate to retain, and under the application's control.

## Guided exercise

Take a repeated task, such as summarizing a project update. Identify the minimum context needed, the information that must not be assumed, and the expected output. Write a short reusable procedure with an input checklist, ordered steps, and a completion check.

Try the procedure with two different synthetic updates. Remove redundant context, then check whether the results remain useful and consistent. Discuss what should be retrieved on demand rather than placed in every request.

## Checkpoint

Ask the learner to identify one source of irrelevant or stale context, describe how they would keep a reusable skill focused, and explain what information should not be stored as memory.
