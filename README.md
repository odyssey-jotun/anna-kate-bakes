# Baking Bloopers

Website for Anna Kate Huneycutt's baking project: short recipe videos, a blooper reel, recipe cards, and a free two-page recipe guide. Built on the StoryBrand wireframe from her answers on the StoryBrand Form tab of her College & Scholarship Plan doc (filled in 2026-10-13). The videos are the edits from `odyssey-jotun/huneycutt`.

## Files

- `build.py` writes `index.html`, `robots.txt` and `favicon.svg`. Copy and recipes live in it. Run `python3 build.py`.
- `styles.css` is minified and inlined by the build.
- `guide/guide.html` is the source of `guide/anna-kate-starter-recipes.pdf` (the download button). Print it with Playwright at Letter size, `printBackground: true`, `preferCSSPageSize: true`. Each page is a fixed 11in flex column, so check neither page overflows (`scrollHeight - clientHeight` should be 0 for each `.page`).
- `videos/` holds 720p web copies of the three edits; `images/poster-*.jpg` are their poster frames.
- Photos are frames from her own iPhone footage, cropped and color-graded.
- Fonts: Fredoka (headings, same as the video captions) and Nunito Sans, self-hosted from Google Fonts.

## Rules this site follows

- People photo hero, palette from the videos (frosting pink, chocolate, cream, butcher block). No em dashes, no eyebrow labels, no bold inside sentences, no external links. Research is cited in plain text.
- `noindex` and `robots.txt Disallow` until Marc and the family approve it going public.

## Open

- Site name: "Baking Bloopers" (Marc, 2026-10-13). Her answer was "annakates baking page (I don't really know)". The repo and URL are still `anna-kate-bakes`.
- Button text: she asked for "download recipe video"; the button says "Download the Recipe Guide" because it downloads the PDF.
- Free guide contents: her form left this blank. The PDF uses her two recipes plus mistakes from her own answers (tablespoon vs teaspoon, baking powder vs soda) and her video tips (runny cookie dough, liquidy mug cake batter).
- Written for her, needs her OK: the plan step descriptions, the stakes "with" list, and the first-person blooper section. Pink quotes on the recipe cards are her own words from the videos; "I bake to not feel like a moron" and the "bake trash" quote come from Marc's Video Guidelines tab, not from her.
- Blooper reel: `videos/bloopers.mp4` is a 720p copy of `edited/bloopers.mp4` from `odyssey-jotun/huneycutt` (built by `video-build/bloopers/build_bloopers.py`).
- Chocolate chip cookies are listed as coming next.
- Research section (`#research`) carries all seven findings from the Research tab, grouped as habits, confidence and mood, later in life. Every citation was checked against the paper on 2026-10-13. The Research tab misstates the Taiwan result ("47 percent more likely to be alive"); the paper's hazard ratio was 0.47 (53% lower risk of death), 0.59 after adjusting for health (41% lower). The site uses the adjusted 41%.
