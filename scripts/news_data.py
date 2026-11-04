"""Static configuration and seed/fallback content for the News page builder.

Nothing here hits the network. `scripts/build_news.py` imports this module for:
  - the hook-sentence pools used to wrap a NASA APOD explanation into one
    simple, exciting paragraph ("Today's Cosmic Wonder"),
  - the keyword -> organisation map used to attach a second "Reference" link
    (an agency / primary-source page) to every auto-pulled headline,
  - a hand-checked fallback dataset used whenever the live APIs cannot be
    reached (offline build, API outage, or a sandboxed CI run with no
    network) so the page never breaks and never goes blank.
"""

# ---------------------------------------------------------------------------
# Hook-sentence pools for the daily "Today's Cosmic Wonder" explainer.
# One opener + one closer is picked deterministically from the build date,
# so the same day always renders the same way (no needless diff churn) but
# the tone rotates from day to day.
# ---------------------------------------------------------------------------
HOOK_OPENERS = [
    "Hold onto your telescope:",
    "Here's something wild:",
    "Picture this:",
    "Get ready to have your mind bent a little:",
    "Today's reason to look up:",
    "You will not believe what the sky just did:",
    "Quick, before you scroll past this:",
    "Here's today's dose of cosmic wonder:",
]

HOOK_CLOSERS = [
    "And that is the magic of astronomy — the universe hands us something stranger and more beautiful than fiction, for free, every single night.",
    "Moments like this are exactly why astronomy never stops being fascinating: the sky is never just sitting there, it is always doing something.",
    "This is why we keep looking up — the universe never runs out of surprises, and anyone with their eyes open gets to see them.",
    "It is a small reminder that the cosmos is far stranger, and far more wonderful, than it looks from a backyard on a quiet night.",
    "Stories like this are proof that the universe is the greatest show there is — and tonight it is playing again, right above your head.",
    "That is the real secret of astronomy: you do not need a mission control room, just a clear sky and a reason to look up.",
]

# ---------------------------------------------------------------------------
# Keyword -> (reference url, reference label) used to give every headline a
# second, deeper "Reference" link (an agency or primary-source page) in
# addition to the "Read more" link to the actual article.
# Checked in order; first match wins.
# ---------------------------------------------------------------------------
REFERENCE_MAP = [
    (("webb", "jwst"), "https://science.nasa.gov/mission/webb/", "NASA Webb mission page"),
    (("hubble",), "https://science.nasa.gov/mission/hubble/", "NASA Hubble mission page"),
    (("artemis",), "https://www.nasa.gov/humans-in-space/artemis/", "NASA Artemis program"),
    (("starship", "super heavy", "booster"), "https://www.spacex.com/vehicles/starship/", "SpaceX Starship page"),
    (("falcon 9", "falcon9", "falcon heavy"), "https://www.spacex.com/vehicles/falcon-9/", "SpaceX Falcon 9 page"),
    (("starlink",), "https://www.spacex.com/constellation/", "SpaceX Starlink page"),
    (("spacex", "musk"), "https://www.spacex.com/", "SpaceX"),
    (("esa", "european space agency"), "https://www.esa.int/", "European Space Agency"),
    (("international space station", "iss"), "https://www.nasa.gov/mission/international-space-station/", "NASA ISS program"),
    (("black hole",), "https://science.nasa.gov/universe/black-holes/", "NASA: Black Holes explained"),
    (("exoplanet", "hot jupiter"), "https://science.nasa.gov/exoplanets/", "NASA Exoplanet Exploration"),
    (("galaxy", "galaxies"), "https://science.nasa.gov/universe/galaxies/", "NASA: Galaxies explained"),
    (("meteor", "comet"), "https://science.nasa.gov/solar-system/comets/", "NASA: Comets & meteors"),
    (("neutron star", "supernova"), "https://science.nasa.gov/universe/stars/", "NASA: Stars explained"),
    (("arxiv", "preprint", "peer-reviewed"), "https://arxiv.org/list/astro-ph/recent", "arXiv astro-ph listings"),
]
DEFAULT_REFERENCE = ("https://www.nasa.gov/news/", "NASA news")

