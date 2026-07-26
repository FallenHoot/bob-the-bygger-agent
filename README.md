# Bob the Bygger — Agent

**BTBA** (Bob the Bygger - Agent) — Norwegian Construction AI Advisor

⚠️ **DISCLAIMER: DEMONSTRATION TOOL ONLY**

**Bob the Bygger is a proof-of-concept demonstration tool created to showcase what an AI-powered Norwegian construction advisor could do. It is NOT:**
- Official guidance from DiBK, Byantikvaren, NVE, or any regulatory authority
- Approved by any government or professional organization
- Guaranteed to be accurate (data may be correct or incorrect)
- Suitable for use in official documentation, permit applications, or professional sign-offs

**Use cases:**
- ✅ Learning resource (understand TEK17 concepts)
- ✅ High-level project planning (early-stage exploration)
- ✅ Research aid (spotting potential issues before consulting professionals)
- ❌ Official permit documentation
- ❌ Structural engineer calculations (without licensed PE review)
- ❌ Heritage building approval (without Byantikvaren consultation)
- ❌ Regulatory compliance certification

**For any real project:** Always consult licensed professionals (structural engineers, architects, heritage consultants, municipal building departments). Bob is a thinking partner, not a replacement for professional judgment.

---

*A production-grade AI assistant for Norwegian building regulation compliance, structural engineering, and architectural design guidance.*

**Version:** 1.3 | **Last updated:** 2026-07-26

---

## Overview

**Bob the Bygger** is a specialized AI agent grounded in Norwegian building codes, Eurocode standards, and practical construction expertise. It operates as a reasoning system (ReAct protocol) with explicit escalation gates for high-risk decisions.

**Designed for:**
- Architects, structural engineers, and builders navigating TEK17 compliance
- Heritage building restoration and energy upgrades
- Structural assessment and sizing
- Permit application preparation (forhåndskonferanse, søknad)
- Project documentation and compliance audits

**Not a replacement for:** Licensed structural engineers (ansvarlig prosjekterende), building permit authorities, or heritage consultants. Bob flags when you need professional sign-off.

---

## Quick Start

### Prerequisites
- Access to Bob the Bygger system (this codebase)
- Optional: Project context file (`project.md`) for session persistence
- Optional: MCP server connections (structural-analysis, Catenda Hub)

### Basic Usage

1. **Load Bob the Bygger in your chat interface:**
   - Point to `system_prompt.md` as the system instructions
   - Bob will automatically load the routing skill first
   - Load domain skills on-demand based on query classification

2. **Ask a question:**
   ```
   "I have a 1952 residential building. I want to add roof insulation 
    for energy compliance. What's required?"
   ```

3. **Expect a structured response:**
   - **ReAct trace** (for complex queries): Thought → Assessment → Code Check → Escalation → Uncertainty → Action Required
   - **Escalation flags** (if applicable): 🚩 WET_STAMP_REQUIRED, 🚩 SØKNAD_REQUIRED, etc.
   - **Next steps**: Clear action sequence with responsible parties

4. **For projects with ongoing context:**
   - Create a `project.md` file at project root
   - Bob loads it at session start and retains state between queries
   - See `project.md` template for structure

---

## Project Structure

```
btba-agent/
├── README.md                          # This file
├── system_prompt.md                   # Bob's identity, ReAct protocol, escalation matrix
├── project.md                         # [TEMPLATE] Per-project context (user fills in)
│
├── skills/
│   ├── routing.md                     # Query classifier; selects domain skills
│   ├── structural-engineering.md      # Load paths, sizing, deflection, connections
│   ├── building-code-tek17.md         # TEK17 regulations + amendments through 2026-07-26
│   ├── sintef-byggforsk.md            # SINTEF Byggforsk details, moisture, insulation
│   ├── historic-preservation.md       # SEFRAK, Byantikvaren, antikvariske krav
│   ├── classical-architecture.md      # Vitruvian principles, proportion, composition
│   ├── construction-execution.md      # Site sequencing, demolition, contractor coordination
│   └── architectural-drawing-reading.md # Plantegninger, snitt, fasader, detaljer
│
├── mcp/
│   ├── mcp-config.json                # Central MCP server configuration
│   ├── tools/
│   │   ├── structural-analysis.md     # Elandu structural-analysis-mcp integration guide
│   │   ├── catenda-hub.md             # [TODO] Catenda Hub IFC + BCF integration
│   │   └── norwegian-building-data.md # [SPECIFICATION] Future MCP: SEFRAK, NVE, NGU, etc.
│
├── templates/
│   ├── structural-assessment-memo.md  # Site visit findings + recommendations
│   ├── pre-application-meeting-notes.md # Forhåndskonferanse output template
│   ├── compliance-gap-analysis.md     # Regulatory audit + remediation path
│   ├── post-approval-checklist.md     # [TODO] Post-søknad verification steps
│   ├── construction-sequence.md       # [TODO] Phased execution + trade coordination
│   └── heritage-assessment.md         # [TODO] Cultural significance + mitigation options
│
└── docs/
    ├── ARCHITECTURE.md                # [TODO] System design + skill dependency map
    ├── BATTLE_TEST_RESULTS.md         # [TODO] Test scenarios + performance evaluation
    └── ROADMAP.md                     # [TODO] Future features + MCP roadmap
```

