# Documentation Style Guide: Phase 0

**Purpose**: Establish consistent formatting and structural standards for all Phase 0 deliverables.

## Markdown Standards

### File Naming
- Use `UPPERCASE_WITH_UNDERSCORES.md` for primary deliverables (e.g., `ICP.md`, `USE_CASES.md`)
- Use `lowercase-with-hyphens.md` for supporting documents
- All files must have `.md` extension

### Document Structure
Every deliverable document MUST include:
1. **Title**: `# Document Title`
2. **Purpose**: Brief description of the document's role
3. **Sections**: Logical groupings using `##` and `###` headers
4. **Tables**: For structured data (criteria, metrics, definitions)
5. **Lists**: For enumerated items (requirements, scenarios)

### Formatting Rules
- **Bold**: For key terms on first use, and for emphasis on critical criteria
- **Italic**: For document references and file paths
- **Code blocks**: For structured data examples or Gherkin scenarios
- **Tables**: For comparison data, metrics, and structured definitions
- **Links**: Use relative paths for intra-project references (e.g., `./ICP.md`)

### Content Guidelines
- **Concise**: Avoid unnecessary verbosity; prefer tables over paragraphs where possible
- **Testable**: All requirements and criteria must be verifiable
- **Consistent**: Use the same terminology across all documents (see [GLOSSARY.md](./GLOSSARY.md))
- **Version-aware**: Include creation date and status at the top of each document

### Header Hierarchy
```
# Level 1: Document Title
## Level 2: Major Sections
### Level 3: Subsections
#### Level 4: Detailed breakdowns (use sparingly)
```

### Checklist Format
Use GitHub-flavored markdown task lists for validation:
```markdown
- [x] Completed item
- [ ] Pending item
```

### Table Format
Align columns and include headers:
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value    | Value    | Value    |
```

## Cross-Referencing
- Link to other Phase 0 documents using relative paths: `[Document Name](./FILENAME.md)`
- Link to source specifications using relative paths from project root: `[Spec](../specs/001-product-spec-phase0/spec.md)`
- Use anchor links for sections within the same document: `[Section](#section-name)`

## Review Process
1. Draft created following this style guide
2. Self-review against checklist
3. Peer review for consistency and completeness
4. Final approval and status update to "Complete"
