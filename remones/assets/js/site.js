/* Remones site: progressive enhancement only. Without JS every page works;
   demos simply run continuously and the download bar stays hidden. */
(function () {
  var root = document.documentElement;
  root.classList.add("js");
  // Scroll-driven feature demos: native view timelines where supported,
  // otherwise a passive scroll listener sets --p (0..1). Never blocks scrolling.
  var scrubs = document.querySelectorAll("[data-scrub]");
  var motionOK = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var native = window.CSS && CSS.supports && CSS.supports("animation-timeline: view()");
  if (scrubs.length && motionOK && !native) {
    var ticking = false;
    var update = function () {
      ticking = false;
      var vh = window.innerHeight;
      scrubs.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -vh || r.top > 2 * vh) return;
        var cover = (vh - r.top) / (vh + r.height);
        var p = Math.min(1, Math.max(0, (cover - 0.15) / 0.45));
        el.style.setProperty("--p", p.toFixed(3));
      });
    };
    var onScroll = function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    update();
  }

  if (!("IntersectionObserver" in window)) return;

  // Play demos only while on screen (saves battery, starts from the beginning).
  var play = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { e.target.classList.toggle("is-playing", e.isIntersecting); });
  }, { threshold: 0.2 });
  document.querySelectorAll("[data-demo]").forEach(function (el) { play.observe(el); });

  // One-shot reveals (step progress line).
  var reveal = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add("is-in"); reveal.unobserve(e.target); }
    });
  }, { threshold: 0.35 });
  document.querySelectorAll("[data-reveal]").forEach(function (el) { reveal.observe(el); });

  // Compact download bar: visible after the hero, hidden over the final download section.
  var bar = document.querySelector(".dl-bar");
  var hero = document.querySelector("[data-hero]");
  var finalDl = document.querySelector("[data-final-download]");
  if (!bar || !hero) return;
  var pastHero = false, atFinal = false, atPlay = false;
  function update() { var on = pastHero && !atFinal && !atPlay; bar.classList.toggle("is-shown", on); bar.inert = !on; }
  new IntersectionObserver(function (entries) {
    var e = entries[0]; pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; update();
  }).observe(hero);
  // Keep the bar off the playground so it never covers the demo phone.
  var pg = document.querySelector(".pg-stage");
  if (pg) new IntersectionObserver(function (entries) { atPlay = entries[0].isIntersecting; update(); }).observe(pg);
  if (finalDl) new IntersectionObserver(function (entries) { atFinal = entries[0].isIntersecting; update(); }).observe(finalDl);
  update();
})();