---

## How Bob Thinks

### ReAct Reasoning Protocol

For any non-trivial query (structural, regulatory, heritage-related), Bob uses explicit reasoning:

```
Thought:      What do I know? Which skill applies? What assumptions am I making?

Assessment:   The technical answer, grounded in the loaded skill.

Code Check:   What does TEK17 / PBL / SINTEF / Kulturminneloven say?
              (Quote the governing section)

Escalation:   Does this trigger any safety/compliance/heritage flags?
              (See Escalation Matrix below)

Uncertainty:
  - Assumptions: [what did I assume?]
  - Sensitivity: [which assumptions most affect the conclusion?]
  - Confidence: High / Medium / Low
  - If Low: state what additional info would change the answer

Action Required: What must the user, licensed professional, or third party do next?
```

**Example output structure:**
```
Thought:
  Query is about [specific domain]. Checking [applicable section].
  Key assumption: [X]. Uncertainty: [Y].

Assessment:
  Technical answer...

Code Check:
  TEK17 §7-2: "[relevant quote]"
  PBL §20-5: "[relevant quote]"

Escalation:
  🚩 WET_STAMP_REQUIRED — Because [reason]
  ⚠️ NVE_CHECK_REQUIRED — Because [reason]

Uncertainty:
  - Assumptions: [list]
  - Confidence: MEDIUM
  - If foundation soil type changes, answer shifts to [alternative]
  
Action Required:
  (1) [First step]
  (2) [Second step]
  (3) [Responsible party: licensed engineer / municipality / owner]
```

**For quick lookups (material specs, terminology, quick math):** Skip the trace, give direct answer.

---

### Escalation Matrix

Bob flags high-risk decisions explicitly. Flags do **not** stop the answer — they **frame** it.

| Flag | Triggered By | Required Action |
|---|---|---|
| **WET_STAMP_REQUIRED** | Structural modification affecting loads > 2 floors; beam span > 6 m; foundation work near boundary | Ansvarlig prosjekterende (licensed PE) must sign design + calculations |
| **SØKNAD_REQUIRED** | Building modification requiring permit; new construction; change of use | Building permit must be granted before work begins |
| **GEOTECHNICAL_REPORT_REQUIRED** | Foundation work on unknown soil; suspected quick clay (kvikkleire); slope > 1:2 | Grunnundersøkelse (soil investigation) by qualified geotechnical firm |
| **NVE_CHECK_REQUIRED** | Site in flood zone; avalanche zone; landslide hazard area | Verify hazard classification via NVE maps; may require mitigation design |
| **BYANTIKVAREN_CONSULTATION_REQUIRED** | SEFRAK-registered building; heritage zone; antikvarisk building interest | Forhåndskonferanse (pre-application meeting) with municipal heritage officer |
| **RIKSANTIKVAREN_CONSENT_REQUIRED** | Building formally listed (fredete) under Kulturminneloven §15 | Riksantikvaren (national heritage agency) must approve before intervention |
| **ASBESTOS_SURVEY_REQUIRED** | Building constructed 1940–1985; any disturbance planned | Accredited lab analysis before work begins |
| **HAZARDOUS_WASTE_SURVEY_REQUIRED** | Demolition of any building | Kartlegging av farlig avfall before physical demolition |

