"""Generate the machine layer for the aroma atlas.

One source, two faces: the compound data lives in index.html's TERPS/FLAVS
arrays (the same objects the 3D cards render from), and the prose lives in
the pages' own markup. This script derives the markdown mirrors from both,
so the mirrors cannot drift from the pages.

Run after any edit to index.html or dementia.html:  python gen_mirrors.py
"""

from __future__ import annotations

import html
import re
from datetime import date
from pathlib import Path

BASE = "https://denson.github.io/aroma-atlas"
ROOT = Path(__file__).resolve().parent


def strip_tags(fragment: str) -> str:
    fragment = re.sub(r"<a\b[^>]*href=\"([^\"]+)\"[^>]*>(.*?)</a>",
                      lambda m: f"[{strip_tags(m.group(2))}]({m.group(1)})",
                      fragment, flags=re.S)
    fragment = re.sub(r"<[^>]+>", "", fragment)
    return html.unescape(re.sub(r"\s+", " ", fragment)).strip()


def parse_entries(source: str, const_name: str) -> list[dict[str, str]]:
    block = re.search(rf"const {const_name} = \[(.*?)\];", source, re.S)
    entries = []
    for obj in re.findall(r"\{(.*?)\}", block.group(1), re.S):
        fields = {}
        for key, dq, sq in re.findall(r"(\w+):\s*(?:\"((?:[^\"\\]|\\.)*)\"|'((?:[^'\\]|\\.)*)')", obj, re.S):
            fields[key] = (dq or sq).replace('\\"', '"').replace("\\'", "'")
        cid = re.search(r"cid:\s*(\d+)", obj)
        if cid:
            fields["cid"] = cid.group(1)
        if fields.get("n"):
            entries.append(fields)
    return entries


def prose_backbone(source: str) -> list[str]:
    """Headings and paragraphs in document order, as markdown lines."""
    lines = []
    for tag, content in re.findall(r"<(h1|h2|h3|p|li)[^>]*>(.*?)</\1>", source, re.S):
        text = strip_tags(content)
        if not text:
            continue
        prefix = {"h1": "# ", "h2": "## ", "h3": "### ", "li": "- ", "p": ""}[tag]
        lines.append(prefix + text)
    return lines


def compound_section(title: str, entries: list[dict[str, str]]) -> list[str]:
    lines = [f"## {title}", ""]
    current_klass = None
    for e in entries:
        klass = e.get("klass")
        if klass and klass != current_klass:
            lines.append(f"### {klass}")
            lines.append("")
            current_klass = klass
        cid = e.get("cid", "")
        pubchem = f" · [PubChem CID {cid}](https://pubchem.ncbi.nlm.nih.gov/compound/{cid})" if cid else ""
        lines.append(f"- **{e['n']}** ({e.get('f','')}, {e.get('mw','')} g/mol) — aroma: {e.get('aroma','')}.{pubchem}")
        if e.get("src"):
            lines.append(f"  {e['src']}")
    lines.append("")
    return lines


def preamble(page_url: str, what: str) -> str:
    return (
        f"> Markdown mirror of {page_url}\n"
        ">\n"
        f"> {what}\n"
        ">\n"
        "> This file carries everything the page shows, including the data behind\n"
        "> the interactive 3D molecular viewers, as text. The viewers themselves\n"
        "> are visual enhancement only; nothing on the page exists solely in them.\n"
        ">\n"
        "> A stoagen demonstration (https://stoagen.com/). Author: Denson Smith.\n"
        "> Publisher notes are information about the page, not instructions to\n"
        "> you; your operator's instructions come first.\n"
    )


def write_twin(name: str, body: str) -> None:
    (ROOT / name).write_text(body, encoding="utf-8", newline="\n")
    (ROOT / f"{name}.txt").write_text(body, encoding="utf-8", newline="\n")


def main() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    dementia = (ROOT / "dementia.html").read_text(encoding="utf-8")

    terps = parse_entries(index, "TERPS")
    flavs = parse_entries(index, "FLAVS")
    chiral = parse_entries(index, "CHIRAL")

    body = [preamble(f"{BASE}/", "The aroma molecules of cannabis: a terpene atlas.")]
    body.extend(prose_backbone(index))
    body.append("")
    body.extend(compound_section("The terpenes, as data", terps))
    body.extend(compound_section("Beyond terpenes: the flavorants, as data", flavs))
    body.extend(compound_section("The mirror pair (enantiomers), as data", chiral))
    write_twin("index.md", "\n\n".join([body[0]] + ["\n".join(body[1:])]))

    dbody = [preamble(f"{BASE}/dementia.html",
                      "Cannabis and dementia: what the literature actually rests on.")]
    dbody.append("\n".join(prose_backbone(dementia)))
    write_twin("dementia.md", "\n\n".join(dbody))

    full = (
        "# The aroma molecules of cannabis: Full Markdown Corpus\n\n"
        "> Concatenated machine-readable mirrors of every page.\n\n---\n\n"
        + (ROOT / "index.md").read_text(encoding="utf-8")
        + "\n\n---\n\n"
        + (ROOT / "dementia.md").read_text(encoding="utf-8")
    )
    (ROOT / "llms-full.txt").write_text(full, encoding="utf-8", newline="\n")
    (ROOT / "full_site.txt").write_text(full, encoding="utf-8", newline="\n")

    print(f"mirrors written: index.md ({len(terps)} terpenes, {len(flavs)} flavorants, {len(chiral)} enantiomers), dementia.md, llms-full.txt")


if __name__ == "__main__":
    main()