# ---------------------------------------------------------------------------
# Fallback "Today's Cosmic Wonder" — used only if the live NASA APOD API call
# fails. Based on the real APOD for 3 November 2026, "Comet PanSTARRs and
# Rainbow Meteor" (credit: Eddy Metais / NASA).
# ---------------------------------------------------------------------------
FALLBACK_HERO = {
    "date": "3 November 2026",
    "title": "A comet and a rainbow meteor, caught in the same photo by accident",
    "paragraph": (
        "A sky-watcher in Hautacam, France pointed a camera at a faint, slow-drifting comet and "
        "caught something else entirely: a brilliant, multicoloured meteor slicing through the same "
        "frame. Here is the twist — they are not related at all. The meteor is a speck of rock, maybe "
        "the size of a grain of sand, burning up in our atmosphere in less than a second; the comet "
        "behind it is a giant dirty snowball from the edge of the Solar System that takes centuries to "
        "complete one orbit, and it only looks nearby because of where the camera happened to be "
        "pointed. The timing is no accident, though: this same week two meteor showers, the Southern "
        "and Northern Taurids, are peaking, with the famous Leonids blazing up in about two weeks."
    ),
    "image_url": None,
    "image_alt": "A comet with a long glowing tail beneath a star-filled sky, with a bright multicoloured meteor streaking past it.",
    "further_reading": {
        "url": "https://science.nasa.gov/image-article/apod-2026-november-3-comet-panstarrs-and-rainbow-meteor/",
        "label": "NASA Astronomy Picture of the Day, 3 Nov 2026",
    },
    "reference": {
        "url": "https://science.nasa.gov/solar-system/comets/",
        "label": "NASA: Comets & meteor showers explained",
    },
}

