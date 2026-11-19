"""English pages (mirror of content_ja.py under /en/)."""

from __future__ import annotations

import components as c
import site_config as cfg
import legal_en
import demos

HOST = cfg.MAC_APP_NAME


def home() -> dict:
    body = f"""
<section class="hero2" data-hero aria-labelledby="hero-title">
<div class="wrap">
<p class="eyebrow">{c.picture("assets/img/icon-standard-128.webp", "assets/img/icon-standard-128-dark.webp", "", 128, 128, lazy=False)}Remote desktop for iPhone and iPad</p>
<h1 id="hero-title" class="display">Your iPhone becomes your Mac.</h1>
<p class="lead">Not just a mirrored screen. Remones fits a Mac app’s window to your iPhone, so you can work the way you always do — with your fingers or a keyboard. No servers, no account.</p>
<div class="actions">
{c.app_store_button("en")}
<a class="btn btn-primary" href="~/mac/">{c.icon("laptop")}Get the Mac app</a>
</div>
<p class="fineprint">For iPhone and iPad (iOS / iPadOS {cfg.MIN_IOS} or later) with a Mac (macOS {cfg.MIN_MACOS} or later).</p>
<div class="hero-stage" data-demo="hero">
{demos.hero("en")}
<ol class="demo-steps">
<li><b>1</b>Move your finger and the Mac’s cursor follows</li>
<li><b>2</b>The window you open fits your iPhone screen</li>
</ol>
</div>
</div>
</section>

<div class="values" id="features">
<div class="wrap">

<section class="value" aria-labelledby="v1-title">
<div class="value-text">
<span class="kicker">Window</span>
<h2 id="v1-title" class="display">Readable. No pinching.</h2>
<p class="lead">Shrink a big Mac screen onto a phone and the text becomes unreadable. Pick one Mac app in Remones and its window is fitted to your iPhone or iPad screen.</p>
<ul class="ticks">
<li>Adjust the text size to taste.</li>
<li>Switch to Display when you want the whole Mac screen.</li>
</ul>
</div>
<div class="stage" data-scrub>
{demos.window_demo("en")}
<div class="stage-caption" aria-hidden="true"><span class="chip s-anim">Display</span><span class="chip s-anim">Window</span></div>
</div>
</section>

<section class="value" aria-labelledby="v2-title">
<div class="value-text">
<span class="kicker">Multiple Macs</span>
<h2 id="v2-title" class="display">Every Mac, on one Home.</h2>
<p class="lead">Your home Mac and your work Mac, side by side. Home shows which ones are online before you open them.</p>
<ul class="ticks">
<li>While waiting, only status is checked — no screen is sent until you tap Open.</li>
<li>Apps from a Mac you’ve connected to stay on Home even when it’s offline.</li>
<li>The Shelf takes you to other windows and Macs in a moment.</li>
</ul>
</div>
<div class="stage" data-scrub>
{demos.macs_demo("en")}
</div>
</section>

<section class="value" aria-labelledby="v3-title">
<div class="value-text">
<span class="kicker">Away from home</span>
<h2 id="v3-title" class="display">Away from home. No port forwarding.</h2>
<p class="lead">Same Wi-Fi at home, Tailscale when you’re out. Your iPhone remembers the routes to a Mac it has connected to and tries one that’s available.</p>
<ul class="ticks">
<li>With a VPN such as Tailscale, there’s no need for router port forwarding.</li>
<li>No Remones server, no account. Your screen never passes through our servers.</li>
</ul>
<p><a href="~/tailscale/">Using Remones with Tailscale</a></p>
</div>
<div class="stage" data-scrub>
{demos.remote_demo("en")}
</div>
</section>

<section class="value" aria-labelledby="v4-title">
<div class="value-text">
<span class="kicker">Input</span>
<h2 id="v4-title" class="display">Fingers or keyboard.</h2>
<p class="lead">Touch the screen directly, move the cursor like a Trackpad, or use Hybrid to have both. Choose the input mode that suits what you’re doing.</p>
<ul class="ticks">
<li>Type with the iPhone keyboard. Japanese input is supported.</li>
<li>Paste text you copied on your iPhone into the Mac.</li>
<li>Haptic feedback as you control the Mac.</li>
</ul>
</div>
<div class="stage" data-demo="input">
{demos.input_demo("en")}
</div>
</section>

<aside class="more-features" aria-labelledby="more-title">
<h2 id="more-title" class="more-title">More features</h2>
<div class="card more-item"><div class="glyph">{c.icon("pip")}</div><div><h3>Audio and Picture in Picture</h3><p>Play your Mac’s sound on your iPhone. Keep an eye on your Mac in a small window while you use other apps (the small window is view-only).</p></div></div>
</aside>

</div>
</div>

<section class="section playground" id="try" aria-labelledby="try-title">
<div class="wrap">
<div class="section-head">
<span class="eyebrow">Try it</span>
<h2 id="try-title" class="display">Get a feel for it.</h2>
<p class="lead">Switch the view and input mode, then use the iPhone screen with your finger or mouse. Click an app in the Dock to open a window.</p>
</div>
{demos.playground("en")}
</div>
</section>

<section class="section" id="how" aria-labelledby="how-title">
<div class="wrap">
<div class="section-head">
<span class="eyebrow">Get started</span>
<h2 id="how-title" class="display">Three steps to get going.</h2>
</div>
<ol class="flow" data-reveal>
<li><h3>Install Remones on your iPhone</h3><p>Remones for iPhone and iPad is coming soon to the App Store.</p></li>
<li><h3>Install the Mac app</h3><p>Install {HOST} on the Mac you want to control and allow Screen Recording and Accessibility.</p><a href="~/mac/">About the Mac app</a></li>
<li><h3>Pair, then open</h3><p>Choose your Mac on the iPhone, check the code and approve on the Mac. Then just tap Open.</p><a href="~/setup/">Setup guide</a></li>
</ol>
</div>
</section>

<section class="section privacy2" id="privacy" aria-labelledby="privacy-title">
<div class="wrap">
<div class="band">
<span class="eyebrow">Privacy</span>
<h2 id="privacy-title" class="display">Nothing in between but your own network.</h2>
<p class="lead" style="max-width:40rem">Remones has no relay servers — so there’s no way for us to see your screen.</p>
{demos.privacy_diagram("en")}
<div class="grid">
<div class="point"><h3>Direct connection</h3><p>Traffic goes over your local network or a VPN you set up. Screen, audio and input never pass through Remones servers.</p></div>
<div class="point"><h3>No account</h3><p>There is no Remones account to create, and no email address to give.</p></div>
<div class="point"><h3>Verify, then approve</h3><p>On first connection, check the six-digit code on both screens and approve on the Mac. Connections use TLS.</p></div>
<div class="point"><h3>No ads, no analytics</h3><p>No advertising or third-party analytics SDKs are built in, and logs are never uploaded automatically.</p></div>
</div>
</div>
</div>
</section>

<section class="section" id="plus" aria-labelledby="plus-title">
<div class="wrap">
<div class="card" style="padding:32px">
{c.accent_strip()}
<span class="eyebrow">Remones Plus</span>
<h2 id="plus-title" class="display">An icon in your colour.</h2>
<p class="lead" style="max-width:40rem">Remones Plus is a subscription that lets you choose the app icon and the matching in-app accent colour. Standard and Lemon are free.</p>
{c.icon_row("en")}
<p class="fineprint">Remones Plus is optional. Prices and free-trial terms are shown on the App Store and in the app’s purchase screen.</p>
</div>
</div>
</section>

<section class="section final-dl" id="download" data-final-download aria-labelledby="download-title">
<div class="wrap">
{c.app_icon("Remones app icon", "icon-big")}
<h2 id="download-title" class="display">Get started with Remones.</h2>
<p class="lead" style="max-width:36rem;margin:0 auto">One app for your iPhone or iPad, one for your Mac. That’s all you need.</p>
{platform_list()}
</div>
</section>
"""
    return {
        "slug": "",
        "nav": "home",
        "dl_bar": True,
        "scripts": ["assets/js/playground.js"],
        "title": "Remones — Your iPhone becomes your Mac.",
        "title_is_full": True,
        "description": "Remones is a remote desktop app for controlling your own Mac from iPhone and iPad. Windows fitted to your screen, all your Macs on one Home, and access from away via Tailscale. No relay servers, no account.",
        "og_alt": "The Remones icon and the line “Your iPhone becomes your Mac.”",
        "body": body,
    }


