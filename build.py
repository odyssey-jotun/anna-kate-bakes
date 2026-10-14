#!/usr/bin/env python3
"""Builds index.html for Baking Bloopers.

Run: python3 build.py
SITE_NAME is Marc's pick, "Baking Bloopers" (her form said "annakates baking
page (I don't really know)"). Change it here and rebuild; titles follow.
Copy comes from her StoryBrand Form answers and her own video voiceovers.
"""
import json
import re

SITE_NAME = "Baking Bloopers"
AUTHOR = "Anna Kate Huneycutt"
SITE = "https://odyssey-jotun.github.io/anna-kate-bakes/"
GUIDE = "guide/anna-kate-starter-recipes.pdf"


def css():
    t = open("styles.css").read()
    t = re.sub(r"/\*.*?\*/", "", t, flags=re.S)
    t = re.sub(r"\s+", " ", t)
    return re.sub(r"\s*([{};:,>])\s*", r"\1", t).replace(";}", "}").strip()


def svg(body, sw="2.6"):
    return (f'<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


MARK = ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#5A2E1C"/>'
        '<circle cx="16" cy="16" r="9.5" fill="#F4A9BB"/><circle cx="12.5" cy="13" r="1.6" fill="#5A2E1C"/>'
        '<circle cx="18.5" cy="12" r="1.4" fill="#5A2E1C"/><circle cx="19.5" cy="18.5" r="1.7" fill="#5A2E1C"/>'
        '<circle cx="13" cy="19.5" r="1.3" fill="#5A2E1C"/></svg>')
I_RECIPE = svg('<rect x="9" y="6" width="30" height="36" rx="4"/><path d="M16 16h16M16 23h16M16 30h9"/>'
               '<path d="M33 34a3 3 0 11-.1 0"/>')
I_FLAT = svg('<ellipse cx="24" cy="30" rx="17" ry="6"/><path d="M18 18c0-3 3-3 3-6M27 18c0-3 3-3 3-6"/>')
I_HEART = svg('<path d="M24 41s-15-8.5-15-20a8 8 0 0115-4 8 8 0 0115 4c0 11.5-15 20-15 20z"/>')
I_BAG = svg('<path d="M10 16h28l-2 24H12z"/><path d="M18 16v-3a6 6 0 0112 0v3"/>')
I_BOWL = svg('<path d="M6 22h36c0 10-8 17-18 17S6 32 6 22z"/><path d="M30 22l9-14"/>')
I_COOKIE = svg('<circle cx="24" cy="24" r="17"/><circle cx="18" cy="19" r="1.8"/><circle cx="28" cy="17" r="1.6"/>'
               '<circle cx="30" cy="28" r="2"/><circle cx="19" cy="30" r="1.6"/>')
I_SPOON = svg('<ellipse cx="17" cy="15" rx="7" ry="9" transform="rotate(-35 17 15)"/><path d="M22 22l18 18"/>')
CHECK = svg('<path d="M10 25l9 9 19-20"/>', "3.4")
CROSS = svg('<path d="M14 14l20 20M34 14L14 34"/>', "3.4")
DOWN = svg('<path d="M24 8v24M14 23l10 10 10-10M10 40h28"/>', "3.4")

BAKED = ["Cookies", "Pies", "Muffins", "Cakes", "Cake pops"]

RECIPES = [
    dict(id="peanut-butter-cookies", name="Peanut Butter Cookies",
         says="This recipe is super duper simple, and it's so good for just an after-school snack.", meta=["3 ingredients", "350&deg;F", "About 12 minutes"],
         items=["1 cup peanut butter", "1 cup sugar", "1 egg"],
         steps="Mix everything in one bowl, roll the dough into little balls on parchment paper, and bake at 350&deg; for about 12 minutes. Press a fork across the top first if you want them to look cute.",
         tip="The dough should hold a cookie shape. If it's runny, add a little more sugar: these are cookies, not a cake.",
         poster="Anna Kate holding a jar of peanut butter in her kitchen"),
    dict(id="chocolate-mug-cake", name="Chocolate Mug Cake",
         says="Nothing says ambition like a chocolate mug cake.", meta=["One mug", "Microwave", "About 2 minutes"],
         items=["3 tbsp flour", "2 tbsp cocoa powder", "2 tbsp sugar", "&frac12; tsp baking powder",
                "&frac12; tsp baking soda", "&frac14; cup milk", "Chocolate chips, if you want them"],
         steps="Stir everything together right in the mug, drop in a few chocolate chips, and microwave for about 2 minutes.",
         tip="This batter should be liquidy, because it's a cake. Read the spoon twice: tablespoons and teaspoons are not the same thing.",
         poster="Anna Kate measuring flour into a mug"),
]


