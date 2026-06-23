/* TerrAgrox global — main.js
   Navbar scroll, back-to-top, counters, filters, contact→WhatsApp,
   hero animations, i18n, product-grid + checklist observers, AOS
*/

(function () {
  "use strict";

  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  const WA_NUMBER = "917695929907";
  const WA_BASE = `https://wa.me/${WA_NUMBER}`;
  const LANG_KEY = "tgLang";

  // ---------- Navbar scroll ----------
  const navbar = $(".tg-navbar");
  function onScroll() {
    if (!navbar) return;
    navbar.classList.toggle("scrolled", window.scrollY > 60);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // ---------- Smooth scroll ----------
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

  // ---------- data-bg backgrounds ----------
  $$("[data-bg]").forEach((el) => {
    const url = el.getAttribute("data-bg");
    if (!url) return;
    el.style.backgroundImage = `url('${url}')`;
  });

  // ---------- Counters ----------
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

    const introImg = $("#productIntroImg");
    const introTitle = $("#productIntroTitle");
    const introText = $("#productIntroText");
    if (introImg && introTitle && introText) {
      const imgs = {
        all: { img: "assets/images/image%205.jpg", alt: "TerrAgrox global products" },
        herbal: { img: "assets/herbal%20powders.jpeg", alt: "Herbal powders" },
        spices: { img: "assets/spices.jpg", alt: "Premium spices" },
        jaggery: { img: "assets/jaggery-hero.jpeg", alt: "Jaggery and natural sweeteners" },
      };
      const keys = FILTER_I18N[filter] || FILTER_I18N.all;
      const dict = window.TG_I18N || {};
      introTitle.textContent = dict[keys.title] || introTitle.textContent;
      introText.textContent = dict[keys.text] || introText.textContent;
      const im = imgs[filter] || imgs.all;
      introImg.setAttribute("src", im.img);
      introImg.setAttribute("alt", im.alt);
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


  // ---------- Contact form ----------
  const waForm = $("#waContactForm");
  if (waForm) {
    waForm.addEventListener("submit", (e) => {
      e.preventDefault();
      waForm.classList.add("was-validated");
      if (!waForm.checkValidity()) return;

      const name    = $("#fullName").value.trim();
      const email   = $("#email").value.trim();
      const phone   = $("#phone").value.trim();
      const message = $("#message").value.trim();

      const subject = "Website enquiry from " + name;
      const body =
        "Hello TerrAgrox Global,\n\n" +
        "I would like to send an enquiry via your website.\n\n" +
        "Name: " + name + "\n" +
        "Email: " + email + "\n" +
        "Phone: " + phone + "\n\n" +
        "Message:\n" + message;

      const gmailUrl = "https://mail.google.com/mail/u/0/?view=cm&fs=1"
        + "&to=info%40terragroxglobal.com"
        + "&su=" + encodeURIComponent(subject)
        + "&body=" + encodeURIComponent(body);

      window.open(gmailUrl, "_blank");
    });
  }

  // ---------- Nested dropdowns ----------
  function setupSubmenus() {
    $$(".dropdown-submenu").forEach((li) => {
      const trigger = $('a.dropdown-item, a.dropdown-toggle, button.dropdown-item', li) || $("a", li);
      const menu = $(".dropdown-menu", li);
      if (!trigger || !menu) return;

      li.addEventListener("mouseenter", () => {
        if (window.matchMedia("(min-width: 992px)").matches) menu.classList.add("show");
      });
      li.addEventListener("mouseleave", () => {
        if (window.matchMedia("(min-width: 992px)").matches) menu.classList.remove("show");
      });

      trigger.addEventListener("click", (e) => {
        if (window.matchMedia("(max-width: 991.98px)").matches) {
          e.preventDefault();
          menu.classList.toggle("show");
        }
      });
    });
  }
  setupSubmenus();

  $$(".dropdown").forEach((dd) => {
    dd.addEventListener("hidden.bs.dropdown", () => {
      $$(".dropdown-menu.show", dd).forEach((m) => m.classList.remove("show"));
    });
  });

  // ---------- i18n ----------
  let i18nDict = {};

  async function loadJson(path) {
    const res = await fetch(path, { cache: "no-cache" });
    if (!res.ok) throw new Error(path);
    return res.json();
  }

  function deepMerge(a, b) {
    const out = { ...a };
    Object.keys(b || {}).forEach((k) => {
      out[k] = b[k] !== undefined ? b[k] : a[k];
    });
    return out;
  }

  const FILTER_I18N = {
    all: { title: "filter_all_title", text: "filter_all_text" },
    herbal: { title: "filter_herbal_title", text: "filter_herbal_text" },
    spices: { title: "filter_spices_title", text: "filter_spices_text" },
    jaggery: { title: "filter_jaggery_title", text: "filter_jaggery_text" },
  };

  function applyI18n(lang) {
    const dict = i18nDict;
    window.TG_I18N = dict;

    $$("[data-i18n]").forEach((el) => {
      if (el.hasAttribute("data-i18n-html")) return;
      const key = el.getAttribute("data-i18n");
      if (!key || dict[key] === undefined) return;
      el.textContent = dict[key];
    });

    $$("[data-i18n-html]").forEach((el) => {
      const key = el.getAttribute("data-i18n-html");
      if (!key || dict[key] === undefined) return;
      el.innerHTML = dict[key];
    });

    $$("[data-i18n-placeholder]").forEach((el) => {
      const key = el.getAttribute("data-i18n-placeholder");
      if (!key || dict[key] === undefined) return;
      el.setAttribute("placeholder", dict[key]);
    });

    $$("label[data-i18n]").forEach((el) => {
      const key = el.getAttribute("data-i18n");
      if (!key || dict[key] === undefined) return;
      el.textContent = dict[key];
    });

    const pageTitleKey = document.body?.getAttribute("data-i18n-page-title");
    if (pageTitleKey && dict[pageTitleKey]) {
      document.title = dict[pageTitleKey];
    }

    const year = $("#year");
    const copyEl = $("[data-i18n-copyright]");
    if (copyEl && dict.footer_copyright) {
      copyEl.textContent = dict.footer_copyright.replace("{year}", year ? year.textContent : String(new Date().getFullYear()));
    }

    const waLabel = dict.btn_enquire_wa || "Enquire Now";
    $$(".btn-product-wa").forEach((btn) => {
      const icon = btn.querySelector("i");
      btn.innerHTML = icon ? `${icon.outerHTML} ${waLabel}` : waLabel;
    });

    document.documentElement.lang = lang === "zh" ? "zh" : lang === "en" ? "en" : lang;
    document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";

    const codeEl = $("#activeLangCode");
    const flagEl = $("#activeLangFlag");
    const map = {
      en: "EN",
      ar: "AR",
      zh: "ZH",
      fr: "FR",
      de: "DE",
      es: "ES",
      ms: "MS",
      hi: "HI",
      ja: "JA",
      pt: "PT",
    };
    if (codeEl) codeEl.textContent = map[lang] || "EN";

    const activeOpt = $(`.lang-opt[data-lang="${lang}"]`);
    const flagFile = activeOpt?.getAttribute("data-flag") || "en.svg";
    if (flagEl) flagEl.setAttribute("src", `assets/img/flags/${flagFile}`);

    window.dispatchEvent(new CustomEvent("tg:langchange", { detail: { lang, dict } }));

    if (typeof window.TG_renderFaq === "function") {
      window.TG_renderFaq();
    }
  }

  async function setLanguage(lang) {
    const safe = ["en", "ar", "zh", "fr", "de", "es", "ms", "hi", "ja", "pt"].includes(lang) ? lang : "en";
    try {
      const base = await loadJson("assets/locales/en.json");
      let extra = {};
      if (safe !== "en") {
        try {
          extra = await loadJson(`assets/locales/${safe}.json`);
        } catch {
          extra = {};
        }
      }
      i18nDict = deepMerge(base, extra);
      localStorage.setItem(LANG_KEY, safe);
      applyI18n(safe);
      $$(".lang-opt").forEach((a) => a.classList.toggle("active", a.getAttribute("data-lang") === safe));
      if (window.AOS) window.AOS.refresh();
    } catch (err) {
      console.warn("i18n load failed", err);
    }
  }

  function setupLangSwitcher() {
    const saved = localStorage.getItem(LANG_KEY) || "en";
    setLanguage(saved);

    $$(".lang-opt").forEach((a) => {
      a.addEventListener("click", (e) => {
        e.preventDefault();
        const lang = a.getAttribute("data-lang") || "en";
        setLanguage(lang);
      });
    });
  }
  setupLangSwitcher();

  // ---------- Legacy product cards (layout + WA button) ----------
  function enhanceLegacyProductCards() {
    $$(".product-card").forEach((card) => {
      const media = $(".product-media", card);
      const body = $(".card-body", card);
      if (!media || !body) return;

      $$(".product-overlay", card).forEach((el) => el.remove());

      if (!$(".product-cat-badge", media)) {
        const row = body.querySelector(".d-flex");
        let cat = row ? row.querySelector(".pill.cat") : body.querySelector(".pill.cat");
        if (!cat) {
          const col = card.closest("[data-cat]");
          if (col) {
            const d = (col.getAttribute("data-cat") || "").toLowerCase();
            const map = { herbal: "Herbal", spices: "Spices", jaggery: "Jaggery" };
            if (map[d]) {
              const badge = document.createElement("span");
              badge.className = "product-cat-badge";
              badge.textContent = map[d];
              media.insertBefore(badge, media.firstChild);
            }
          }
        } else {
          const badge = document.createElement("span");
          badge.className = "product-cat-badge";
          badge.textContent = cat.textContent.replace(/\s+/g, " ").trim().slice(0, 20);
          media.insertBefore(badge, media.firstChild);
          cat.remove();
        }
        const best = row ? row.querySelector(".pill.best") : body.querySelector(".pill.best");
        if (best) {
          const bb = document.createElement("span");
          bb.className = "product-best-badge";
          bb.textContent = best.textContent.replace(/\s+/g, " ").trim().slice(0, 18);
          const img = media.querySelector("img");
          if (img) media.insertBefore(bb, img);
          else media.appendChild(bb);
          best.remove();
        }
        if (row && !row.querySelector(".pill")) row.remove();
      }

      if ($(".btn-product-wa", card)) return;
      body.classList.add("product-card-body");
      const h5 = $("h5", body);
      if (!h5) return;
      const p = $("p.muted", body);
      if (p) {
        p.classList.add("product-card-desc");
        p.classList.remove("mb-3");
      }
      const a = document.createElement("a");
      a.className = "btn-product-wa";
      a.href = "contact-us.html#waContactForm";
      const waLabel = (window.TG_I18N && window.TG_I18N.btn_enquire_wa) || "Enquire Now";
      a.innerHTML = `<i class="fa-solid fa-paper-plane"></i> ${waLabel}`;
      body.appendChild(a);
    });
  }
  enhanceLegacyProductCards();

  // ---------- Product spec panels ----------
  function buildSpecPanels() {
    $$(".product-card[data-spec]").forEach((card) => {
      if ($(".product-spec-panel", card)) return;
      let spec;
      try {
        // Decode HTML entities before parsing JSON
        const raw = card.getAttribute("data-spec").replace(/&amp;/g,"&").replace(/&#39;/g,"'").replace(/&quot;/g,'"');
        spec = JSON.parse(raw);
      } catch (e) { return; }

      const name = ($("h5", card) || {}).textContent || "";
      const rows = [
        ["Botanical", spec.botanical],
        ["Family", spec.family],
        ["Plant Part", spec.parts],
        ["Form", spec.form],
        ["Colour", spec.color],
        spec.mesh ? ["Mesh Size", spec.mesh] : null,
        ["Origin", "India"],
      ].filter(Boolean).filter(([, v]) => v);

      const productName = name.trim().replace(/\s+/g," ");
      const waMsg = encodeURIComponent(`Hi, I am interested in ${productName}. Please share more details.`);
      const waUrl = `${WA_BASE}?text=${waMsg}`;

      const panel = document.createElement("div");
      panel.className = "product-spec-panel";
      panel.innerHTML = `
        <div class="spec-cat-label">${spec.cat || ""}</div>
        <div class="spec-product-name">${name}</div>
        <div class="spec-rows">
          ${rows.map(([l, v]) => `<div class="spec-row"><span class="spec-row-label">${l}</span><span class="spec-row-val">${v}</span></div>`).join("")}
        </div>
        ${spec.applications ? `<div class="spec-applications"><strong>Applications</strong>${spec.applications}</div>` : ""}
        <a class="spec-enquire-btn" href="${waUrl}" target="_blank" rel="noopener noreferrer">
          <i class="fa-brands fa-whatsapp"></i> Enquire Now
        </a>`;
      card.appendChild(panel);
      card.classList.add("has-spec");

      card.addEventListener("mouseenter", () => panel.classList.add("active"));
      card.addEventListener("mouseleave", () => panel.classList.remove("active"));
    });
  }
  buildSpecPanels();

  // ---------- AOS ----------
  if (window.AOS) {
    window.AOS.init({
      duration: 700,
      easing: "ease-out-cubic",
      once: true,
      offset: 80,
    });
  }

  // ---------- Product grid entrance ----------
  const productObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        productObserver.unobserve(entry.target);
      });
    },
    { threshold: 0, rootMargin: "0px 0px -10% 0px" }
  );
  $$(".products-grid").forEach((grid) => productObserver.observe(grid));

  // ---------- Animated checklists ----------
  const listObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in-view");
        listObserver.unobserve(entry.target);
      });
    },
    { threshold: 0.15 }
  );
  $$(".animated-list").forEach((ul) => listObserver.observe(ul));

  // ---------- Back-to-top ----------
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

  // ---------- Hero text animation ----------
  const hero = $("#tgHero");
  if (hero) {
    hero.addEventListener("slide.bs.carousel", () => {
      $$(".carousel-item", hero).forEach((s) => s.classList.remove("hero-animate"));
    });
    hero.addEventListener("slid.bs.carousel", () => {
      const active = $(".carousel-item.active", hero);
      if (active) {
        void active.offsetWidth;
        active.classList.add("hero-animate");
      }
    });
    const active = $(".carousel-item.active", hero);
    if (active) active.classList.add("hero-animate");
  }

  // ---------- Active nav ----------
  const path = (window.location.pathname.split("/").pop() || "index.html").toLowerCase();
  $$("a.nav-link, .dropdown-item").forEach((a) => {
    const href = (a.getAttribute("href") || "").toLowerCase();
    if (!href || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) return;
    const clean = href.split("#")[0];
    if (clean && clean === path) a.classList.add("active");
  });

  // ---------- Mobile nav: close menu after link tap ----------
  const mainNav = $("#mainNav");
  if (mainNav && typeof bootstrap !== "undefined") {
    const closeMobileNav = () => {
      if (window.innerWidth >= 992) return;
      const instance = bootstrap.Collapse.getInstance(mainNav);
      if (instance && mainNav.classList.contains("show")) instance.hide();
    };
    $$("#mainNav .nav-link:not(.dropdown-toggle), #mainNav .dropdown-item").forEach((link) => {
      link.addEventListener("click", closeMobileNav);
    });
  }

  // ---------- Footer year ----------
  const year = $("#year");
  if (year) year.textContent = String(new Date().getFullYear());

  // ---------- Testimonials: horizontal auto-scroll ----------
  function setupTestimonialsMarquee() {
    const track = $("#tgTestimonialsTrack");
    if (!track) return;

    const firstSet = $(".testimonials-marquee-set", track);
    if (!firstSet) return;

    let clone = $(".testimonials-marquee-set--clone", track);
    if (!clone) {
      clone = firstSet.cloneNode(true);
      clone.classList.add("testimonials-marquee-set--clone");
      clone.setAttribute("aria-hidden", "true");
      track.appendChild(clone);
    } else {
      clone.innerHTML = firstSet.innerHTML;
    }

    const syncClone = () => {
      const c = $(".testimonials-marquee-set--clone", track);
      if (c) c.innerHTML = firstSet.innerHTML;
    };

    const setSpeed = () => {
      const w = firstSet.getBoundingClientRect().width;
      const pxPerSec = 55;
      track.style.setProperty("--marquee-duration", `${Math.max(w / pxPerSec, 30)}s`);
    };

    syncClone();
    requestAnimationFrame(setSpeed);

    if (!track.dataset.marqueeReady) {
      track.dataset.marqueeReady = "1";
      window.addEventListener("resize", setSpeed);
      window.addEventListener("tg:langchange", () => {
        requestAnimationFrame(() => {
          syncClone();
          setSpeed();
        });
      });
    }
  }

  setupTestimonialsMarquee();
  window.setTimeout(setupTestimonialsMarquee, 400);
})();
