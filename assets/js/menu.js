/* Ariyalur Golden Hospital — mobile navigation toggle (progressive enhancement) */
(function () {
  "use strict";

  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  var scrim = document.querySelector("[data-nav-scrim]");
  if (!toggle || !nav) return;

  function setState(open) {
    toggle.setAttribute("aria-expanded", String(open));
    nav.setAttribute("data-open", String(open));
    if (scrim) scrim.setAttribute("data-open", String(open));
    document.body.style.overflow = open && window.innerWidth <= 1199 ? "hidden" : "";
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
})();