def video(vid, label, poster_alt):
    return (f'<figure class="video"><video controls playsinline preload="none" width="720" height="1280" '
            f'poster="images/poster-{vid}.jpg" aria-label="{label}"><source src="videos/{vid}.mp4" type="video/mp4">'
            f'</video></figure>')


def recipe_card(r):
    lis = "".join(f"<li>{i}</li>" for i in r["items"])
    meta = "".join(f"<span>{m}</span>" for m in r["meta"])
    return f"""
      <article class="recipe reveal" id="{r['id']}">
        {video(r['id'], f"Anna Kate's {r['name']} video", r['poster'])}
        <div>
          <h3>{r['name']}</h3>
          <p class="meta">{meta}</p>
          <p class="says">&ldquo;{r['says']}&rdquo;</p>
          <ul>{lis}</ul>
          <p>{r['steps']}</p>
          <p class="tip">{r['tip']}</p>
        </div>
      </article>"""


def page():
    title = f"{SITE_NAME} | Easy Baking Recipes for Beginners"
    desc = ("Simple, slightly awkward baking videos and recipes from Anna Kate Huneycutt: three-ingredient peanut butter cookies, "
            "a two-minute chocolate mug cake, and the beginner mistakes to skip. Free recipe guide.")
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": SITE + "#site", "url": SITE, "name": SITE_NAME, "inLanguage": "en-US",
         "author": {"@id": SITE + "#anna-kate"}},
        {"@type": "Person", "@id": SITE + "#anna-kate", "name": AUTHOR,
         "description": "High school senior who has baked since seventh grade and films simple recipe videos."},
    ] + [{"@type": "Recipe", "name": r["name"], "author": {"@id": SITE + "#anna-kate"},
          "recipeIngredient": [re.sub(r"&frac12;", "1/2", re.sub(r"&frac14;", "1/4", i)) for i in r["items"]],
          "image": SITE + f"images/poster-{r['id']}.jpg", "url": SITE + "#" + r["id"],
          "description": re.sub(r"&deg;", "°", r["steps"])} for r in RECIPES]}
    hero_srcset = ", ".join(f"images/hero-{w}.webp {w}w" for w in (480, 640, 800, 1000))
    hero_sizes = "(max-width: 620px) calc(100vw - 40px), (max-width: 900px) 520px, 460px"
    made = "".join(f"<li>{I_COOKIE}{b}</li>" for b in BAKED)
    first = SITE_NAME.rsplit(" ", 1)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex,nofollow">
