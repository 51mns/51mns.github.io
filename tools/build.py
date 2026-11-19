#!/usr/bin/env python3
"""Generate the static Remones site into ../remones/ (and the repo-root shims).

No dependencies beyond the Python 3 standard library. Output is committed;
GitHub Pages serves it as-is. Content lives in content_ja.py / content_en.py.

Link tokens inside page bodies (only inside attribute values):
  "~/..."  -> path relative to the current language root (ja: remones/, en: remones/en/)
  "^/..."  -> path relative to the site root (remones/), for shared assets
"""

from __future__ import annotations

import html
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import site_config as cfg  # noqa: E402
import components as c  # noqa: E402
import content_ja  # noqa: E402
import content_en  # noqa: E402

REPO = HERE.parent
SITE = REPO / "remones"
BASE_PATH = urlparse(cfg.BASE_URL).path  # e.g. "/remones/"

UI = {
    "ja": {
        "skip": "本文へ移動",
        "nav_label": "メインメニュー",
        "nav": [("features", "機能", "~/#features"), ("setup", "はじめかた", "~/setup/"),
                ("mac", "Mac アプリ", "~/mac/"), ("support", "サポート", "~/support/")],
        "dl": "ダウンロード",
        "bar_label": "ダウンロード",
        "bar_mac": "Mac アプリ",
        "switch_label": "English",
        "switch_hreflang": "en",
        "switch_aria": "English version",
        "switch_short": "EN",
        "footer_tagline": "iPhone が、あなたの Mac になる。",
        "footer_cols": [
            ("製品", [("機能", "~/#features"), ("はじめかた", "~/#how"), ("Remones Plus", "~/#plus"), ("ダウンロード", "~/download/")]),
            ("ガイド", [("はじめかた", "~/setup/"), ("Mac アプリ", "~/mac/"), ("外出先から使う", "~/tailscale/"), ("サポート", "~/support/")]),
            ("規約", [("プライバシーポリシー", "~/privacy/"), ("利用条件", "~/terms/")]),
        ],
        "trademarks": "Apple、Mac、iPhone、iPad、macOS は Apple Inc. の商標です。Tailscale は Tailscale Inc. の商標です。",
        "home": "ホーム",
        "og_locale": "ja_JP",
        "site_name": "Remones",
    },
    "en": {
        "skip": "Skip to content",
        "nav_label": "Main",
        "nav": [("features", "Features", "~/#features"), ("setup", "Get started", "~/setup/"),
                ("mac", "Mac app", "~/mac/"), ("support", "Support", "~/support/")],
        "dl": "Download",
        "bar_label": "Download",
        "bar_mac": "Mac app",
        "switch_label": "日本語",
        "switch_hreflang": "ja",
        "switch_aria": "日本語版",
        "switch_short": "JA",
        "footer_tagline": "Your iPhone becomes your Mac.",
        "footer_cols": [
            ("Product", [("Features", "~/#features"), ("How it works", "~/#how"), ("Remones Plus", "~/#plus"), ("Download", "~/download/")]),
            ("Guides", [("Get started", "~/setup/"), ("Mac app", "~/mac/"), ("Use it away from home", "~/tailscale/"), ("Support", "~/support/")]),
            ("Legal", [("Privacy Policy", "~/privacy/"), ("Terms of Use", "~/terms/")]),
        ],
        "trademarks": "Apple, Mac, iPhone, iPad and macOS are trademarks of Apple Inc. Tailscale is a trademark of Tailscale Inc.",
        "home": "Home",
        "og_locale": "en_US",
        "site_name": "Remones",
    },
}


def lang_root(lang: str) -> str:
    return "" if lang == "ja" else "en/"


def rel_prefix(out_rel: str) -> str:
    """Relative prefix from a page (e.g. 'en/mac/index.html') to the site root."""
    depth = out_rel.count("/")
    return "../" * depth


