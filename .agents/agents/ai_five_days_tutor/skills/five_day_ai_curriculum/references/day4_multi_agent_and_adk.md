# Day 4 — Multi-Agent Systems and Google ADK

## Outcome

Decide when a multi-agent design is warranted, describe how agents can coordinate, and identify the responsibilities of an orchestration framework such as Google's Agent Development Kit (ADK).

## Concepts

- A multi-agent system separates work across agents with defined roles or capabilities. Multiple agents add coordination and failure modes; they are not automatically better than one well-designed agent.
- An orchestrator coordinates task assignment, information handoff, and completion. Clear boundaries and shared state rules help prevent conflicting work.
- Google ADK is a framework for building and orchestrating AI agents. Exact APIs and deployment choices are version-dependent; consult the official documentation for implementation details.
- Tool permissions, timeouts, retries, and human approval should be considered for each agent and tool.
- A system should make failures observable and have a bounded response when an agent or tool cannot complete its task.

## Guided exercise

Design a small research-and-summary workflow using a single agent first. If separate responsibilities provide a clear benefit, sketch two bounded agents, such as a source finder and a summarizer, plus an orchestrator.

For each component, specify its responsibility, allowed inputs and tools, expected handoff, and failure behavior. Walk through a case where no sources are found and one where the agents return conflicting results. Compare the design's complexity with the single-agent version.

## Checkpoint

Ask the learner to justify whether their example needs more than one agent, describe the orchestrator's role, and identify one permission or failure-handling boundary.
