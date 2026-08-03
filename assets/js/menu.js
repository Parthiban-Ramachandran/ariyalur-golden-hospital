/* Ariyalur Golden Hospital — mobile navigation toggle (progressive enhancement) */
(function () {
  "use strict";

  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  var scrim = document.querySelector("[data-nav-scrim]");
  if (!toggle || !nav) return;

  var items = nav.querySelectorAll("[data-nav-item]");

  /* Drawer accordions. On desktop the groups open on hover/focus and these
     buttons are hidden, so the collapsed state only matters below 1200px. */
  function closeGroups() {
    Array.prototype.forEach.call(items, function (item) {
      item.setAttribute("data-open", "false");
      var btn = item.querySelector("[data-nav-expand]");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  }

  Array.prototype.forEach.call(items, function (item) {
    var btn = item.querySelector("[data-nav-expand]");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var open = item.getAttribute("data-open") !== "true";
      closeGroups();
      item.setAttribute("data-open", String(open));
      btn.setAttribute("aria-expanded", String(open));
    });
  });

  function setState(open) {
    toggle.setAttribute("aria-expanded", String(open));
    nav.setAttribute("data-open", String(open));
    if (scrim) scrim.setAttribute("data-open", String(open));
    document.body.style.overflow = open && window.innerWidth <= 1199 ? "hidden" : "";
    if (!open) closeGroups();
  }

  toggle.addEventListener("click", function () {
    setState(toggle.getAttribute("aria-expanded") !== "true");
  });

  if (scrim) scrim.addEventListener("click", function () { setState(false); });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") setState(false);
  });

  nav.addEventListener("click", function (e) {
    if (e.target.closest("a") && window.innerWidth <= 1199) setState(false);
  });

  window.addEventListener("resize", function () {
    if (window.innerWidth > 1199) setState(false);
  });

  /* Open the group that holds the current page so the drawer shows where
     the visitor is without them having to hunt for it. */
  Array.prototype.forEach.call(items, function (item) {
    if (!item.querySelector('[aria-current="page"]')) return;
    item.setAttribute("data-open", "true");
    var btn = item.querySelector("[data-nav-expand]");
    if (btn) btn.setAttribute("aria-expanded", "true");
  });
})();
