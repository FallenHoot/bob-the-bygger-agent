# Contributing to Bob the Bygger

Thanks for your interest in contributing! This document outlines how to work with this project.

## Branch Strategy (GitFlow)

- **`main`** — Stable releases only. Tagged with version (e.g., `v1.3`)
- **`develop`** — Active development. Integration branch for features and fixes
- **`feature/*`** — Feature branches: `feature/bilingual-polish`, `feature/add-foundation-skill`, etc.
- **`bugfix/*`** — Bug fixes: `bugfix/routing-language-detection`, etc.
- **`release/*`** — Release preparation: `release/1.4`, etc.

## Workflow

### Adding a Feature
```bash
# Branch off develop
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

# Make changes
# Commit frequently with clear messages
git add .
git commit -m "feat: add [specific capability]"

# Push and create PR against develop
git push origin feature/your-feature-name
# Create Pull Request on GitHub: feature branch → develop
```

### Bugfix
```bash
git checkout develop
git checkout -b bugfix/describe-bug
# Fix + commit
git push origin bugfix/describe-bug
# Create Pull Request: bugfix branch → develop
```

### Release (Maintainers Only)
```bash
git checkout -b release/1.4 develop
# Update version in README.md, system_prompt.md, etc.
git commit -m "chore: bump version to 1.4"
git push origin release/1.4
# Create PR: release/1.4 → main
# After merge to main, tag: git tag v1.4
# Merge release branch back to develop
```

## Commit Message Convention

Follow conventional commits for clarity:

```
feat:     New skill, feature, or capability
fix:      Bug fix in existing skill
docs:     Documentation updates (README, guides)
refactor: Restructure without changing behavior
chore:    Version bumps, dependency updates
test:     Test scenarios, validation examples
```

Examples:
```
feat: add drawing-investigation-protocol skill
fix: correct language detection for code-switching
docs: add bilingual glossary to technical-education-support
refactor: simplify routing classification rules
chore: bump version to 1.4
```

## Code Quality Guidelines

### Skills
- **Local authoring contract** — Follow [skills/README.md](skills/README.md) for
   required fields, flat frontmatter, workflow structure and validation limits.
- **Clear structure** — Purpose, content sections, examples, links
- **Norway-first evidence** — Distinguish law, standards/NA editions, contractual
   requirements and guidance. Verify applicability and sources; do not treat a
   skill table, product preset or prior AI output as design approval.
- **Bilingual support** — Include English equivalents, resource links in both languages
- **Trust boundaries** — Follow [system_prompt.md](system_prompt.md); high/critical
   skills need a Trust Boundary section. Use synthetic examples, not private data.

### System Prompt & Routing
- **Loading order** — System prompt, shared constraints, startup once, then scoped
   routing. Extend existing skills where practical; avoid duplicate orchestration.
- **Checkable answers** — Concise conclusions, evidence, assumptions, formulas
   when useful and next actions; do not demand private internal deliberation.
- **Review triggers** — Use task-specific evidence and appropriate Norwegian
   reviewers, not generic foreign licensing or mandatory-stamp thresholds.
- **Scope and language** — Match the user language and selected mode/project.
- **Privacy and actions** — Preserve unrelated local edits. Never stage ignored
   project data. External writes, moves and destructive actions require explicit
   authorization; commits and publication are separate from drafting changes.

### Documentation
- **README.md** — Updated with new features
- **Bilingual examples** — For international clarity
- **Resource links** — Norwegian and English sources
- **Templates** — Output templates in `/templates/` for users

## Testing / Validation

Use [docs/development.md](docs/development.md) for the shared environment and
commands, and [docs/evaluations/README.md](docs/evaluations/README.md) for live-host
evaluation cases. Local test success is not a remotely executed CI result.

Before submitting PR:

1. **Static contracts** — Run [tests/Test-AgentContracts.ps1](tests/Test-AgentContracts.ps1)
   without a project argument for repository-only checks.
2. **Skill lint** — Run [skills/validate_skills.py](skills/validate_skills.py) after
   skill edits; report warnings as review needs rather than suppressing them.
3. **Changed code** — Run relevant tests, including the local beam suite when
   changing that calculator. Record the actual command/result and test scope.
4. **Behavior** — Exercise applicable synthetic success, missing-evidence,
   revision-conflict and language cases. Record expected and observed results
   separately; unrun examples and source assertions are not behavioral tests.
5. **Sources and links** — Verify changed references and technical applicability.
   Clean static checks do not establish engineering/legal accuracy or approval.

## Reporting Issues

When reporting a bug or suggesting a feature:

1. **Check existing issues** — Avoid duplicates
2. **Be specific** — Include:
   - What you tried
   - What you expected
   - What actually happened
   - Reproduction steps (if applicable)
3. **Bilingual context** — If issue is language-specific, note whether Norwegian or English

## License

By contributing, you agree your work is licensed under MIT (see LICENSE file).

---

Thank you for improving Bob the Bygger! Questions? Open an issue or discussion on GitHub.
