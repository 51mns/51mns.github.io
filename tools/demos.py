"""Inline SVG product demos for the landing page.

Rule: every animation demonstrates a real feature. The static SVG
attributes describe the END state, so with prefers-reduced-motion (where the
CSS removes all animations) visitors see the finished picture. Keyframes live
in assets/css/site.css under "demos". Labels come from Localizable.xcstrings.
"""

from __future__ import annotations

L = {
    "ja": {
        "online": "オンライン", "offline": "オフライン", "open": "開く", "computers": "コンピュータ",
        "home": "自宅", "away": "外出先", "trackpad": "トラックパッド", "touch": "タッチ操作", "direct": "直接操作",
        "typed": "こんにちは、Mac", "server": "Remones のサーバー", "none": "経由しません",
        "direct_tls": "直接・暗号化（TLS）",
    },
    "en": {
        "online": "Online", "offline": "Offline", "open": "Open", "computers": "Computers",
        "home": "Home", "away": "Away", "trackpad": "Trackpad", "touch": "Touch", "direct": "Direct",
        "typed": "Hello from iPhone", "server": "Remones server", "none": "not involved",
        "direct_tls": "Direct · encrypted (TLS)",
    },
}


def _lines(x: float, y: float, w: float, gap: float, h: float, widths: list[float], cls: str = "f-line") -> str:
    out = []
    for i, f in enumerate(widths):
        k = "f-line2" if i == 0 else cls
        out.append(f'<rect class="{k}" x="{x}" y="{y + i * gap:.1f}" width="{w * f:.1f}" height="{h}" rx="{h / 2}"/>')
    return "".join(out)


def _cursor() -> str:
    return ('<path class="f-cursor" d="M0 0 L0 22 L6 16.5 L10 26 L14 24.2 L10 15 L18 15 Z" '
            'stroke-width="1.6" stroke-linejoin="round"/>')


def _phone(x: float, y: float, w: float, h: float, r: float = 30) -> str:
    nw, nh = w * 0.24, max(5.0, w * 0.06)
    return (f'<rect class="f-frame" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>'
            f'<rect class="f-phone" x="{x + 9}" y="{y + 9}" width="{w - 18}" height="{h - 18}" rx="{r - 8}"/>'
            f'<rect class="f-frame" x="{x + w / 2 - nw / 2}" y="{y + 14 + w * 0.02}" width="{nw}" height="{nh}" rx="{nh / 2}"/>')