def platform_list() -> str:
    return f"""<ul class="platforms">
<li class="card platform">
<div class="meta">{c.icon("phone")}<div><h3>iPhone and iPad</h3><span class="badge badge-soon">Coming soon</span></div></div>
<p>The Remones app itself. Finds your Mac, connects, and lets you control it.</p>
<dl><dt>Requires</dt><dd>iOS / iPadOS {cfg.MIN_IOS} or later</dd><dt>Available on</dt><dd>App Store</dd></dl>
<div class="actions">{c.app_store_button("en")}</div>
</li>
<li class="card platform">
<div class="meta">{c.icon("laptop")}<div><h3>Mac ({HOST})</h3><span class="badge badge-soon">In preparation</span></div></div>
<p>The companion app for the Mac you control. It accepts connections from your iPhone or iPad and streams the screen and sound.</p>
<dl><dt>Requires</dt><dd>macOS {cfg.MIN_MACOS} or later</dd><dt>Available on</dt><dd>GitHub Releases</dd></dl>
<div class="actions"><a class="btn btn-primary" href="~/mac/">{c.icon("laptop")}Get the Mac app</a></div>
</li>
</ul>"""


def download() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">Home</a> / Download</p>
<h1>Download</h1>
<p class="lead">Remones uses two apps: one on the iPhone or iPad you control from, and one on the Mac you control.</p>
</div>
<div class="wrap" style="padding-top:24px;padding-bottom:72px">
{platform_list()}
<p class="fineprint" style="margin-top:24px">When more platforms are supported, they will be added to this page.</p>
</div>
"""
    return {"slug": "download", "nav": None, "title": "Download",
            "description": f"Where to get Remones for iPhone and iPad and the companion Mac app ({HOST}), with system requirements.",
            "body": body}


def mac() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">Home</a> / <a href="~/download/">Download</a> / Mac app</p>
<h1>The Mac app: {HOST}</h1>
<p class="lead">Install it on the Mac you want to control from Remones on your iPhone or iPad. It accepts connections, streams the Mac’s screen and sound, and passes your input to the Mac.</p>
<div class="actions" style="margin-top:24px">{c.mac_download_button("en")}</div>
<p class="fineprint" style="margin-top:12px">The download is being prepared. Once released, you can download it from this page.</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="On this page"><p class="toc-title">On this page</p><ol>
<li><a href="#requirements">Requirements</a></li>
<li><a href="#install">Install</a></li>
<li><a href="#permissions">Permissions</a></li>
<li><a href="#pairing">Pair with your iPhone</a></li>
<li><a href="#update">Updating</a></li>
<li><a href="#troubleshooting">Troubleshooting</a></li>
</ol></nav>
<div class="doc-main">

<section id="requirements" aria-labelledby="requirements-title">
<h2 id="requirements-title">Requirements</h2>
<table class="spec">
<tr><th scope="row">Mac</th><td>macOS {cfg.MIN_MACOS} or later</td></tr>
<tr><th scope="row">iPhone and iPad</th><td>The Remones app on iOS / iPadOS {cfg.MIN_IOS} or later</td></tr>
<tr><th scope="row">Network</th><td>A local network such as the same Wi-Fi. From elsewhere, a VPN such as Tailscale (<a href="~/tailscale/">guide</a>)</td></tr>
<tr><th scope="row">Permissions</th><td>Screen Recording (required), Accessibility (to control the Mac)</td></tr>
</table>
<p>Use Remones only with Macs you own or are authorized to control.</p>
</section>

<section id="install" aria-labelledby="install-title">
<h2 id="install-title">Install</h2>
<ol class="steps">
<li><h3>Download and move to Applications</h3><p>Download the file with the button above, open it, and move {HOST} to your Applications folder.</p></li>
<li><h3>Open it for the first time</h3><p>Open {HOST} from the Applications folder. If macOS says it was downloaded from the internet, choose Open.</p><p>If macOS asks about network access, allow it. Otherwise your iPhone can’t find the Mac.</p></li>
</ol>
</section>

<section id="permissions" aria-labelledby="permissions-title">
<h2 id="permissions-title">Permissions</h2>
<p>To share the Mac’s screen and pass your input to it, macOS needs your permission. Both are in System Settings → Privacy &amp; Security. The buttons in the {HOST} window open them too.</p>
<ol class="steps">
<li><h3>Screen Recording (required)</h3><p>Turn on {HOST} under Screen &amp; System Audio Recording. This is used to show the Mac’s screen on your iPhone.</p><p>Without it, your iPhone can’t show the Mac’s screen (Remones says “Allow Screen Recording on your Mac”).</p></li>
<li><h3>Accessibility (to control the Mac)</h3><p>Turn on {HOST} under Accessibility. This is used to pass keyboard and pointer input from your iPhone to the Mac.</p><p>Without it you can still view the screen, but you can’t type or use the pointer.</p></li>
<li><h3>Quit and reopen {HOST}</h3><p>After allowing Screen Recording, quit {HOST} and open it again. macOS may not apply the permission until the app is reopened.</p></li>
</ol>
<div class="note"><p>Remones uses the screen and input only while connected to an iPhone or iPad you approved. Screen and input content is never sent to a developer server.</p></div>
</section>

<section id="pairing" aria-labelledby="pairing-title">
<h2 id="pairing-title">Pair with your iPhone</h2>
<ol class="steps">
<li><h3>Add the Mac on your iPhone</h3><p>In Remones on your iPhone, tap “+” on Home and choose your Mac under Nearby Macs. If it isn’t listed, add it by entering the Mac’s IP address or host name.</p></li>
<li><h3>Check the code</h3><p>Your iPhone shows a pairing code. The Mac shows the same code — make sure they match.</p></li>
<li><h3>Approve on the Mac</h3><p>Approve the request on the Mac. <span class="ui-term">Always Allow</span> saves this iPhone so it can connect without approval next time. <span class="ui-term">Approve Once</span> allows this connection only.</p><p>If you don’t recognise the request, choose <span class="ui-term">Reject</span>.</p></li>
</ol>
<p>You can remove a saved iPhone from the list on the Mac. On the iPhone, remove a Mac from its “…” menu on Home.</p>
</section>

<section id="update" aria-labelledby="update-title">
<h2 id="update-title">Updating</h2>
<p>After you update Remones on your iPhone, an older Mac app may fail to connect. If Remones asks you to check the Host and Remones versions, update the Mac app too.</p>
<ol class="steps">
<li><h3>Download the latest version</h3><p>Download the latest version from this page.</p></li>
<li><h3>Replace the app</h3><p>Quit {HOST}, then replace the app in your Applications folder with the new one.</p></li>
<li><h3>Open it and check permissions</h3><p>Open {HOST}. If Screen Recording or Accessibility is no longer allowed, allow it again and reopen the app. Your pairings keep working.</p></li>
</ol>
</section>

<section id="troubleshooting" aria-labelledby="troubleshooting-title">
<h2 id="troubleshooting-title">Troubleshooting</h2>
<h3>My iPhone can’t find the Mac</h3>
<ul>
<li>Make sure your iPhone and Mac are on the same Wi-Fi network.</li>
<li>On your iPhone, check Settings → Privacy &amp; Security → Local Network and make sure Remones is on. Without it, Remones can’t look for nearby Macs.</li>
<li>Make sure {HOST} is running on the Mac and the Mac isn’t asleep.</li>
<li>You can also tap “+” on Home and enter the Mac’s IP address or host name.</li>
<li>To connect from a different network, see <a href="~/tailscale/">using Tailscale</a>.</li>
</ul>
<h3>The screen is black</h3>
<p>Screen Recording is probably not allowed. Check <a href="#permissions">Permissions</a>, then quit and reopen {HOST}.</p>
<h3>I can see the screen but can’t control it</h3>
<p>Check that Accessibility is allowed. If another iPhone or iPad is controlling the same Mac, close it there and try again.</p>
<h3>Remones asks me to check versions</h3>
<p>The Mac app is probably out of date. Follow the steps in <a href="#update">Updating</a>.</p>
<p>Still stuck? See <a href="~/support/">Support</a>.</p>
</section>

</div>
</div>
"""
    return {"slug": "mac", "nav": "mac", "title": f"Mac app ({HOST})",
            "description": f"Requirements, installation, Screen Recording and Accessibility permissions, pairing, updating and troubleshooting for {HOST}, the Remones Mac app.",
            "body": body}


