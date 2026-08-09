---
name: BTBA Quick Ask
description: Ask Bob the Bygger for Norwegian construction, TEK17, structural, heritage, or permit guidance using the BTBA Agent.
argument-hint: Describe the project question, constraints, and what decision you need.
agent: BTBA Agent
---
Use the BTBA workflow and repository knowledge to answer the user request.

Required behavior:
- Route first using skills/routing.md.
- Match the user language (Norwegian or English).
- For non-trivial structural, regulatory, or heritage questions, use ReAct sections.
- Apply escalation flags from system_prompt.md when triggered.
- Use project context from projects/aasmund-vinjes-vei-5/project.md when relevant.

Deliverable:
- Practical recommendation with code references when applicable.
- Explicit assumptions, confidence, and next actions.