def hero(lang: str) -> str:
    """Mac + iPhone. Finger drags -> Mac cursor moves -> click opens a window ->
    the window flies into the iPhone and fits it (Fit Window)."""
    win_x, win_y, win_w, win_h = 150, 92, 330, 214
    dock = "".join(f'<rect class="f-dockicon{" f-dockicon-hi" if i == 2 else ""}" x="{236 + i * 36}" y="{356}" width="26" height="26" rx="7"/>' for i in range(5))
    mac_win = (
        f'<g class="h-macwin">'
        f'<rect class="f-win" x="{win_x}" y="{win_y}" width="{win_w}" height="{win_h}" rx="10"/>'
        f'<rect class="f-titlebar" x="{win_x}" y="{win_y}" width="{win_w}" height="24" rx="10"/>'
        f'<rect class="f-titlebar" x="{win_x}" y="{win_y + 12}" width="{win_w}" height="12"/>'
        f'<circle class="f-dot-r" cx="{win_x + 14}" cy="{win_y + 12}" r="4"/><circle class="f-dot-y" cx="{win_x + 27}" cy="{win_y + 12}" r="4"/><circle class="f-dot-g" cx="{win_x + 40}" cy="{win_y + 12}" r="4"/>'
        + _lines(win_x + 18, win_y + 40, win_w - 36, 17, 6, [0.45, 0.95, 0.88, 0.92, 0.7, 0.9, 0.84, 0.5, 0.86, 0.6])
        + "</g>"
    )
    px, py, pw, ph = 664, 34, 196, 400
    sx, sy, sw, sh = px + 9, py + 40, pw - 18, ph - 58  # fitted window area
    phone_win = (
        f'<g class="h-phonewin">'
        f'<rect class="f-win" x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="12"/>'
        f'<rect class="f-titlebar" x="{sx}" y="{sy}" width="{sw}" height="30" rx="12"/>'
        f'<rect class="f-titlebar" x="{sx}" y="{sy + 14}" width="{sw}" height="16"/>'
        + _lines(sx + 14, sy + 48, sw - 28, 26, 10, [0.55, 0.96, 0.9, 0.93, 0.72, 0.95, 0.85, 0.6, 0.9, 0.7, 0.8])
        + "</g>"
    )
    trackpad = (
        f'<g class="h-trackpad">'
        f'<rect class="f-pad" x="{px + 20}" y="{py + 120}" width="{pw - 40}" height="{ph - 150}" rx="18"/>'
        f'<rect class="f-line" x="{px + 64}" y="{py + 96}" width="{pw - 128}" height="8" rx="4"/>'
        f'</g>'
    )
    finger = ('<g class="h-finger"><circle class="f-ripple" cx="0" cy="0" r="16"/>'
              '<circle class="f-finger" cx="0" cy="0" r="15"/></g>')
    ghost = (f'<rect class="h-ghost" x="{win_x}" y="{win_y}" width="{win_w}" height="{win_h}" rx="10" '
             'vector-effect="non-scaling-stroke"/>')
    return f"""<svg class="demo-svg" viewBox="0 0 880 470" role="img" aria-labelledby="hero-demo-title">
<title id="hero-demo-title">{"iPhone で指を動かすと Mac のカーソルが動き、開いたウインドウが iPhone の画面にぴったり収まる様子" if lang == "ja" else "Moving a finger on the iPhone moves the Mac’s cursor; the window it opens then fits the iPhone screen"}</title>
<rect class="f-frame" x="20" y="20" width="600" height="388" rx="20"/>
<rect class="f-desk" x="34" y="34" width="572" height="360" rx="8"/>
<rect class="f-menubar" x="34" y="34" width="572" height="18" rx="8"/><rect class="f-menubar" x="34" y="44" width="572" height="8"/>
<rect class="f-dock" x="224" y="350" width="192" height="38" rx="12"/>
{dock}
<circle class="f-run h-dockdot" cx="{236 + 72 + 13}" cy="386" r="2.2"/>
<path class="f-stand" d="M282 408 h76 l10 38 h-96 z"/><rect class="f-stand" x="240" y="444" width="160" height="10" rx="5"/>
{mac_win}
<g class="h-cursor" transform="translate(420 232)">{_cursor()}</g>
{_phone(px, py, pw, ph, 34)}
{trackpad}
{phone_win}
{ghost}
{finger}
</svg>"""


def window_demo(lang: str) -> str:
    """Desktop (tiny, unreadable) -> Fit Window (readable)."""
    px, py, pw, ph = 100, 10, 180, 300
    sx, sy, sw, sh = px + 9, py + 9, pw - 18, ph - 18
    # desktop: a 16:10 Mac screen letterboxed in the portrait phone
    dw = sw - 8
    dh = dw * 10 / 16
    dx, dy = sx + 4, sy + (sh - dh) / 2
    desktop = (f'<g class="w-desk"><rect class="f-desk" x="{dx}" y="{dy}" width="{dw}" height="{dh}" rx="3"/>'
               f'<rect class="f-win" x="{dx + 30}" y="{dy + 14}" width="{dw * 0.55}" height="{dh * 0.6}" rx="2"/>'
               + _lines(dx + 35, dy + 22, dw * 0.45, 5, 1.6, [0.5, 0.95, 0.9, 0.8, 0.92, 0.6, 0.85])
               + '</g>')
    fit = (f'<g class="w-fit"><rect class="f-win" x="{sx}" y="{sy + 26}" width="{sw}" height="{sh - 26}" rx="14"/>'
           + _lines(sx + 14, sy + 50, sw - 28, 24, 10, [0.6, 0.96, 0.9, 0.94, 0.7, 0.92, 0.86, 0.55, 0.9, 0.75])
           + '</g>')
    return f"""<svg class="demo-svg" viewBox="0 0 380 320" role="img" aria-label="{"Desktop では小さすぎて読めない文字が、ウインドウ表示では読める大きさになる" if lang == "ja" else "Text too small to read in Desktop becomes readable in Fit Window"}">
{_phone(px, py, pw, ph, 32)}
{desktop}
{fit}
<g class="w-lens"><circle class="f-lens" cx="{dx + 60}" cy="{dy + 40}" r="22"/><path class="f-lens" d="M{dx + 76} {dy + 56} l14 14"/></g>
</svg>"""


