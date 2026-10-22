# Visual assets

## Cover

[hero-imagegen.png](hero-imagegen.png) was generated with the built-in ImageGen tool on 2026-10-22. It is a conceptual illustration, not a screenshot of a verification run. The original vector banner is retained as [hero.svg](hero.svg).

Final prompt:

> Use case: ads-marketing. Asset type: striking GitHub README hero banner for the open-source frontend verification skill Verify Feature. Create a finished wide landscape editorial illustration, around 2:1 aspect ratio, sharp and beautifully art-directed. Deep graphite black background, warm ivory typography, vivid mint/lime accents, tiny restrained coral red accents. Primary copy on the left, very large and perfectly legible, exact text: 'Your AI says done.' then 'Ask for evidence.' Product label smaller at top: 'VERIFY FEATURE'. On the right, a sculptural exploded stack of browser-window cards: a frontend form, a captured request/payload receipt, a screenshot frame, and a crisp evidence check marker. These should look like tactile precision-cut glass and paper, controlled isometric perspective, fine edge lighting and subtle grain. A single mint line visually connects browser action to evidence. This is a conceptual illustration, not a screenshot of real test results. Composition has generous negative space, bold hierarchy, and strong readable silhouette even at README width. Include only those three exact text phrases; no extra microcopy, no fake metrics, no other brand logos, no robots, no people, no purple gradients, no excessive neon, no generic dashboard wallpaper, no watermark. Elegant and memorable developer-tool branding, not a busy sci-fi scene.

The output was inspected for headline spelling, clipping, legibility, composition, and unexpected labels. One image was generated and selected.

## Workflow diagrams

Generated with [Archify](https://github.com/tt-a1i/archify), using workflow schema v2 and the showcase quality profile. The diagram follows [SKILL.md](../SKILL.md) and its browser/mock references. Main-path arrows indicate the order of the named steps; the two labeled branches describe mock preparation and request isolation.

| Language | Source | README image | Interactive artifact |
| --- | --- | --- | --- |
| English | [JSON](workflow.en.json) | [SVG](workflow.en.svg) | [HTML](workflow.en.html) |
| Chinese | [JSON](workflow.zh-CN.json) | [SVG](workflow.zh-CN.svg) | [HTML](workflow.zh-CN.html) |

Download the HTML and open it locally. GitHub displays the SVGs, but does not run the HTML viewer. The viewer supports theme switching, zoom, search, and canonical image exports. Its runtime is distributed under the [included MIT notice](ARCHIFY-LICENSE.txt).

Both final artifacts passed 9/9 deterministic showcase checks with 0 composition errors and 0 warnings. Automated browser checks passed at 1440×900, 1600×1000, 1920×1080, and 2048×1320; light/dark captures were collected at both endpoint sizes. Screenshots were separately inspected for readable labels, route collisions, clipping, and layout. English spacing received two visual correction rounds; Chinese received none.

These checks apply to the diagrams, not to frontend applications using the skill. Raw local browser receipts are excluded from publication because they contain machine-specific paths.

## Delivery receipts

### en

```text
diagram_type: workflow
output: workflow.en.html
specification_sha256: 4f9b0b24e1b3602733405b2b830dd02ca569e693d7d3af4828714f0b0f649b47
specification_bytes: 3219
artifact_sha256: 21c3693b991657d11fb576a6d07771a464c040774494fac19c2bfcced499e069
artifact_bytes: 708059
validation: 9/9 showcase, 0 errors, 0 warnings
browser_evidence: passed
visual_review: passed
correction_rounds: 2
```

### zh-CN

```text
diagram_type: workflow
output: workflow.zh-CN.html
specification_sha256: 61dd2b6670c7a2aa8afe2efbe221619801a3448b2cd8447aab983588fe59d102
specification_bytes: 3080
artifact_sha256: 6fa73d3a219cfe45875c0c7578e1db9519d3c30b76471484d8054cb5614bac71
artifact_bytes: 707813
validation: 9/9 showcase, 0 errors, 0 warnings
browser_evidence: passed
visual_review: passed
correction_rounds: 0
```

## README references

The README structure was reviewed against [Playwright](https://github.com/microsoft/playwright/blob/main/README.md), [MSW](https://github.com/mswjs/msw/blob/main/README.md), and [Anthropic Skills](https://github.com/anthropics/skills/blob/main/README.md). Wording and examples are specific to this skill; no testimonials or usage figures were copied.
