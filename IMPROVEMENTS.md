# BTBA Agent — Change Log

---

## v2.0 (2026-08-09) — Architecture Overhaul

Major release. See README.md for the full feature list.

**Key changes:**
- **20-skill modular architecture** — all skills restructured to `skills/<name>/SKILL.md` directory format per agentskills.io spec
- **3 new domain skills**: `geotechnical`, `soknad-package`, `bim-ifc`
- **2 new utility skills**: `drawing-reader` (with OCR pipeline + security fencing), `drawing-investigation-protocol` (now separate from reading)
- **`formulas-reference` split** into core SKILL.md + `references/` for historical materials and worked examples
- **DOK arealanalyse** section added to `building-code-tek17`
- **Structural failure modes** diagnosis guide added to `structural-engineering`
- **Decision log persistence** — session facts can be written back to `project.md`
- **MCP config** expanded: Marker, ocr-skill, ezdxf, ifcmcp, Geonorge added
- **README** completely rewritten to match actual architecture
- All `license: Proprietary` fields added to every skill (agentskills.io spec compliance)
- All stale file paths removed from system_prompt.md, README, routing

---

## v1.3 (2026-07-27) — Session Initialization Fix

> **Historical note:** Skill paths in this section (e.g., `skills/session-initialization.md`) use the old flat-file format. The current system uses `skills/<name>/SKILL.md`. All functionality described below is still present — only the paths changed.

You were right: BTBA was asking questions in circles and not reading from its own documentation. This fixes it.

---

### The Core Problems (Identified)

1. **No forced documentation reading** — Skills existed but BTBA would skip them.
2. **No image/attachment checking** — If you uploaded photos, BTBA might not ask to see them.
3. **No decision logging** — Questions got asked multiple times in the same session.
4. **No session context** — Every response started from scratch instead of building on what was already discussed.
5. **No structured questioning** — BTBA would ask 15 questions at once instead of the 3-4 that actually matter.

---

### The Fixes (v1.3)

### 1. **Mandatory Session Initialization** (`skills/session-initialization.md`)

Before answering ANY question, BTBA now:

```
✓ Detects your language (Norwegian/English)
✓ Checks for attachments or images
✓ Loads project context if one exists
✓ Reads foundational skills (routing, structure, code)
✓ Creates a Decision Log to track what's been asked
✓ Orients you with one clear question
```

**Result**: No more starting from zero. No more "what's the material?" after you already said it.

### 2. **Non-Repetition Rule** (Part of Session Init)

Every question is checked against the Decision Log first:

```
IF question already answered this session:
  → Skip it, reference the prior answer
  → Move to the NEXT logical question

IF question is similar but different:
  → Acknowledge the context
  → Ask only what's new
```

**Result**: Focused conversations. One answer per question per session.

### 3. **Structured Drawing Protocol** (`drawing-investigation-protocol.md` + Session Init)

If you provide photos or drawings:

```
1. Ask you to upload them (if you haven't)
2. Load them immediately
3. Describe what's visible
4. Ask systematic gaps (dimensions, materials, loads, conditions)
5. Document in Decision Log: "Drawing shown: [description]"
```

**Result**: Drawings get examined before structural claims are made.

### 4. **Decision Log** (Updated Core Framework)

Every session now has a running log:

```
# Decision Log
- Question 1: Is the beam load-bearing?
  Answer: Yes, supports floor above
  Source: User + drawing inspection
  Confidence: High

- Question 2: What material?
  Answer: Timber, ~200×100mm (observed)
  Source: Drawing measurement
  Confidence: Medium

- Assumption 1: C24 grade (not specified)
  Impact: Load-bearing capacity
  Can override: Yes
```

You can always see what's been established and what's still open.

### 5. **Documentation-First Workflow**

The updated `system_prompt.md` now requires:

```
Step 1: Check Decision Log (don't repeat)
Step 2: Load relevant skills (routing.md applies)
Step 3: Read the drawings (if present)
Step 4: Do the analysis
Step 5: Document it in Decision Log
```

**Result**: Every answer is grounded in documentation, not improvisation.

---

## How It Works in Practice

### Old Flow (Broken)
```
User: "Is my kitchen beam adequate?"
BTBA: "What's the span? What material? What loads? When was it built?"
      [15 questions at once — feels circular]
```

### New Flow (Fixed)
```
[Session Init runs]
BTBA: "I'm ready. What's the project address or name?"

User: "Kitchen at Aasmund Vinjes vei 5, beam was installed 12 months ago."
[Decision Log creates entry for project + prior knowledge]

BTBA: "Got it. Can you share a photo of the beam?"
[Waits for image, then loads drawing-investigation-protocol]

User: [Uploads photo]
BTBA: "I see a concrete tile roof, ~3m span. I need:
      - Exact beam dimensions (take a tape measure?)
      - Support type at each end
      - Any visible distress?"
[Each question MATTERS; none repeated]
```

---

## Files Changed

| File | What Changed |
|---|---|
| `system_prompt.md` | Added Session Initialization requirement + updated Core Decision Framework to include Decision Log steps |
| `skills/session-initialization.md` | NEW — Defines the startup checklist, non-repetition rule, and Decision Log structure |
| (All other skills) | No changes — they're loaded on-demand as before |

---

## What You'll Notice

✅ **First message is always an orientation**, not a flood of questions  
✅ **Second message asks only what you haven't answered yet**  
✅ **Photos/drawings are requested explicitly** and examined before analysis  
✅ **Assumptions are documented** — you can challenge them  
✅ **Conversations don't loop** — each new question moves forward  

❌ **Less freestyle**, more structured  
❌ **Requires you to provide data** (won't pretend to know things)  
❌ **More reliance on drawings** — "show me" before "tell me"  

That's intentional. Circles happen when there's no structure.

---

## Next Steps for You

1. **Try it on your kitchen beam question** — see if the flow feels different
2. **Upload that photo or drawing** when prompted — BTBA will wait
3. **Let me know if the questions make more sense now** — they should be focused, not circular

This fix is about discipline: reading docs first, checking what's been said, asking only what matters, documenting everything. That's how a real contractor works.

---
