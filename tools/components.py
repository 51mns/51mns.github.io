"""Shared HTML snippets for the Remones site."""

from __future__ import annotations

import html
from pathlib import Path

import site_config as cfg

_HERE = Path(__file__).resolve().parent
# Paths copied verbatim from Apps/Prototype/Client/AppIcons/AppIcon.icon/Assets
_BASE_D = (_HERE / "mark-base.d").read_text().strip()
_CURSOR_D = (_HERE / "mark-cursor.d").read_text().strip()


def mark_svg() -> str:
    """The two-tone cursor R, coloured by CSS tokens (decorative)."""
    return (
        '<svg viewBox="200 210 640 640" aria-hidden="true" focusable="false">'
        f'<path class="mark-base" fill-rule="evenodd" d="{_BASE_D}"/>'
        f'<path class="mark-cursor" d="{_CURSOR_D}"/></svg>'
    )


_ICONS = {
    "display": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "window": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 9.5h18"/><path d="M6 7.2h.01M8.5 7.2h.01"/>',
    "macs": '<rect x="2" y="9" width="12" height="9" rx="1.5"/><path d="M6 21h4"/><path d="M8 6V5.5A1.5 1.5 0 0 1 9.5 4h11A1.5 1.5 0 0 1 22 5.5v7a1.5 1.5 0 0 1-1.5 1.5H17"/>',
    "shelf": '<rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M14.5 4v16"/><path d="M17 8h1.5M17 11h1.5M17 14h1.5"/>',
    "audio": '<path d="M4 9.5h3l4.5-4v13L7 14.5H4z"/><path d="M15.5 9a4 4 0 0 1 0 6"/><path d="M18.5 6a8 8 0 0 1 0 12"/>',
    "keyboard": '<rect x="2" y="6" width="20" height="12" rx="2.5"/><path d="M6 10h.01M10 10h.01M14 10h.01M18 10h.01M7.5 14h9"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 3.8 5.5 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.5-3.8-9S9.5 5.5 12 3z"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8 10.5V8a4 4 0 0 1 8 0v2.5"/>',
    "search": '<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.3-4.3"/>',
    "pip": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><rect x="12" y="11.5" width="6.5" height="5" rx="1.2"/>',
    "phone": '<rect x="6.5" y="2.5" width="11" height="19" rx="2.8"/><path d="M10.5 18.5h3"/>',
    "laptop": '<rect x="4" y="4.5" width="16" height="11" rx="1.6"/><path d="M2 19h20"/>',
    "link": '<path d="M7 17L17 7M9 7h8v8"/>',
    "download": '<path d="M12 4v11M7.5 10.5L12 15l4.5-4.5M5 19.5h14"/>',
}


def icon(name: str) -> str:
    return f'<svg class="i" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{_ICONS[name]}</svg>'


def app_store_button(lang: str, compact: bool = False) -> str:
    if cfg.APP_STORE_URL:
        label = "App Store で入手" if lang == "ja" else "Download on the App Store"
        if compact:
            label = "App Store"
        return f'<a class="btn btn-primary" href="{html.escape(cfg.APP_STORE_URL)}">{icon("phone")}{label}</a>'
    label = "App Store で近日公開" if lang == "ja" else "Coming soon on the App Store"
    if compact:
        label = "App Store 近日公開" if lang == "ja" else "App Store · soon"
    note = "まだ公開されていません" if lang == "ja" else "not yet available"
    return (f'<span class="btn btn-soon" role="link" aria-disabled="true">{icon("phone")}{label}'
            f'<span class="visually-hidden">（{note}）</span></span>')


def mac_download_button(lang: str, primary: bool = True) -> str:
    cls = "btn-primary" if primary else "btn-secondary"
    if cfg.MAC_DOWNLOAD_READY:
        label = f"{cfg.MAC_APP_NAME} をダウンロード" if lang == "ja" else f"Download {cfg.MAC_APP_NAME}"
        return f'<a class="btn {cls}" href="{html.escape(cfg.MAC_DOWNLOAD_URL)}">{icon("download")}{label}</a>'
    label = "ダウンロード準備中" if lang == "ja" else "Download coming soon"
    note = "まだ配布していません" if lang == "ja" else "not yet released"
    return (f'<span class="btn btn-soon" role="link" aria-disabled="true">{icon("download")}{label}'
            f'<span class="visually-hidden">（{note}）</span></span>')


def picture(light: str, dark: str, alt: str, width: int, height: int, cls: str = "", lazy: bool = True) -> str:
    """Light/dark image pair; only the matching one is downloaded."""
    loading = ' loading="lazy"' if lazy else ""
    klass = f' class="{cls}"' if cls else ""
    return (f'<picture><source srcset="^/{dark}" media="(prefers-color-scheme: dark)">'
            f'<img{klass} src="^/{light}" alt="{html.escape(alt)}" width="{width}" height="{height}"{loading} decoding="async"></picture>')


def app_icon(alt: str, cls: str = "hero-icon") -> str:
    return picture("assets/img/icon-256.webp", "assets/img/icon-256-dark.webp", alt, 256, 256, cls, lazy=False)


ACCENTS = [
    ("standard", "標準", "Standard", False),
    ("lemon", "レモン", "Lemon", False),
    ("orange", "オレンジ", "Orange", True),
    ("coral", "コーラル", "Coral", True),
    ("violet", "バイオレット", "Violet", True),
    ("blue", "ブルー", "Blue", True),
    ("green", "グリーン", "Green", True),
]


def icon_row(lang: str) -> str:
    items = []
    for key, ja, en, plus in ACCENTS:
        name = ja if lang == "ja" else en
        alt = (f"{name}のアプリアイコン" if lang == "ja" else f"{name} app icon")
        badge = ('<span class="badge badge-plus">Plus</span>' if plus else
                 f'<span class="badge">{"無料" if lang == "ja" else "Free"}</span>')
        img = picture(f"assets/img/icon-{key}-128.webp", f"assets/img/icon-{key}-128-dark.webp", alt, 128, 128)
        items.append(f"<li>{img}<span>{name}</span><br>{badge}</li>")
    return '<ul class="icon-row">' + "".join(items) + "</ul>"


def accent_strip() -> str:
    spans = "".join(f'<span style="background:var(--accent-{k})"></span>' for k, *_ in ACCENTS if k != "standard")
    return f'<div class="accent-strip" aria-hidden="true">{spans}</div>'
