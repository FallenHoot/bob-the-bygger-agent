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
- **YAML frontmatter required** — Every skill must have `name`, `description`, `triggers`, `load_with`, `safety_level`
- **Clear structure** — Purpose, content sections, examples, links
- **Norwegian-first expertise** — Standards (TEK17, NEK 400, VS 6050) are authoritative
- **Bilingual support** — Include English equivalents, resource links in both languages
- **Safety disclaimers** — If skill touches regulatory or structural topics, include disclaimer note

### System Prompt & Routing
- **ReAct protocol** — Explicit reasoning before conclusions
- **Escalation checks** — Flag high-risk decisions (WET_STAMP_REQUIRED, etc.)
- **Language detection** — Route to correct language response
- **Safety gates** — Data-first for structural; education-first for technical

### Documentation
- **README.md** — Updated with new features
- **Bilingual examples** — For international clarity
- **Resource links** — Norwegian and English sources
- **Templates** — Output templates in `/templates/` for users

## Testing / Validation

Before submitting PR:

1. **Routing logic** — Test that your skill is correctly triggered by keywords
2. **Language detection** — Verify both Norwegian and English queries route correctly
3. **Links** — All resource links are active and point to intended content
4. **Disclaimers** — High-risk topics (structural, regulatory) include appropriate warnings
5. **Examples** — Provide realistic scenario examples in the skill

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
