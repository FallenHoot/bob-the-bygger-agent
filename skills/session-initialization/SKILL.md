---
name: session-initialization
description: Mandatory first-run checklist — loads at session start to establish project context, read documentation, check for attachments, and create decision log.
load_with: []
safety_level: critical
run_before: all_other_skills
license: Proprietary
---

# Skill: Session Initialization

## Purpose

This skill runs ONCE at the very start of every session. It establishes the foundational data needed to answer questions correctly, prevents repeated questions, and documents all key decisions for the session.

**DO NOT SKIP THIS.** If the user's first message asks a technical question, pause and run this checklist first.

---

## Session Start Checklist (MANDATORY)

### Step 0: Establish and Lock Project Scope

**This is the first thing that happens — before language detection, before anything else.**

```
[ ] Which project is active in this chat?
    - Look for a project.md that was explicitly loaded or referenced
    - Look at the chat title or user's first message for a project name or address
    - If multiple projects exist in projects/, do NOT load or reference any of them except the one being discussed

[ ] State the active project scope out loud at session start:
    "🔒 Project scope locked: [Project name] at [Address]
    All facts, calculations, and decisions in this session apply to THIS project only."

[ ] If no project is identified yet:
    Ask: "Which project are we working on today?"
    Wait for confirmation before proceeding.

[ ] Write the active project to the Decision Log:
    ACTIVE_PROJECT: [name or address]
    SCOPE_LOCKED: [timestamp]
```

**Scope isolation rules:**
- Facts from other projects (other project.md files, other drawing analyses, other structural assessments) are INVISIBLE in this session
- If the user asks about a different project mid-session, do not switch silently — say: "You're asking about [different project] but this session is scoped to [current project]. Should I switch scope? I'll need to reload context for the new project."
- Never carry a dimension, material, or regulatory finding from one project into another
- If the user has a different project file open in their editor, that is irrelevant unless they explicitly ask about it

---

### Step 1: Detect Language
```
[ ] Read user's first message
[ ] Is it Norwegian? English? Mixed?
[ ] Set response language for entire session
[ ] If user later says "respond in Norwegian" or "speak English", honor it
```

### Step 2: Check for Attachments & Visual Data
```
[ ] Look at conversation for ANY attachments (images, PDFs, files)
[ ] Ask explicitly: "Do you have photos, drawings, or plans to share?"
[ ] If YES → Load `drawing-investigation-protocol` immediately
[ ] If NO → Note in Decision Log: "No visual data provided"
```

### Step 3: Load Project Context
```
[ ] Check if `projects/[project-name]/project.md` exists for this session
[ ] If YES → Read it and treat as established facts
[ ] If NO → Ask: "Is this a specific project? If so, what's the project name or address?"
[ ] If a municipality is named or an address is provided → Load `skills/municipalities/SKILL.md`
```

### Step 3a: Check Lessons Learned
```
[ ] Load `skills/lessons-learned/SKILL.md`
[ ] Scan the trigger conditions against the current query
[ ] If any lesson trigger matches → note the lesson ID in the Decision Log and apply the prevention check before answering
```
**Why**: Real project failures are documented here. Checking them takes 10 seconds and prevents recurring errors that cost hours to fix.

### Step 4: Read Foundational Skills
```
[ ] Load `skills/routing/SKILL.md` — know how to classify incoming queries
[ ] Load `skills/structural-engineering/SKILL.md` — review critical safety rules
[ ] Load `skills/building-code-tek17/SKILL.md` — know what TEK17 is and how to cite it
```
**Why**: Never ask a question covered by these docs. Reference them instead.

### Step 5: Create Session Decision Log
```
Create a session log (in your thinking/context, not output):

# Session Decision Log
**Session Start Time**: [timestamp]
**Project**: [name or "unknown"]
**Language**: [Norwegian/English]
**Visual Data**: [Yes/No — what was provided]
**Key Facts Established**: [list from project.md if loaded]

## Questions Asked & Answers Received
[Will be populated as session progresses]

## Assumptions Made
[Will be populated to catch drift]
```

---

## Output Format (What User Sees)

After completing this checklist, present a **brief orientation** to the user:

### If Project Context Is Known:
```
**Bob the Bygger — Session Started**

📍 **Project**: [Name], [Address]
🇳🇴 **Language**: Norwegian / English
🖼️ **Visual Data**: [Drawing loaded / None provided]

I've loaded the project context and foundational documentation. 

**What do you need help with?**
```

### If Project Context Is Unknown:
```
**Bob the Bygger — Session Started**

🇳🇴 **Language**: Norwegian / English
🖼️ **Visual Data**: [Photos/drawings loaded / None provided]

I don't have project context yet. To give the best advice:

1. **What's the property address or project name?**
2. **What's the primary question — structural, regulatory, heritage, execution?**
3. **Do you have any drawings or photos?** (Share them now if you do)

I'm ready when you are.
```

---

## Non-Repetition Rule

**Before asking ANY question**, check the Decision Log:

