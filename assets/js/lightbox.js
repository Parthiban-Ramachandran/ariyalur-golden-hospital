/* Ariyalur Golden Hospital — gallery lightbox / slider (progressive enhancement)

   Any container marked [data-gallery] has its .gallery-item--photo figures
   turned into buttons that open a full-screen viewer with prev/next paging.
   With JavaScript off the gallery stays a plain grid of captioned photographs. */
(function () {
  "use strict";

  var SVG_NS = "http://www.w3.org/2000/svg";

  var groups = [].slice.call(document.querySelectorAll("[data-gallery]"));
  if (!groups.length) return;

  var items = [];
  groups.forEach(function (group) {
    [].slice.call(group.querySelectorAll(".gallery-item--photo")).forEach(function (figure) {
      var picture = figure.querySelector("picture");
      var img = figure.querySelector("img");
      var caption = figure.querySelector("figcaption");
      if (!picture || !img) return;
      items.push({
        figure: figure,
        picture: picture,
        caption: caption ? caption.textContent.trim() : "",
        alt: img.getAttribute("alt") || ""
      });
    });
  });
  if (!items.length) return;

  /* ---------------------------------------------------------------- icons */
  function icon(paths, extra) {
    var svg = document.createElementNS(SVG_NS, "svg");
    svg.setAttribute("viewBox", "0 0 24 24");
    svg.setAttribute("fill", "none");
    svg.setAttribute("stroke", "currentColor");
    svg.setAttribute("stroke-width", extra || "2");
    svg.setAttribute("stroke-linecap", "round");
    svg.setAttribute("stroke-linejoin", "round");
    svg.setAttribute("aria-hidden", "true");
    paths.forEach(function (d) {
      var p = document.createElementNS(SVG_NS, "path");
      p.setAttribute("d", d);
      svg.appendChild(p);
    });
    return svg;
  }

  var ICON_CLOSE = ["M18 6 6 18", "M6 6l12 12"];
  var ICON_PREV = ["M15 18 9 12l6-6"];
  var ICON_NEXT = ["M9 18l6-6-6-6"];
  var ICON_ZOOM = ["M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16z", "M21 21l-4.35-4.35", "M11 8v6", "M8 11h6"];

  /* --------------------------------------------------------- viewer shell */
  var root = document.createElement("div");
  root.className = "lightbox";
  root.setAttribute("hidden", "");

  var backdrop = document.createElement("div");
  backdrop.className = "lightbox__backdrop";
  root.appendChild(backdrop);

  var dialog = document.createElement("div");
  dialog.className = "lightbox__dialog";
  dialog.setAttribute("role", "dialog");
  dialog.setAttribute("aria-modal", "true");
  dialog.setAttribute("aria-label", "Photograph viewer");
  root.appendChild(dialog);

  function makeButton(cls, label, paths) {
    var b = document.createElement("button");
    b.type = "button";
    b.className = "lightbox__btn " + cls;
    b.setAttribute("aria-label", label);
    b.appendChild(icon(paths));
    dialog.appendChild(b);
    return b;
  }

  var btnClose = makeButton("lightbox__btn--close", "Close viewer", ICON_CLOSE);
  var btnPrev = makeButton("lightbox__btn--prev", "Previous photograph", ICON_PREV);
  var btnNext = makeButton("lightbox__btn--next", "Next photograph", ICON_NEXT);

  var figure = document.createElement("figure");
  figure.className = "lightbox__figure";

  var stage = document.createElement("div");
  stage.className = "lightbox__stage";
  figure.appendChild(stage);

  var caption = document.createElement("figcaption");
  caption.className = "lightbox__caption";
  var captionText = document.createElement("span");
  captionText.className = "lightbox__caption-text";
  var counter = document.createElement("span");
  counter.className = "lightbox__count";
  caption.appendChild(captionText);
  caption.appendChild(counter);
  figure.appendChild(caption);

  dialog.appendChild(figure);

  var live = document.createElement("p");
  live.className = "visually-hidden";
  live.setAttribute("aria-live", "polite");
  dialog.appendChild(live);

  document.body.appendChild(root);

  /* --------------------------------------------------------------- state */
  var index = 0;
  var open = false;
  var lastFocus = null;

  /* Rebuilds the <picture> for a slide from the thumbnail's own srcset, but
     asks for a viewport-sized candidate instead of a tile-sized one. */
  function buildSlide(item) {
    var slide = document.createElement("div");
    slide.className = "lightbox__slide";

    var picture = item.picture.cloneNode(true);
    [].slice.call(picture.querySelectorAll("source, img")).forEach(function (node) {
      node.setAttribute("sizes", "92vw");
    });

    var img = picture.querySelector("img");
    img.removeAttribute("loading");
    img.removeAttribute("width");
    img.removeAttribute("height");
    img.className = "lightbox__img";

    slide.appendChild(picture);
    return slide;
  }

  function preload(i) {
    var item = items[(i + items.length) % items.length];
    var img = item.picture.querySelector("img");
    var pre = new Image();
    pre.sizes = "92vw";
    if (img.srcset) pre.srcset = img.srcset;
    pre.src = img.src;
  }

  function show(next, direction) {
    var total = items.length;
    index = (next + total) % total;
    var item = items[index];

    var slide = buildSlide(item);
    if (direction) slide.setAttribute("data-enter", direction > 0 ? "next" : "prev");

    var previous = stage.firstChild;
    if (previous) stage.removeChild(previous);
    stage.appendChild(slide);

    captionText.textContent = item.caption;
    counter.textContent = (index + 1) + " / " + total;
    live.textContent = item.caption + " — photograph " + (index + 1) + " of " + total;

    if (total > 1) {
      preload(index + 1);
      preload(index - 1);
    }
  }

  function openAt(i) {
    lastFocus = document.activeElement;
    root.removeAttribute("hidden");
    document.body.classList.add("has-lightbox");
    open = true;
    show(i, 0);
    /* let the [hidden] removal paint before the fade-in starts */
    requestAnimationFrame(function () { root.setAttribute("data-open", "true"); });
    btnClose.focus();
  }

  function close() {
    if (!open) return;
    open = false;
    root.removeAttribute("data-open");
    document.body.classList.remove("has-lightbox");
    root.setAttribute("hidden", "");
    stage.textContent = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  /* ------------------------------------------------------------- triggers */
  items.forEach(function (item, i) {
    var trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "gallery-item__zoom";
    trigger.setAttribute("aria-label", "View larger: " + (item.caption || item.alt));
    trigger.appendChild(icon(ICON_ZOOM, "1.9"));
    trigger.addEventListener("click", function () { openAt(i); });
    item.figure.appendChild(trigger);
  });

  btnClose.addEventListener("click", close);
  backdrop.addEventListener("click", close);
  btnPrev.addEventListener("click", function () { show(index - 1, -1); });
  btnNext.addEventListener("click", function () { show(index + 1, 1); });

  if (items.length < 2) {
    btnPrev.hidden = true;
    btnNext.hidden = true;
    counter.hidden = true;
  }

  document.addEventListener("keydown", function (e) {
    if (!open) return;
    if (e.key === "Escape") { e.preventDefault(); close(); return; }
    if (items.length < 2) return;
    if (e.key === "ArrowRight") { e.preventDefault(); show(index + 1, 1); }
    if (e.key === "ArrowLeft") { e.preventDefault(); show(index - 1, -1); }
  });

  /* Keep tabbing inside the dialog while it is open. */
  root.addEventListener("keydown", function (e) {
    if (e.key !== "Tab") return;
    var focusable = [btnClose, btnPrev, btnNext].filter(function (b) { return !b.hidden; });
    var first = focusable[0];
    var last = focusable[focusable.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });

  /* ---------------------------------------------------------- touch swipe */
  var startX = 0;
  var startY = 0;
  var tracking = false;

  stage.addEventListener("touchstart", function (e) {
    if (e.touches.length !== 1) return;
    tracking = true;
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
  }, { passive: true });

  stage.addEventListener("touchend", function (e) {
    if (!tracking) return;
    tracking = false;
    if (items.length < 2) return;
    var touch = e.changedTouches[0];
    var dx = touch.clientX - startX;
    var dy = touch.clientY - startY;
    if (Math.abs(dx) < 45 || Math.abs(dx) < Math.abs(dy)) return;
    show(index + (dx < 0 ? 1 : -1), dx < 0 ? 1 : -1);
  }, { passive: true });
})();