<link rel="canonical" href="{SITE}">
<meta name="author" content="{AUTHOR}">
<meta name="theme-color" content="#FFF7EE">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}">
<meta property="og:image" content="{SITE}images/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" as="image" type="image/webp" href="images/hero-800.webp" imagesrcset="{hero_srcset}" imagesizes="{hero_sizes}" fetchpriority="high">
<link rel="preload" href="fonts/fredoka.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/nunito-sans.woff2" as="font" type="font/woff2" crossorigin>
<style>{css()}</style>
<script type="application/ld+json">{json.dumps(ld, separators=(",", ":"), ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<nav class="site" aria-label="Primary">
  <div class="wrap">
    <a class="wordmark" href="./">{MARK}<span>{first[0]} <span class="last">{first[1]}</span></span></a>
    <ul>
      <li><a href="#recipes"><span>Recipes</span></a></li>
      <li><a href="#bloopers"><span>Bloopers</span></a></li>
      <li class="x"><a href="#about"><span>About Anna Kate</span></a></li>
    </ul>
  </div>
</nav>

<main id="main">

<header class="hero">
  <div class="wrap">
    <div class="hero-text">
      <h1>Easy baking for anyone who wants to make something good today</h1>
      <p class="lede">Short recipe videos from {AUTHOR}, a high school senior who has baked since seventh grade. Each recipe takes a few ingredients and very little time, and the bloopers stay in.</p>
      <div class="btn-row">
        <a href="{GUIDE}" class="btn" download>{DOWN}Download the Recipe Guide</a>
      </div>
    </div>
    <figure class="hero-photo"><img src="images/hero-800.webp" srcset="{hero_srcset}" sizes="{hero_sizes}" width="1000" height="1250" alt="Anna Kate smiling at her kitchen counter with a measuring spoon, a mug and her baking ingredients" fetchpriority="high" decoding="async"></figure>
  </div>
</header>

<section class="band" id="problem">
  <div class="wrap">
    <div class="section-head center">
      <h2>Starting to bake is harder than it looks</h2>
      <p>Plenty of people would love to bake and never start, or try once and give up.</p>
    </div>
    <div class="cards">
      <div class="card reveal">
        <div class="icon">{I_RECIPE}</div>
        <h3>Nobody knows where to start</h3>
        <p>New bakers don't know which recipe to try first, what to buy, or what the dough is supposed to look like.</p>
      </div>
      <div class="card reveal">
        <div class="icon">{I_FLAT}</div>
        <h3>One failed batch and they quit</h3>
        <p>When a recipe flops, people feel like they can't bake. They stop trying and buy cookies at the store instead.</p>
      </div>
      <div class="card reveal">
        <div class="icon">{I_HEART}</div>
        <h3>Every baker fails at first</h3>
        <p>Nobody should feel bad about missing on the first try. Every good baker has a flat batch somewhere in their past.</p>
      </div>
    </div>
    <div class="research">
      <figure>
        <blockquote>Adults who learned to cook before age 18 reported more cooking skills, more confidence and better diet quality than people who learned later.</blockquote>
        <figcaption>Lavelle and colleagues, 2016</figcaption>
      </figure>
      <figure>
        <blockquote>Across 23 randomized trials, kids' cooking programs reliably raised confidence and know-how in the kitchen.</blockquote>
        <figcaption>Systematic review of cooking programs for children, 2024</figcaption>
      </figure>
    </div>
  </div>
</section>

<section id="about">
  <div class="wrap split">
    <div>
      <h2>A high school senior who still double-checks the teaspoons</h2>
      <p class="name-line">I'm Anna Kate, and I bake to not feel like a moron.</p>
      <p class="quote">I used to freak out because I'd forget if it was 2 tablespoons or 2 teaspoons. I still double-check every time, because I'm so afraid of messing up.</p>
      <p>I've been baking since seventh grade. One time I put baking powder in my cookies instead of baking soda, and they came out completely flat. You just start over until it turns out right.</p>
      <ul class="made" aria-label="Things Anna Kate has baked">{made}</ul>
    </div>
    <figure class="photo reveal"><img src="images/guide-900.webp" srcset="images/guide-600.webp 600w, images/guide-900.webp 900w" sizes="(max-width: 900px) calc(100vw - 40px), 512px" width="900" height="1125" alt="Anna Kate in a red shirt laughing at her kitchen island" loading="lazy" decoding="async"></figure>
  </div>
  <div class="wrap intro-video">
    {video("intro", "Anna Kate's introduction video", "")}
    <div>
      <h3>&ldquo;Ever wonder what a high school senior does after school?&rdquo;</h3>
      <p>After tests, cheer practices, and girl drama, I bake. So come a little closer.</p>
    </div>
  </div>
</section>

<section class="band" id="bloopers">
  <div class="wrap intro-video flip">
    <div>
      <h2>The bloopers stay in</h2>
      <p>I sneezed into the sugar. I took an energy drink break in the middle of the cookie dough. I made a mug cake in honor of the Queen of Country herself. I kept all of it.</p>
      <p class="says">&ldquo;When I follow a recipe and it tastes good, I invite my friends over and they think I'm useful and cool. When I bake trash, I don't tell them. And you don't have to tell yours either.&rdquo;</p>
    </div>
    {video("bloopers", "Baking Bloopers: Anna Kate's blooper reel", "")}
  </div>
</section>

<section class="wood" id="plan">
  <div class="wrap">
    <div class="section-head center">
      <h2>Bake your first batch in three steps</h2>
    </div>
    <ol class="steps">
      <li class="reveal"><div class="icon">{I_BAG}</div><h3>Gather your ingredients</h3><p>Pick a recipe and pull out what it needs. You probably have all of it already.</p></li>
      <li class="reveal"><div class="icon">{I_BOWL}</div><h3>Follow the recipe</h3><p>Bake along with my video, one step at a time. Pause it whenever you need to.</p></li>
      <li class="reveal"><div class="icon">{I_COOKIE}</div><h3>Enjoy!</h3><p>Eat what you made, or share it and become everyone's favorite person.</p></li>
    </ol>
    <p class="promise">These recipes are super simple, and they use things almost everyone keeps in the kitchen.</p>
    <div class="btn-row">
      <a href="{GUIDE}" class="btn" download>{DOWN}Download the Recipe Guide</a>
    </div>
  </div>
</section>

<section id="recipes">
  <div class="wrap">
    <div class="section-head center">
      <h2>Recipes to bake this week</h2>
      <p>Watch the video, then bake along with the recipe card.</p>
    </div>
    <div class="recipes">{''.join(recipe_card(r) for r in RECIPES)}
    </div>
    <p class="next">Coming next: chocolate chip cookies.</p>
  </div>
</section>

<section class="band" id="success">
  <div class="wrap split">
    <figure class="photo reveal"><img src="images/cookies-900.webp" srcset="images/cookies-600.webp 600w, images/cookies-900.webp 900w" sizes="(max-width: 900px) calc(100vw - 40px), 512px" width="900" height="1125" alt="Anna Kate shaping peanut butter cookie dough onto a parchment-lined tray" loading="lazy" decoding="async"></figure>
    <div>
      <h2>Baking takes almost zero skill</h2>
      <p>That's what you find out after the first batch. Every recipe you finish makes you feel more accomplished, and soon you have a short list of treats you can make any afternoon.</p>
      <div class="before-after">
        <div><h3>Before</h3><p>Feeling unproductive and not knowing what to bake.</p></div>
        <div><h3>After</h3><p>Productive, with simple recipes ready to go.</p></div>
      </div>
    </div>
  </div>
</section>

<section id="stakes">
  <div class="wrap">
    <div class="section-head center">
      <h2>What staying out of the kitchen costs</h2>
    </div>
    <div class="stakes">
      <div class="stake reveal">
        <h3>Without baking</h3>
        <ul class="outcomes">
          <li class="x">{CROSS}<span>You miss the feeling of having made something yourself.</span></li>
          <li class="x">{CROSS}<span>You miss out on something totally delicious.</span></li>
          <li class="x">{CROSS}<span>You spend a ton on takeout and DoorDash for treats you could make at home.</span></li>
        </ul>
      </div>
      <div class="stake good reveal">
        <h3>With a few easy recipes</h3>
        <ul class="outcomes">
          <li>{CHECK}<span>You learn a basic skill that stays with you for life.</span></li>
          <li>{CHECK}<span>You feel productive and proud of what you made.</span></li>
          <li>{CHECK}<span>You become the friend who brings the cookies.</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="closing wood">
  <div class="wrap">
    <figure class="photo" style="max-width:300px;margin:0 auto 32px"><img src="images/oven-600.webp" width="600" height="750" alt="Anna Kate sliding a tray of peanut butter cookies into the oven" loading="lazy" decoding="async"></figure>
    <h2>Your first batch is three ingredients away</h2>
    <p>The free recipe guide has both recipes, the mistakes I made so you can skip them, and what the dough should look like at each step.</p>
    <div class="btn-row">
      <a href="{GUIDE}" class="btn" download>{DOWN}Download the Recipe Guide</a>
    </div>
  </div>
</section>

<section class="refs">
  <div class="wrap">
    <h2>Sources</h2>
    <ol>
      <li>Lavelle, F., et al. "Learning cooking skills at different ages: a cross-sectional study." <em>International Journal of Behavioral Nutrition and Physical Activity</em>, 2016.</li>
      <li>Systematic review of 23 randomized controlled trials of cooking interventions for children, 2024.</li>
    </ol>
  </div>
</section>

</main>

<footer>
  <div class="wrap">
    <p>{SITE_NAME} by {AUTHOR}. Made with just a few ingredients and a cup of ambition.</p>
  </div>
</footer>

<script>
(function(){{
  var els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return;}}
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}})}},{{rootMargin:'0px 0px -8% 0px'}});
  els.forEach(function(e){{io.observe(e)}});
}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    open("index.html", "w").write(page())
    open("robots.txt", "w").write("User-agent: *\nDisallow: /\n")
    open("favicon.svg", "w").write(MARK.replace(' class="mark"', ' xmlns="http://www.w3.org/2000/svg"'))
    print("wrote index.html")
