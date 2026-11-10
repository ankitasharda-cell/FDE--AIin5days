# Day 1 — LLM Foundations and Prompting

## Outcome

Explain the basic request/response flow of an LLM application and improve a prompt using clear instructions, context, and output requirements.

## Concepts

- A language model generates likely continuations from input tokens; it does not automatically verify that its response is true.
- A typical application sends messages and settings to a model and receives generated output. The exact interface depends on the provider and model.
- Prompts can include instructions, relevant context, examples, and a requested output format.
- Sampling settings influence generation but do not replace clear task design or validation.
- Model outputs can be incomplete, inconsistent, or fabricated; important results need verification.

## Guided exercise

Choose a low-risk task, such as turning a short public paragraph into a summary. First write a vague prompt. Then improve it by specifying:

1. The task and intended audience.
2. The source material the model may use.
3. Constraints such as length, tone, or what to preserve.
4. The desired output structure.

Compare both responses against the source. Identify unsupported claims, omissions, and formatting differences. Revise the prompt and test it on a second paragraph.

## Checkpoint

Ask the learner to explain why a more detailed prompt helped, name one limitation that prompting cannot eliminate, and describe how they would verify the answer.