def setup() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">Home</a> / Get started</p>
<h1>Get started</h1>
<p class="lead">Setting up Remones for the first time. It goes smoothly with your iPhone or iPad and your Mac nearby, on the same Wi-Fi.</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="Steps"><p class="toc-title">Steps</p><ol>
<li><a href="#step-mac">1. Install the Mac app</a></li>
<li><a href="#step-permissions">2. Allow permissions</a></li>
<li><a href="#step-add">3. Add your Mac</a></li>
<li><a href="#step-approve">4. Approve on the Mac</a></li>
<li><a href="#step-open">5. Open</a></li>
</ol></nav>
<div class="doc-main">

<section id="step-mac" aria-labelledby="step-mac-title">
<h2 id="step-mac-title">1. Install the Mac app</h2>
<p>On the Mac you want to control, open this address:</p>
<p><code>51mns.github.io/remones/en/mac/</code></p>
<p>Download {HOST}, move it to the Applications folder and open it. See <a href="~/mac/#install">installing the Mac app</a> for details.</p>
</section>

<section id="step-permissions" aria-labelledby="step-permissions-title">
<h2 id="step-permissions-title">2. Allow permissions</h2>
<p>On the Mac, open System Settings → Privacy &amp; Security and allow these two for {HOST}:</p>
<ul>
<li><strong>Screen &amp; System Audio Recording</strong> — needed to show the Mac’s screen on your iPhone.</li>
<li><strong>Accessibility</strong> — needed to control the Mac from your iPhone. Not required if you only want to view.</li>
</ul>
<p>Then quit {HOST} and open it again.</p>
</section>

