#!/usr/bin/env python3
"""Add page-specific data-i18n attributes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, pairs: list[tuple[str, str]]) -> None:
    p = ROOT / path
    t = p.read_text(encoding="utf-8")
    orig = t
    for old, new in pairs:
        if old in t and new not in t:
            t = t.replace(old, new, 1)
    if t != orig:
        p.write_text(t, encoding="utf-8")
        print("patched", path)


INDEX = [
    (
        '<div class="section-label">Welcome to</div>\n            <h2 class="section-title section-title-lg mt-2">TerrAgrox global</h2>\n            <p class="muted mt-3">',
        '<div class="section-label" data-i18n="welcome_label">Welcome to</div>\n            <h2 class="section-title section-title-lg mt-2" data-i18n="welcome_h2">TerrAgrox global</h2>\n            <p class="muted mt-3" data-i18n="welcome_p1">',
    ),
    (
        'We specialize in herbal &amp; superfood powders, premium spices, and natural sweeteners—offering export-ready packing, inspection support, and dependable documentation for global buyers.\n            </p>',
        'We specialize in herbal &amp; superfood powders, premium spices, and natural sweeteners—offering export-ready packing, inspection support, and dependable documentation for global buyers.\n            </p>'.replace(
            "</p>",
            '</p>\n            <p class="muted mb-0" data-i18n="welcome_p2" style="display:none"></p>',
        ),
    ),
    ('<div class="label">Herbal Powders</div>', '<div class="label" data-i18n="nav_herbal">Herbal Powders</div>'),
    ('<div class="label">Herbal Powders</div>', '<div class="label" data-i18n="nav_herbal">Herbal Powders</div>'),
    ('<div class="label">Herbal Powders</div>', '<div class="label" data-i18n="nav_herbal">Herbal Powders</div>'),
    ('<div class="label">Spices</div>', '<div class="label" data-i18n="nav_spices">Spices</div>'),
    ('<div class="label">Jaggery</div>', '<div class="label" data-i18n="nav_jaggery">Jaggery</div>'),
    ('<div class="label">Product Categories</div>', '<div class="label" data-i18n="stat_cat">Product Categories</div>'),
    ('<div class="label">Export Products</div>', '<div class="label" data-i18n="stat_products">Export Products</div>'),
    ('<div class="label">Countries Served</div>', '<div class="label" data-i18n="stat_countries">Countries Served</div>'),
    ('<div class="label">Quality Assured</div>', '<div class="label" data-i18n="stat_quality">Quality Assured</div>'),
    ('<div class="section-label">Our Reach</div>', '<div class="section-label" data-i18n="reach_label">Our Reach</div>'),
    (
        '<h2 class="section-title section-title-lg mt-2">From Salem, India to The Entire World</h2>',
        '<h2 class="section-title section-title-lg mt-2" data-i18n="reach_h2">From Salem, India to The Entire World</h2>',
    ),
    (
        '<p class="muted mt-3 mb-3">\n              TerrAgrox global connects international buyers',
        '<p class="muted mt-3 mb-3" data-i18n="reach_p">\n              TerrAgrox global connects international buyers',
    ),
    (
        '<li><i class="fa-solid fa-circle-check"></i> Direct farm sourcing from Tamil Nadu</li>',
        '<li><i class="fa-solid fa-circle-check"></i> <span data-i18n="reach_li1">Direct farm sourcing from Tamil Nadu</span></li>',
    ),
    (
        '<li><i class="fa-solid fa-circle-check"></i> Export-grade packaging and certification</li>',
        '<li><i class="fa-solid fa-circle-check"></i> <span data-i18n="reach_li2">Export-grade packaging and certification</span></li>',
    ),
    (
        '<li><i class="fa-solid fa-circle-check"></i> Timely delivery with full documentation</li>',
        '<li><i class="fa-solid fa-circle-check"></i> <span data-i18n="reach_li3">Timely delivery with full documentation</span></li>',
    ),
    (
        '<li><i class="fa-solid fa-circle-check"></i> Dedicated support from inquiry to shipment</li>',
        '<li><i class="fa-solid fa-circle-check"></i> <span data-i18n="reach_li4">Dedicated support from inquiry to shipment</span></li>',
    ),
    ('<div class="section-label">TerrAgrox global</div>\n          <h2 class="section-title mt-2">Our Export Products</h2>',
     '<div class="section-label" data-i18n="products_section_label">TerrAgrox global</div>\n          <h2 class="section-title mt-2" data-i18n="products_section_h2">Our Export Products</h2>'),
    (
        '<p class="muted mb-0">\n            Premium Indian agricultural products',
        '<p class="muted mb-0" data-i18n="products_section_p">\n            Premium Indian agricultural products',
    ),
    ('<span class="product-cat-badge">Herbal</span>', '<span class="product-cat-badge" data-i18n="badge_herbal">Herbal</span>'),
    ('<span class="product-cat-badge">Spices</span>', '<span class="product-cat-badge" data-i18n="badge_spices">Spices</span>'),
    ('<span class="product-cat-badge">Jaggery</span>', '<span class="product-cat-badge" data-i18n="badge_jaggery">Jaggery</span>'),
    ('<span class="product-best-badge">Best Seller</span>', '<span class="product-best-badge" data-i18n="badge_best_seller">Best Seller</span>'),
    ('<h5>Herbal &amp; Superfood Powders</h5>', '<h5 data-i18n="prod_herbal_title">Herbal &amp; Superfood Powders</h5>'),
    (
        '<p class="muted product-card-desc">Moringa, Beetroot, Ginger, Onion, Banana, Neem — 6 natural powders</p>',
        '<p class="muted product-card-desc" data-i18n="prod_herbal_desc">Moringa, Beetroot, Ginger, Onion, Banana, Neem — 6 natural powders</p>',
    ),
    ('<h5>Premium Spices</h5>', '<h5 data-i18n="prod_spices_title">Premium Spices</h5>'),
    (
        '<p class="muted product-card-desc">Turmeric, Chili, Black Pepper, Cardamom and 6 more export-grade spices</p>',
        '<p class="muted product-card-desc" data-i18n="prod_spices_desc">Turmeric, Chili, Black Pepper, Cardamom and 6 more export-grade spices</p>',
    ),
    ('<h5>Jaggery</h5>', '<h5 data-i18n="prod_jaggery_title">Jaggery</h5>'),
    (
        '<p class="muted product-card-desc">Jaggery Balls, Powder, Palmyra Jaggery, Palm Sugar Candy — pure and unrefined</p>',
        '<p class="muted product-card-desc" data-i18n="prod_jaggery_desc">Jaggery Balls, Powder, Palmyra Jaggery, Palm Sugar Candy — pure and unrefined</p>',
    ),
    ('<h5>Farm-Direct Sourcing</h5>', '<h5 data-i18n="why1_h">Farm-Direct Sourcing</h5>'),
    (
        '<p>We source directly from verified Tamil Nadu farms — no middlemen, ensuring freshness and fair pricing for every buyer.</p>',
        '<p data-i18n="why1_p">We source directly from verified Tamil Nadu farms — no middlemen, ensuring freshness and fair pricing for every buyer.</p>',
    ),
    ('<h5>Strict Quality Control</h5>', '<h5 data-i18n="why2_h">Strict Quality Control</h5>'),
    (
        '<p>Every batch undergoes pre-shipment inspection. We follow international quality norms from harvest to the final packed consignment.</p>',
        '<p data-i18n="why2_p">Every batch undergoes pre-shipment inspection. We follow international quality norms from harvest to the final packed consignment.</p>',
    ),
    ('<h5>Custom Export Packaging</h5>', '<h5 data-i18n="why3_h">Custom Export Packaging</h5>'),
    (
        '<p>Export-grade cartons, vacuum-sealed pouches, and custom labeling — packaging tailored to your market and buyer requirements.</p>',
        '<p data-i18n="why3_p">Export-grade cartons, vacuum-sealed pouches, and custom labeling — packaging tailored to your market and buyer requirements.</p>',
    ),
    ('<h5>Complete Documentation</h5>', '<h5 data-i18n="why4_h">Complete Documentation</h5>'),
    (
        '<p>We handle all export documentation — phytosanitary certificates, COA, invoices, packing lists — for smooth customs clearance worldwide.</p>',
        '<p data-i18n="why4_p">We handle all export documentation — phytosanitary certificates, COA, invoices, packing lists — for smooth customs clearance worldwide.</p>',
    ),
    ('<h5>On-Time Global Delivery</h5>', '<h5 data-i18n="why5_h">On-Time Global Delivery</h5>'),
    (
        '<p>Reliable logistics partnerships ensure your shipment reaches its destination on schedule, every time.</p>',
        '<p data-i18n="why5_p">Reliable logistics partnerships ensure your shipment reaches its destination on schedule, every time.</p>',
    ),
    ('<h5>Dedicated Export Support</h5>', '<h5 data-i18n="why6_h">Dedicated Export Support</h5>'),
    (
        '<p>A responsive team available Mon–Sat 9AM–6PM IST to handle your queries, samples, and orders via WhatsApp or email.</p>',
        '<p data-i18n="why6_p">A responsive team available Mon–Sat 9AM–6PM IST to handle your queries, samples, and orders via WhatsApp or email.</p>',
    ),
    ('<h5 class="fw-bold">Send Enquiry</h5>', '<h5 class="fw-bold" data-i18n="exp1_h">Send Enquiry</h5>'),
    (
        '<p class="muted small mb-0">WhatsApp or email us with your product, quantity, and destination country.</p>',
        '<p class="muted small mb-0" data-i18n="exp1_p">WhatsApp or email us with your product, quantity, and destination country.</p>',
    ),
    ('<h5 class="fw-bold">Sample &amp; Approval</h5>', '<h5 class="fw-bold" data-i18n="exp2_h">Sample &amp; Approval</h5>'),
    (
        '<p class="muted small mb-0">We send product samples for your quality evaluation and approval before bulk order.</p>',
        '<p class="muted small mb-0" data-i18n="exp2_p">We send product samples for your quality evaluation and approval before bulk order.</p>',
    ),
    ('<h5 class="fw-bold">Packing &amp; Documentation</h5>', '<h5 class="fw-bold" data-i18n="exp3_h">Packing &amp; Documentation</h5>'),
    (
        '<p class="muted small mb-0">Products are packed to your specification with all export documents prepared — COA, phytosanitary certificate, invoice, packing list.</p>',
        '<p class="muted small mb-0" data-i18n="exp3_p">Products are packed to your specification with all export documents prepared — COA, phytosanitary certificate, invoice, packing list.</p>',
    ),
    ('<h5 class="fw-bold">Shipment &amp; Delivery</h5>', '<h5 class="fw-bold" data-i18n="exp4_h">Shipment &amp; Delivery</h5>'),
    (
        '<p class="muted small mb-0">Your order is dispatched via sea or air freight with full tracking until it reaches your destination port.</p>',
        '<p class="muted small mb-0" data-i18n="exp4_p">Your order is dispatched via sea or air freight with full tracking until it reaches your destination port.</p>',
    ),
    (
        '<p class="review-text">\n                      TerrAgrox global exceeded our expectations',
        '<p class="review-text" data-i18n="test1_text">\n                      TerrAgrox global exceeded our expectations',
    ),
    (
        '<p class="review-text">\n                      We import turmeric powder',
        '<p class="review-text" data-i18n="test2_text">\n                      We import turmeric powder',
    ),
    (
        '<p class="review-text">\n                      The Palmyra Jaggery we sourced',
        '<p class="review-text" data-i18n="test3_text">\n                      The Palmyra Jaggery we sourced',
    ),
    (
        '<p class="review-text">\n                      Excellent supplier for organic Indian spices.',
        '<p class="review-text" data-i18n="test4_text">\n                      Excellent supplier for organic Indian spices.',
    ),
    (
        '<p class="review-text">\n                      TerrAgrox global is our go-to supplier',
        '<p class="review-text" data-i18n="test5_text">\n                      TerrAgrox global is our go-to supplier',
    ),
    (
        '<p class="text-center muted mb-4 mx-auto" style="max-width:640px;" data-aos="fade-up">\n          Quick answers for international buyers.',
        '<p class="text-center muted mb-4 mx-auto" style="max-width:640px;" data-aos="fade-up" data-i18n="faq_home_intro">\n          Quick answers for international buyers.',
    ),
    (
        '<a class="btn btn-accent" href="faq.html"><i class="fa-solid fa-circle-question me-2"></i>View All FAQs</a>',
        '<a class="btn btn-accent" href="faq.html"><i class="fa-solid fa-circle-question me-2"></i><span data-i18n="btn_view_all_faq">View All FAQs</span></a>',
    ),
]

ABOUT = [
    ('<h1>About Us</h1>', '<h1 data-i18n="about_hero_h1">About Us</h1>'),
    ('<li class="breadcrumb-item active" aria-current="page">About Us</li>', '<li class="breadcrumb-item active" aria-current="page" data-i18n="about_hero_crumb">About Us</li>'),
    ('<div class="section-label">Welcome to</div>', '<div class="section-label" data-i18n="about_welcome_label">Welcome to</div>'),
    ('<div class="section-label">Welcome to</div>', '<div class="section-label" data-i18n="about_welcome_label">Welcome to</div>'),
    ('<h2 class="section-title section-title-lg mt-2">TerrAgrox global</h2>\n\n            <p class="muted mt-3">', '<h2 class="section-title section-title-lg mt-2" data-i18n="about_welcome_h2">TerrAgrox global</h2>\n\n            <p class="muted mt-3" data-i18n="about_p1">'),
    ('<p class="muted">\n              We specialize in', '<p class="muted" data-i18n="about_p2">\n              We specialize in'),
    ('<p class="muted mb-0">\n              With a strong commitment', '<p class="muted mb-0" data-i18n="about_p3">\n              With a strong commitment'),
    ('<h3 class="h4 text-white mb-3">Our Mission</h3>', '<h3 class="h4 text-white mb-3" data-i18n="about_mission_h">Our Mission</h3>'),
    ('<p class="mb-0">Deliver premium Indian products', '<p class="mb-0" data-i18n="about_mission_p">Deliver premium Indian products'),
    ('<h3 class="h4 text-white mb-3">Our Vision</h3>', '<h3 class="h4 text-white mb-3" data-i18n="about_vision_h">Our Vision</h3>'),
    ('<p class="mb-0">Become a trusted global export partner', '<p class="mb-0" data-i18n="about_vision_p">Become a trusted global export partner'),
    ('<div class="section-label">Who We Are</div>', '<div class="section-label" data-i18n="about_values_label">Who We Are</div>'),
    ('<h2 class="section-title section-title-lg mt-2">Core Values</h2>', '<h2 class="section-title section-title-lg mt-2" data-i18n="about_values_h2">Core Values</h2>'),
    ('<h5 class="mb-2">Integrity</h5>', '<h5 class="mb-2" data-i18n="about_val1_h">Integrity</h5>'),
    ('<p class="muted small mb-0">Transparent dealings', '<p class="muted small mb-0" data-i18n="about_val1_p">Transparent dealings'),
    ('<h5 class="mb-2">Quality</h5>', '<h5 class="mb-2" data-i18n="about_val2_h">Quality</h5>'),
    ('<p class="muted small mb-0">Rigorous checks', '<p class="muted small mb-0" data-i18n="about_val2_p">Rigorous checks'),
    ('<h5 class="mb-2">Partnership</h5>', '<h5 class="mb-2" data-i18n="about_val3_h">Partnership</h5>'),
    ('<p class="muted small mb-0">Long-term relationships', '<p class="muted small mb-0" data-i18n="about_val3_p">Long-term relationships'),
    ('<h5 class="mb-2">Growth</h5>', '<h5 class="mb-2" data-i18n="about_val4_h">Growth</h5>'),
    ('<p class="muted small mb-0">Serving buyers across', '<p class="muted small mb-0" data-i18n="about_val4_p">Serving buyers across'),
]

CONTACT = [
    ('<h1>Contact Us</h1>', '<h1 data-i18n="contact_hero_h1">Contact Us</h1>'),
    ('<li class="breadcrumb-item active" aria-current="page">Contact Us</li>', '<li class="breadcrumb-item active" aria-current="page" data-i18n="contact_hero_crumb">Contact Us</li>'),
    ('<h6>ADDRESS</h6>', '<h6 data-i18n="contact_address_h">ADDRESS</h6>'),
    ('<h6>PHONE</h6>', '<h6 data-i18n="contact_phone_h">PHONE</h6>'),
    ('<h6>EMAIL</h6>', '<h6 data-i18n="contact_email_h">EMAIL</h6>'),
    ('<div class="section-label">We’re Here to Help</div>', '<div class="section-label" data-i18n="contact_form_label">We’re Here to Help</div>'),
    ('<h2 class="contact-form-title mt-1">Let’s Start a Conversation</h2>', '<h2 class="contact-form-title mt-1" data-i18n="contact_form_h2">Let’s Start a Conversation</h2>'),
    ('<label for="fullName">Name *</label>', '<label for="fullName" data-i18n="form_name">Name *</label>'),
    ('<label for="email">Email *</label>', '<label for="email" data-i18n="form_email">Email *</label>'),
    ('<label for="phone">Phone *</label>', '<label for="phone" data-i18n="form_phone">Phone *</label>'),
    ('<label for="message">Message *</label>', '<label for="message" data-i18n="form_message">Message *</label>'),
    ('<div class="invalid-feedback">Please enter your name.</div>', '<div class="invalid-feedback" data-i18n="form_err_name">Please enter your name.</div>'),
    ('<div class="invalid-feedback">Please enter a valid email.</div>', '<div class="invalid-feedback" data-i18n="form_err_email">Please enter a valid email.</div>'),
    ('<div class="invalid-feedback">Please enter your phone number.</div>', '<div class="invalid-feedback" data-i18n="form_err_phone">Please enter your phone number.</div>'),
    ('<div class="invalid-feedback">Please enter your message.</div>', '<div class="invalid-feedback" data-i18n="form_err_message">Please enter your message.</div>'),
    ('<button class="btn-submit" type="submit">Submit</button>', '<button class="btn-submit" type="submit" data-i18n="btn_submit">Submit</button>'),
    (
        '<p class="text-center muted mb-4" data-aos="fade-up">\n          Common questions before you reach out.',
        '<p class="text-center muted mb-4" data-aos="fade-up" data-i18n="faq_contact_intro">\n          Common questions before you reach out.',
    ),
    ('<a class="btn btn-accent" href="faq.html">View All FAQs</a>', '<a class="btn btn-accent" href="faq.html" data-i18n="btn_view_all_faq">View All FAQs</a>'),
]

FAQ_PAGE = [
    (
        '<p class="text-center muted mb-4 mx-auto" style="max-width:720px;" data-aos="fade-up">\n          Answers to common questions',
        '<p class="text-center muted mb-4 mx-auto" style="max-width:720px;" data-aos="fade-up" data-i18n="faq_page_intro">\n          Answers to common questions',
    ),
]


def main():
    patch("index.html", INDEX)
    patch("about-us.html", ABOUT)
    patch("contact-us.html", CONTACT)
    patch("faq.html", FAQ_PAGE)
    for f in ROOT.glob("*.html"):
        t = f.read_text(encoding="utf-8")
        if "div" in t:
            f.write_text(t.replace("div", "div").replace("<div", "<div").replace("</div>", "</div>"), encoding="utf-8")


if __name__ == "__main__":
    main()
