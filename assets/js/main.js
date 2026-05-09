/* TerraGrox Global — main.js
   - Sticky navbar (transparent -> solid) on scroll
   - Back-to-top button
   - Floating WhatsApp button (always)
   - Animated counters (IntersectionObserver, data-count + data-suffix)
   - Product category filter tabs (data-filter + data-cat)
   - WhatsApp card click + enquiry buttons
   - WhatsApp contact form redirect (validation + message builder)
   - Hero slide text animations reset/replay on slide change
   - Nested dropdown support (Products submenu)
   - Active nav link highlight
   - AOS init
*/

(function () {
  "use strict";

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  const WA_NUMBER = "917695929907";
  const WA_BASE = `https://wa.me/${WA_NUMBER}`;

  // ---------- Navbar scroll state ----------
  const navbar = $(".tg-navbar");
  function onScroll() {
    if (!navbar) return;
    navbar.classList.toggle("scrolled", window.scrollY > 60);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---------- Smooth scroll for anchor links ----------
  $$('a[href^="#"]').forEach((a) => {
    a.addEventListener("click", (e) => {
      const href = a.getAttribute("href");
      if (!href || href === "#") return;
      const target = document.getElementById(href.slice(1));
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });

  // ---------- Apply background images without inline styles ----------
  // Elements can provide data-bg="https://images.unsplash.com/..." and JS will apply background-image.
  $$("[data-bg]").forEach((el) => {
    const url = el.getAttribute("data-bg");
    if (!url) return;
    el.style.backgroundImage = `url('${url}')`;
  });

  // ---------- Animated counters ----------
  function animateCounter(el) {
    const target = Number(el.getAttribute("data-count") || "0");
    const suffix = el.getAttribute("data-suffix") || "";
    const duration = 2000;
    const startTime = performance.now();

    function tick(now) {
      const t = Math.min(1, (now - startTime) / duration);
      const eased = 1 - Math.pow(1 - t, 3);
      const value = Math.round(target * eased);
      el.textContent = `${value}${suffix}`;
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  const counters = $$("[data-count]");
  if (counters.length) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          if (el.dataset.counted) return;
          el.dataset.counted = "1";
          animateCounter(el);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach((el) => io.observe(el));
  }

  // ---------- Product category filter ----------
  const filterButtons = $$("[data-filter]");
  const cards = $$("[data-cat]");
  function applyFilter(filter) {
    cards.forEach((c) => {
      const cat = (c.getAttribute("data-cat") || "all").toLowerCase();
      const show = filter === "all" || cat === filter;
      c.classList.toggle("d-none", !show);
    });

    // Products page: update right-side intro block (if present)
    const introImg = $("#productIntroImg");
    const introTitle = $("#productIntroTitle");
    const introText = $("#productIntroText");
    if (introImg && introTitle && introText) {
      const meta = {
        all: {
          title: "All Export Products",
          text: "Explore our complete range of export-ready herbal powders, premium spices, and natural sweeteners — sourced from trusted farms and packed for global markets.",
          img: "assets/images/image%205.jpg",
          alt: "TerraGrox Global products",
        },
        herbal: {
          title: "Herbal & Superfood Powders",
          text: "Naturally processed powders including Moringa, Onion, Beetroot, Ginger, Banana and Neem — hygienically packed to meet global buyer requirements.",
          img: "assets/herbal%20powders.jpeg",
          alt: "Herbal powders",
        },
        spices: {
          title: "Premium Indian Spices",
          text: "Aromatic, export-grade spices including Turmeric, Chili, Black Pepper, Cardamom and more — prepared for consistent quality and flavour.",
          img: "assets/spices.jpg",
          alt: "Premium spices",
        },
        jaggery: {
          title: "Jaggery & Natural Sweeteners",
          text: "Traditional, unrefined jaggery products from Tamil Nadu — clean processing, export packing, and authentic natural sweetness.",
          img: "assets/healthy-jaggery-still-life-arrangement.jpg",
          alt: "Jaggery and natural sweeteners",
        },
      };
      const m = meta[filter] || meta.all;
      introTitle.textContent = m.title;
      introText.textContent = m.text;
      introImg.setAttribute("src", m.img);
      introImg.setAttribute("alt", m.alt);
    }
  }
  filterButtons.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const filter = (btn.getAttribute("data-filter") || "all").toLowerCase();
      filterButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      applyFilter(filter);
    });
  });

  // ---------- WhatsApp enquiry helpers ----------
  function buildWaUrl(message) {
    const text = encodeURIComponent(message);
    return `${WA_BASE}?text=${text}`;
  }

  // Whole-card click => WhatsApp with product name
  $$("[data-wa-product]").forEach((el) => {
    el.addEventListener("click", () => {
      const name = el.getAttribute("data-wa-product") || "Product";
      const url = buildWaUrl(`Hi, I am interested in ${name}. Please share details.`);
      window.open(url, "_blank", "noopener,noreferrer");
    });
  });

  // ---------- Contact form -> WhatsApp redirect ----------
  const waForm = $("#waContactForm");
  if (waForm) {
    waForm.addEventListener("submit", (e) => {
      e.preventDefault();

      // Basic Bootstrap validation
      waForm.classList.add("was-validated");
      if (!waForm.checkValidity()) return;

      const name = $("#fullName", waForm)?.value?.trim() || $("#name", waForm)?.value?.trim() || "";
      const company = $("#companyName", waForm)?.value?.trim() || "";
      const email = $("#email", waForm)?.value?.trim() || "";
      const phone = $("#phone", waForm)?.value?.trim() || "";
      const product = $("#productInterest", waForm)?.value?.trim() || "";
      const message = $("#message", waForm)?.value?.trim() || "";

      const lines = [
        "Hello TerraGrox Global,",
        "",
        `*Name:* ${name}`,
        company ? `*Company:* ${company}` : null,
        `*Email:* ${email}`,
        `*Phone:* ${phone}`,
        product ? `*Product Interest:* ${product}` : null,
        "",
        "*Message:*",
        message,
      ].filter(Boolean);

      const url = buildWaUrl(lines.join("\n"));
      window.open(url, "_blank", "noopener,noreferrer");

      const status = $("#waStatus");
      if (status) {
        status.classList.remove("d-none");
        status.textContent = "Opening WhatsApp... Your enquiry will be sent directly to our team.";
      }
    });
  }

  // ---------- Nested dropdown behavior (desktop hover & click) ----------
  // For desktop: open submenus on hover to match typical multi-level menus.
  // For mobile: allow click to toggle submenus.
  function setupSubmenus() {
    const submenus = $$(".dropdown-submenu");
    submenus.forEach((li) => {
      const trigger = $('a.dropdown-item, a.dropdown-toggle, button.dropdown-item', li) || $("a", li);
      const menu = $(".dropdown-menu", li);
      if (!trigger || !menu) return;

      // Desktop hover
      li.addEventListener("mouseenter", () => {
        if (window.matchMedia("(min-width: 992px)").matches) {
          menu.classList.add("show");
        }
      });
      li.addEventListener("mouseleave", () => {
        if (window.matchMedia("(min-width: 992px)").matches) {
          menu.classList.remove("show");
        }
      });

      // Mobile click toggle
      trigger.addEventListener("click", (e) => {
        if (window.matchMedia("(max-width: 991.98px)").matches) {
          e.preventDefault();
          menu.classList.toggle("show");
        }
      });
    });
  }
  setupSubmenus();

  // Close any open nested submenu when parent dropdown hides
  $$(".dropdown").forEach((dd) => {
    dd.addEventListener("hidden.bs.dropdown", () => {
      $$(".dropdown-menu.show", dd).forEach((m) => m.classList.remove("show"));
    });
  });

  // ---------- AOS ----------
  if (window.AOS) {
    window.AOS.init({
      duration: 800,
      easing: "ease-out-cubic",
      once: true,
      offset: 80,
    });
  }

  // ---------- Back-to-top button ----------
  const backToTop = $("#backToTop");
  function onScrollBackToTop() {
    if (!backToTop) return;
    backToTop.classList.toggle("show", window.scrollY > 300);
  }
  window.addEventListener("scroll", onScrollBackToTop, { passive: true });
  onScrollBackToTop();
  if (backToTop) {
    backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  // ---------- Hero slide text animation reset/replay ----------
  const hero = $("#tgHero");
  if (hero) {
    hero.addEventListener("slide.bs.carousel", () => {
      // remove animation class from all slides before transition
      $$(".carousel-item", hero).forEach((s) => s.classList.remove("hero-animate"));
    });
    hero.addEventListener("slid.bs.carousel", () => {
      const active = $(".carousel-item.active", hero);
      if (active) {
        // trigger reflow to restart keyframes
        void active.offsetWidth; // eslint-disable-line no-unused-expressions
        active.classList.add("hero-animate");
      }
    });
    // initial
    const active = $(".carousel-item.active", hero);
    if (active) active.classList.add("hero-animate");
  }

  // ---------- Active nav link ----------
  // Highlights links matching current HTML page (simple static hosting).
  const path = (window.location.pathname.split("/").pop() || "index.html").toLowerCase();
  $$('a.nav-link, .dropdown-item').forEach((a) => {
    const href = (a.getAttribute("href") || "").toLowerCase();
    if (!href || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) return;
    const clean = href.split("#")[0];
    if (clean && clean === path) a.classList.add("active");
  });

  // ---------- Footer year ----------
  const year = $("#year");
  if (year) year.textContent = "2025";
})();