def macs_demo(lang: str) -> str:
    t = L[lang]
    names = ["MacBook Pro", "Mac Studio", "Mac mini"]
    rows = []
    for i, name in enumerate(names):
        y = 64 + i * 78
        rows.append(f"""<g class="m-row m-row-{i}">
<rect class="f-row" x="20" y="{y}" width="340" height="64" rx="16"/>
<rect class="f-line" x="38" y="{y + 18}" width="34" height="22" rx="4"/><rect class="f-line" x="50" y="{y + 42}" width="10" height="5" rx="1.5"/>
<text class="f-text f-strong" x="88" y="{y + 28}">{name}</text>
<circle class="m-dot" cx="93" cy="{y + 44}" r="4.5"/>
<text class="f-text f-sub m-off" x="104" y="{y + 49}">{t['offline']}</text>
<text class="f-text f-sub m-on" x="104" y="{y + 49}">{t['online']}</text>
<rect class="m-btn" x="270" y="{y + 15}" width="74" height="34" rx="17"/>
<text class="f-text m-btn-text" x="307" y="{y + 37}" text-anchor="middle">{t['open']}</text>
</g>""")
    return f"""<svg class="demo-svg" viewBox="0 0 380 300" role="img" aria-label="{"Home のコンピュータ一覧。MacBook Pro、Mac Studio、Mac mini が順にオンラインになる" if lang == "ja" else "Home’s computer list. MacBook Pro, Mac Studio and Mac mini come online one by one"}">
<text class="f-text f-title" x="22" y="40">{t['computers']}</text>
{''.join(rows)}
</svg>"""


def remote_demo(lang: str) -> str:
    t = L[lang]
    packets = "".join(f'<circle class="r-pkt r-pkt-{i}" cx="118" cy="150" r="5"/>' for i in range(3))
    back = "".join(f'<circle class="r-pkt-back r-pkt-back-{i}" cx="262" cy="158" r="4"/>' for i in range(2))
    return f"""<svg class="demo-svg" viewBox="0 0 380 300" role="img" aria-label="{"iPhone と Mac が、自宅では LAN、外出先では Tailscale で直接つながる" if lang == "ja" else "iPhone and Mac connect directly: over the LAN at home, over Tailscale when away"}">
<g class="r-phone">{_phone(46, 70, 72, 150, 16)}</g>
<rect class="f-frame" x="262" y="96" width="100" height="70" rx="8"/><rect class="f-desk" x="268" y="102" width="88" height="58" rx="3"/>
<path class="f-stand" d="M300 166 h24 l4 16 h-32 z"/><rect class="f-stand" x="290" y="180" width="44" height="5" rx="2.5"/>
<path class="r-link" d="M118 154 H262"/>
{packets}{back}
<g class="r-lan"><rect class="r-chip" x="140" y="104" width="100" height="30" rx="15"/><text class="f-text r-chip-text" x="190" y="124" text-anchor="middle">LAN</text></g>
<g class="r-ts"><rect class="r-chip r-chip-hi" x="140" y="104" width="100" height="30" rx="15"/><text class="f-text r-chip-text r-chip-text-hi" x="190" y="124" text-anchor="middle">Tailscale</text></g>
<text class="f-text f-sub r-loc-home" x="82" y="250" text-anchor="middle">{t['home']}</text>
<text class="f-text f-sub r-loc-away" x="82" y="250" text-anchor="middle">{t['away']}</text>
<text class="f-text f-sub" x="312" y="210" text-anchor="middle">{t['home']}</text>
</svg>"""