def resolve_tokens(text: str, out_rel: str, lang: str) -> str:
    to_site = rel_prefix(out_rel)
    to_lang = to_site + lang_root(lang)

    def fix(prefix: str, rest: str) -> str:
        target = prefix + rest
        # "./" when the result would be empty (link to the current root)
        return target if target else "./"

    text = re.sub(r'(=")~/([^"]*)"', lambda m: f'{m.group(1)}{fix(to_lang, m.group(2))}"', text)
    text = re.sub(r'(=")\^/([^"]*)"', lambda m: f'{m.group(1)}{fix(to_site, m.group(2))}"', text)
    # srcset values may hold several URLs
    text = re.sub(r'(srcset="[^"]*)', lambda m: m.group(1).replace("^/", to_site), text)
    return text


def page_url(lang: str, slug: str) -> str:
    return cfg.BASE_URL + lang_root(lang) + (slug + "/" if slug else "")


def render(page: dict, lang: str) -> tuple[str, str]:
    slug = page["slug"]
    out_rel = lang_root(lang) + (slug + "/" if slug else "") + "index.html"
    ui = UI[lang]
    other = "en" if lang == "ja" else "ja"
    title = page["title"]
    full_title = title if page.get("title_is_full") else f"{title} — Remones"
    desc = page["description"]
    canonical = page_url(lang, slug)
    og_image = cfg.BASE_URL + f"assets/img/og-{lang}.png"

    nav_items = []
    for key, label, href in ui["nav"]:
        current = ' aria-current="page"' if page.get("nav") == key else ""
        nav_items.append(f'<li><a href="{href}"{current}>{label}</a></li>')

    robots = '\n<meta name="robots" content="noindex">' if page.get("noindex") else ""
    dl_href = "#download" if page.get("dl_bar") else "~/download/"
    body_class = ' class="has-dl-bar"' if page.get("dl_bar") else ""
    dl_bar = ""
    if page.get("dl_bar"):
        dl_bar = (f'<aside class="dl-bar" aria-label="{ui["bar_label"]}">'
                  f'<span class="brand-mini">{c.mark_svg()}<span>Remones</span></span>'
                  f'{c.app_store_button(lang, compact=True)}'
                  f'<a class="btn btn-secondary" href="~/mac/">{c.icon("laptop")}{ui["bar_mac"]}</a></aside>')

    footer_cols = "".join(
        f'<div><h2>{html.escape(h)}</h2><ul>' + "".join(f'<li><a href="{u}">{html.escape(t)}</a></li>' for t, u in links) + "</ul></div>"
        for h, links in ui["footer_cols"]
    )

    doc = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">{robots}
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ja" href="{page_url('ja', slug)}">
<link rel="alternate" hreflang="en" href="{page_url('en', slug)}">
<link rel="alternate" hreflang="x-default" href="{page_url('ja', slug)}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#f2f2f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121316" media="(prefers-color-scheme: dark)">
<link rel="icon" href="^/favicon.svg" type="image/svg+xml">
<link rel="icon" href="^/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="^/apple-touch-icon.png">
<link rel="stylesheet" href="^/assets/css/site.css">
<script src="^/assets/js/site.js" defer></script>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Remones">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(page.get('og_alt', 'Remones'))}">
<meta property="og:locale" content="{ui['og_locale']}">
<meta name="twitter:card" content="summary_large_image">
</head>
<body{body_class}>
<a class="skip-link" href="#main">{ui['skip']}</a>
<header class="site-header">
<div class="wrap">
<a class="brand" href="~/">{c.mark_svg()}<span>Remones</span></a>
<nav class="site-nav" aria-label="{ui['nav_label']}"><ul>{''.join(nav_items)}</ul></nav>
<a class="btn btn-primary header-dl" href="{dl_href}">{c.icon("download")}{ui['dl']}</a>
<a class="lang-switch" href="{'^/en/' if lang == 'ja' else '^/'}{slug + '/' if slug else ''}" hreflang="{ui['switch_hreflang']}" lang="{other}" aria-label="{ui['switch_aria']}"><span class="long">{ui['switch_label']}</span><span class="short" aria-hidden="true">{ui['switch_short']}</span></a>
</div>
</header>
<main id="main">
{page['body'].strip()}
</main>
{dl_bar}
<footer class="site-footer">
<div class="wrap">
<div class="footer-grid">
<div class="footer-brand"><a class="brand" href="~/">{c.mark_svg()}<span>Remones</span></a><p>{ui['footer_tagline']}</p></div>
{footer_cols}
</div>
<p class="copyright">© 2026 Remones. {ui['trademarks']}</p>
</div>
</footer>
</body>
</html>
"""
    doc = resolve_tokens(doc, out_rel, lang)
    # links to the language switch target should not carry an empty "./" + slug glitch
    doc = doc.replace('href="./"', 'href="./"')
    return out_rel, doc


def write(rel: str, text: str, root: Path = SITE) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_404() -> str:
    """Root 404 for the whole user site. Uses absolute paths because GitHub
    Pages serves it at arbitrary depths."""
    b = BASE_PATH
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ページが見つかりません — Remones</title>
<meta name="robots" content="noindex">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{b}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{b}assets/css/site.css">
</head>
<body>
<main id="main" class="wrap" style="min-height:80vh;display:grid;place-items:center;padding-top:48px;padding-bottom:48px">
<div class="card" style="max-width:34rem;width:100%">
<a class="brand" href="{b}">{c.mark_svg()}<span>Remones</span></a>
<h1 style="font-size:1.75rem;margin:24px 0 12px">ページが見つかりません</h1>
<p>URL が変わったか、ページが移動した可能性があります。</p>
<div class="actions" style="margin-bottom:28px"><a class="btn btn-primary" href="{b}">Remones ホームへ</a><a class="btn btn-secondary" href="{b}mac/">Mac アプリ</a></div>
<hr>
<div lang="en">
<h2 style="font-size:1.25rem;margin-bottom:8px">Page not found</h2>
<p>The address may have changed or the page may have moved.</p>
<div class="actions"><a class="btn btn-secondary" href="{b}en/">Remones home</a><a class="btn btn-secondary" href="{b}en/mac/">Mac app</a></div>
</div>
</div>
</main>
</body>
</html>
"""


