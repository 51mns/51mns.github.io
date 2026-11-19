/* Remones site: progressive enhancement only. Without JS every page works;
   demos simply run continuously and the download bar stays hidden. */
(function () {
  var root = document.documentElement;
  root.classList.add("js");
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
  var pastHero = false, atFinal = false;
  function update() { bar.classList.toggle("is-shown", pastHero && !atFinal); bar.inert = !(pastHero && !atFinal); }
  new IntersectionObserver(function (entries) {
    var e = entries[0]; pastHero = !e.isIntersecting && e.boundingClientRect.top < 0; update();
  }).observe(hero);
  if (finalDl) new IntersectionObserver(function (entries) { atFinal = entries[0].isIntersecting; update(); }).observe(finalDl);
  update();
})();
