"""Snapshot the PubChem SDF structures the atlas displays.

The pages serve these local copies (sdf/<cid>.sdf) so a visitor never
depends on PubChem being up or unthrottled; PubChem remains the
fallback in the page for a missing file. Molecular structures do not
change, but run this occasionally to pick up any PubChem record
corrections, then commit the diff (usually none).

Polite by design: one request per second, well under PubChem's
5-requests-per-second limit. Prefers the 3D conformer record and falls
back to the 2D record where PubChem has no 3D.
"""

import time
import urllib.request
from pathlib import Path

# Every CID shown on index.html (terpenes + flavorants). Keep in sync
# with the TERPS and FLAVS arrays there.
CIDS = [31253, 22311, 6654, 14896, 6549, 5281515, 5281520, 11463,
        6434062, 5284507, 146586, 521348, 31265, 8635, 6736, 379,
        439570, 16724]  # carvone enantiomers (CHIRAL array)

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/SDF?record_type={rt}"
OUT = Path(__file__).resolve().parent / "sdf"


def fetch(cid: int) -> str:
    for rt in ("3d", "2d"):
        req = urllib.request.Request(
            BASE.format(cid=cid, rt=rt),
            headers={"User-Agent": "aroma-atlas-sdf-refresh/1.0"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                text = r.read().decode("utf-8")
            if "$$$$" in text:
                return text
        except Exception as exc:  # noqa: BLE001 - try the next record type
            print(f"  {cid} {rt}: {exc}")
    raise RuntimeError(f"no usable SDF for CID {cid}")


def normalized(text: str) -> str:
    """SDF content minus the volatile parts of PubChem's export.

    Line 2 is an OEChem stamp carrying the export timestamp, so a raw
    comparison reports every re-download as changed. Mask it (and line
    endings) so CHANGED means the structure record actually changed.
    """
    lines = text.replace("\r\n", "\n").split("\n")
    if len(lines) > 1 and "OEChem" in lines[1]:
        lines[1] = "  -OEChem-"
    return "\n".join(lines)


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for cid in CIDS:
        text = fetch(cid)
        path = OUT / f"{cid}.sdf"
        old = path.read_text(encoding="utf-8") if path.is_file() else None
        if old is not None and normalized(old) == normalized(text):
            print(f"{path.name}: unchanged")
        else:
            path.write_text(text, encoding="utf-8")
            print(f"{path.name}: {len(text)} bytes" + (" (CHANGED)" if old is not None else " (new)"))
        time.sleep(1)
    print(f"done: {len(CIDS)} structures in {OUT}")


if __name__ == "__main__":
    main()
