---
name: session-initialization
description: "Initialize repository, general, or project mode once; establish scope, read current context, and handle new evidence without repeated intake."
triggers: [session start, explicit reset, scope change]
load_with: []
safety_level: critical
run_before: routing
license: Proprietary
---

# Skill: Session Initialization

## Purpose

Establish only the context needed for the request. Run once after
[system_prompt.md](../../system_prompt.md), then hand off to
[routing](../routing/SKILL.md). Do not recursively initialize from other skills.
The 200-character description limit is a local authoring preference, not a
safety rule or a claim about every host's upload limits.

## Trust Boundary

The critical rating concerns process integrity, not professional authority.
BTBA may select mode, read scoped files, and maintain reversible local notes.
It may summarize claims provisionally, but cannot verify site conditions or
approve work through initialization. Follow the system prompt's safety and
authorization boundaries. Immediate danger takes priority over this procedure.

## Select Mode and Scope

| Mode | When | Initial context |
|---|---|---|
| Repository | Agent, skills, tools, or repository maintenance | Requested files and applicable conventions only. Do not open private projects as examples without a task-specific need. |
| General | Concepts or advice without a property-specific assessment | User question and relevant domain sources. No mandatory address, project file, or attachment intake. |
| Project | An identified property/folder or a site-specific request | Active folder's index/current summary, then sources relevant to the question. |

- An explicitly supplied folder, project name, or unambiguous user selection is
    sufficient. Do not ask for it again. Use editor context only as a hint.
- If ambiguity affects a site-specific conclusion or write destination, ask one
    targeted question. Otherwise proceed with bounded general guidance.
- On an explicit project switch, acknowledge it and replace project context;
    no redundant approval question. If the switch is only inferred, clarify first.
    Explicit comparisons may use separate, clearly labeled project contexts.
- Match the user's language. Do not infer language from an address or code term.

## Read in Scope

1. Reuse relevant conversation context and already loaded, unchanged files.
2. In project mode, list the active folder as needed and read its INDEX.md first
     if present, then the linked current summary and relevant decision/hold entries.
     If no index exists, read a current summary if identifiable. Read project.md
     only as needed for context or as a fallback, not as a verified fact register.
3. Follow links to the specific drawings, decisions, reports, or correspondence
     needed to substantiate claims. Record date/revision, source type, and scope.
     Separate proposed, existing/reported, reviewed, issued, and approved states.
4. Use routing for relevant domain skills. Load municipality guidance only when
     local requirements affect the answer; load lessons lazily for a matching
     failure mode or explicit retrospective, not as a startup scan.
5. If navigation, conflicting versions, or document updates need attention, load
     [project-lifecycle](../project-lifecycle/SKILL.md). Do not count or audit all
     project files by default, and do not make an index a prerequisite to answering.

## Incremental Evidence and Questions

- Check what was actually supplied. Do not ask for photos, an address, or a task
    the user already provided. Ask only for missing information that changes the
    conclusion; explain the limit when proceeding without it.
- New attachments do not restart intake. Identify source/revision and affected
    question, inspect relevant content through routing, and update only affected
    evidence and dependencies. Do not assume an attachment was saved to disk.
- A changed design is an evidence update, not an automatic new project. Reset
    scope only when requested or genuinely changed; retain relevant source history.
- If the user declines data, give useful bounded guidance without repeatedly
    requesting it. Do not turn assumptions into verified inputs.

## Compact Session Record and Completion

Track only useful state: mode/scope, loaded sources and revisions, answered
questions, material claims with evidence status, assumptions and their impact,
open holds, and next actions. Record an evidence summary, not internal deliberation.

Skip a startup banner when the task is clear. If useful, state scope and material
limits in one sentence and answer the actual question, not another intake form.

For meaningful project updates, use the existing decision log/index as appropriate
and preserve provenance. Routine reversible local edits within scope do not need
another approval prompt. External writes, moves, destructive actions, and release
of private data require explicit authorization. State what was actually saved;
do not promise persistence or background checks. New versions or corrected inputs
trigger only the scoped lifecycle completion check, not an automatic full audit.

*Last reviewed: 2026-09-06*