<section id="step-add" aria-labelledby="step-add-title">
<h2 id="step-add-title">3. Add your Mac</h2>
<p>Open Remones on your iPhone or iPad and tap “+” on Home. There are three ways to add a Mac.</p>
<div class="grid grid-3" style="margin-bottom:16px">
<div class="card"><h3>Nearby Macs</h3><p>Macs on the same network appear automatically. Just pick yours.</p></div>
<div class="card"><h3>Enter an address</h3><p>Enter the Mac’s IP address or host name. You can usually leave the port empty (the default is {cfg.DEFAULT_PORT}).</p></div>
<div class="card"><h3>Tailscale</h3><p>Enter the Mac’s Tailscale name or its address beginning with 100. <a href="~/tailscale/">Learn more</a></p></div>
</div>
<div class="note"><p>The first time Remones looks for Macs, iOS asks whether it may find devices on your local network. Choose Allow. To change it later, go to Settings → Privacy &amp; Security → Local Network on your iPhone and turn on Remones.</p></div>
</section>

<section id="step-approve" aria-labelledby="step-approve-title">
<h2 id="step-approve-title">4. Approve on the Mac</h2>
<p>Your iPhone shows a pairing code, and the Mac shows a request. Check that the codes match, then approve.</p>
<ul>
<li><span class="ui-term">Always Allow</span> — saves this iPhone so it can connect without approval next time.</li>
<li><span class="ui-term">Approve Once</span> — allows this connection only.</li>
<li><span class="ui-term">Reject</span> — declines. Use this if you don’t recognise the request.</li>
</ul>
</section>