def input_demo(lang: str) -> str:
    t = L[lang]
    segs = [t["trackpad"], t["touch"], t["direct"]]
    seg_text = "".join(f'<text class="f-text f-small" x="{78 + i * 112}" y="{170}" text-anchor="middle">{s}</text>' for i, s in enumerate(segs))
    keys = []
    for r, (n, off) in enumerate([(10, 0), (9, 16), (7, 48)]):
        for k in range(n):
            x = 24 + off + k * 33.2
            keys.append(f'<rect class="f-key i-key i-key-{r}-{k}" x="{x:.1f}" y="{204 + r * 30}" width="29" height="24" rx="5"/>')
    return f"""<svg class="demo-svg" viewBox="0 0 380 300" role="img" aria-label="{"入力モードを切り替えながら、iPhone のキーボードで打った日本語が Mac に入力される" if lang == "ja" else "Switching input modes, and text typed on the iPhone keyboard appearing on the Mac"}">
<rect class="f-win" x="20" y="14" width="340" height="104" rx="12"/>
<rect class="f-titlebar" x="20" y="14" width="340" height="24" rx="12"/><rect class="f-titlebar" x="20" y="26" width="340" height="12"/>
<circle class="f-dot-r" cx="34" cy="26" r="4"/><circle class="f-dot-y" cx="47" cy="26" r="4"/><circle class="f-dot-g" cx="60" cy="26" r="4"/>
<svg x="20" y="40" width="340" height="70" overflow="hidden"><text class="f-text f-type" x="18" y="42">{t['typed']}</text>
<g class="i-cover"><rect class="f-win" x="16" y="6" width="320" height="56"/><rect class="i-caret" x="16" y="16" width="2.5" height="32"/></g></svg>
<rect class="f-seg" x="22" y="148" width="336" height="34" rx="17"/>
<rect class="i-seg-hi" x="25" y="151" width="106" height="28" rx="14"/>
{seg_text}
{''.join(keys)}
</svg>"""


def privacy_diagram(lang: str) -> str:
    t = L[lang]
    return f"""<svg class="demo-svg" viewBox="0 0 640 280" role="img" aria-label="{"iPhone と Mac は直接つながり、Remones のサーバーは経由しない" if lang == "ja" else "iPhone and Mac connect directly; no Remones server is involved"}">
<g class="p-cloud"><path class="f-cloud" d="M262 78 a26 26 0 0 1 8-50 a36 36 0 0 1 68-6 a28 28 0 0 1 40 30 a24 24 0 0 1-8 46 z"/>
<path class="f-strike" d="M254 18 L392 104"/></g>
<text class="f-text f-sub" x="320" y="136" text-anchor="middle">{t['server']}</text>
<text class="f-text f-sub" x="320" y="162" text-anchor="middle">{t['none']}</text>
{_phone(60, 118, 76, 140, 16)}
<rect class="f-frame" x="470" y="138" width="130" height="88" rx="9"/><rect class="f-desk" x="477" y="145" width="116" height="74" rx="3"/>
<path class="f-stand" d="M522 226 h26 l5 18 h-36 z"/>
<path class="p-link" d="M150 206 H456"/>
<path class="f-arrow" d="M446 198 l12 8 l-12 8 M160 198 l-12 8 l12 8"/>
<text class="f-text f-strong" x="303" y="246" text-anchor="middle">{t['direct_tls']}</text>
</svg>"""
