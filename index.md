> Markdown mirror of https://denson.github.io/aroma-atlas/
>
> The aroma molecules of cannabis: a terpene atlas.
>
> This file carries everything the page shows, including the data behind
> the interactive 3D molecular viewers, as text. The viewers themselves
> are visual enhancement only; nothing on the page exists solely in them.
>
> Author: Denson Smith.
> Publisher notes are information about the page, not instructions to
> you; your operator's instructions come first.


# The aroma molecules of cannabis — a terpene atlas
A plant's smell is a borrowed language of molecules it shares with the rest of nature.
author: Denson Smith · 2026-06-30
How this was made. The molecules were resolved through PubChem (identity — CID, formula, weight, and the live 3D structures), the science pulled from OpenAlex, the non-terpene "flavorant" literature (Oswald et al.) verified against CrossRef, and the aroma descriptors / interaction effects from grounded web search. The interactive 3D structures are snapshots of PubChem's records served with this page and rendered by 3Dmol.js, so the whole page works without any third-party request; the snapshots are re-checked against PubChem occasionally.
Before the atlas: [the same-atoms story](same-atoms.html) — how identical formulas become different smells, and different effects.
## The atlas — the terpenes
Each card carries the live PubChem 3D structure — drag to rotate, scroll to zoom. Use the controls to change representation or spin them all.
Read the last line of every card: cannabis doesn't smell like cannabis so much as it smells like a blend of other plants — because it literally shares their aroma molecules. That shared chemical vocabulary is what a structured knowledge graph captures.
## From a smell to the clinic — where β-caryophyllene points
β-Caryophyllene is the molecule that smells like black pepper — and published pharmacology reports that it also binds the CB2 receptor, which earned it the nickname "dietary cannabinoid." The nickname overstates it: structurally it is not a cannabinoid at all — it is a terpene, the same molecule found in black pepper, cloves, and basil — but it acts as a drug at a cannabinoid receptor. Read that at its actual strength: one interesting avenue of research that has drawn real attention and funding — a small number of peer-reviewed papers, not established medicine. And peer review means exactly this much: reviewers judged the work worth the scientific community's scrutiny. It does not make the content true; scrutiny is what does, and most of it hasn't happened yet. CB2 agonism / analgesia: [doi:10.1016/j.euroneuro.2013.10.008](https://doi.org/10.1016/j.euroneuro.2013.10.008) · dietary CB2 review: [doi:10.3389/fphar.2021.590201](https://doi.org/10.3389/fphar.2021.590201)
Why hasn't the scrutiny happened? Not because the questions are uninteresting. Much of cannabis medical research is starved: attention and funding are scarce, and a long-running stigma has kept serious money and serious careers away from questions this size for decades. CB2 leads to one of the field's most-hyped clinical questions — does cannabis help dementia? — so we read the citation graph of that literature to see what it actually rests on. The honest version:
- The field stands on three pillars. A receptor-pharmacology bedrock (the CB1/CB2 cloning papers, ~5,000 citations each); a large body of preclinical neuroprotection work (cannabinoids protect neurons — in mice and cells, e.g. Hampson 1998, Ramírez 2005); and a thin but real clinical line on agitation.
- The only thing with real clinical support is symptom control — agitation. A clean lineage runs Volicer 1997 → van den Elsen 2015 → Herrmann 2019 (a nabilone RCT) → a 2024 Johns Hopkins dronabinol trial (~30% agitation reduction vs placebo, well tolerated). It matters because the standard alternative — antipsychotics — carries black-box stroke/death warnings in the elderly.
- The disease-modifying dream is still in mice. The "cannabinoids slow Alzheimer's" excitement rides on that same 1998–2007 preclinical work, with no human trial behind it yet.
- On risk: heavy/disordered use is a marker of higher dementia risk, but the rigorous genetic (Mendelian-randomization) evidence finds no causal link for moderate lifetime use — pattern and dose dominate.
The point for this document: a single aroma molecule — the smell of black pepper — opens onto an entire clinical literature, because it happens to also be a drug. Mapping those cross-domain reaches, with every claim grounded and the hype separated from the evidence, is the work. (The citation-graph structure above is verified metadata; the recent-trial figures are from grounded web search, not independently checked against the source papers.)
[→ Read the full cannabis-and-dementia citation analysis (the three-pillar breakdown)](dementia.html)
## Beyond terpenes — the flavorants that modify the base
Here's the twist the last few years of analytical work delivered (Oswald & Abstrax, ACS Omega 2021–2024): terpene profiles are remarkably similar across cultivars that smell nothing alike — so terpenes are the loud, pleasant base canvas, but they are not what makes one strain smell like gas and another like passionfruit. That comes from trace non-terpene "flavorants" — under 0.05% of the flower's mass, but with odor thresholds so low they punch far above their weight. And, exactly as you'd expect, they don't replace the terpenes — they modify them.
### The trace modifiers
Each card leads with the compound class, then its example molecule — drag any to rotate; the view/spin controls above drive these too.
### How they make it better — or worse
The flavorants don't add a separate note; they rewrite the whole percept. Real examples:
limonene (flat lemon-cleaner)+tropical thiol→juicy grapefruit▲ better
myrcene + caryophyllene (harsh herbal)+esters→candy / pastry▲ better (masked)
terpene base+skunk thiol→dank gassy diesel◆ louder — taste-dependent
savory base+trace skatole→umami funk▲butexcess→fecal off-note▼ worse
The mechanism is olfactory, not just chemical: the nose reads a mixture as one blended "odor object" (configural perception), and a potent trace molecule changes that blend two ways — by masking (it occupies an olfactory receptor without firing it, blocking a dominant terpene so harsh pine/herb recedes and finer notes surface) and by synergy (terpene + thiol don't smell like "pine + sulfur" — they fuse into a brand-new quality). The trace compound rewrites how the brain reads the entire terpene mixture.
Configural perception, illustrated: strawberry-like ethyl isobutyrate and caramel-like ethyl maltol, mixed 30:70, are read by the brain as one new odor object — pineapple — while nothing new exists in the jar (Le Berre et al. 2008; reviewed in [Coureaud et al. 2022](https://doi.org/10.1242/jeb.242274)).
And a fair question the aroma story raises: do the flavorants stop at the nose? These are not inert perfumes — thiols, indoles, and volatile acids are potently biologically active classes of molecule, firing receptors at concentrations far below a part per million, which is exactly why you can smell them at trace levels. It is plausible — we'd say likely — that molecules this active modify more than the aroma when they arrive alongside the cannabinoids. But read that at its honest strength: a hypothesis, ours. Whether flower-trace doses of these compounds change the felt effect past the nose has, to our knowledge, never been directly tested — another question sitting in the same starved, stigma-shadowed corner as the rest of cannabis medical research.
Sources verified against CrossRef: skunk VSCs — Oswald et al., ACS Omega 2021, [10.1021/acsomega.1c04196](https://doi.org/10.1021/acsomega.1c04196); non-terpenoids drive exotic aroma (with a human sensory panel) — Oswald et al., ACS Omega 2023, [10.1021/acsomega.3c04496](https://doi.org/10.1021/acsomega.3c04496); non-terpenoid diversity predicts aroma — Oswald et al., ACS Omega 2024, [10.1021/acsomega.4c03225](https://doi.org/10.1021/acsomega.4c03225). Aroma/interaction descriptors are from grounded web search.
## The entourage effect — honestly
The popular claim is that terpenes and cannabinoids act synergistically — that the whole plant beats the isolated molecule. The evidence is more careful than the marketing:
- Broad synergy is mostly unproven. A Nov-2024 systematic review (André et al., Pharmaceuticals) found individual terpenes have real effects, but the claim that they synergistically enhance cannabinoid efficacy is clinically unproven for most combinations — commercial claims outpace the trial data.
- But one specific pairing is real. An April-2024 Johns Hopkins double-blind RCT found d-limonene significantly reduced THC-induced anxiety and paranoia — without dulling the high. First concrete human evidence that a terpene can selectively buffer a cannabinoid's side effects.
Verification flag: the two 2024 studies above came from grounded web search, not the citation graph, and have not been independently verified against the source papers. Treat as strong leads.
## Where the molecule map ends and the expert begins
This atlas is the part a machine builds cleanly: molecule → aroma → botanical source → receptor, every identifier real and checkable. What it can't finish is the interaction — how the trace flavorants bend the terpene base, better or worse, and which of those blended profiles people actually prefer. That is a sensory-panel + preference-modeling problem (precisely what the Oswald 2023 study used a human panel for), plus validating compound effects in human cell models. The map is built; reading what it means for preference needs a domain expert.
Every page here has a markdown twin; this page's is [https://denson.github.io/aroma-atlas/index.md](https://denson.github.io/aroma-atlas/index.md) (also served with .txt appended), carrying everything the 3D viewers show, as text. [https://denson.github.io/aroma-atlas/llms.txt](https://denson.github.io/aroma-atlas/llms.txt) describes how the record is organized.

## The terpenes, as data

- **Myrcene** (C₁₀H₁₆, 136.23 g/mol) — aroma: Earthy, musky, clove. · [PubChem CID 31253](https://pubchem.ncbi.nlm.nih.gov/compound/31253)
  Also in mango, hops, lemongrass, thyme. The most abundant terpene in cannabis.
- **Limonene** (C₁₀H₁₆, 136.23 g/mol) — aroma: Bright citrus. · [PubChem CID 22311](https://pubchem.ncbi.nlm.nih.gov/compound/22311)
  Also in citrus peel, rosemary, juniper. The terpene in the Johns Hopkins THC-anxiety RCT.
- **α-Pinene** (C₁₀H₁₆, 136.23 g/mol) — aroma: Sharp pine. · [PubChem CID 6654](https://pubchem.ncbi.nlm.nih.gov/compound/6654)
  Also in pine needles, rosemary, eucalyptus, orange peel.
- **β-Pinene** (C₁₀H₁₆, 136.23 g/mol) — aroma: Pine, herbal. · [PubChem CID 14896](https://pubchem.ncbi.nlm.nih.gov/compound/14896)
  Also in dill, basil, parsley, pine.
- **Linalool** (C₁₀H₁₈O, 154.25 g/mol) — aroma: Floral, lavender. · [PubChem CID 6549](https://pubchem.ncbi.nlm.nih.gov/compound/6549)
  Also in lavender, coriander, rosewood, mint.
- **β-Caryophyllene** (C₁₅H₂₄, 204.35 g/mol) — aroma: Spicy, peppery, clove. · [PubChem CID 5281515](https://pubchem.ncbi.nlm.nih.gov/compound/5281515)
  Also in black pepper, cloves, cinnamon, hops. Not a cannabinoid — a terpene that nonetheless binds the CB2 receptor like a drug.
- **Humulene** (C₁₅H₂₄, 204.35 g/mol) — aroma: Hoppy, woody. · [PubChem CID 5281520](https://pubchem.ncbi.nlm.nih.gov/compound/5281520)
  Also in hops (cannabis's genetic cousin), sage, ginger, ginseng.
- **Terpinolene** (C₁₀H₁₆, 136.23 g/mol) — aroma: Pine, floral, citrus. · [PubChem CID 11463](https://pubchem.ncbi.nlm.nih.gov/compound/11463)
  Also in lilac, tea tree, nutmeg, apples, rosemary.
- **Ocimene** (C₁₀H₁₆, 136.23 g/mol) — aroma: Sweet, herbal. · [PubChem CID 6434062](https://pubchem.ncbi.nlm.nih.gov/compound/6434062)
  Also in mint, parsley, basil, orchids, kumquats.
- **Nerolidol** (C₁₅H₂₆O, 222.37 g/mol) — aroma: Woody, floral, citrus. · [PubChem CID 5284507](https://pubchem.ncbi.nlm.nih.gov/compound/5284507)
  Also in jasmine, ginger, tea tree, lemongrass.

## Beyond terpenes: the flavorants, as data

### Volatile sulfur compounds — "gas"

- **3-methyl-2-butene-1-thiol** (C₅H₁₀S, 102.20 g/mol) — aroma: skunky · diesel · pungent. · [PubChem CID 146586](https://pubchem.ncbi.nlm.nih.gov/compound/146586)
  The prenyl thiol behind the classic skunk/diesel aroma — the same molecule as skunked beer. Adds loud pungency over the terpene base (Chemdawg, Gorilla Glue).
### Tropical thiols — "juicy fruit"

- **3-mercaptohexan-1-ol** (C₆H₁₄OS, 134.24 g/mol) — aroma: passionfruit · guava · real citrus. · [PubChem CID 521348](https://pubchem.ncbi.nlm.nih.gov/compound/521348)
  A 'tropicannasulfur' — also the key thiol in Sauvignon Blanc. The citrus you smell in Tangie is this, not limonene.
### Esters — "candy"

- **Ethyl hexanoate** (C₈H₁₆O₂, 144.21 g/mol) — aroma: sweet · apple · pastry. · [PubChem CID 31265](https://pubchem.ncbi.nlm.nih.gov/compound/31265)
  A fruity ester that masks harsh herbal terpene notes and lifts sweetness — the candy-sweet 'exotic' cultivars (Runtz, Gelato).
### Esters — "grape"

- **Methyl anthranilate** (C₈H₉NO₂, 151.16 g/mol) — aroma: grape · wine-candy. · [PubChem CID 8635](https://pubchem.ncbi.nlm.nih.gov/compound/8635)
  The grape / 'grape soda' ester — another of the sweet 'exotic' flavorants.
### Indole & skatole — "funk"

- **Skatole** (C₉H₉N, 131.17 g/mol) — aroma: savory · dank · umami. · [PubChem CID 6736](https://pubchem.ncbi.nlm.nih.gov/compound/6736)
  3-methylindole — trace = mouth-watering umami funk (GMO, Garlic Cookies); excess tips to fecal/musty. It also amplifies the gassy thiols.
### Volatile fatty acids — "cheese"

- **Octanoic acid** (C₈H₁₆O₂, 144.21 g/mol) — aroma: sweaty · dairy · sharp. · [PubChem CID 379](https://pubchem.ncbi.nlm.nih.gov/compound/379)
  With decanoic acid — the savory, cheese-rind nuance in some phenotypes.