<section id="step-open" aria-labelledby="step-open-title">
<h2 id="step-open-title">5. Open</h2>
<p>When your Mac shows as online on Home, tap Open. You’re all set.</p>
<h3>Tips for your first session</h3>
<ul>
<li>The session menu switches between <span class="ui-term">Display</span>, <span class="ui-term">Input</span> and <span class="ui-term">Audio</span>.</li>
<li>Open the Shelf to jump to other windows, apps and Macs.</li>
<li>Going back to <span class="ui-term">Home</span> keeps the Mac connected.</li>
<li>To send text copied on your iPhone, use Paste in <span class="ui-term">Input</span>.</li>
</ul>
<p>Having trouble? See <a href="~/mac/#troubleshooting">Troubleshooting</a> or <a href="~/support/">Support</a>.</p>
</section>

</div>
</div>
"""
    return {"slug": "setup", "nav": "setup", "title": "Get started",
            "description": "How to start using Remones: install the Mac app, allow permissions, add your Mac (nearby, by address or via Tailscale) and approve it on the Mac.",
            "body": body}


def tailscale() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">Home</a> / Use it away from home</p>
<h1>Use it away from home (Tailscale)</h1>
<p class="lead">Remones connects your iPhone directly to your Mac. To use it away from home, put both on the same VPN. This page explains how to do that with Tailscale.</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="On this page"><p class="toc-title">On this page</p><ol>
<li><a href="#how">How it works</a></li>
<li><a href="#steps">Setting it up</a></li>
<li><a href="#manual">Adding a Mac manually</a></li>
<li><a href="#safety">Staying safe</a></li>
</ol></nav>
<div class="doc-main">

<section id="how" aria-labelledby="how-title">
<h2 id="how-title">How it works</h2>
<p>Tailscale is a VPN service that connects your own devices to each other. When your iPhone and Mac join the same Tailscale network (a tailnet), your Mac becomes reachable from anywhere.</p>
<p>Remones uses your local network when you’re nearby, and the Tailscale route when the local one can’t be reached. Nothing goes through Remones servers. Tailscale is optional; other VPNs work too.</p>
</section>

<section id="steps" aria-labelledby="steps-title">
<h2 id="steps-title">Setting it up</h2>
<ol class="steps">
<li><h3>Install Tailscale on both</h3><p>Install Tailscale on your iPhone (or iPad) and on your Mac. <a href="https://tailscale.com/download" rel="noopener">Download Tailscale</a></p></li>
<li><h3>Sign in to the same account</h3><p>Sign in to the same Tailscale account on both devices so they join the same tailnet, and make sure Tailscale is on for both.</p></li>
<li><h3>Connect once on the same Wi-Fi</h3><p>With Tailscale on for the Mac, connect to it once from Remones while you’re on the same Wi-Fi. Your iPhone then learns the Mac’s Tailscale address.</p></li>
<li><h3>Open it while away</h3><p>Away from home, turn on Tailscale on your iPhone and open your Mac from Remones’ Home as usual.</p></li>
</ol>
<p>For more on Tailscale itself, see the <a href="https://tailscale.com/docs/features/magicdns" rel="noopener">Tailscale documentation</a>.</p>
</section>

<section id="manual" aria-labelledby="manual-title">
<h2 id="manual-title">Adding a Mac manually</h2>
<p>If you can’t connect on the same Wi-Fi first, add the Mac by its Tailscale address. Tap “+” on Home and enter one of these as the address:</p>
<ul>
<li>The Mac’s Tailscale name (MagicDNS name). The short name and the full name both work.</li>
<li>The Mac’s Tailscale address, beginning with <code>100.</code></li>
</ul>
<p>The Tailscale app on your Mac shows both. See <a href="https://tailscale.com/docs/features/magicdns" rel="noopener">MagicDNS in the Tailscale docs</a>. The first connection still needs approval on the Mac.</p>
</section>

<section id="safety" aria-labelledby="safety-title">
<h2 id="safety-title">Staying safe</h2>
<div class="warn"><p>Don’t expose the Mac’s port (default {cfg.DEFAULT_PORT}) directly to the internet, for example with port forwarding on your router. Use a VPN such as Tailscale instead.</p></div>
<p>Connections are encrypted with TLS, and only paired devices can connect. You can review and remove paired devices in {HOST} on the Mac.</p>
</section>

</div>
</div>
"""
    return {"slug": "tailscale", "nav": "setup", "title": "Use it away from home (Tailscale)",
            "description": "How to connect to your Mac from Remones on iPhone and iPad when you’re away from home, using Tailscale. Setup, adding by MagicDNS name, and safety notes.",
            "body": body}


