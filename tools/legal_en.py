"""English legal pages, built from remones-legal-drafts.raw.md (2026-11-17).

DRAFT: not legal advice. Same deviations from the raw draft as legal_ja.py.
"""

from __future__ import annotations


def _ph(text: str) -> str:
    return f'<span class="placeholder">[{text}]</span>'


def _banner() -> str:
    return ('<div class="draft-banner" role="note"><strong>Draft — under review before publication</strong>'
            'This document is a pre-publication draft. It is not final and is not legal advice. '
            '<span lang="ja">（草案 — 公開前に確認中）</span></div>')


def _head(title: str, crumb: str) -> str:
    return f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">Home</a> / {crumb}</p>
<h1>{title}</h1>
{_banner()}
</div>"""


def _meta() -> str:
    return f"""<ul class="legal-meta">
<li>Effective date: {_ph("complete before publication")}</li>
<li>Provider: {_ph("legal name")}</li>
<li>Contact: {_ph("email address")}</li>
</ul>"""


def privacy() -> dict:
    body = _head("Remones Privacy Policy", "Privacy Policy") + f"""
<div class="wrap doc">
<nav class="toc" aria-label="Contents"><p class="toc-title">Contents</p><ol>
<li><a href="#p1">1. Scope and approach</a></li>
<li><a href="#p2">2. Information exchanged between devices</a></li>
<li><a href="#p3">3. Information stored locally</a></li>
<li><a href="#p4">4. Purchases and external services</a></li>
<li><a href="#p5">5. Advertising, analytics and diagnostics</a></li>
<li><a href="#p6">6. Choices, retention and deletion</a></li>
<li><a href="#p7">7. Security</a></li>
<li><a href="#p8">8. Contact and changes</a></li>
</ol></nav>
<div class="doc-main legal">
{_meta()}
<section id="p1"><h2>1. Scope and approach</h2>
<p>This policy covers the Remones iPhone/iPad app and Mac Host.</p>
<p>Remones connects to a Mac you own or are authorized to control, using your local network or a VPN you arrange. It requires no Remones account or developer-operated shared backend or relay.</p>
<p>Normal remote sessions do not send screen content, audio, input, or clipboard content to a developer-operated server.</p>
</section>
<section id="p2"><h2>2. Information exchanged between devices</h2>
<p>Depending on the features you use, connected devices process and exchange:</p>
<ul>
<li>Mac screen and window video, cursor information, and Mac playback audio when enabled.</li>
<li>Keyboard input, entered text, pointer/touch/trackpad actions, and focus information needed for control.</li>
<li>Device identifiers and names, connection addresses, authentication information, connection status, capabilities, build information, and battery status.</li>
<li>Application names, identifiers and icons, running status, and window titles and geometry used to select remote applications and views.</li>
<li>Text and URLs when clipboard synchronization is enabled. In versions supporting multiple Macs, switching the active computer with synchronization enabled may send copied text to the destination Mac.</li>
<li>Search queries and results when file search is allowed on the Mac. Search uses filename metadata on the Mac. Results include names, parent-folder names, types, and temporary identifiers for opening items. Search results do not transfer file contents or full paths, although opened content can appear in the screen stream.</li>
</ul>
<p>The destination Mac and applications running on it may process or retain received input and clipboard content.</p>
<p>The reviewed implementation contains iPhone/iPad microphone and camera forwarding code, but the normal Mac Host configuration disables these capabilities. Enabling them in a release requires reviewing this policy and permission descriptions.</p>
</section>
<section id="p3"><h2>3. Information stored locally</h2>
<p>Remones stores information on your devices to support reconnection and restore settings:</p>
<ul>
<li><strong>Keychain:</strong> client identity, paired-device information, and shared secrets. The Mac also stores approved-device information.</li>
<li><strong>Preferences:</strong> display, input, audio and clipboard settings, favorites, recent remote targets, and workspace names, targets and layouts.</li>
<li><strong>Application files:</strong> connected Macs’ application catalogs, names, identifiers, usage timestamps and related metadata, and application icons.</li>
<li><strong>Mac recovery records:</strong> identifiers, window geometry, settings and operation states needed to restore windows or system settings.</li>
<li><strong>Diagnostics:</strong> local connection, error and timing logs.</li>
</ul>
<p>In the reviewed version, session screen thumbnails are held in memory; no Remones code persisting those thumbnails as image files was identified.</p>
<p>OS backups, system clipboard sharing, and storage by other applications follow their respective settings and policies.</p>
</section>
<section id="p4"><h2>4. Purchases and external services</h2>
<p>Remones Plus uses Apple StoreKit for purchases, restoration and subscription status. The app processes product and transaction information, expiration dates and renewal status. Remones does not receive your payment card number or Apple Account password.</p>
<p>Apple’s payment, distribution and diagnostic processing is governed by <a href="https://www.apple.com/legal/privacy/en-ww/" rel="noopener">Apple’s Privacy Policy</a>.</p>
<p>Downloading the Mac Host or viewing documents through GitHub or GitHub Pages exposes access information, such as your IP address, to GitHub. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub Privacy Statement</a>.</p>
<p>VPN use is optional. Your chosen VPN provider and network administrator may process information under their own terms.</p>
</section>
<section id="p5"><h2>5. Advertising, analytics and diagnostics</h2>
<p>No advertising, third-party usage analytics, or third-party crash-reporting SDK was identified in the reviewed app implementation. Remones has no proprietary advertising tracking or automatic local-log upload feature.</p>
<p>Diagnostic sharing through the OS or Apple services follows your settings and Apple’s mechanisms.</p>
</section>
<section id="p6"><h2>6. Choices, retention and deletion</h2>
<p>Clipboard synchronization is off by default. Disable synchronization, audio or Picture in Picture when you do not want those features. Picture in Picture may continue displaying Mac video or playing audio after you leave the main view.</p>
<p>The computer-removal feature removes the corresponding pairing and cached application information. Recent items and workspaces may require separate removal. Revoke the approved client on the Mac as appropriate.</p>
<p>Local records may remain until removed or replaced. Log retention is managed by the OS and relevant logging mechanism. Uninstalling the app does not necessarily erase Keychain entries, Mac-side data, backups or Apple purchase records. The developer cannot remotely delete data stored on your devices.</p>
</section>
<section id="p7"><h2>7. Security</h2>
<p>Connections use TLS. During initial pairing, compare the six-digit codes on both devices and approve only the intended connection. Encryption alone does not authenticate the initial peer.</p>
</section>
<section id="p8"><h2>8. Contact and changes</h2>
<p>If you voluntarily provide contact details, descriptions or logs for support, they will be used for responding and investigating the issue and retained only as needed for that purpose and applicable legal obligations. Do not send secret keys or unnecessary personal information.</p>
<p>Changes to this policy will be published here with an updated effective date.</p>
</section>
</div>
</div>
"""
    return {"slug": "privacy", "nav": None, "noindex": True,
            "title": "Privacy Policy (draft)",
            "description": "Remones Privacy Policy (pre-publication draft).",
            "body": body}


def terms() -> dict:
    body = _head("Remones Terms of Use", "Terms of Use") + f"""