**Example escalation in response:**
> 🚩 **WET_STAMP_REQUIRED** — Structural modification of load-bearing wall. Ansvarlig prosjekterende (licensed structural engineer) must sign beam design before construction proceeds.

---

## Bilingual Support (Norwegian & English)

**Bob operates fluently in both Norwegian and English:**

### Language Detection
- **Automatic:** Bob detects which language you use (Norwegian keywords: "varmepumpe", "TEK17", "søknad", etc.) and responds in kind
- **Code-switching OK:** If you mix languages, Bob defaults to your primary language
- **Manual override:** Request "svar på norsk" or "respond in English" anytime; Bob honors the request for the session

### Resource Prioritization
- **Norwegian speaker:** Bob prioritizes Norwegian resources (DiBK, SINTEF, lovdata.no, NVE, NGU, Byantikvaren)
- **English speaker:** Bob includes international standards (Eurocode, ASHRAE, ISO) alongside Norwegian context
- **Heritage projects:** Both languages supported for international collaboration

### Technical Glossary
- **Bilingual terminology:** Every technical skill (structural, HVAC, plumbing, electrical) includes Norwegian ↔ English term pairs
- **Education support:** The `technical-education-support` skill provides:
  - Plain-language explanations in both languages
  - Real-world analogies
  - Translated technical glossary (50+ terms)
  - Resource links in both languages

### Example (Norwegian)
```
Bruker: "Hva betyr 'load path'?"
Bob: "Load path = lastfordeling. Det betyr: hvor vekten går.
      Som vann som renner ned en bakke, går byggvekten fra taket → ned gjennom veggene 
      → ned til fundamentet. Hvis noe av kjeden er brutt, kollapser hele bygningen.
      Tenk på det som domino-steiner stilt opp vertikalt — fjern en, og resten faller."
```

### Example (English)
```
User: "What does 'lastfordeling' mean?"
Bob: "Load path (lastfordeling) = where weight goes. Like water flowing downhill, 
      structural loads flow from roof → walls → foundation → ground. If any part breaks, 
      entire building fails. Think of it as dominoes stacked vertically."
```

---

## Skill Map & Dependencies

### Routing Skill (`routing.md`)
**Purpose:** Query classifier. Selects minimum necessary domain skills.
**Always loaded first:** Every query passes through routing logic.
**Usage:** Prevents "skill soup" (loading all skills for every question).

**Routing logic example:**
- Query mentions "TEK17" → load `building-code-tek17.md`
- Query mentions "beam" or "load path" → load `structural-engineering.md`
- Query mentions "1895 villa" + "heritage" → load `historic-preservation.md` + `building-code-tek17.md`
- Query mentions "drawings" → load `architectural-drawing-reading.md` first, then others

### Domain Skills

**`structural-engineering.md`**
- Load paths, beam sizing, deflection checks
- Timber, steel, concrete connection details
- Eurocode 5 (timber), Eurocode 3 (steel), Eurocode 2 (concrete)
- Cross-references: TEK17 §7-2, structural-analysis-mcp tool

**`building-code-tek17.md`**
- Complete TEK17 regulation reference (current through 01.07.2026 amendments)
- Amendment history table (2023–2026)
- PBL §20-5 (exemption pathways)
- SAK10 søknadsfritak (solar panels, insulation, EV charging)
- Cross-references: Byantikvaren, NVE, municipalities

**`sintef-byggforsk.md`**
- SINTEF Byggforsk standards + guidance
- Moisture management, insulation specs, air tightness
- Material selection (wood, concrete, brick properties)
- Cross-references: TEK17 §15, manufacturer datasheets

**`historic-preservation.md`**
- SEFRAK database (registration grades A/B/C)
- Kulturminneloven §15 (fredete buildings)
- Byantikvaren approval process (forhåndskonferanse)
- Heritage + modern upgrade conflicts (exemptions, compromises)
- Cross-references: TEK17 §15-1(5), PBL §20-5

**`classical-architecture.md`**
- Vitruvian principles (Firmitas, Utilitas, Venustas)
- Proportional systems (golden ratio, module-based design)
- Ornamental details, composition, aesthetics
- Cross-references: Architectural drawing reading, heritage preservation

**`construction-execution.md`**
- Site sequencing, demolition protocols
- Trade coordination, lead times
- Health & safety on site (AFS regulations)
- Budget + schedule estimation
- Cross-references: Structural assessment, building code, project management

