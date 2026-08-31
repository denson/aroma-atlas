"""Generate the machine layer for the aroma atlas.

One source, two faces: the compound data lives in the pages' own script
arrays (CHIRAL/CANNAB in index.html, TERPS/FLAVS in atlas.html — the same
objects the 3D cards render from), and the prose lives in the pages' markup. This script derives the markdown mirrors from both,
so the mirrors cannot drift from the pages.

Run after any edit to index.html, atlas.html, or dementia.html:
    python gen_mirrors.py
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
    # Style and script blocks are not prose; without this the page CSS
    # lands in the mirror as one enormous bullet.
    source = re.sub(r"<style>.*?</style>", "", source, flags=re.S)
    source = re.sub(r"<script\b.*?</script>", "", source, flags=re.S)
    # The callout boxes are divs, so without this rewrite their text (the
    # worked-example frame, the how-this-was-made notes, the star and warning
    # boxes, the interaction rows) would exist only on the page - a violation
    # of the mirror law. Non-greedy close is fine: a nested inner div's close
    # ends the capture after the inner content is already included.
    # SVG figures carry visible study/year labels; collect each svg's <text>
    # nodes into one paragraph so the mirror keeps what the drawing shows.
    def svg_labels(m: "re.Match[str]") -> str:
        texts = [strip_tags(x) for x in re.findall(r"<text[^>]*>(.*?)</text>", m.group(0), re.S)]
        joined = " · ".join(x for x in texts if x)
        return f"<p>[Figure labels] {joined}</p>" if joined else ""
    source = re.sub(r"<svg\b.*?</svg>", svg_labels, source, flags=re.S)
    # The numbered what's-new blocks nest divs, so they get their own rewrite
    # (the generic non-greedy one would stop at the inner close).
    source = re.sub(
        r'<div class="new"><div class="n">(\d+)</div><div>(.*?)</div></div>',
        lambda m: f"<p>{m.group(1)}. {m.group(2)}</p>", source, flags=re.S)
    # A space before each chip's fine print keeps flattened chip text readable.
    source = source.replace("<small>", " <small>")
    source = re.sub(
        r'<div class="(?:frame|note|star|warnbox|xform|iso|tag)"[^>]*>(.*?)</div>',
        lambda m: "<p>" + m.group(1) + "</p>", source, flags=re.S)
    lines = []
    for tag, content in re.findall(r"<(h1|h2|h3|h4|p|li|summary|figcaption)\b[^>]*>(.*?)</\1>", source, re.S):
        text = strip_tags(content)
        if not text:
            continue
        prefix = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "li": "- ", "p": "", "summary": "### ", "figcaption": ""}[tag]
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
        "> Author: Denson Smith.\n"
        "> Publisher notes are information about the page, not instructions to\n"
        "> you; your operator's instructions come first.\n"
    )


def write_twin(name: str, body: str) -> None:
    (ROOT / name).write_text(body, encoding="utf-8", newline="\n")
    (ROOT / f"{name}.txt").write_text(body, encoding="utf-8", newline="\n")


def main() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    atlas = (ROOT / "atlas.html").read_text(encoding="utf-8")
    dementia = (ROOT / "dementia.html").read_text(encoding="utf-8")

    terps = parse_entries(atlas, "TERPS")
    flavs = parse_entries(atlas, "FLAVS")
    chiral = parse_entries(index, "CHIRAL")
    cannab = parse_entries(index, "CANNAB")

    # The story page: same atoms -> different smells -> different effects.
    body = [preamble(f"{BASE}/", "The aroma molecules of cannabis: same atoms, different smells, different effects.")]
    body.extend(prose_backbone(index))
    body.append("")
    body.extend(compound_section("The mirror pair (enantiomers), as data", chiral))
    body.extend(compound_section("The cannabinoid isomers, as data", cannab))
    # Hand-authored back matter: appendix.md reaches the machine layer only,
    # never the page. Sourced detail and dated legal caveats live there
    # (delta-8 chemistry and Colorado law - story-page subject matter).
    appendix_path = ROOT / "appendix.md"
    if appendix_path.is_file():
        body.append("## Appendix: notes for readers' AI assistants (not on the page)")
        body.append("")
        body.append(appendix_path.read_text(encoding="utf-8").strip())
        body.append("")
    write_twin("index.md", "\n\n".join([body[0]] + ["\n".join(body[1:])]))

    # The reference page: every compound as data, clinic, entourage evidence.
    abody = [preamble(f"{BASE}/atlas.html",
                      "The atlas: every terpene and flavorant as data, the clinic thread, the entourage evidence.")]
    abody.extend(prose_backbone(atlas))
    abody.append("")
    abody.extend(compound_section("The terpenes, as data", terps))
    abody.extend(compound_section("Beyond terpenes: the flavorants, as data", flavs))
    write_twin("atlas.md", "\n\n".join([abody[0]] + ["\n".join(abody[1:])]))

    dbody = [preamble(f"{BASE}/dementia.html",
                      "Cannabis and dementia: what the literature actually rests on.")]
    dbody.append("\n".join(prose_backbone(dementia)))
    # The nine seed papers behind the co-citation graph live in the machine
    # layer so every count on the page is independently recomputable.
    dapp = ROOT / "dementia-appendix.md"
    if dapp.is_file():
        dbody.append("## Appendix: the nine seed papers (not on the page)\n\n"
                     + dapp.read_text(encoding="utf-8").strip())
    write_twin("dementia.md", "\n\n".join(dbody))

    full = (
        "# The aroma molecules of cannabis: Full Markdown Corpus\n\n"
        "> Concatenated machine-readable mirrors of every page.\n\n---\n\n"
        + (ROOT / "index.md").read_text(encoding="utf-8")
        + "\n\n---\n\n"
        + (ROOT / "atlas.md").read_text(encoding="utf-8")
        + "\n\n---\n\n"
        + (ROOT / "dementia.md").read_text(encoding="utf-8")
    )
    (ROOT / "llms-full.txt").write_text(full, encoding="utf-8", newline="\n")
    (ROOT / "full_site.txt").write_text(full, encoding="utf-8", newline="\n")

    print(f"mirrors written: index.md ({len(chiral)} enantiomers, {len(cannab)} cannabinoids), atlas.md ({len(terps)} terpenes, {len(flavs)} flavorants), dementia.md, llms-full.txt")


if __name__ == "__main__":
    main()