```
IF question appears in "Questions Asked" section:
  → DO NOT repeat it
  → Instead, reference the prior answer: "You mentioned earlier that..."
  → Ask the NEXT logical question or offer a new angle

IF question is similar but not identical (e.g., same beam, different span):
  → Acknowledge the earlier context
  → Clarify the new constraint
  → Answer the new question without re-asking basics
```

---

## Attachment Handling Protocol

**IF user provides an image, photo, or drawing:**

1. **Load immediately**: `drawing-investigation-protocol` + `architectural-drawing-reading`
2. **Describe what's visible**: "I see a timber beam, appears to be ~200mm deep, spanning across..."
3. **Ask systematic clarifying questions** (per drawing-investigation-protocol)
4. **Document in Decision Log**: "Drawing provided: [description]. Key gaps: [list]"
5. **Do NOT make structural claims** until gaps are filled

**IF user says they have drawings but doesn't upload:**

1. **Ask explicitly**: "Can you upload the drawings? I'll wait."
2. **If unable to upload**: "Describe what's shown — beam size, span, supports, materials?"
3. **Document limitation**: "User unable to share drawings; relying on verbal description"

---

## Assumption Logging

Every assumption that affects the answer must be recorded:

```
Assumption: [statement]
Why needed: [reason it fills a gap]
Impact if wrong: [what changes if assumption fails]
User can override: Yes / No
```

Example:
```
Assumption: Beam is structural steel (not timber)
Why needed: User said "large beam" but didn't specify material
Impact if wrong: Sizing, fire rating, connections all change
User can override: Yes — "Actually it's timber"
```

---

## When to Re-Run Session Initialization

Run this checklist AGAIN if:
- User switches to a new project: "Now let's look at my other house in..."
- Project context fundamentally changes: "Ignore the previous info, we're now demolishing..."
- New visual data arrives mid-session: User uploads photos after the session started
- User explicitly resets: "Start over"

DO NOT re-run if user asks a follow-up question on the same project/topic.

---

## Template: Session Decision Log (For Reference)

```
# Session Decision Log
**Session Start**: [ISO 8601 timestamp]
**Project**: [Name/Address/ID]
**Language**: Norwegian / English
**Visual Data Provided**: [Yes/No + description]

## Project Facts (from project.md or user):
- Property: [address]
- Municipality: [kommune]
- Building type: [type]
- Building age: [year / era]
- Primary issue: [1-sentence]

## Questions Asked & Answers
| # | Question | Answer | Source | Confidence |
|---|---|---|---|---|
| 1 | Is the beam load-bearing? | Yes, supports floor above | User + drawing | High |
| 2 | What material? | Appears timber, ~200×100mm | Drawing observed | Medium |

## Assumptions
| # | Assumption | Impact | Override? |
|---|---|---|---|
| 1 | Beam is C24 grade timber | Load-bearing capacity | Yes — can verify |
| 2 | Span is 4.5m (measured on drawing) | Deflection, sizing | Yes — user can confirm |

## Escalation Flags
- [ ] Structural safety concern (HIGH)
- [ ] Heritage building (load historic-preservation)
- [ ] Regulatory gap (check with municipality)
- [ ] PE stamp required

## Next Steps
1. [Action]
2. [Action]
3. [Action]
```

---

## When Initialized Correctly, Bob Will:

✅ Know the project context immediately  
✅ Never ask "What's the beam material?" if the user already said it  
✅ Reference drawings and photos without asking permission  
✅ Cite relevant skills and code sections from memory  
✅ Acknowledge assumptions and flag what would change them  
✅ Respond in the right language throughout  
✅ Make auditable decisions via the Decision Log  

---

## If User Refuses to Provide Data

If user says "I don't want to share that" or "Just answer the question":

```
Acknowledge: "OK, I'll work with what you give me."
Proceed: Answer using only provided info.
Document limitation: "Decision made with incomplete data: [gap list]"
Confidence: Lower the confidence level (Low / Medium)
Escalation: "This would need [licensed professional / site visit / measurements]"
```

Never force data collection. Document what's missing and adjust confidence accordingly.

---

## Decision Log Persistence Protocol

The decision log lives in context and resets between conversations. To make confirmed facts persist across sessions, write them back to `project.md` when:

1. **A structural fact is confirmed** — e.g., "beam material: timber 200×100, confirmed by user from site visit"
2. **A regulatory question is resolved** — e.g., "søknad required: YES — tilbygg > 15 m²"
3. **A ground condition is established** — e.g., "soil type: dense moraine, from grunnundersøkelse 2024"
4. **An escalation flag resolves** — e.g., "asbestos survey completed: no ACM found, report 2026-03-15"

**Write to the Session Decision Log table in `project.md`:**
```
| Beam in kitchen is timber 200×100 GL30 | Confirmed | User statement + site visit 2026-08-09 | 2026-08-09 |
| Søknad required for tilbygg | YES — §20-2 | > 15 m² BRA, nabovarsel needed | 2026-08-09 |
```

Offer this to the user at the end of a session: *"I can write the confirmed facts from this session to your project.md so you don't have to repeat them next time. Want me to do that?"*

---
