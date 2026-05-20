#!/usr/bin/env python3
"""Add data-i18n attributes to HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGE_TITLES = {
    "index.html": "page_title_home",
    "about-us.html": "page_title_about",
    "contact-us.html": "page_title_contact",
    "faq.html": "page_title_faq",
    "products.html": "page_title_products",
    "founder.html": "page_title_founder",
    "herbal-powders.html": "page_title_herbal",
    "spices.html": "page_title_spices",
    "jaggery.html": "page_title_jaggery",
}

REPLACEMENTS = [
    ('<div class="mt-2 fw-semibold">Pure from India. Trusted Worldwide.</div>',
     '<div class="mt-2 fw-semibold" data-i18n="footer_tagline">Pure from India. Trusted Worldwide.</div>'),
    ('<div class="mt-2 fw-semibold">Pure from India. Trusted Worldwide.</div>',
     '<div class="mt-2 fw-semibold" data-i18n="footer_tagline">Pure from India. Trusted Worldwide.</div>'),
    ('<div class="fw-bold text-white mb-3">Quick Links</div>',
     '<div class="fw-bold text-white mb-3" data-i18n="footer_quick_links">Quick Links</div>'),
    ('<div class="fw-bold text-white mb-3">Our Products</div>',
     '<div class="fw-bold text-white mb-3" data-i18n="footer_our_products">Our Products</div>'),
    ('<div class="fw-bold text-white mb-3">Contact Info</div>',
     '<div class="fw-bold text-white mb-3" data-i18n="footer_contact_info">Contact Info</div>'),
    ('<li class="mb-2"><a href="index.html">Home</a></li>',
     '<li class="mb-2"><a href="index.html" data-i18n="nav_home">Home</a></li>'),
    ('<li class="mb-2"><a href="about-us.html">About Us</a></li>',
     '<li class="mb-2"><a href="about-us.html" data-i18n="nav_about">About Us</a></li>'),
    ('<li class="mb-2"><a href="founder.html">Founder Profile</a></li>',
     '<li class="mb-2"><a href="founder.html" data-i18n="nav_founder">Founder Profile</a></li>'),
    ('<li class="mb-2"><a href="products.html">All Products</a></li>',
     '<li class="mb-2"><a href="products.html" data-i18n="nav_all_products">All Products</a></li>'),
    ('<li class="mb-2"><a href="faq.html">FAQs</a></li>',
     '<li class="mb-2"><a href="faq.html" data-i18n="nav_faq">FAQs</a></li>'),
    ('<li class="mb-2"><a href="contact-us.html">Contact Us</a></li>',
     '<li class="mb-2"><a href="contact-us.html" data-i18n="nav_contact">Contact Us</a></li>'),
    ('<li class="mb-2"><a href="herbal-powders.html">Herbal Powders</a></li>',
     '<li class="mb-2"><a href="herbal-powders.html" data-i18n="nav_herbal">Herbal Powders</a></li>'),
    ('<li class="mb-2"><a href="spices.html">Premium Spices</a></li>',
     '<li class="mb-2"><a href="spices.html" data-i18n="footer_premium_spices">Premium Spices</a></li>'),
    ('<li class="mb-2"><a href="jaggery.html">Jaggery</a></li>',
     '<li class="mb-2"><a href="jaggery.html" data-i18n="nav_jaggery">Jaggery</a></li>'),
    ('<li class="mb-0"><i class="fa-solid fa-clock me-2"></i> Mon–Sat: 9:00 AM – 6:00 PM IST</li>',
     '<li class="mb-0"><i class="fa-solid fa-clock me-2"></i> <span data-i18n="footer_hours">Mon–Sat: 9:00 AM – 6:00 PM IST</span></li>'),
    ('<li class="breadcrumb-item"><a href="index.html">Home</a></li>',
     '<li class="breadcrumb-item"><a href="index.html" data-i18n="breadcrumb_home">Home</a></li>'),
    ('<span class="visually-hidden">Previous</span>', '<span class="visually-hidden" data-i18n="carousel_prev">Previous</span>'),
    ('<span class="visually-hidden">Next</span>', '<span class="visually-hidden" data-i18n="carousel_next">Next</span>'),
    ('<button class="btn btn-filter active" type="button" data-filter="all">All</button>',
     '<button class="btn btn-filter active" type="button" data-filter="all" data-i18n="btn_filter_all">All</button>'),
    ('<button class="btn btn-filter" type="button" data-filter="all">All</button>',
     '<button class="btn btn-filter" type="button" data-filter="all" data-i18n="btn_filter_all">All</button>'),
    ('<button class="btn btn-filter" type="button" data-filter="herbal">Herbal Powders</button>',
     '<button class="btn btn-filter" type="button" data-filter="herbal" data-i18n="nav_herbal">Herbal Powders</button>'),
    ('<button class="btn btn-filter" type="button" data-filter="spices">Spices</button>',
     '<button class="btn btn-filter" type="button" data-filter="spices" data-i18n="nav_spices">Spices</button>'),
    ('<button class="btn btn-filter" type="button" data-filter="jaggery">Jaggery</button>',
     '<button class="btn btn-filter" type="button" data-filter="jaggery" data-i18n="nav_jaggery">Jaggery</button>'),
]

FOOTER_DESC_OLD = """<p class="mt-2 mb-3 footer-desc">
                TerrAgrox global exports premium herbal powders, spices, and natural sweeteners from Salem, Tamil Nadu — with export-ready packing and dependable documentation.
              </p>"""

FOOTER_DESC_NEW = """<p class="mt-2 mb-3 footer-desc" data-i18n="footer_desc">
                TerrAgrox global exports premium herbal powders, spices, and natural sweeteners from Salem, Tamil Nadu — with export-ready packing and dependable documentation.
              </p>"""


def tag_body(html_name: str, text: str) -> str:
    key = PAGE_TITLES.get(html_name)
    if not key:
        return text
    if "data-i18n-page-title" in text[:800]:
        return text
    return text.replace("<body>", f'<body data-i18n-page-title="{key}">', 1)


def main():
    for html in sorted(ROOT.glob("*.html")):
        t = html.read_text(encoding="utf-8")
        orig = t
        t = tag_body(html.name, t)
        if FOOTER_DESC_OLD in t:
            t = t.replace(FOOTER_DESC_OLD, FOOTER_DESC_NEW)
        for old, new in REPLACEMENTS:
            if old in t and new not in t:
                t = t.replace(old, new)
        if t != orig:
            html.write_text(t, encoding="utf-8")
            print("updated", html.name)


if __name__ == "__main__":
    main()
