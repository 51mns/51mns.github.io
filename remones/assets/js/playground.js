/* Remones "try it" playground — an on-page simulation, no network.
   Input routing mirrors Apps/Prototype/Client/RemoteInputSurface.swift:
   - Touch (direct): pointer goes to the touched point; lifting clicks there.
   - Trackpad: relative movement; a tap (travel < 8) clicks at the cursor.
   - Hybrid: a gesture that starts on the trackpad area is trackpad, else touch.
   View modes follow RemonesPreviewView: Display (whole desktop) / Window. */
(function () {
  var root = document.querySelector("[data-pg]");
  if (!root) return;
  var L = JSON.parse(root.getAttribute("data-l10n"));
  var SVGNS = "http://www.w3.org/2000/svg";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  var phone = root.querySelector(".pg-phone");
  var mirror = root.querySelector("#pg-mirror");
  var pad = root.querySelector("#pg-pad");
  var winG = root.querySelector("#pg-win");
  var cursor = root.querySelector("#pg-cursor");
  var ripple = root.querySelector("#pg-ripple");
  var hint = root.querySelector(".pg-hint");
  var status = root.querySelector(".pg-status");
  var descView = root.querySelector('[data-desc="view"]');
  var descInput = root.querySelector('[data-desc="input"]');

  var W = 1000, H = 625;                 // Mac desktop units
  var SX = 14, SY = 14, SW = 272, SH = 572; // phone screen in phone units
  var PAD_TOP = 430;                       // hybrid trackpad area (phone units)
  var state = { view: "display", input: "touch", cx: 500, cy: 300, win: null };

  // ---------- drawing ----------
  function el(tag, attrs, parent) {
    var n = document.createElementNS(SVGNS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }

  function winRect() {
    if (state.view === "window") {
      // Fit Window: the Mac window takes the phone screen's shape.
      var h = 520, w = Math.round(h * SW / SH);
      return { x: Math.round((W - w) / 2), y: 30, w: w, h: h };
    }
    return { x: 230, y: 80, w: 540, h: 380 };
  }

  function drawWindow() {
    while (winG.firstChild) winG.removeChild(winG.firstChild);
    if (!state.win) { winG.style.display = "none"; return; }
    var r = winRect();
    state.win.r = r;
    winG.style.display = "";
    winG.setAttribute("transform", "translate(" + r.x + " " + r.y + ")");
    el("rect", { "class": "f-win pg-win-bg", x: 0, y: 0, width: r.w, height: r.h, rx: 12 }, winG);
    el("rect", { "class": "f-titlebar", x: 0, y: 0, width: r.w, height: 34, rx: 12 }, winG);
    el("rect", { "class": "f-titlebar", x: 0, y: 18, width: r.w, height: 16 }, winG);
    el("circle", { "class": "f-dot-r", cx: 18, cy: 17, r: 7 }, winG);
    el("circle", { "class": "f-dot-y", cx: 40, cy: 17, r: 7 }, winG);
    el("circle", { "class": "f-dot-g", cx: 62, cy: 17, r: 7 }, winG);
    var title = el("text", { "class": "f-text pg-wtitle", x: r.w / 2, y: 23, "text-anchor": "middle" }, winG);
    title.textContent = L.apps[state.win.app];
    var seed = state.win.app * 7 + 3, y = 62, inner = r.w - 48;
    el("rect", { "class": "f-line2", x: 24, y: y, width: inner * 0.5, height: 14, rx: 7 }, winG);
    for (y = y + 34; y < r.h - 80; y += 26) {
      seed = (seed * 37 + 11) % 100;
      el("rect", { "class": "f-line", x: 24, y: y, width: inner * (0.55 + seed / 230), height: 10, rx: 5 }, winG);
    }
    var bw = 120, bh = 40, bx = r.w - bw - 20, by = r.h - bh - 20;
    state.win.btn = { x: bx, y: by, w: bw, h: bh };
    el("rect", { "class": "pg-btn" + (state.win.done ? " is-done" : ""), x: bx, y: by, width: bw, height: bh, rx: 20 }, winG);
    var bt = el("text", { "class": "f-text pg-btn-text" + (state.win.done ? " is-done" : ""), x: bx + bw / 2, y: by + 26, "text-anchor": "middle" }, winG);
    bt.textContent = state.win.done ? "✓ " + L.msgs.done : L.msgs.ok;
    if (!reduce.matches) {
      winG.classList.remove("is-opening"); void winG.getBBox(); winG.classList.add("is-opening");
    }
  }

  function viewTransform() {
    if (state.view === "window" && state.win) {
      var r = winRect(), s = SW / r.w;
      return { s: s, tx: SX - r.x * s, ty: SY - r.y * s };
    }
    var sd = SW / W;
    return { s: sd, tx: SX, ty: SY + (SH - H * sd) / 2 };
  }

  function applyView() {
    var v = viewTransform();
    mirror.style.transform = "translate(" + v.tx + "px," + v.ty + "px) scale(" + v.s + ")";
    pad.style.display = state.input === "hybrid" ? "" : "none";
    root.classList.toggle("is-nowin", state.view === "window" && !state.win);
  }

  function moveCursor(x, y) {
    state.cx = Math.max(0, Math.min(W - 4, x));
    state.cy = Math.max(0, Math.min(H - 4, y));
    cursor.setAttribute("transform", "translate(" + state.cx.toFixed(1) + " " + state.cy.toFixed(1) + ")");
  }

  function say(msg) { status.textContent = ""; setTimeout(function () { status.textContent = msg; }, 30); }

  // ---------- clicking ----------
  function click() {
    var x = state.cx, y = state.cy;
    ripple.setAttribute("cx", x); ripple.setAttribute("cy", y);
    if (!reduce.matches) { ripple.classList.remove("is-on"); void ripple.getBBox(); ripple.classList.add("is-on"); }
    var w = state.win;
    if (w && w.r && x >= w.r.x && x <= w.r.x + w.r.w && y >= w.r.y && y <= w.r.y + w.r.h) {
      var lx = x - w.r.x, ly = y - w.r.y;
      if (Math.hypot(lx - 18, ly - 17) <= 14) { state.win = null; drawWindow(); applyView(); say(L.msgs.close); return; }
      var b = w.btn;
      if (lx >= b.x && lx <= b.x + b.w && ly >= b.y && ly <= b.y + b.h) {
        w.done = !w.done; drawWindow(); say(L.msgs.button); return;
      }
      return;
    }
    var apps = root.querySelectorAll(".pg-app");
    for (var i = 0; i < apps.length; i++) {
      var a = apps[i], ax = +a.getAttribute("x"), ay = +a.getAttribute("y");
      if (x >= ax - 6 && x <= ax + 62 && y >= ay - 6 && y <= ay + 50) {
        if (!reduce.matches) { a.classList.remove("is-bounce"); void a.getBBox(); a.classList.add("is-bounce"); }
        state.win = { app: i, done: false };
        drawWindow(); applyView(); say(L.msgs.open);
        return;
      }
    }
  }

  // ---------- pointer input ----------
  function phonePoint(e) {
    var r = phone.getBoundingClientRect();
    return { x: (e.clientX - r.left) * 300 / r.width, y: (e.clientY - r.top) * 600 / r.height };
  }
  function toMac(p) {
    var v = viewTransform();
    return { x: (p.x - v.tx) / v.s, y: (p.y - v.ty) / v.s };
  }

  var g = null; // active gesture
  phone.addEventListener("pointerdown", function (e) {
    if (g || (e.pointerType === "mouse" && e.button !== 0)) return;
    var p = phonePoint(e);
    if (p.x < SX || p.x > SX + SW || p.y < SY || p.y > SY + SH) return;
    e.preventDefault();
    try { phone.setPointerCapture(e.pointerId); } catch (err) { /* synthetic or already released */ }
    root.classList.add("is-used");
    var route = state.input === "hybrid" ? (p.y >= PAD_TOP ? "trackpad" : "touch") : state.input;
    g = { id: e.pointerId, route: route, last: p, start: p, travel: 0 };
    if (route === "touch") { var m = toMac(p); moveCursor(m.x, m.y); }
    root.classList.toggle("is-pad-active", route === "trackpad");
  });
  phone.addEventListener("pointermove", function (e) {
    if (!g || e.pointerId !== g.id) return;
    var p = phonePoint(e);
    var dx = p.x - g.last.x, dy = p.y - g.last.y;
    g.travel += Math.hypot(dx, dy) * (phone.getBoundingClientRect().width / 300);
    g.last = p;
    if (g.route === "touch") { var m = toMac(p); moveCursor(m.x, m.y); }
    else { moveCursor(state.cx + dx * 2.6, state.cy + dy * 2.6); }
  });
  function end(e, cancelled) {
    if (!g || e.pointerId !== g.id) return;
    var tap = !cancelled && g.travel < 8;
    // Touch clicks where the finger lifts; Trackpad clicks only on a tap.
    if (!cancelled && (g.route === "touch" ? g.travel < 24 : tap)) click();
    g = null;
    root.classList.remove("is-pad-active");
  }
  phone.addEventListener("pointerup", function (e) { end(e, false); });
  phone.addEventListener("pointercancel", function (e) { end(e, true); });

  // ---------- keyboard ----------
  phone.addEventListener("keydown", function (e) {
    var step = e.shiftKey ? 60 : 20, k = e.key;
    if (k === "ArrowLeft") moveCursor(state.cx - step, state.cy);
    else if (k === "ArrowRight") moveCursor(state.cx + step, state.cy);
    else if (k === "ArrowUp") moveCursor(state.cx, state.cy - step);
    else if (k === "ArrowDown") moveCursor(state.cx, state.cy + step);
    else if (k === "Enter" || k === " ") click();
    else return;
    e.preventDefault();
    root.classList.add("is-used");
  });

  // ---------- controls ----------
  root.addEventListener("change", function (e) {
    var t = e.target;
    if (t.name === "pg-view") { state.view = t.value; descView.textContent = L.desc[t.value]; drawWindow(); }
    if (t.name === "pg-input") { state.input = t.value; descInput.textContent = L.desc[t.value]; }
    applyView();
    if (state.view === "window" && !state.win) say(L.msgs.nowin);
  });

  root.classList.add("is-ready");
  applyView();
})();