# ---------------------------------------------------------------------------
# Fallback headline list — a hand-checked, real, sourced set of recent
# astronomy / spaceflight stories. Used only if the live Spaceflight News
# API call fails; otherwise the live feed replaces this entirely.
# Buckets: "astro", "mission", "musk".
# ---------------------------------------------------------------------------
FALLBACK_ARTICLES = [
    {
        "bucket": "astro",
        "date": "27 October 2026",
        "title": "Webb finds a feeding black hole when the universe was 470 million years old",
        "summary": (
            "A faint red speck named MoM-BL-z10 hides a black hole of roughly 2 to 36 million suns, "
            "seen just 3% of the way back to the Big Bang. The team dug it out of public Webb archive "
            "data by spotting hydrogen gas smeared to 3,480 km/s — a merry-go-round too fast for "
            "anything but a black hole. The mass estimates disagree by a factor of ~17, and the team "
            "published both rather than picking a favourite, a nice lesson in honest error bars."
        ),
        "sources": [
            {"label": "Daily Galaxy", "url": "https://dailygalaxy.com/2026/10/jwst-feeding-black-hole-36-million-solar-masses/"},
        ],
    },
    {
        "bucket": "astro",
        "date": "25 October 2026",
        "title": "Three active black holes in a single galaxy, 12.5 billion light-years away",
        "summary": (
            "Galaxy J0148-4214 contains not one but three feeding supermassive black holes — two only "
            "620 light-years apart, destined to merge, plus a third 5,500 light-years out. The find "
            "suggests early galaxies may grow their monsters by merging them together, a fast track to "
            "the giants we see today."
        ),
        "sources": [
            {"label": "ScienceDaily / MPE", "url": "https://www.sciencedaily.com/releases/2026/10/261024222000.htm"},
        ],
    },
    {
        "bucket": "astro",
        "date": "21 October 2026",
        "title": "Webb detects heavy metals surrounding the Milky Way's black hole",
        "summary": (
            "Sagittarius A* is eating less than expected, and JWST just found a trove of supernova-forged "
            "metals in gas clouds near it, matching the composition of nearby stars. Why our galactic "
            "centre is so picky about its meals remains an open mystery; the metals may even relate to "
            "how Earth got its share of heavy elements."
        ),
        "sources": [
            {"label": "Live Science", "url": "https://www.livescience.com/space/astronomy/james-webb-telescope-discovers-surprising-trove-of-metals-around-the-milky-ways-supermassive-black-hole"},
        ],
    },
    {
        "bucket": "astro",
        "date": "16 October 2026",
        "title": "The atmosphere of WASP-17b is not round — it's being stretched",
        "summary": (
            "A new \"transmission strings\" technique uses JWST to map the true, lopsided shape of a hot "
            "Jupiter's atmosphere 1,300 light-years away: equatorial jets shovel heat from the permanent "
            "dayside to the nightside, inflating one limb. It's a first step toward weather maps of alien "
            "worlds."
        ),
        "sources": [
            {"label": "University of Bristol", "url": "https://www.bristol.ac.uk/news/2026/october/trailblazing-technique-uncovers-real-shape-of-scorching-hot-exoplanet-atmosphere.html"},
        ],
    },
    {
        "bucket": "astro",
        "date": "12 August 2026",
        "title": "A brand-new type of object: the \"black hole star\"",
        "summary": (
            "Webb's bright red dot MoM-BH*-1, seen 660 million years after the Big Bang, outshines its "
            "whole galaxy yet produces 100 billion times more energy than any star could. A MIT-led team "
            "argues it is a hybrid: a ~100,000-solar-mass black hole inside a star-sized cocoon of "
            "hydrogen, possibly the answer to the mysterious \"little red dots\" filling Webb's deep "
            "images."
        ),
        "sources": [
            {"label": "MIT News", "url": "https://news.mit.edu/2026/astronomers-discover-brand-new-type-astrophysical-object-black-hole-star-0812"},
        ],
    },
    {
        "bucket": "mission",
        "date": "1–11 April 2026 · recap",
        "title": "Artemis II: humans flew around the Moon — and came home safe",
        "summary": (
            "NASA's Artemis II carried astronauts Reid Wiseman, Victor Glover, Christina Koch and Jeremy "
            "Hansen on a free-return loop behind the lunar far side, the first crewed flight beyond low "
            "Earth orbit since Apollo 17 in 1972. On 6 April they passed 252,706 miles from Earth "
            "(breaking Apollo 13's record). Splashdown in the Pacific came on 11 April after 9 days. Next "
            "up: Artemis III's crewed landing attempt."
        ),
        "sources": [
            {"label": "NASA blog", "url": "https://www.nasa.gov/blogs/missions/2026/04/06/artemis-ii-flight-day-6-crew-ready-for-lunar-flyby/"},
            {"label": "ScienceDaily", "url": "https://www.sciencedaily.com/releases/2026/04/260402004721.htm"},
        ],
    },
    {
        "bucket": "mission",
        "date": "28 September 2026",
        "title": "Starship Flight 14: first Starship to reach orbit with a payload",
        "summary": (
            "The largest rocket ever built reached orbit and deployed 26 Starlink V3 satellites, Flight "
            "14's milestone, despite one upper-stage Raptor engine shutting down early during ascent. The "
            "setback became Flight 15's homework."
        ),
        "sources": [
            {"label": "List of Starship launches", "url": "https://en.wikipedia.org/wiki/List_of_Starship_launches"},
        ],
    },
    {
        "bucket": "mission",
        "date": "30 October 2026",
        "title": "Falcon 9 flies its 700th mission",
        "summary": (
            "Starlink 15-18 (27 satellites, Vandenberg) marked Falcon 9's 700th launch; booster B1093 "
            "landed after its 18th flight. Reusable boosters went from experiment to routine, even as "
            "SpaceX pivots its future to Starship."
        ),
        "sources": [
            {"label": "Technology.org", "url": "https://www.technology.org/2026/11/02/spacex-700th-falcon-9-launch-starlink-15-18-b1093/"},
        ],
    },
    {
        "bucket": "musk",
        "date": "Target: November 2026 · Flight 15",
        "title": "Starship Flight 15 will try to catch BOTH rocket stages at once",
        "summary": (
            "The plan: return the Super Heavy booster to the tower arms, as done three times before, and "
            "catch the Starship upper stage itself after re-entry, something never achieved. Musk puts "
            "first-try odds at 50 to 60% and calls a full recovery \"a profound technology milestone\". "
            "Success would unlock rapid reusability and feed the Artemis III lander schedule."
        ),
        "sources": [
            {"label": "Space.com", "url": "https://www.space.com/space-exploration/launches-spacecraft/spacex-will-attempt-1st-ever-double-starship-rocket-catch-on-next-test-launch-a-profound-technology-milestone-elon-musk-says"},
            {"label": "Interesting Engineering", "url": "https://interestingengineering.com/space/spacex-starship-flight-15-launch-date-objectives"},
        ],
    },
    {
        "bucket": "musk",
        "date": "30 October – 1 November 2026",
        "title": "\"Terrestrial compute will be peanuts compared to orbital compute\"",
        "summary": (
            "Musk is pushing a plan to move AI data centres to space: solar-powered satellite clusters, "
            "with orbital compute deployed per month exceeding Earth-based capacity around end-2028, he "
            "claims. The engineering questions — thermal control, radiation, launch cost per kilowatt — "
            "are excellent club-research material whether or not the timeline holds."
        ),
        "sources": [
            {"label": "Teslarati", "url": "https://www.teslarati.com/elon-musk-calls-earths-data-centers-peanuts-next-to-what-spacex-is-planning-in-orbit/"},
        ],
    },
]

ASTRO_KEYWORDS = (
    "galaxy", "galaxies", "black hole", "telescope", "webb", "jwst", "hubble", "star", "stars",
    "nebula", "exoplanet", "planet", "universe", "cosmic", "asteroid", "comet", "supernova",
    "neutron star", "dwarf", "moon", "solar system", "astronomers", "light-year", "observatory",
)
MISSION_KEYWORDS = (
    "launch", "rocket", "falcon", "starship", "booster", "artemis", "mission", "iss",
    "space station", "crew", "astronaut", "capsule", "orbital", "satellite", "rover", "lander",
)
MUSK_KEYWORDS = ("musk", "spacex", "starlink", "grok", "tesla")

# Keywords above are matched with word boundaries (see has_any_keyword in
# build_news.py), so short entries like "iss" or "star" cannot accidentally
# match inside unrelated words such as "Missing" or "started".
