---
name: project-lifecycle
description: "Maintain project navigation, correspondence/RFI evidence, release holds, and dependencies; use for scoped document control, revision review, and safe archiving."
license: Proprietary
triggers: [project index, current summary, document revision, evidence conflict, corrected input, release hold, archive, superseded, project folder hygiene, correspondence register, RFI tracking]
load_with: []
safety_level: medium
---

# Skill: Project Lifecycle

## Purpose

Keep the active project navigable without duplicating its history or turning
document housekeeping into technical approval. Load for the triggers above,
not for every session. Use [system_prompt.md](../../system_prompt.md) for shared
safety rules; do not load startup or routing recursively.

## Trust Boundary

BTBA may maintain scoped local navigation, draft labels, and dependency holds.
It may identify conflicts and possible supersession, but cannot approve a design,
verify an as-built condition, or revoke an authority's decision. Technical and
regulatory conclusions need appropriate source evidence and review. Routine
reversible local edits may proceed; external writes, moves/renames, deletion,
bulk restructuring, and difficult-to-reverse actions require explicit authorization.
Never stage or publish ignored project data or copy it into shared instructions.

## Current-State Navigation

Read the active folder's INDEX.md first if present, then its linked current
summary and the relevant underlying sources. If neither exists, use targeted
listing/search and state coverage limits. File count alone does not require an
audit or new index. Create an index only when useful and within the requested
scope; if new files are prohibited, update an existing navigation document.

An index should link, not repeat all project facts:
- **Current scope/phase** and the current summary, with source/date where needed.
- **Active documents** with role, revision, evidence/release status, and source.
- **Open decisions and release holds**, including affected downstream documents.
- **Needs verification before reuse**, with reason and the evidence needed.
- **Superseded/archived references**, replacement links, and retained unique scope.
- **Output destination and convention**, when local deliverables are requested:
  existing folder/file to update, naming and revision practice, and draft status.
  Resolve paths within the active project; do not overwrite source or issued
  records. Record only files actually saved. Do not create another context file
  merely because an external guide uses a different filename.

Use an existing drawing/document register to identify relevant revisions before
opening sheets. Check newer revisions for changes, but establish applicability
and approval separately. A newer draft does not automatically displace an
approved issue, and an older approval does not cover newly changed scope.
If register and file disagree, flag the conflict and state review coverage;
do not silently choose either or force a whole-folder rescan.

Keep existing naming conventions for new revisions. Do not rename existing
files just to normalize style. A navigational label such as "active" means useful
for current work, not legally valid, technically verified, or approved.

## Evidence and Release Status

Track claim status separately from document status, with source, date/revision,
scope, and reviewer/authority where known. Authority is not recency: a newer
draft cannot supersede an applicable permit or signed design merely by its date.

| Status | Meaning and limit |
|---|---|
| Reported | User or third-party claim; preserve attribution, not independent verification. |
| Observed/documented | Evidence actually inspected; state what it establishes and what remains hidden or outside scope. |
| Proposed/assumed | Design intent or calculation assumption; not an existing condition. |
| Derived | Calculation or interpretation; depends on identified inputs and method. |
| Reviewed | Named reviewer and defined scope; not automatically approved or issued. |
| Submitted/issued | Supported transmission record identifying destination, date, and exact version; a draft filename or attachment list is insufficient. |
| Approved | Identifiable decision by the competent authority or authorized reviewer, limited to its scope, revision, and conditions. Distinguish client design acceptance from statutory approval. |
| Disputed/unverified | Conflicting or missing evidence; retain alternatives and a resolution action. |
| Superseded | A documented replacement covers the identified scope; unique content and history still matter. |

Input confirmation, a "design lock", AI review, or a machine check does not
constitute professional or statutory approval. A missing report is an evidence
gap, not proof of illegality. Never promote a draft email to "sent" or an
attachment mentioned in it to "issued" without transmission evidence.

Release gates must match purpose. An explicitly authorized clarification,
professional-appointment enquiry or preliminary pricing request can disclose
open design holds, exact assumptions and its attachment manifest. It does not
release construction, ordering or fixed-price scope. Do not require a completed
design before the enquiry needed to appoint its designer. Those consequential
uses retain their relevant verified-design, scope and permission gates.

## Scoped Correspondence and RFI Records

For requested correspondence or RFI (request for information) work, read only
the relevant thread, attachments, and linked register entries. Prefer the existing
correspondence/RFI register or decision log; preserve its IDs and conventions.
Do not require new parallel files. If no suitable register exists, return a
scoped draft record in the response rather than mandate a new tracking system.