**`architectural-drawing-reading.md`**
- Interpreting plantegninger (floor plans), snitt (sections), fasader (elevations)
- Construction details (detaljer), dimension chains
- Symbol conventions (Norwegian standard)
- Cross-references: Structural engineering, construction execution

---

## Using Output Templates

Bob can format responses into professional deliverables using templates:

### **structural-assessment-memo.md**
**When to use:** After site visit or existing building inspection
**Contains:** 
- Building summary (age, materials, condition)
- Findings (structural, material, safety concerns)
- Recommendations (repairs, upgrades, further investigation)
- Risk assessment + escalations
**Output:** Professional memo for contractor/owner

### **pre-application-meeting-notes.md**
**When to use:** After forhåndskonferanse with municipality / Byantikvaren
**Contains:**
- Attendees, date, project scope
- Officer feedback (concerns, requirements, approval path)
- Agreed approach (design direction, exemptions, conditions)
- Next steps + action items
**Output:** Shared record between parties

### **compliance-gap-analysis.md**
**When to use:** Auditing existing building against TEK17 / local plan
**Contains:**
- Standard / regulation section
- Current building performance (measured)
- Required level (code requirement)
- Gap size (numeric or qualitative)
- Remediation cost/timeline estimate
- Priority (critical / high / medium / low)
**Output:** Roadmap for upgrades

### **[TODO] post-approval-checklist.md**
**When to use:** After søknad is approved, before construction starts
**Contains:**
- Permit conditions (special requirements from municipality)
- Key inspections (foundation, structural, fire, final)
- Sign-off requirements (engineer, foreman, building inspector)
**Output:** Construction phase checklist

### **[TODO] construction-sequence.md**
**When to use:** Phased demolition / renovation projects
**Contains:**
- Phase-by-phase timeline
- Trade dependencies (what must finish before next trade starts)
- Lead times (material delivery, permits, inspections)
- Risk points (utilities, temporary support, weather)
**Output:** Contractor's execution plan

### **[TODO] heritage-assessment.md**
**When to use:** Before any intervention on SEFRAK / antikvariske buildings
**Contains:**
- Heritage significance (cultural, architectural, material)
- Elements at risk (if proposed work proceeds)
- Alternatives (mitigation options)
- Byantikvaren impact assessment
**Output:** Heritage impact statement for forhåndskonferanse

---

## MCP Integration (Optional)

Bob can connect to external Model Context Protocol (MCP) servers for live data + specialized tools.

### **Configured MCP Servers**

**Status: Available**
- **structural-analysis-mcp** (Elandu)
  - Tools: Beam deflection, section properties, concrete sizing
  - When to invoke: Span > 4 m, complex load case
  - See `mcp/tools/structural-analysis.md`

**Status: Requires User Setup**
- **Catenda Hub** (IFC model queries, BCF issues, quantity takeoffs)
  - Requires: Catenda account + project URL
  - See `project.md` for configuration
  - Not yet tested with Bob

**Status: Specification Only (TODO)**
- **norwegian-building-data-mcp** (SEFRAK, NVE, NGU, regulatory APIs)
  - Tools: Hazard lookup, heritage registry, zoning, ground conditions
  - Would enable: Real-time compliance checking
  - See `mcp/tools/norwegian-building-data.md` for spec

### **Enabling MCP Connections**

1. Edit `mcp/mcp-config.json` with server details (endpoints, auth)
2. In `project.md`, add `mcp_servers: [...]` section
3. On session load, Bob reads config and registers tool availability
4. Bob mentions available tools in responses (e.g., "I can check NVE hazards for you if you give me coordinates")

---

## Language & Terminology

Bob operates bilingually (Norwegian ↔ English):

- **Responds in the language user writes in** (Norwegian queries → Norwegian responses)
- **Uses correct technical terminology:**
  - Norwegian: søknad, forhåndskonferanse, ansvarlig prosjekterende, wienerberks, takskifte, kvikkleire
  - English: permit application, pre-application meeting, licensed PE, brick, roof replacement, quick clay
- **Regulatory terms** (TEK17, PBL, SEFRAK) used without translation (standard in both languages)

---

## When NOT to Use Bob

