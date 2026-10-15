"""Regenerate README.md from resources.json. Usage: python build_readme.py"""
import json
from collections import OrderedDict

ACCESS = {"open": "", "reg": " *(free registration)*", "ctrl": " *(approval or controlled access)*"}

with open("resources.json", encoding="utf-8") as f:
    items = json.load(f)

groups = OrderedDict()
for r in items:
    groups.setdefault(r["category"], []).append(r)

def anchor(s):
    return "".join(c for c in s.lower().replace(" ", "-") if c.isalnum() or c == "-")

extra = ["Evaluating Sources", "Inclusion Criteria", "Contributing", "License"]
out = ["# Awesome Women's Health Resources [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n",
 "Openly accessible, reputable resources that support the biology and health of women: clinical guidance, datasets, "
 "open-access research, and open-source software and apps. This is not a femtech directory. "
 "Everything here is free to read or has a free access tier, and is linked to an institutional, peer-reviewed or "
 "open-source origin.\n",
 "**Interactive view:** see `index.html` (deploy with GitHub Pages).\n",
 "> This list is for education and research. It is not medical advice. For personal health concerns, talk to a qualified clinician.\n",
 "## Contents\n"]
out += [f"- [{c}](#{anchor(c)})" for c in list(groups) + extra]
out.append("\n---\n")
for cat, rs in groups.items():
    out.append(f"## {cat}\n")
    for r in rs:
        lang = f" ({r['language']})" if r.get("language") else ""
        out.append(f"- [{r['name']}]({r['url']}){lang} - {r['description']}{ACCESS[r['access']]}")
    out.append("\n---\n")

out.append("""## Evaluating Sources

Fake or low-quality medical sites are common. Before adding or relying on a resource, check that it:

- is run by an identifiable institution (government, university, hospital, professional society, established nonprofit) with a named editorial or review process;
- cites primary literature or guidelines and shows when the page was last reviewed;
- does not sell supplements, "detox" kits or miracle cures, or promise to cure chronic conditions;
- does not push alarmist or "secret the doctors hide" claims, and avoids paywalled "diagnosis" quizzes that collect personal data;
- states how health data is handled, if it is an app (prefer offline or self-hosted, open-source code).

For research use, prefer primary sources (guidelines, systematic reviews, registered datasets) over summaries.

---

## Inclusion Criteria

1. Directly relevant to women's biology or health, including sex-specific or sex-disaggregated data.
2. Freely accessible. Free-registration or approval-gated data is allowed and labelled.
3. From a reputable institution, peer-reviewed venue, or open-source project with a stated licence and recent activity.
4. No commercial femtech products, affiliate links or ad-driven content sites.
5. Community-curated lists are included only when they link to primary sources, and are flagged.

GitHub projects were checked for licence and recent activity when added. Research code is not a clinical tool.

---

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

---

## License

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under [Creative Commons Attribution 4.0 International](LICENSE). Linked resources keep their own licences.

**Last reviewed:** October 2026
""")
open("README.md", "w", encoding="utf-8").write("\n".join(out))
print(len(items), "resources,", len(groups), "categories")