def build_root_index() -> str:
    b = BASE_PATH
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Remones</title>
<link rel="canonical" href="{cfg.BASE_URL}">
<meta http-equiv="refresh" content="0; url=remones/">
<meta name="color-scheme" content="light dark">
</head>
<body style="font-family:system-ui,-apple-system,'Hiragino Sans',sans-serif;padding:24px">
<p><a href="remones/">Remones</a> へ移動します。 / Redirecting to <a href="remones/">Remones</a>.</p>
</body>
</html>
"""


def build_sitemap(slugs: list[str]) -> str:
    rows = []
    for slug in slugs:
        for lang in ("ja", "en"):
            alts = "".join(
                f'<xhtml:link rel="alternate" hreflang="{l}" href="{page_url(l, slug)}"/>' for l in ("ja", "en")
            )
            rows.append(f"<url><loc>{page_url(lang, slug)}</loc>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def main() -> None:
    ja_pages = content_ja.pages()
    en_pages = content_en.pages()
    if not getattr(cfg, "LEGAL_PUBLISHED", True):
        legal = {"privacy", "terms"}
        ja_pages = [p for p in ja_pages if p["slug"] not in legal]
        en_pages = [p for p in en_pages if p["slug"] not in legal]
        for ui in UI.values():
            ui["footer_cols"] = [c for c in ui["footer_cols"] if c[0] not in ("規約", "Legal")]
    ja_slugs = [p["slug"] for p in ja_pages]
    en_slugs = [p["slug"] for p in en_pages]
    if ja_slugs != en_slugs:
        raise SystemExit(f"ja/en page lists differ: {ja_slugs} vs {en_slugs}")
    for lang, pages in (("ja", ja_pages), ("en", en_pages)):
        for page in pages:
            rel, doc = render(page, lang)
            write(rel, doc)
    indexable = [p["slug"] for p in ja_pages if not p.get("noindex")]
    write("sitemap.xml", build_sitemap(indexable))
    write("404.html", build_404(), REPO)
    write("index.html", build_root_index(), REPO)
    (REPO / ".nojekyll").write_text("", encoding="utf-8")
    print(f"built {len(ja_pages) + len(en_pages)} pages into {SITE}")


if __name__ == "__main__":
    main()
