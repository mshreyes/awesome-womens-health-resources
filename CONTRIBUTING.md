# Contributing

Thanks for helping improve this list. Please keep it reputable, open and useful.

## What to add

A resource qualifies if it meets all of the [inclusion criteria](README.md#inclusion-criteria): relevant to women's biology or health, freely accessible (free-registration data is fine and labelled), from a reputable institution, peer-reviewed venue or open-source project, and not a commercial product or ad-driven site.

## Vetting checklist (required in your pull request)

- [ ] The publisher is identifiable and institutional (government, university, hospital, society, established nonprofit).
- [ ] Content cites evidence and shows a review or update date.
- [ ] No supplement sales, miracle-cure claims or data-harvesting quizzes.
- [ ] For GitHub or F-Droid projects: an open-source licence file, activity within the last 24 months (or a clear note if older), and no known undisclosed tracking.
- [ ] The link works and goes to the specific resource, not a generic homepage, unless the homepage is the resource.
- [ ] Not already in the list.

## How to add an entry

Edit **`resources.json`** only, then regenerate the README:

```bash
python build_readme.py
```

Each entry looks like this:

```json
{"name": "Resource name", "url": "https://...", "category": "Existing category name",
 "type": "education|guideline|data|tool|software|app|journal",
 "access": "open|reg|ctrl", "description": "One factual sentence. No marketing language.",
 "language": "R"}
```

`access`: `open` = free, no sign-up; `reg` = free registration; `ctrl` = approval or controlled access. `language` is optional (use `R` or `Python` for code resources).

## Style

- One sentence, factual, ending with a full stop.
- Mention licence, maintenance caveats and access limits where relevant.
- Keep the alphabetical or logical order within a category.
- Commit message: `Add <resource name>`.

## Reporting problems

Open an issue for broken links, outdated resources or concerns about reliability. A link check runs weekly via GitHub Actions.

By contributing, you agree your contribution is licensed under [CC BY 4.0](LICENSE).