def support() -> dict:
    faq = [
        ("What do I need?",
         f"<p>An iPhone or iPad with iOS / iPadOS {cfg.MIN_IOS} or later, and a Mac with macOS {cfg.MIN_MACOS} or later running the Mac app, {HOST}.</p>"),
        ("Does it work with Windows or Android?",
         "<p>Remones currently supports controlling a Mac from an iPhone or iPad.</p>"),
        ("Do I need an account?",
         "<p>No. Just pair your iPhone with your Mac.</p>"),
        ("Is my screen or input sent anywhere?",
         "<p>It goes directly between your iPhone and your Mac, never to a developer server.</p>"),
        ("Is the connection encrypted?",
         "<p>Yes, connections use TLS. When you connect for the first time, compare the six-digit code on your iPhone and Mac to make sure it’s the right Mac before approving.</p>"),
        ("Can I use it away from home?",
         "<p>Yes, with a VPN such as Tailscale. See <a href=\"~/tailscale/\">Use it away from home</a>.</p>"),
        ("Can I add more than one Mac?",
         "<p>Yes. Your Macs appear side by side on Home and you can switch between them.</p>"),
        ("Can two iPhones control the same Mac at once?",
         "<p>One device controls a Mac at a time. If another device is connected, close it there and try again.</p>"),
        ("The screen is black",
         "<p>Screen Recording is probably not allowed on the Mac. Check <a href=\"~/mac/#permissions\">Permissions</a>, then quit and reopen the Mac app.</p>"),
        ("I can see the screen but can’t control it",
         f"<p>Allow Accessibility for {HOST} on the Mac.</p>"),
        ("My iPhone can’t find the Mac",
         "<p>Check that both are on the same Wi-Fi and that Remones is on under Settings → Privacy &amp; Security → Local Network on your iPhone. See <a href=\"~/mac/#troubleshooting\">Troubleshooting</a> for more.</p>"),
        ("iOS keeps asking before every paste",
         "<p>To send text copied on your iPhone, tap Paste under Input in the session menu. That way iOS doesn’t need to ask.</p>"),
        ("How do I remove a Mac?",
         "<p>On your iPhone, use the “…” menu of the Mac on Home. Files and apps on the Mac are not deleted. You can also remove the approved device in the Mac app.</p>"),
        ("What is Remones Plus?",
         "<p>An optional subscription that lets you choose the app icon and in-app accent colour. Standard and Lemon are free. Prices are shown in the app and on the App Store. Cancel in Settings → your name → Subscriptions on your iPhone.</p>"),
    ]
    items = "\n".join(f'<details><summary>{q}</summary><div class="answer">{a}</div></details>' for q, a in faq)
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">Home</a> / Support</p>
<h1>Support</h1>
<p class="lead">Frequently asked questions, and how to report a problem. For setup steps, see <a href="~/setup/">Get started</a>.</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="On this page"><p class="toc-title">On this page</p><ol>
<li><a href="#faq">FAQ</a></li>
<li><a href="#report">Report a problem</a></li>
</ol></nav>
<div class="doc-main">
<section id="faq" aria-labelledby="faq-title">
<h2 id="faq-title">FAQ</h2>
<div class="faq">
{items}
</div>
</section>

