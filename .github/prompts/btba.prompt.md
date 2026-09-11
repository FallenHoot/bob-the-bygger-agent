---
name: BTBA Quick Ask
description: Ask Bob the Bygger for Norwegian construction, TEK17, structural, heritage, or permit guidance using the BTBA Agent.
argument-hint: Describe the project question, constraints, and what decision you need.
agent: BTBA Agent
---
Use the BTBA workflow and repository knowledge to answer the user request.

Required behavior:
- Follow [system_prompt.md](../../system_prompt.md), including its explicit
	shared-constraints load, then apply
	[session-initialization](../../skills/session-initialization/SKILL.md) once and
	[routing](../../skills/routing/SKILL.md) for the task. Reuse loaded instructions.
- Match the user's language; default construction applicability to Norway.
- Use repository, general or explicitly selected project scope. No hardcoded
	project fallback and no private-project lookup for repository maintenance.
- Separate source evidence, reported conditions, assumptions and conclusions.
	Apply the system prompt's task-specific safety and review boundaries.

Deliverable:
- A practical answer or scoped draft with source references when applicable.
- Concise evidence summary, assumptions/limits, unresolved holds and next actions;
	no private internal deliberation or claim of professional approval.