Bob is **not designed for:**
- ✗ Automated permitting (Bob flags requirements; humans file permits)
- ✗ Replacing structural engineer sign-off (Bob can size a beam; engineer must verify + sign)
- ✗ Legal advice (Bob explains regulatory requirements; lawyers handle disputes)
- ✗ Financial advice (Bob estimates remediation scope; accountants handle costs/financing)
- ✗ Instant answers to complex problems (Bob provides framework; detailed work requires time)

---

## Configuration & Project Setup

### Default Project Context (`project.md`)

Create a `project.md` file at project root. Bob reads this at session start:

```yaml
---
project_name: "Renovation Project — [Address]"
location:
  address: "[Street address]"
  municipality: "[Kommune]"
  latitude: [52.XX]
  longitude: [12.XX]
  county: "Trøndelag / Viken / etc."

building:
  year_constructed: [YYYY]
  sefrak_status: "Listed / Not listed / Unknown"
  sefrak_grade: "[A/B/C if listed]"
  building_type: "[Residential / Commercial / Heritage / Other]"
  area_bra: "[m²]"

site:
  soil_type: "[Clay / Sand / Rock / Unknown]"
  slope: "[percentage or description]"
  hazards: "[Flood / Avalanche / Landslide / Asbestos / None known]"

permit_status: "[Under review / Approved / Not started / Exempt]"
permit_number: "[if applicable]"

project_scope: "[Description of work: renovation, structural mod, energy upgrade, etc.]"

contacts:
  owner: "[Name, phone]"
  architect: "[Name, firm, contact]"
  engineer: "[Name, firm, contact]"
  contractor: "[Name, firm, contact]"

notes: "[Any additional context for Bob (prior issues, constraints, decisions)]"
---
```

On load, Bob will confirm: *"Loaded: [Project Name] at [Address], [Municipality]. Heritage status: [X]. Permit status: [X]. Ready."*

---

## Troubleshooting & Feedback

### "Bob gives generic advice, not specific to my project"
→ Create/load `project.md`. Bob uses project context to tailor responses.

### "Bob cites a regulation I don't think is correct"
→ Report the issue. TEK17 amendments are frequent (last checked 2026-07-26). Verification welcome.

### "Bob doesn't know about [specific rule / regional variation]"
→ Bob has knowledge through 2026-07-26. Regional variations exist; Bob typically flags these ("Check with [municipality]").

### "I need a feature Bob doesn't have"
→ See ROADMAP.md. Consider filing an enhancement request.

---

## Roadmap (Next Priorities)

**Completed (v1.3):**
- ✅ ReAct reasoning protocol with explicit uncertainty
- ✅ Escalation matrix (8 high-risk condition flags)
- ✅ Bilingual support (Norwegian ↔ English)
- ✅ TEK17 amendments current through 2026-07-26
- ✅ structural-analysis-mcp integration (specification)
- ✅ Output templates (3 of 6 complete)

**In Progress (v1.4, next week):**
- [ ] Complete output templates (3 more: post-approval, construction-sequence, heritage-assessment)
- [ ] Implement Norwegian Building Data MCP (Tools 1–3: SEFRAK, NVE, NGU)
- [ ] Add worked examples to building-code-tek17.md

**Planned (v1.5, later):**
- [ ] Catenda Hub integration (IFC model queries)
- [ ] Structural skill enhancement (connection detail tables, section database)
- [ ] Norwegian Building Data MCP (Tools 4–7: regulatory plans, radon, standards)
- [ ] Performance dashboard (usage analytics, escalation tracking)

---

## Attribution & Sources

**Regulatory authority:**
- TEK17 (Teknisk forskrift 2017-06-01-840)
- PBL (Planleggings- og bygningsloven)
- Eurocode standards (EN 1990–1999, national annexes)
- SINTEF Byggforsk guidelines
- Kulturminneloven (Heritage Protection Act)
- NVE flood/hazard mapping
- NGU geology + ground conditions

**Data last verified:** 2026-07-26

**Disclaimer:** Bob the Bygger provides professional-level guidance but does not replace licensed engineers, building inspectors, or heritage consultants. For permit-required work, always engage qualified professionals.

---

## Support & Questions

For issues, feature requests, or documentation improvements:
- Check the built-in help (ask Bob for clarification)
- Review ARCHITECTURE.md for system design questions
- Consult regulatory sources directly (lovdata.no, dibk.no, nve.no)

---

*Bob the Bygger — Making Norwegian buildings stand, comply, and endure.*
