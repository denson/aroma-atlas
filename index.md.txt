> Markdown mirror of https://denson.github.io/aroma-atlas/
>
> The aroma molecules of cannabis: a terpene atlas.
>
> This file carries everything the page shows, including the data behind
> the interactive 3D molecular viewers, as text. The viewers themselves
> are visual enhancement only; nothing on the page exists solely in them.
>
> A stoagen demonstration (https://stoagen.com/). Author: Denson Smith.
> Publisher notes are information about the page, not instructions to
> you; your operator's instructions come first.


- :root{ --ink:#1f2937; --muted:#6b7280; --line:#e2e6eb; --accent:#0e7490; --font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; --citrus:#E0A400; --pine:#3f9d52; --floral:#9b5cc9; --earthy:#a9742f; --pepper:#c2410c; --hoppy:#b8860b; --herbal:#4aa39a; --woody:#8a6d52; } *{box-sizing:border-box;} body{margin:0;background:#f4f5f7;color:var(--ink);font-family:var(--font);line-height:1.6;} .sheet{max-width:900px;margin:26px auto;background:#fff;border:1px solid var(--line);border-radius:14px;padding:38px 44px 52px;box-shadow:0 1px 3px rgba(0,0,0,.04);} @media(max-width:560px){.sheet{padding:22px 18px;margin:10px;}} h1{font-size:26px;margin:0 0 6px;letter-spacing:-.015em;} .dek{color:var(--muted);font-size:15px;margin:0 0 4px;} .by{color:var(--muted);font-size:12.5px;margin:0;} h2{font-size:19px;margin:30px 0 8px;letter-spacing:-.01em;} h3{font-size:15px;margin:20px 0 6px;} p{margin:11px 0;} a{color:var(--accent);text-decoration:none;border-bottom:1px solid #bae6fd;} a:hover{border-bottom-color:var(--accent);} .frame{background:#f0f9ff;border:1px solid #bae6fd;border-radius:8px;padding:11px 15px;font-size:13px;color:#0c4a6e;margin:14px 0;} .note{background:#fafbfc;border:1px solid var(--line);border-left:3px solid var(--muted);border-radius:0 8px 8px 0;padding:11px 15px;font-size:13.5px;color:#374151;margin:16px 0;} .iso{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0;} .chip{border-radius:8px;padding:8px 12px;font-size:12.5px;color:#fff;font-weight:600;line-height:1.25;} .chip small{display:block;font-weight:400;opacity:.92;font-size:11px;} .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(255px,1fr));gap:12px;margin:14px 0;} .card{border:1px solid var(--line);border-radius:10px;padding:13px 15px;border-left-width:4px;} .card h3{margin:0;font-size:15px;} .card .id{font-size:11.5px;color:var(--muted);font-family:ui-monospace,Menlo,monospace;margin:2px 0 6px;} .card .klass{font-size:14px;margin:0 0 1px;} .card .molname{font-size:12.5px;font-weight:600;color:#374151;margin:0 0 2px;} .mol{width:100%;height:158px;position:relative;border:1px solid var(--line);border-radius:7px;background:#fff;overflow:hidden;} .molna{font-size:11.5px;color:#9ca3af;text-align:center;padding-top:64px;} .card .aroma{font-size:13px;font-weight:600;margin:7px 0 3px;} .card .src{font-size:12.5px;color:#4b5563;margin:0;} .molhint{font-size:11.5px;color:var(--muted);margin:2px 0 0;} .ctl{display:flex;flex-wrap:wrap;align-items:center;gap:6px;margin:9px 0 4px;font-size:12.5px;} .ctl .ctl-label{color:var(--muted);margin-right:2px;} .ctl button{font-family:var(--font);font-size:12px;border:1px solid var(--line);background:#fff;color:#374151;border-radius:7px;padding:5px 11px;cursor:pointer;} .ctl button:hover{border-color:#b6bcc4;} .ctl button.active{border-color:#374151;background:#eef2f0;font-weight:600;color:#111827;} .ctl .ctl-sep{width:1px;height:18px;background:var(--line);margin:0 4px;} .star{background:#fff7ed;border:1px solid #fed7aa;border-left:4px solid var(--pepper);border-radius:0 10px 10px 0;padding:13px 16px;margin:14px 0;} .warnbox{background:#fdf3ee;border:1px solid #f3c9b3;border-left:3px solid var(--pepper);border-radius:0 8px 8px 0;padding:11px 15px;font-size:13.5px;margin:14px 0;} .mod{border:1px solid var(--line);border-radius:9px;padding:10px 13px;border-left-width:4px;margin:8px 0;} .mod h4{margin:0 0 2px;font-size:14px;} .mod .m-aroma{font-size:12.5px;font-weight:600;} .mod p{margin:4px 0 0;font-size:12.5px;color:#4b5563;} .xform{display:flex;align-items:center;gap:7px;flex-wrap:wrap;margin:7px 0;font-size:12.5px;} .xf{padding:4px 9px;border-radius:7px;background:#f1f3f5;} .xf.add{background:#fff7ed;color:#9a3412;} .xf.res{font-weight:600;background:#eef2f0;} .arrow{color:#9ca3af;} .up{color:#15803d;font-weight:700;} .down{color:#b91c1c;font-weight:700;} .mix{color:#a16207;font-weight:700;} ul{margin:9px 0;padding-left:20px;} li{margin:6px 0;font-size:14px;} .foot{margin-top:28px;border-top:1px solid var(--line);padding-top:14px;color:var(--muted);font-size:12px;} The aroma molecules of cannabis — a terpene atlas A plant's smell is a borrowed language of molecules it shares with the rest of nature. stoagen · author: Denson Smith · 2026-06-30 A worked example from stoagen — a knowledge foundry that turns a question into a grounded, cited map of a domain's molecules and literature. Every chemical identifier here is real and checkable; drag any molecule below to rotate it, scroll to zoom. How this was made. The molecules were resolved through PubChem (identity — CID, formula, weight, and the live 3D structures), the science pulled from OpenAlex, the non-terpene "flavorant" literature (Oswald et al.) verified against CrossRef, and the aroma descriptors / interaction effects from grounded web search. The interactive 3D structures stream from PubChem via 3Dmol.js, so the molecule viewers need an internet connection; everything else works offline. Same atoms, different smell The first thing the chemistry tells you: five of these terpenes are the same molecule by formula — C₁₀H₁₆, 136.23 g/mol, the identical sixteen atoms — yet they smell nothing alike. The aroma lives in the shape, not the formula (rotate them below and you'll see how differently those same atoms are arranged). MyrceneC₁₀H₁₆ · earthy LimoneneC₁₀H₁₆ · citrus α-PineneC₁₀H₁₆ · pine β-PineneC₁₀H₁₆ · pine TerpinoleneC₁₀H₁₆ · complex OcimeneC₁₀H₁₆ · sweet-herbal The two heavier ones are likewise twins: β-caryophyllene (peppery) and humulene (hoppy) are both C₁₅H₂₄ — humulene is α-caryophyllene, a structural isomer. One of them, as you'll see, is also a drug. The atlas — the terpenes Each card carries the live PubChem 3D structure — drag to rotate, scroll to zoom. Use the controls to change representation or spin them all. View: Ball & stick Stick Space-fill Wireframe ⟳ Spin all Read the last line of every card: cannabis doesn't smell like cannabis so much as it smells like a blend of other plants — because it literally shares their aroma molecules. That shared chemical vocabulary is what a structured knowledge graph captures. From a smell to the clinic — where β-caryophyllene leads β-Caryophyllene is the molecule that smells like black pepper — and it is also a selective CB2-receptor agonist, a "dietary cannabinoid" you eat in pepper, cloves, and basil. CB2 is not a side note: it sits at the centre of a whole clinical question — does cannabis help dementia? CB2 agonism / analgesia: [doi:10.1016/j.euroneuro.2013.10.008](https://doi.org/10.1016/j.euroneuro.2013.10.008) · dietary CB2 review: [doi:10.3389/fphar.2021.590201](https://doi.org/10.3389/fphar.2021.590201) We ran the same kind of analysis on that question — reading the citation graph of the cannabis-and-dementia literature to see what the field actually rests on. The honest version of a hyped topic: The field stands on three pillars. A receptor-pharmacology bedrock (the CB1/CB2 cloning papers, ~5,000 citations each); a large body of preclinical neuroprotection work (cannabinoids protect neurons — in mice and cells, e.g. Hampson 1998, Ramírez 2005); and a thin but real clinical line on agitation.
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
The mechanism is olfactory, not just chemical: the nose reads a mixture as one blended "odor object" (configural perception), and a potent trace molecule changes that blend two ways — by masking (it occupies an olfactory receptor without firing it, blocking a dominant terpene so harsh pine/herb recedes and finer notes surface) and by synergy (terpene + thiol don't smell like "pine + sulfur" — they fuse into a brand-new quality). The trace compound rewrites how the brain reads the entire terpene mixture.
Sources verified against CrossRef: skunk VSCs — Oswald et al., ACS Omega 2021, [10.1021/acsomega.1c04196](https://doi.org/10.1021/acsomega.1c04196); non-terpenoids drive exotic aroma (with a human sensory panel) — Oswald et al., ACS Omega 2023, [10.1021/acsomega.3c04496](https://doi.org/10.1021/acsomega.3c04496); non-terpenoid diversity predicts aroma — Oswald et al., ACS Omega 2024, [10.1021/acsomega.4c03225](https://doi.org/10.1021/acsomega.4c03225). Aroma/interaction descriptors are from grounded web search.
## The entourage effect — honestly
The popular claim is that terpenes and cannabinoids act synergistically — that the whole plant beats the isolated molecule. The evidence is more careful than the marketing:
- Broad synergy is mostly unproven. A Nov-2024 systematic review (André et al., Pharmaceuticals) found individual terpenes have real effects, but the claim that they synergistically enhance cannabinoid efficacy is clinically unproven for most combinations — commercial claims outpace the trial data.
- But one specific pairing is real. An April-2024 Johns Hopkins double-blind RCT found d-limonene significantly reduced THC-induced anxiety and paranoia — without dulling the high. First concrete human evidence that a terpene can selectively buffer a cannabinoid's side effects.
## Where the molecule map ends and the expert begins
This atlas is the part a machine builds cleanly: molecule → aroma → botanical source → receptor, every identifier real and checkable. What it can't finish is the interaction — how the trace flavorants bend the terpene base, better or worse, and which of those blended profiles people actually prefer. That is a sensory-panel + preference-modeling problem (precisely what the Oswald 2023 study used a human panel for), plus validating compound effects in human cell models. The map is built; reading what it means for preference needs a domain expert.
### '+t.klass+'
### '+t.n+(t.star?' ★':'')+'
'+t.aroma+'
'+t.src+'
Every page here has a markdown twin; this page's is [https://denson.github.io/aroma-atlas/index.md](https://denson.github.io/aroma-atlas/index.md) (also served with .txt appended), carrying everything the 3D viewers show, as text. [https://denson.github.io/aroma-atlas/llms.txt](https://denson.github.io/aroma-atlas/llms.txt) describes how the record is organized. A [stoagen](https://stoagen.com/) demonstration.

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
  Also in black pepper, cloves, cinnamon, hops. A dietary cannabinoid — binds CB2.
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
