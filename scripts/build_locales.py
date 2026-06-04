#!/usr/bin/env python3
"""Build assets/locales/*.json from embedded translation tables."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ROOT / "assets" / "locales"

# Master English strings — single source of truth
EN = {
    "nav_home": "Home",
    "nav_about": "About",
    "nav_products": "Products",
    "nav_faq": "FAQs",
    "nav_services": "Services",
    "nav_contact": "Contact Us",
    "nav_whatsapp": "WhatsApp Us",
    "nav_company": "Company",
    "nav_founder": "Founder Profile",
    "nav_all_products": "All Products",
    "nav_herbal": "Herbal Powders",
    "nav_spices": "Spices",
    "nav_jaggery": "Jaggery",
    "lang_en": "English",
    "lang_ar": "Arabic",
    "lang_zh": "Chinese",
    "lang_fr": "French",
    "lang_de": "German",
    "lang_es": "Spanish",
    "lang_ms": "Malay",
    "lang_hi": "Hindi",
    "lang_ja": "Japanese",
    "lang_pt": "Portuguese",
    "breadcrumb_home": "Home",
    "btn_submit": "Submit",
    "btn_view_all_faq": "View All FAQs",
    "btn_enquire_wa": "Enquire on WhatsApp",
    "btn_filter_all": "All",
    "carousel_prev": "Previous",
    "carousel_next": "Next",
    "footer_tagline": "Pure from India. Trusted Worldwide.",
    "footer_desc": "TerrAgrox global exports premium herbal powders, spices, and natural sweeteners from Salem, Tamil Nadu — with export-ready packing and dependable documentation.",
    "footer_quick_links": "Quick Links",
    "footer_our_products": "Our Products",
    "footer_contact_info": "Contact Info",
    "footer_about": "About Us",
    "footer_premium_spices": "Premium Spices",
    "footer_hours": "Mon–Sat: 9:00 AM – 6:00 PM IST",
    "footer_copyright": "© {year} TerrAgrox global. All rights reserved.",
    "page_title_home": "TerrAgrox global | Home",
    "page_title_about": "About Us | TerrAgrox global",
    "page_title_services": "Services | TerrAgrox global",
    "page_title_contact": "Contact Us | TerrAgrox global",
    "page_title_faq": "FAQs | TerrAgrox global",
    "page_title_products": "Products | TerrAgrox global",
    "page_title_founder": "Founder | TerrAgrox global",
    "founder_name": "Srikanth C",
    "founder_title": "CEO & Export Director",
    "founder_company": "TerrAgrox global",
    "page_title_herbal": "Herbal Powders | TerrAgrox global",
    "page_title_spices": "Spices | TerrAgrox global",
    "page_title_jaggery": "Jaggery | TerrAgrox global",
    "hero1_label": "India's Trusted Agricultural Exporter",
    "hero1_h1": "From Farm to the World — Premium Quality, Every Shipment",
    "hero1_p": "TerrAgrox global connects international buyers with the finest Indian herbal powders, spices, and natural sweeteners. Export-ready. Certified. Reliable.",
    "hero1_btn1": "Explore Our Products",
    "hero1_btn2": "WhatsApp Us",
    "hero2_label": "Bold · Aromatic · Export Grade",
    "hero2_h1": "Premium Indian Spices Trusted by Global Buyers",
    "hero2_p": "From Turmeric and Black Pepper to Cardamom and Tamarind — sourced from the finest Indian farms and packed to international standards.",
    "hero2_btn1": "View Spices",
    "hero2_btn2": "Request a Quote",
    "hero3_label": "Traditional · Unrefined · 100% Natural",
    "hero3_h1": "Authentic Indian Jaggery — Pure, Natural, Export Grade",
    "hero3_p": "Palmyra Jaggery, Jaggery Balls, and Palm Sugar Candy from Tamil Nadu's finest farms. Chemical-free and packed for global markets.",
    "hero3_btn1": "View Jaggery",
    "hero3_btn2": "WhatsApp Us",
    "welcome_label": "Welcome to",
    "welcome_h2": "TerrAgrox global",
    "welcome_p1": "At <strong>TerrAgrox global</strong>, we build seamless export connections, delivering premium Indian agricultural products with integrity, precision, and trust. Headquartered in <strong>Salem, Tamil Nadu (India)</strong>, our foundation is built on the values of <strong>reliability</strong>, <strong>transparency</strong>, and <strong>long-term partnerships</strong>.",
    "welcome_p2": "We specialize in herbal & superfood powders, premium spices, and natural sweeteners—offering export-ready packing, inspection support, and dependable documentation for global buyers.",
    "home_cat_label": "Our Product",
    "home_cat_h2": "Categories",
    "stat_cat": "Product Categories",
    "stat_products": "Export Products",
    "stat_countries": "Countries Served",
    "stat_quality": "Quality Assured",
    "reach_label": "Our Reach",
    "reach_h2": "From Salem, India to The Entire World",
    "reach_p": "TerrAgrox global connects international buyers with premium Indian agricultural products. Based in Salem, Tamil Nadu, we source directly from trusted farms and deliver to buyers across Asia, Europe, the Middle East, and beyond. Transparency, quality, and reliability define every shipment.",
    "reach_li1": "Direct farm sourcing from Tamil Nadu",
    "reach_li2": "Export-grade packaging and certification",
    "reach_li3": "Timely delivery with full documentation",
    "reach_li4": "Dedicated support from inquiry to shipment",
    "markets_h2": "Global Footprint: Our Export Markets",
    "markets_p": "From our roots in Tamil Nadu to the storefronts of global metropolises, we deliver premium organic products to the world's most discerning markets with dedicated logistics and quality assurance.",
    "market_us_h": "United States",
    "market_us_p": "Turmeric, Moringa, Premium Spices",
    "market_uk_h": "United Kingdom",
    "market_uk_p": "Moringa Superfoods, Turmeric",
    "market_uae_h": "UAE",
    "market_uae_p": "Luxury Spices, Turmeric Exports",
    "market_au_h": "Australia",
    "market_au_p": "Superfood Powders, Herbs",
    "market_de_h": "Germany",
    "market_de_p": "Organic Spices & Botanical Herbs",
    "market_ca_h": "Canada",
    "market_ca_p": "Bulk Spices & Organic Herbs",
    "market_fr_h": "France",
    "market_fr_p": "Botanical Ingredients, Moringa",
    "market_nl_h": "Netherlands",
    "market_nl_p": "Global Distribution Spices",
    "journey_h2": "The Global Export Journey",
    "journey_p": "From our roots in Salem to destinations across the globe, we ensure a seamless and transparent shipping process for every partner.",
    "journey1_h": "Inquiry & Requirements",
    "journey1_p": "Defining your global needs",
    "journey2_h": "Quote & Sample",
    "journey2_p": "Lab-tested quality verification",
    "journey3_h": "Order Confirmed",
    "journey3_p": "Contracting & documentation",
    "journey4_h": "Quality Check",
    "journey4_p": "Rigorous batch inspections",
    "journey5_h": "Shipment & Docs",
    "journey5_p": "Secure worldwide delivery",
    "products_section_label": "TerrAgrox global",
    "products_section_h2": "Our Export Products",
    "products_section_p": "Premium Indian agricultural products — herbal powders, aromatic spices, and natural jaggery sourced with care for global markets.",
    "prod_herbal_title": "Herbal & Superfood Powders",
    "prod_herbal_desc": "Moringa, Beetroot, Ginger, Onion, Banana, Neem — 6 natural powders",
    "prod_spices_title": "Premium Spices",
    "prod_spices_desc": "Turmeric, Chili, Black Pepper, Cardamom and 6 more export-grade spices",
    "prod_jaggery_title": "Jaggery",
    "prod_jaggery_desc": "Jaggery Balls, Powder, Palmyra Jaggery, Palm Sugar Candy — pure and unrefined",
    "badge_herbal": "Herbal",
    "badge_spices": "Spices",
    "badge_jaggery": "Jaggery",
    "badge_best_seller": "Best Seller",
    "cert_label": "TerrAgrox global",
    "cert_h3": "Our Certifications & Registrations",
    "cert_p": "Trusted by global buyers backed by internationally recognized certifications.",
    "why_label": "Our Advantage",
    "why_h2": "Why Choose TerrAgrox global?",
    "why_p": "We go beyond just exporting — we build lasting partnerships built on quality, trust, and transparency.",
    "why1_h": "Farm-Direct Sourcing",
    "why1_p": "We source directly from verified Tamil Nadu farms — no middlemen, ensuring freshness and fair pricing for every buyer.",
    "why2_h": "Strict Quality Control",
    "why2_p": "Every batch undergoes pre-shipment inspection. We follow international quality norms from harvest to the final packed consignment.",
    "why3_h": "Custom Export Packaging",
    "why3_p": "Export-grade cartons, vacuum-sealed pouches, and custom labeling — packaging tailored to your market and buyer requirements.",
    "why4_h": "Complete Documentation",
    "why4_p": "We handle all export documentation — phytosanitary certificates, COA, invoices, packing lists — for smooth customs clearance worldwide.",
    "why5_h": "On-Time Global Delivery",
    "why5_p": "Reliable logistics partnerships ensure your shipment reaches its destination on schedule, every time.",
    "why6_h": "Dedicated Export Support",
    "why6_p": "A responsive team available Mon–Sat 9AM–6PM IST to handle your queries, samples, and orders via WhatsApp or email.",
    "exp_label": "How We Work",
    "exp_h2": "Our Export Process",
    "exp_p": "Simple, transparent, and reliable — from your first inquiry to delivery at your port.",
    "exp1_h": "Send Enquiry",
    "exp1_p": "WhatsApp or email us with your product, quantity, and destination country.",
    "exp2_h": "Sample & Approval",
    "exp2_p": "We send product samples for your quality evaluation and approval before bulk order.",
    "exp3_h": "Packing & Documentation",
    "exp3_p": "Products are packed to your specification with all export documents prepared — COA, phytosanitary certificate, invoice, packing list.",
    "exp4_h": "Shipment & Delivery",
    "exp4_p": "Your order is dispatched via sea or air freight with full tracking until it reaches your destination port.",
    "cta_h3": "Ready to Source Premium Indian Products?",
    "cta_p": "Partner with TerrAgrox global for consistent quality, export-ready packaging, and seamless worldwide shipping.",
    "cta_btn_wa": "WhatsApp Us Now",
    "cta_btn_mail": "Send Enquiry",
    "test_label": "Testimonials",
    "test_h2": "What Our Clients Say",
    "test1_text": "TerrAgrox global exceeded our expectations with their moringa powder quality. Consistent grade, excellent packaging, and on-time delivery every single time. A reliable partner for our health food brand.",
    "test2_text": "We import turmeric powder and dried chili from TerrAgrox regularly. The quality is superb and the team is extremely responsive. Their export documentation is always perfect.",
    "test3_text": "The Palmyra Jaggery we sourced from TerrAgrox global is authentic and our customers love it. Professional team with transparent processes. Highly recommended.",
    "test4_text": "Excellent supplier for organic Indian spices. Their beetroot powder and ginger powder quality is outstanding. The export team is knowledgeable and very easy to work with.",
    "test5_text": "TerrAgrox global is our go-to supplier for natural sweeteners. Jaggery Balls and Palm Sugar Candy arrive perfectly packed. Great quality, fair pricing, and dependable service.",
    "faq_label": "FAQs",
    "faq_h2": "Frequently Asked Questions",
    "faq_home_intro": "Quick answers for international buyers. Need more detail? See our full FAQ page.",
    "faq_contact_intro": "Common questions before you reach out. Browse quick answers below or see the full list.",
    "faq_page_intro": "Answers to common questions from international buyers about our products, MOQ, shipping, and export process.",
    "faq_hero_h1": "Frequently Asked Questions",
    "faq_hero_crumb": "FAQs",
    "faq_page_intro_html": "Answers to common questions about our export products, orders, documentation, and pricing. Still need help? <a href=\"contact-us.html\">Contact us</a> or <a href=\"https://wa.me/917695929907\" target=\"_blank\" rel=\"noopener noreferrer\">WhatsApp</a> our team.",
    "services_hero_h1": "Our Services",
    "services_hero_crumb": "Services",
    "services_intro_label": "What We Offer",
    "services_intro_h2": "End-to-End Export Solutions",
    "services_intro_p": "From farm-gate sourcing in Tamil Nadu to delivery at your port, TerrAgrox global provides complete export support for international buyers of herbal powders, spices, and natural sweeteners.",
    "svc1_h": "Product Sourcing",
    "svc1_p": "Direct procurement from verified farms and processors across Tamil Nadu and India for consistent quality and traceability.",
    "svc2_h": "Quality Control & Testing",
    "svc2_p": "Batch-wise inspection, moisture and purity checks, and lab reports (COA) available on request for export compliance.",
    "svc3_h": "Export Packaging",
    "svc3_p": "Vacuum bags, cartons, and custom packing to your specifications — hygienic, durable, and ready for international shipment.",
    "svc4_h": "Documentation & Compliance",
    "svc4_p": "Commercial invoices, packing lists, certificates of origin, phytosanitary certificates, and COA prepared for smooth customs clearance.",
    "svc5_h": "Logistics & Shipping",
    "svc5_p": "Sea and air freight coordination with reliable partners — FOB, CIF, and other terms arranged to suit your import needs.",
    "svc6_h": "Private Label & Custom Orders",
    "svc6_p": "Custom blends, branding, and labeling for distributors and retailers — MOQ and specifications discussed per product.",
    "services_why_label": "Why Work With Us",
    "services_why_h2": "Your Partner From Inquiry to Delivery",
    "services_why_p": "We combine deep local sourcing knowledge with export-grade processes so you receive premium Indian agricultural products without the complexity of managing multiple vendors.",
    "services_why_li1": "Dedicated export team — Mon–Sat, 9 AM–6 PM IST",
    "services_why_li2": "Samples available before bulk orders",
    "services_why_li3": "Transparent pricing and timely communication",
    "services_why_li4": "Shipments to the USA, UK, UAE, EU, Australia & more",
    "services_cta_btn": "Request a Quote",
    "services_cta_h3": "Ready to Start Your Export Order?",
    "services_cta_p": "Tell us your product, quantity, and destination — we will respond with specifications, MOQ, and a competitive quote within 24–48 hours.",
    "about_hero_h1": "About Us",
    "about_hero_crumb": "About Us",
    "about_welcome_label": "Welcome to",
    "about_welcome_h2": "TerrAgrox global",
    "about_p1": "At <strong>TerrAgrox global</strong>, we build seamless export connections, delivering premium Indian agricultural products with integrity, precision, and trust. Headquartered in <strong>Salem, Tamil Nadu (India)</strong>, our foundation is built on the values of <strong>reliability</strong>, <strong>transparency</strong>, and <strong>long-term partnerships</strong>.",
    "about_p2": "We specialize in <strong>export solutions</strong> across key sectors including herbal &amp; superfood powders, premium spices, and natural sweeteners. Our mission is to <strong>showcase India's rich heritage to the world</strong> with consistent quality and export-ready packaging.",
    "about_p3": "With a strong commitment to ethical trade, uncompromising quality, and timely delivery, we ensure complete satisfaction—whether you're a small retailer or a large-scale distributor. When you choose us, you gain not just a supplier, but a dedicated partner for your global trade journey.",
    "about_mission_h": "Our Mission",
    "about_mission_p": "To deliver premium Indian agricultural products to global markets with uncompromising authenticity, export-grade quality, and dependable service—building trust in every shipment we send.",
    "about_mission_li1": "Source directly from verified farms and processors across Tamil Nadu and India",
    "about_mission_li2": "Supply herbal powders, spices, and natural sweeteners that meet international buyer standards",
    "about_mission_li3": "Provide transparent pricing, timely communication, and complete export documentation",
    "about_mission_li4": "Support importers, distributors, and brands with samples, custom packing, and long-term supply",
    "about_vision_h": "Our Vision",
    "about_vision_p": "To become a globally trusted export partner from India—recognized for integrity, sustainable sourcing, and relationships that grow stronger with every order.",
    "about_vision_li1": "Expand TerrAgrox global's reach across Asia, Europe, the Middle East, and new markets worldwide",
    "about_vision_li2": "Set benchmarks for quality, food safety, and ethical trade in Indian agri-exports",
    "about_vision_li3": "Empower farmers and local communities through fair, consistent export demand",
    "about_vision_li4": "Be the first choice for buyers who value reliability, honesty, and partnership over short-term deals",
    "about_values_label": "Who We Are",
    "about_values_h2": "Core Values",
    "about_val1_h": "Integrity",
    "about_val1_p": "Transparent dealings and honest communication with every buyer.",
    "about_val2_h": "Quality",
    "about_val2_p": "Rigorous checks from sourcing to packing for export-grade consistency.",
    "about_val3_h": "Partnership",
    "about_val3_p": "Long-term relationships built on reliability and responsive support.",
    "about_val4_h": "Growth",
    "about_val4_p": "Serving buyers across Asia, Europe, the Middle East, and beyond.",
    "contact_hero_h1": "Contact Us",
    "contact_hero_crumb": "Contact Us",
    "contact_address_h": "ADDRESS",
    "contact_phone_h": "PHONE",
    "contact_email_h": "EMAIL",
    "contact_form_label": "We're Here to Help",
    "contact_form_h2": "Let's Start a Conversation",
    "form_name": "Name *",
    "form_email": "Email *",
    "form_phone": "Phone *",
    "form_message": "Message *",
    "form_err_name": "Please enter your name.",
    "form_err_email": "Please enter a valid email.",
    "form_err_phone": "Please enter your phone number.",
    "form_err_message": "Please enter your message.",
    "form_wa_status": "Opening WhatsApp... Your enquiry will be sent directly to our team.",
    "faq_moq_q": "What is the minimum order quantity (MOQ)?",
    "faq_moq_a": "MOQ depends on the product. Please contact us directly via email at <a href=\"mailto:info@terragroxglobal.com\">info@terragroxglobal.com</a> or <a href=\"https://wa.me/917695929907\" target=\"_blank\" rel=\"noopener noreferrer\">WhatsApp</a> for specific product MOQ details.",
    "faq_products_q": "What products do you export?",
    "faq_products_a": "<p>We export:</p><ul><li><strong>Herbal &amp; Superfood Powders</strong> (Moringa, Beetroot, Ginger, Onion, Banana, Neem, and more)</li><li><strong>Premium Spices</strong> (Turmeric, Chili, Black Pepper, Cardamom, and more)</li><li><strong>Natural Sweeteners</strong> (Jaggery Balls, Powder, Palmyra Jaggery, Palm Sugar Candy)</li></ul><p>Additional products are available on request. All products are sourced from trusted Indian farmers and processed to meet international standards.</p>",
    "faq_countries_q": "Which countries do you supply to?",
    "faq_countries_a": "We supply to buyers across Asia, Europe, the Middle East, and beyond. We welcome inquiries from any country and can arrange shipment as per buyer requirements.",
    "faq_quality_q": "How do you ensure product quality?",
    "faq_quality_a": "We follow strict quality control at every stage — sourcing, processing, and packing. Our products meet international export standards and we provide lab test reports on request.",
    "faq_quote_q": "How do I get a price quotation?",
    "faq_quote_a": "<p>Send your requirements to <a href=\"mailto:info@terragroxglobal.com\">info@terragroxglobal.com</a> or WhatsApp us at <a href=\"https://wa.me/917695929907\" target=\"_blank\" rel=\"noopener noreferrer\">+91 7695929907</a> with:</p><ul><li>Product name</li><li>Quantity needed</li><li>Destination country</li><li>Packaging preference</li></ul><p>We will respond within 24–48 hours.</p>",
    "faq_packaging_q": "Do you offer custom packaging or private labeling?",
    "faq_packaging_a": "Yes. We offer export-ready packaging suited to international standards. For custom branding, private label, or country-specific labeling requirements, please contact us to discuss your specifications.",
    "faq_documents_q": "What documents do you provide for export?",
    "faq_documents_a": "We provide complete, dependable export documentation to support your import requirements — including commercial invoices, packing lists, certificates of origin, phytosanitary certificates, COA (Certificate of Analysis), and additional documents as needed per destination country.",
    "faq_different_q": "What makes TerrAgrox global different from other exporters?",
    "faq_different_a": "<p>We are not just a supplier — we are your dedicated trade partner. We offer:</p><ul><li>Transparent pricing</li><li>Timely delivery</li><li>Consistent quality</li><li>Long-term relationship focus</li><li>Direct communication with the founder</li></ul>",
    "faq_payment_q": "What payment methods do you accept?",
    "faq_payment_a": "<p>We accept:</p><ul><li>T/T (Telegraphic Transfer / Wire Transfer)</li><li>Letter of Credit (LC)</li><li>50% advance + 50% before shipment (standard terms)</li></ul><p>Payment terms can be discussed based on order value and buyer history.</p>",
    "faq_pricing_q": "What pricing terms do you offer?",
    "faq_pricing_a": "<p>We offer standard international pricing terms including:</p><ul><li><strong>FOB</strong> (Free On Board) – Chennai / Tuticorin Port</li><li><strong>CIF</strong> (Cost + Insurance + Freight)</li><li><strong>EXW</strong> (Ex Works) – Salem Warehouse</li></ul>",
    "faq_organic_q": "Are your products organic?",
    "faq_organic_a": "Yes, we source products that meet organic and natural standards. Specific certifications can be shared upon request depending on the product and destination country.",
    "filter_all_title": "All Export Products",
    "filter_all_text": "Explore our complete range of export-ready herbal powders, premium spices, and natural sweeteners — sourced from trusted farms and packed for global markets.",
    "filter_herbal_title": "Herbal & Superfood Powders",
    "filter_herbal_text": "Naturally processed powders including Moringa, Onion, Beetroot, Ginger, Banana and Neem — hygienically packed to meet global buyer requirements.",
    "filter_spices_title": "Premium Indian Spices",
    "filter_spices_text": "Aromatic, export-grade spices including Turmeric, Chili, Black Pepper, Cardamom and more — prepared for consistent quality and flavour.",
    "filter_jaggery_title": "Jaggery & Natural Sweeteners",
    "filter_jaggery_text": "Traditional, unrefined jaggery products from Tamil Nadu — clean processing, export packing, and authentic natural sweetness.",
}

import time
import urllib.parse
import urllib.request

LANGS = ["ar", "zh-CN", "fr", "de", "es", "ms", "hi", "ja", "pt"]
LANG_FILES = {
    "ar": "ar",
    "zh-CN": "zh",
    "fr": "fr",
    "de": "de",
    "es": "es",
    "ms": "ms",
    "hi": "hi",
    "ja": "ja",
    "pt": "pt",
}

# Keys with HTML — translate carefully (keep tags)
HTML_KEYS = {
    k
    for k, v in EN.items()
    if "<" in v and ">" in v
}


def translate_text(text: str, target: str) -> str:
    if not text.strip():
        return text
    q = urllib.parse.quote(text[:4500])
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target}&dt=t&q={q}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as res:
        data = json.loads(res.read().decode())
    parts = [p[0] for p in data[0] if p[0]]
    return "".join(parts)


def build_lang(target: str) -> dict:
    out = {}
    for i, (key, val) in enumerate(EN.items()):
        try:
            out[key] = translate_text(val, target)
        except Exception as e:
            print(f"  skip {key}: {e}")
            out[key] = val
        if (i + 1) % 15 == 0:
            print(f"  {target}: {i + 1}/{len(EN)}")
            time.sleep(0.35)
        else:
            time.sleep(0.12)
    return out


def main():
    import sys

    LOCALES.mkdir(parents=True, exist_ok=True)
    (LOCALES / "en.json").write_text(json.dumps(EN, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("en.json")

    if "--en-only" in sys.argv:
        return

    langs = LANG_FILES.items()
    if len(sys.argv) > 1 and sys.argv[1] not in ("--en-only",):
        want = set(sys.argv[1:])
        langs = [(t, f) for t, f in LANG_FILES.items() if f in want]

    for target, file_code in langs:
        path = LOCALES / f"{file_code}.json"
        if path.exists() and path.stat().st_size > 5000:
            print(f"skip {file_code} (exists)")
            continue
        print(f"Translating -> {file_code} ({target})...")
        translated = build_lang(target)
        merged = {**EN, **translated}
        path.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {file_code}.json")

if __name__ == "__main__":
    main()