Record these fields, marking missing evidence **unknown**, not inferred:
- **Identity and provenance:** record ID/type (RFI, instruction, transmittal,
  clarification, etc.), source link/message ID, source date, sender, recipient(s).
- **Exact document basis:** file/drawing number, revision and date; attachment
  manifest distinguishing referenced, actually received, missing, and unreadable
  attachments. A matching filename alone does not establish the exact revision.
- **Matter and responsibility:** question or reported instruction, affected
  package/drawing/zone, responsible action owner, due date and its basis
  (explicit request, agreed date, or cited contractual provision). Label a
  proposed date as proposed; do not invent a deadline or contractual entitlement.
- **Dispatch and receipt:** separate status, dates, and evidence links for each;
  a draft is not dispatched, and dispatch alone does not prove receipt.
- **Response:** source/date, respondent, exact revision/scope addressed, answer
  or partial answer, and remaining questions. Link follow-ups to the same issue.
- **Closure:** open/pending/closed status, closure evidence, who confirmed it,
  when, and for which scope. Preserve the original question and response history.
- **Unresolved impact:** affected design, quantities, cost, schedule, procurement,
  or release holds, with the next action/evidence needed; label uncertain impacts.

A reply is not design approval, variation authorization, or proof that an issue
is closed. Each requires its own scope-specific evidence and an appropriately
authorized decision-maker. Receipt acknowledgments and partial answers leave
unresolved items open. A reported instruction is not evidence of authority to
change scope or commence work. Apply the evidence/release gates above; route
changed inputs through dependency invalidation below only where affected.

State the correspondence/date range and attachments actually checked. This is
an on-demand review, not automatic monitoring, reminders, sending, or escalation.
External actions still require explicit authorization.

## Drift and Dependency Invalidation

When an input, drawing revision, scope, or authority condition changes:
1. Record old/new claim, source/revision, evidence status, and the affected scope.
2. Search the active project's relevant calculations, quantities, costs, drawings,
   tender text, sequencing, and submissions for direct and downstream dependencies.
3. Mark dependent conclusions **not valid for reuse pending revalidation** where
   the old basis no longer applies. For uncertain impact, label **needs review**.
   Preserve original calculations and issued records; do not silently overwrite
   source evidence or declare every historical document void.
4. Recompute/reconcile only within competence and task scope. Record unresolved
   dependencies as release holds, with the evidence/reviewer needed to close them.
5. Update links and the existing decision log/index where in scope. State what
   was searched, reconciled, or left unchecked. Do not claim a complete cascade
   check from a narrow search or infer approval after closing a local hold.

When quarantining a mixed or unreliable summary, carry forward useful owner
requirements and reported existing conditions with attribution and primary
source links. Preserve retained installations, room programmes, dimensions and
orientation conflicts as explicit requirements or open decisions, not merely
buried historical text. This prevents evidence correction from erasing scope.

## Safe Archiving

Default to an in-place status label and index entry. Before any move:
- Verify the replacement's content and scope, not merely its date, filename, or
  self-declared "outdated" banner. Preserve unique decisions, evidence, and notes.
- Check inbound and outbound links, relative images/assets, comparison references,
  and records of submitted/issued versions. Keep originals of authoritative or
  issued evidence intact; annotate status in navigation or a separate review.
- Explain exact source/destination and link repairs, then obtain authorization
  for the move. Do not overwrite a destination or delete the source history.
- After an authorized move, preserve filename where practical, repair links and
  inventory entries, and verify they resolve. If external or unknown references
  cannot be preserved, leave the source in place and report the limitation.

## Scoped Completion Check

Run only when this task revised documents, corrected inputs, or changed status:
- Are scope, provenance, draft/release status, and unresolved holds explicit?
- Are known affected dependencies reconciled or flagged for revalidation?
- Do touched navigation entries and links still resolve?
- Have unique history, unrelated edits, ownership limits, and privacy survived?
- Which checks remain incomplete, and which external actions were not taken?

Report actual changes and limits. Do not run automatic background audits, scan
other projects, archive without authorization, or promise ongoing monitoring.

Public inspiration: [10 Plug-and-Play Claude Skills for Construction Professionals](https://aiconstructionnews.com/blog/ai-trends/ccc),
May 20, 2026, document-control concept only. These are original BTBA instructions;
no paid skill source was accessed or copied.

*Last reviewed: 2026-09-06*
