/* Renders FAQ accordions from window.TG_FAQ + i18n dictionary */
(function () {
  "use strict";

  function lookup(key, fallback) {
    if (!key) return fallback || "";
    const dict = window.TG_I18N;
    if (dict && dict[key] !== undefined) return dict[key];
    return fallback || "";
  }

  function renderFaqAccordion(container, options) {
    const items = window.TG_FAQ;
    if (!container || !items || !items.length) return;

    const opts = options || {};
    const limit = opts.limit;
    const accordionId = opts.accordionId || "faqAccordion";
    const openFirst = opts.openFirst !== false;

    let list = items;
    if (limit) {
      list = items.filter((i) => i.featured).slice(0, limit);
      if (!list.length) list = items.slice(0, limit);
    }

    const parts = [];
    list.forEach((item, index) => {
      const q = item.qKey ? lookup(item.qKey, item.q) : item.q || "";
      const a = item.aKey ? lookup(item.aKey, item.a) : item.a || "";
      const collapseId = accordionId + "-" + item.id;
      const isOpen = openFirst && index === 0;
      const btnClass = "accordion-button" + (isOpen ? "" : " collapsed");
      const panelClass = "accordion-collapse collapse" + (isOpen ? " show" : "");

      parts.push('<div class="accordion-item">');
      parts.push('<h2 class="accordion-header">');
      parts.push(
        '<button class="' +
          btnClass +
          '" type="button" data-bs-toggle="collapse" data-bs-target="#' +
          collapseId +
          '" aria-expanded="' +
          isOpen +
          '" aria-controls="' +
          collapseId +
          '">' +
          q +
          "</button>"
      );
      parts.push("</h2>");
      parts.push(
        '<div id="' +
          collapseId +
          '" class="' +
          panelClass +
          '" data-bs-parent="#' +
          accordionId +
          '"><div class="accordion-body">' +
          a +
          "</div></div></div>"
      );
    });

    container.innerHTML = parts.join("");
  }

  function renderAll() {
    document.querySelectorAll("[data-faq-render]").forEach(function (el) {
      const limitAttr = el.getAttribute("data-faq-limit");
      const limit = limitAttr ? Number(limitAttr) : null;
      renderFaqAccordion(el, {
        limit: limit || undefined,
        accordionId: el.getAttribute("data-faq-accordion-id") || "faqAccordion",
        openFirst: el.getAttribute("data-faq-open-first") !== "false",
      });
    });
  }

  window.TG_renderFaq = renderAll;
  window.addEventListener("tg:langchange", renderAll);

  /* Show English fallbacks immediately; main.js re-renders when locales load */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderAll);
  } else {
    renderAll();
  }
})();
