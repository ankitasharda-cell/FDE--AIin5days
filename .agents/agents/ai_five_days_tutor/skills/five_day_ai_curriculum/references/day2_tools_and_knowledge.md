# Day 2 — Tools, Retrieval, and MCP

## Outcome

Distinguish model-generated text from application-provided information and actions, and explain how a bounded tool or retrieval step can help an AI application.

## Concepts

- A tool gives an application a defined operation, such as looking up a record or performing a calculation. The application executes the tool and returns its result to the model.
- Tool calls need clear input schemas, validation, error handling, and appropriate authorization. A model proposing a call is not the same as the application executing it.
- Retrieval finds relevant material from a collection and supplies it to the model as context. Retrieval can improve grounding, but does not guarantee relevance or correctness.
- Model Context Protocol (MCP) is a protocol for connecting AI applications with external tools and context sources. It is not itself a model or a guarantee that a connected tool is safe.
- Data from tools and retrieved sources should be treated as untrusted input.

## Guided exercise

Design (or implement, if the learner has a suitable environment) a read-only lookup tool over a small, synthetic dataset. Define its purpose, accepted inputs, result shape, and behavior for missing or invalid values. Trace the flow: user request → model's proposed tool call → application validation and execution → result returned to model → final answer.

For a knowledge exercise, provide a few short public or synthetic notes and ask a question that requires finding one of them. Check whether the response is supported by the selected note, and test a question the notes cannot answer.

## Checkpoint

Ask the learner to distinguish a tool call from ordinary generated text, explain one difference between retrieval and MCP, and name a safeguard for tool inputs or outputs.
