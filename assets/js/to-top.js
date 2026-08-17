/* Ariyalur Golden Hospital — back-to-top button (progressive enhancement) */
(function () {
  "use strict";

  var btn = document.querySelector("[data-to-top]");
  if (!btn) return;

  /* Show it only once the visitor is a screen or so down the page, so short
     pages never get a floating control they have no use for. */
  function threshold() {
    return Math.max(400, window.innerHeight * 0.8);
  }

  var ticking = false;

  function update() {
    ticking = false;
    var y = window.pageYOffset || document.documentElement.scrollTop;
    btn.setAttribute("data-visible", String(y > threshold()));
  }

  function onScroll() {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(update);
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll);

  btn.addEventListener("click", function () {
    var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" });
    /* Send focus to the top of the document so keyboard and screen reader
       users follow the jump instead of being left at the button. Focusing
       body rather than the skip link avoids flashing that link on screen. */
    document.body.setAttribute("tabindex", "-1");
    document.body.focus({ preventScroll: true });
    document.body.removeAttribute("tabindex");
  });

  update();
})();