<section id="report" aria-labelledby="report-title">
<h2 id="report-title">Report a problem</h2>
<p>If something doesn’t work, such as connecting, please include the following. It helps find the cause much faster.</p>
<ol class="steps">
<li><h3>Copy the connection diagnostic</h3><p>When a connection fails, tap “Copy connection diagnostic”. A one-line diagnostic is copied to your iPhone’s clipboard.</p><p>It contains only the app build, the kind of failure and how far the connection got. It does not include device names, IP addresses, host names, keys or pairing codes.</p></li>
<li><h3>Describe what happened</h3><p>When it happened and what you were doing, your iPhone or iPad model and iOS version, your Mac’s macOS version, and whether you were on the same Wi-Fi or on Tailscale.</p></li>
<li><h3>Send it</h3><p>A contact address is being prepared. If you’re testing through TestFlight, please send feedback from the TestFlight app.</p></li>
</ol>
<div class="note"><p>Please don’t send pairing keys, passwords or other secrets, or personal information that isn’t needed.</p></div>
</section>
</div>
</div>
"""
    return {"slug": "support", "nav": "support", "title": "Support",
            "description": "Remones FAQ and how to report a problem with the connection diagnostic.",
            "body": body}


def pages() -> list[dict]:
    return [home(), download(), mac(), setup(), tailscale(), support(), legal_en.privacy(), legal_en.terms()]