<div class="wrap doc">
<nav class="toc" aria-label="Contents"><p class="toc-title">Contents</p><ol>
<li><a href="#t1">1. Applicable agreement</a></li>
<li><a href="#t2">2. Authorized use</a></li>
<li><a href="#t3">3. Requirements and remote actions</a></li>
<li><a href="#t4">4. Remones Plus</a></li>
<li><a href="#t5">5. Warranty and liability</a></li>
<li><a href="#t6">6. Mac Host and source code</a></li>
<li><a href="#t7">7. Privacy and changes</a></li>
</ol></nav>
<div class="doc-main legal">
{_meta()}
<section id="t1"><h2>1. Applicable agreement</h2>
<p>Use <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Apple’s Standard EULA</a> for the Remones iPhone/iPad app distributed through the App Store. These terms supplement it with Remones-specific use and subscription conditions. They do not override the Standard EULA or mandatory legal rights.</p>
</section>
<section id="t2"><h2>2. Authorized use</h2>
<p>Use Remones only with computers you own or are authorized to control.</p>
<p>Do not use it for unauthorized access, surveillance without required consent, bypassing authentication or approval, unlawfully obtaining information, infringing others’ rights, or other illegal purposes.</p>
<p>You are responsible for checking the destination computer, input, clipboard sharing and remote actions, and for obtaining necessary authorization and consent.</p>
</section>
<section id="t3"><h2>3. Requirements and remote actions</h2>
<p>You provide and manage the Mac Host, client devices, network and required OS permissions. A VPN is optional. Network and third-party charges are your responsibility.</p>
<p>Remote input can modify files, send messages, make purchases or trigger other actions. Confirm the destination and outcome of important operations and maintain appropriate backups.</p>
<p>These terms do not promise future Windows, Android or other platform support.</p>
</section>
<section id="t4"><h2>4. Remones Plus</h2>
<p>Remones Plus is an optional auto-renewable subscription. In the reviewed version it provides paid icon colors and matching in-app accent colors.</p>
<p>{_ph("Plan, price and free-trial table: complete after the production App Store Connect configuration is final")}</p>
<p>Check the app and Apple purchase confirmation for the actual price, currency, taxes, benefits and trial eligibility. The yearly plan is billed as one annual amount.</p>
<ul>
<li>Apple processes purchases through your Apple Account.</li>
<li>Apple determines trial eligibility. Unless canceled before the trial ends, the trial converts to a paid yearly subscription at the displayed annual price.</li>
<li>Subscriptions renew for the same period until canceled. Cancel through Apple at least 24 hours before renewal or trial expiration to avoid the next charge.</li>
<li>Manage or cancel in Settings → your name → Subscriptions, or <a href="https://apps.apple.com/account/subscriptions" rel="noopener">Apple’s subscription management page</a>. Uninstalling Remones does not cancel a subscription.</li>
<li>Check Apple’s subscription screen for the access end date. Canceling a trial may end trial access.</li>
<li>Restore purchases using the Apple Account used for purchase.</li>
<li>Price changes follow Apple’s notice and consent procedures and applicable law.</li>
</ul>
<p>Apple transactions are also governed by the applicable Apple Media Services terms. Request refunds through <a href="https://reportaproblem.apple.com/" rel="noopener">Apple’s refund service</a>. Eligibility follows Apple’s rules and applicable law; statutory rights remain unaffected. See <a href="https://support.apple.com/en-us/118223" rel="noopener">Apple’s refund guidance</a>.</p>
</section>
<section id="t5"><h2>5. Warranty and liability</h2>
<p>To the extent permitted by applicable law, Remones is provided as is and as available, without a guarantee of continuous connectivity, compatibility with a particular environment, or uninterrupted or error-free operation. The Standard EULA’s warranty and liability provisions apply.</p>
<p>Nothing here excludes rights or liabilities that applicable consumer protection or other mandatory law does not allow to be excluded or limited.</p>
</section>
<section id="t6"><h2>6. Mac Host and source code</h2>
<p>The Mac Host is distributed separately from the App Store client. Check the applicable license for the Host source and each included component before using, modifying or redistributing them. Public source availability alone does not grant unrestricted reuse rights.</p>
<p>{_ph("Mac Host license name, text, scope and URL: complete once confirmed")}</p>
</section>
<section id="t7"><h2>7. Privacy and changes</h2>
<p>See the <a href="~/privacy/">Privacy Policy</a>.</p>
<p>Changes to these terms will be published with an effective date and any required notice or consent process. Subscription changes also follow Apple’s procedures.</p>
</section>
</div>
</div>
"""
    return {"slug": "terms", "nav": None, "noindex": True,
            "title": "Terms of Use (draft)",
            "description": "Remones Terms of Use (pre-publication draft).",
            "body": body}
