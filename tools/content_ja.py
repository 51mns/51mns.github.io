"""Japanese pages (default language).

Terminology: Desktop / Display / Input / Audio / Home stay in English;
only Shelf is translated (シェルフ). Wording follows Client/Localizable.xcstrings.
"""

from __future__ import annotations

import components as c
import site_config as cfg
import legal_ja
import demos

HOST = cfg.MAC_APP_NAME


def home() -> dict:
    body = f"""
<section class="hero2" data-hero aria-labelledby="hero-title">
<div class="wrap">
<p class="eyebrow">{c.picture("assets/img/icon-standard-128.webp", "assets/img/icon-standard-128-dark.webp", "", 128, 128, lazy=False)}iPhone・iPad 用リモートデスクトップ</p>
<h1 id="hero-title" class="display">iPhone&nbsp;が、<wbr>あなたの&nbsp;Mac&nbsp;になる。</h1>
<p class="lead">Mac の画面を映すだけではありません。アプリのウインドウを iPhone の画面にぴったり合わせて、指でもキーボードでも、いつもどおりに作業できます。サーバーもアカウントも使いません。</p>
<div class="actions">
{c.app_store_button("ja")}
<a class="btn btn-primary" href="~/mac/">{c.icon("laptop")}Mac アプリを入手</a>
</div>
<p class="fineprint">iPhone・iPad（iOS / iPadOS {cfg.MIN_IOS} 以降）と、Mac（macOS {cfg.MIN_MACOS} 以降）で使います。</p>
<div class="hero-stage" data-demo="hero">
{demos.hero("ja")}
<ol class="demo-steps">
<li><b>1</b>指で動かすと、Mac のカーソルが動く</li>
<li><b>2</b>開いたウインドウが、iPhone の画面にぴったり収まる</li>
</ol>
</div>
</div>
</section>

<div class="values" id="features">
<div class="wrap">

<section class="value" aria-labelledby="v1-title">
<div class="value-text">
<span class="kicker">Window</span>
<h2 id="v1-title" class="display">ピンチしなくても、<wbr>読める。</h2>
<p class="lead">Mac の大きな画面を小さく映すと、文字は読めません。Remones は Mac のアプリをひとつ選ぶと、そのウインドウを iPhone や iPad の画面サイズに合わせて表示します。</p>
<ul class="ticks">
<li>文字の大きさも調整できます。</li>
<li>Mac の画面全体を見たいときは Display に切り替え。</li>
</ul>
</div>
<div class="stage" data-scrub>
{demos.window_demo("ja")}
<div class="stage-caption" aria-hidden="true"><span class="chip s-anim">Display</span><span class="chip s-anim">Window</span></div>
</div>
</section>

<section class="value" aria-labelledby="v2-title">
<div class="value-text">
<span class="kicker">複数の Mac</span> <span class="badge badge-plus">Plus</span>
<h2 id="v2-title" class="display">すべての Mac が、<wbr>ひとつの Home に。</h2>
<p class="lead">自宅の Mac も、仕事の Mac も。Home に並べて、開く前からオンラインかどうかが分かります。</p>
<ul class="ticks">
<li>待機中は状態だけを確認。「開く」まで画面は送られません。</li>
<li>一度つないだ Mac のアプリは、オフラインでも Home に残ります。</li>
<li>シェルフから、ほかのウインドウや Mac へすぐ移れます。</li>
</ul>
</div>
<div class="stage" data-scrub>
{demos.macs_demo("ja")}
</div>
</section>

<section class="value" aria-labelledby="v3-title">
<div class="value-text">
<span class="kicker">外出先から</span> <span class="badge badge-plus">Plus</span>
<h2 id="v3-title" class="display">家の外でも。<wbr>ポート開放なしで。</h2>
<p class="lead">家では同じ Wi-Fi で、外出先では Tailscale で。iPhone は一度つないだ Mac の経路を覚えていて、使える経路を選んで接続を試みます。</p>
<ul class="ticks">
<li>Tailscale などの VPN を使うので、ルーターのポート開放は必要ありません。</li>
<li>Remones のサーバーもアカウントもありません。画面が私たちのサーバーを通ることはありません。</li>
</ul>
<p><a href="~/tailscale/">Tailscale での使い方</a></p>
</div>
<div class="stage" data-scrub>
{demos.remote_demo("ja")}
</div>
</section>

<section class="value" aria-labelledby="v4-title">
<div class="value-text">
<span class="kicker">Input</span>
<h2 id="v4-title" class="display">指でも、<wbr>キーボードでも。</h2>
<p class="lead">画面に直接触れる「タッチ」、指でカーソルを動かす「トラックパッド」、その両方を使い分ける「Hybrid」。使い方に合わせて入力モードを選べます。</p>
<ul class="ticks">
<li>iPhone のキーボードで入力。日本語入力にも対応。</li>
<li>iPhone でコピーしたテキストを Mac にペースト。</li>
<li>操作に合わせた触覚フィードバック。</li>
</ul>
</div>
<div class="stage" data-demo="input">
{demos.input_demo("ja")}
</div>
</section>

<aside class="more-features" aria-labelledby="more-title">
<h2 id="more-title" class="more-title">その他の機能</h2>
<div class="card more-item"><div class="glyph">{c.icon("pip")}</div><div><h3>Audio とピクチャ・イン・ピクチャ</h3><p>Mac の音を iPhone で再生。ほかのアプリを使いながら、Mac の画面を小窓で確認できます（小窓は表示のみ）。</p></div></div>
</aside>

</div>
</div>

<section class="section playground" id="try" aria-labelledby="try-title">
<div class="wrap">
<div class="section-head">
<span class="eyebrow">試してみる</span>
<h2 id="try-title" class="display">さわって、<wbr>確かめる。</h2>
<p class="lead">表示と入力モードを切り替えて、iPhone の画面を指やマウスで操作してみてください。Dock のアプリをクリックすると、ウインドウが開きます。</p>
</div>
{demos.playground("ja")}
</div>
</section>

<section class="section" id="how" aria-labelledby="how-title">
<div class="wrap">
<div class="section-head">
<span class="eyebrow">はじめかた</span>
<h2 id="how-title" class="display">3 ステップで、<wbr>はじめられます。</h2>
</div>
<ol class="flow" data-reveal>
<li><h3>iPhone に Remones を入れる</h3><p>iPhone・iPad 用の Remones は App Store で近日公開です。</p></li>
<li><h3>Mac に Mac アプリを入れる</h3><p>操作したい Mac に「{HOST}」を入れて、画面収録とアクセシビリティを許可します。</p><a href="~/mac/">Mac アプリについて</a></li>
<li><h3>ペアリングして、開く</h3><p>iPhone で Mac を選び、表示されたコードを確かめて Mac で承認。あとは「開く」だけです。</p><a href="~/setup/">セットアップガイド</a></li>
</ol>
</div>
</section>

<section class="section privacy2" id="privacy" aria-labelledby="privacy-title">
<div class="wrap">
<div class="band">
<span class="eyebrow">プライバシー</span>
<h2 id="privacy-title" class="display">あいだにあるのは、<wbr>あなたのネットワークだけ。</h2>
<p class="lead" style="max-width:40rem">Remones には中継サーバーがありません。だから、あなたの画面を私たちが見ることはできません。</p>
{demos.privacy_diagram("ja")}
<div class="grid">
<div class="point"><h3>直接つながる</h3><p>ローカルネットワーク、またはあなたが用意した VPN を通ります。画面・音声・入力が Remones のサーバーを経由することはありません。</p></div>
<div class="point"><h3>アカウント不要</h3><p>Remones 独自のアカウント登録はありません。メールアドレスも求めません。</p></div>
<div class="point"><h3>コードを照合して承認</h3><p>初回は両方の画面に出る 6 桁のコードを確かめ、Mac で承認します。通信は TLS で暗号化されます。</p></div>
<div class="point"><h3>広告・解析なし</h3><p>広告や第三者の利用解析 SDK は組み込んでいません。ログも自動では送信しません。</p></div>
</div>
</div>
</div>
</section>

<section class="section" id="plus" aria-labelledby="plus-title">
<div class="wrap">
<div class="card" style="padding:32px">
{c.accent_strip()}
<span class="eyebrow">Remones Plus</span>
<h2 id="plus-title" class="display">外出先から、<wbr>いつもの Mac へ。</h2>
<p class="lead" style="max-width:40rem">同じネットワークの Mac 1 台には無料で接続できます。Remones Plus では、外出先からの接続、2 台目以降の Mac、ピクチャ・イン・ピクチャ、追加のアイコンカラーなどを使えます。</p>
{c.icon_row("ja")}
<p class="fineprint">月額・年額のほかに買い切りを選べます。購入はストアごとで、同じ Apple ID の iPhone・iPad で使えます。Mac アプリは無料です。</p>
</div>
</div>
</section>

<section class="section final-dl" id="download" data-final-download aria-labelledby="download-title">
<div class="wrap">
{c.app_icon("Remones のアプリアイコン", "icon-big")}
<h2 id="download-title" class="display">Remones を、<wbr>はじめよう。</h2>
<p class="lead" style="max-width:36rem;margin:0 auto">iPhone・iPad のアプリと、Mac のアプリ。ふたつそろえば準備完了です。</p>
{platform_list()}
</div>
</section>
"""
    return {
        "slug": "",
        "nav": "home",
        "dl_bar": True,
        "scripts": ["assets/js/playground.js"],
        "title": "Remones — iPhone が、あなたの Mac になる。",
        "title_is_full": True,
        "description": "Remones は iPhone・iPad から自分の Mac を操作するリモートデスクトップアプリ。ウインドウを iPhone の画面に合わせて表示し、複数の Mac を Home で切り替え、外出先からも Tailscale で接続。中継サーバーやアカウントは不要です。",
        "og_alt": "Remones のアイコンと「iPhone が、あなたの Mac になる。」",
        "body": body,
    }


def platform_list() -> str:
    return f"""<ul class="platforms">
<li class="card platform">
<div class="meta">{c.icon("phone")}<div><h3>iPhone・iPad</h3><span class="badge badge-soon">近日公開</span></div></div>
<p>Remones 本体です。Mac を探して接続し、操作します。</p>
<dl><dt>対応 OS</dt><dd>iOS / iPadOS {cfg.MIN_IOS} 以降</dd><dt>配布</dt><dd>App Store</dd></dl>
<div class="actions">{c.app_store_button("ja")}</div>
</li>
<li class="card platform">
<div class="meta">{c.icon("laptop")}<div><h3>Mac（{HOST}）</h3><span class="badge badge-soon">準備中</span></div></div>
<p>操作される側の Mac に入れるアプリです。iPhone・iPad からの接続を受け付け、画面と音声を送ります。</p>
<dl><dt>対応 OS</dt><dd>macOS {cfg.MIN_MACOS} 以降</dd><dt>配布</dt><dd>GitHub Releases</dd></dl>
<div class="actions"><a class="btn btn-primary" href="~/mac/">{c.icon("laptop")}Mac アプリを入手</a></div>
</li>
</ul>"""


def download() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">ホーム</a> / ダウンロード</p>
<h1>ダウンロード</h1>
<p class="lead">Remones は、操作する側の iPhone・iPad と、操作される側の Mac の両方にアプリを入れて使います。</p>
</div>
<div class="wrap" style="padding-top:24px;padding-bottom:72px">
{platform_list()}
<p class="fineprint" style="margin-top:24px">対応するプラットフォームが増えたときは、このページに追加します。</p>
</div>
"""
    return {"slug": "download", "nav": None, "title": "ダウンロード",
            "description": "Remones の iPhone・iPad アプリと Mac アプリ（" + HOST + "）の入手先と対応 OS。",
            "body": body}


def mac() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">ホーム</a> / <a href="~/download/">ダウンロード</a> / Mac アプリ</p>
<h1>Mac アプリ「{HOST}」</h1>
<p class="lead">iPhone・iPad の Remones から操作する Mac に入れるアプリです。接続を受け付け、Mac の画面と音声を送り、iPhone からの入力を Mac に伝えます。</p>
<div class="actions" style="margin-top:24px">{c.mac_download_button("ja")}</div>
<p class="fineprint" style="margin-top:12px">現在、配布の準備中です。公開したらこのページからダウンロードできるようになります。</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="このページの内容"><p class="toc-title">このページの内容</p><ol>
<li><a href="#requirements">動作環境</a></li>
<li><a href="#install">インストール</a></li>
<li><a href="#permissions">権限の許可</a></li>
<li><a href="#pairing">iPhone とペアリング</a></li>
<li><a href="#update">アップデート</a></li>
<li><a href="#troubleshooting">うまくいかないとき</a></li>
</ol></nav>
<div class="doc-main">

<section id="requirements" aria-labelledby="requirements-title">
<h2 id="requirements-title">動作環境</h2>
<table class="spec">
<tr><th scope="row">Mac</th><td>macOS {cfg.MIN_MACOS} 以降</td></tr>
<tr><th scope="row">iPhone・iPad</th><td>iOS / iPadOS {cfg.MIN_IOS} 以降の Remones アプリ</td></tr>
<tr><th scope="row">ネットワーク</th><td>同じ Wi-Fi などのローカルネットワーク。外出先からは Tailscale などの VPN（<a href="~/tailscale/">説明</a>）</td></tr>
<tr><th scope="row">必要な権限</th><td>画面収録（必須）、アクセシビリティ（操作する場合）</td></tr>
</table>
<p>Remones は、自分が所有する Mac、または操作する権限のある Mac でのみ使ってください。</p>
</section>

<section id="install" aria-labelledby="install-title">
<h2 id="install-title">インストール</h2>
<ol class="steps">
<li><h3>ダウンロードして「アプリケーション」へ</h3><p>上のボタンからファイルをダウンロードして開き、「{HOST}」を「アプリケーション」フォルダに移動します。</p></li>
<li><h3>はじめて開く</h3><p>「アプリケーション」フォルダから「{HOST}」を開きます。「インターネットからダウンロードされたアプリケーションです」と確認されたら「開く」を選びます。</p><p>ネットワークの接続について macOS から確認が表示された場合は、許可してください。許可しないと iPhone から見つけられません。</p></li>
</ol>
</section>

<section id="permissions" aria-labelledby="permissions-title">
<h2 id="permissions-title">権限の許可</h2>
<p>Mac の画面を送ったり、iPhone からの操作を Mac に伝えたりするには、macOS の許可が必要です。どちらも「システム設定」→「プライバシーとセキュリティ」で設定します。{HOST} のウインドウにある設定ボタンからも開けます。</p>
<ol class="steps">
<li><h3>画面収録（必須）</h3><p>「画面収録とシステムオーディオ録音」で {HOST} をオンにします。Mac の画面を iPhone に映すために使います。</p><p>許可しないと、iPhone に Mac の画面が表示されません（「Macで画面収録を許可してください」と表示されます）。</p></li>
<li><h3>アクセシビリティ（操作する場合）</h3><p>「アクセシビリティ」で {HOST} をオンにします。iPhone からのキーボードやポインタの操作を Mac に伝えるために使います。</p><p>許可しなくても、画面を見ることはできます。ただしキーボードやポインタでの操作はできません。</p></li>
<li><h3>{HOST} を開き直す</h3><p>画面収録を許可したあとは、{HOST} をいったん終了して、もう一度開いてください。macOS の仕組み上、開き直すまで許可が反映されないことがあります。</p></li>
</ol>
<div class="note"><p>Remones が画面や入力を使うのは、あなたが承認した iPhone・iPad と接続しているあいだだけです。画面や入力の内容が開発者のサーバーに送られることはありません。</p></div>
</section>

<section id="pairing" aria-labelledby="pairing-title">
<h2 id="pairing-title">iPhone とペアリング</h2>
<ol class="steps">
<li><h3>iPhone で Mac を追加</h3><p>iPhone の Remones で Home の「＋」をタップし、「近くのMac」から Mac を選びます。見つからない場合は、Mac の IP アドレスかホスト名を入力して追加できます。</p></li>
<li><h3>コードを確かめる</h3><p>iPhone にペアリングコードが表示されます。Mac にも同じコードが表示されるので、一致していることを確認します。</p></li>
<li><h3>Mac で承認</h3><p>Mac に表示される確認で承認します。<span class="ui-term">Always Allow</span> を選ぶと、この iPhone を登録して、次回から承認なしで接続できます。<span class="ui-term">Approve Once</span> はその回だけ許可します。</p><p>心当たりのない接続は <span class="ui-term">Reject</span> で拒否してください。</p></li>
</ol>
<p>登録した iPhone は、Mac 側の一覧から削除できます。iPhone 側では、Home の Mac の「…」メニューから登録を解除できます。</p>
</section>

<section id="update" aria-labelledby="update-title">
<h2 id="update-title">アップデート</h2>
<p>iPhone の Remones をアップデートしたあとに、Mac 側が古いと接続できないことがあります。「HostとRemonesのバージョンを確認してください」と表示されたら、Mac アプリも最新にしてください。</p>
<ol class="steps">
<li><h3>最新版をダウンロード</h3><p>このページから最新版をダウンロードします。</p></li>
<li><h3>入れ替える</h3><p>{HOST} を終了してから、「アプリケーション」フォルダのアプリを新しいものに置き換えます。</p></li>
<li><h3>開いて権限を確認</h3><p>{HOST} を開きます。画面収録やアクセシビリティの許可が外れていたら、もう一度許可して開き直してください。ペアリングはそのまま使えます。</p></li>
</ol>
</section>

<section id="troubleshooting" aria-labelledby="troubleshooting-title">
<h2 id="troubleshooting-title">うまくいかないとき</h2>
<h3>iPhone から Mac が見つからない</h3>
<ul>
<li>iPhone と Mac が同じ Wi-Fi（同じネットワーク）につながっているか確認してください。</li>
<li>iPhone の「設定」→「プライバシーとセキュリティ」→「ローカルネットワーク」で Remones がオンになっているか確認してください。オフだと近くの Mac を探せません。</li>
<li>Mac で {HOST} が起動しているか、Mac がスリープしていないか確認してください。</li>
<li>見つからない場合は、Home の「＋」から Mac の IP アドレスかホスト名を入力して追加できます。</li>
<li>別のネットワークから接続する場合は <a href="~/tailscale/">Tailscale を使う方法</a>をご覧ください。</li>
</ul>
<h3>画面が真っ黒・何も映らない</h3>
<p>画面収録が許可されていない可能性があります。<a href="#permissions">権限の許可</a>を確認し、許可したあとに {HOST} を開き直してください。</p>
<h3>画面は見えるが操作できない</h3>
<p>アクセシビリティが許可されているか確認してください。ほかの iPhone・iPad が同じ Mac を操作している場合は、そちらを閉じてからもう一度お試しください。</p>
<h3>「バージョンを確認してください」と表示される</h3>
<p>Mac アプリが古い可能性があります。<a href="#update">アップデート</a>の手順で最新にしてください。</p>
<p>解決しないときは、<a href="~/support/">サポート</a>をご覧ください。</p>
</section>

</div>
</div>
"""
    return {"slug": "mac", "nav": "mac", "title": f"Mac アプリ（{HOST}）",
            "description": f"Remones の Mac アプリ「{HOST}」の動作環境、インストール、画面収録とアクセシビリティの許可、iPhone とのペアリング、アップデート、困ったときの対処。",
            "body": body}


def setup() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">ホーム</a> / はじめかた</p>
<h1>はじめかた</h1>
<p class="lead">はじめて Remones を使うときの手順です。iPhone・iPad と Mac を手もとに用意して、同じ Wi-Fi につないでおくとスムーズです。</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="手順"><p class="toc-title">手順</p><ol>
<li><a href="#step-mac">1. Mac アプリを入れる</a></li>
<li><a href="#step-permissions">2. 権限を許可する</a></li>
<li><a href="#step-add">3. Mac を追加する</a></li>
<li><a href="#step-approve">4. Mac で承認する</a></li>
<li><a href="#step-open">5. 開く</a></li>
</ol></nav>
<div class="doc-main">

<section id="step-mac" aria-labelledby="step-mac-title">
<h2 id="step-mac-title">1. Mac アプリを入れる</h2>
<p>操作したい Mac で、このページのアドレスを開いてください。</p>
<p><code>51mns.github.io/remones/mac/</code></p>
<p>Mac アプリ「{HOST}」をダウンロードして、「アプリケーション」フォルダに入れ、開きます。詳しくは <a href="~/mac/#install">Mac アプリのインストール</a>をご覧ください。</p>
</section>

<section id="step-permissions" aria-labelledby="step-permissions-title">
<h2 id="step-permissions-title">2. 権限を許可する</h2>
<p>Mac の「システム設定」→「プライバシーとセキュリティ」で、{HOST} に次の 2 つを許可します。</p>
<ul>
<li><strong>画面収録とシステムオーディオ録音</strong> — Mac の画面を iPhone に映すために必要です。</li>
<li><strong>アクセシビリティ</strong> — iPhone から Mac を操作するために必要です。画面を見るだけなら、なくても使えます。</li>
</ul>
<p>許可したら、{HOST} をいったん終了して開き直します。</p>
</section>

<section id="step-add" aria-labelledby="step-add-title">
<h2 id="step-add-title">3. Mac を追加する</h2>
<p>iPhone・iPad で Remones を開き、Home の「＋」をタップします。Mac の追加方法は 3 つあります。</p>
<div class="grid grid-3" style="margin-bottom:16px">
<div class="card"><h3>近くのMac</h3><p>同じネットワークにある Mac が自動で表示されます。選ぶだけです。</p></div>
<div class="card"><h3>アドレスを入力</h3><p>Mac の IP アドレスかホスト名を入力します。ポートは空欄のままで通常は問題ありません（既定は {cfg.DEFAULT_PORT}）。</p></div>
<div class="card"><h3>Tailscale</h3><p>Mac の Tailscale 上の名前か、100. で始まるアドレスを入力します。<a href="~/tailscale/">詳しく</a></p></div>
</div>
<div class="note"><p>はじめて Mac を探すとき、iPhone に「ローカルネットワーク上のデバイスの検索」についての確認が表示されます。「許可」を選んでください。あとから変えるときは、iPhone の「設定」→「プライバシーとセキュリティ」→「ローカルネットワーク」で Remones をオンにします。</p></div>
</section>

<section id="step-approve" aria-labelledby="step-approve-title">
<h2 id="step-approve-title">4. Mac で承認する</h2>
<p>iPhone にペアリングコードが表示されます。Mac にも確認が表示されるので、同じコードであることを確かめてから承認します。</p>
<ul>
<li><span class="ui-term">Always Allow</span> — この iPhone を登録し、次回から承認なしで接続します。</li>
<li><span class="ui-term">Approve Once</span> — 今回だけ許可します。</li>
<li><span class="ui-term">Reject</span> — 拒否します。心当たりがない場合はこちらを選んでください。</li>
</ul>
</section>

<section id="step-open" aria-labelledby="step-open-title">
<h2 id="step-open-title">5. 開く</h2>
<p>Home に Mac が「オンライン」と表示されたら、「開く」をタップします。これで準備は完了です。</p>
<h3>使いはじめのヒント</h3>
<ul>
<li>セッション中のメニューから <span class="ui-term">Display</span>（表示）、<span class="ui-term">Input</span>（入力）、<span class="ui-term">Audio</span>（音声）を切り替えられます。</li>
<li>シェルフを開くと、ほかのウインドウ、アプリ、Mac にすぐ移れます。</li>
<li><span class="ui-term">Home</span> に戻っても、Mac との接続は保たれます。</li>
<li>iPhone でコピーしたテキストは、<span class="ui-term">Input</span> の「ペースト」で Mac に送れます。</li>
</ul>
<p>うまくいかないときは <a href="~/mac/#troubleshooting">うまくいかないとき</a>、または <a href="~/support/">サポート</a>をご覧ください。</p>
</section>

</div>
</div>
"""
    return {"slug": "setup", "nav": "setup", "title": "はじめかた",
            "description": "Remones を使いはじめる手順。Mac アプリのインストール、権限の許可、Mac の追加（近くのMac・アドレス入力・Tailscale）、Mac での承認まで。",
            "body": body}


def tailscale() -> dict:
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">ホーム</a> / 外出先から使う</p>
<h1>外出先から使う（Tailscale）</h1>
<p class="lead">Remones は、iPhone と Mac が直接つながるアプリです。自宅の外から使うときは、iPhone と Mac を同じ VPN に参加させます。ここでは Tailscale を使う方法を説明します。</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="このページの内容"><p class="toc-title">このページの内容</p><ol>
<li><a href="#how">しくみ</a></li>
<li><a href="#steps">設定の手順</a></li>
<li><a href="#manual">手動で追加する</a></li>
<li><a href="#safety">安全に使うために</a></li>
</ol></nav>
<div class="doc-main">

<section id="how" aria-labelledby="how-title">
<h2 id="how-title">しくみ</h2>
<p>Tailscale は、自分の端末どうしをつなぐ VPN サービスです。iPhone と Mac を同じ Tailscale のネットワーク（tailnet）に参加させると、離れた場所からでも Mac に届くようになります。</p>
<p>Remones は、近くにいるときは同じネットワーク（LAN）の経路を、届かないときは Tailscale の経路を使って接続します。Remones のサーバーを経由することはありません。Tailscale の利用は任意で、ほかの VPN でも使えます。</p>
</section>

<section id="steps" aria-labelledby="steps-title">
<h2 id="steps-title">設定の手順</h2>
<ol class="steps">
<li><h3>Tailscale を両方に入れる</h3><p>iPhone（または iPad）と Mac の両方に Tailscale をインストールします。<a href="https://tailscale.com/download" rel="noopener">Tailscale のダウンロード</a></p></li>
<li><h3>同じアカウントでサインイン</h3><p>両方の端末で同じ Tailscale アカウントにサインインし、同じ tailnet に参加させます。両方で Tailscale がオンになっていることを確認してください。</p></li>
<li><h3>一度、同じ Wi-Fi で接続する</h3><p>Mac で Tailscale がオンの状態で、同じ Wi-Fi にいるときに Remones で一度 Mac に接続します。このとき iPhone は、Mac の Tailscale 上のアドレスを覚えます。</p></li>
<li><h3>外出先で開く</h3><p>外出先では iPhone の Tailscale をオンにして、Remones の Home からいつもどおり Mac を開きます。</p></li>
</ol>
<p>Tailscale の使い方は <a href="https://tailscale.com/docs/features/magicdns" rel="noopener">Tailscale のドキュメント</a>もご覧ください。</p>
</section>

<section id="manual" aria-labelledby="manual-title">
<h2 id="manual-title">手動で追加する</h2>
<p>同じ Wi-Fi で接続できない場合は、Tailscale のアドレスを直接入力して追加できます。Home の「＋」から、アドレス欄に次のどちらかを入力します。</p>
<ul>
<li>Mac の Tailscale 上の名前（MagicDNS 名）。短い名前でも、完全な名前でも入力できます。</li>
<li><code>100.</code> で始まる Mac の Tailscale アドレス。</li>
</ul>
<p>Mac の名前とアドレスは、Mac の Tailscale アプリで確認できます。MagicDNS については <a href="https://tailscale.com/docs/features/magicdns" rel="noopener">Tailscale の MagicDNS の説明</a>をご覧ください。はじめて接続するときは、Mac での承認が必要です。</p>
</section>

<section id="safety" aria-labelledby="safety-title">
<h2 id="safety-title">安全に使うために</h2>
<div class="warn"><p>Mac のポート（既定は {cfg.DEFAULT_PORT}）を、ルーターのポート開放などでインターネットに直接公開しないでください。外から使うときは、Tailscale などの VPN を使ってください。</p></div>
<p>通信は TLS で暗号化され、ペアリング済みの端末だけが接続できます。接続できる端末は、Mac の {HOST} で確認・削除できます。</p>
</section>

</div>
</div>
"""
    return {"slug": "tailscale", "nav": "setup", "title": "外出先から使う（Tailscale）",
            "description": "Tailscale を使って、自宅の外から iPhone・iPad の Remones で Mac に接続する方法。設定の手順、MagicDNS 名での手動追加、安全に使うための注意。",
            "body": body}


def support() -> dict:
    faq = [
        ("何が必要ですか？",
         f"<p>iOS / iPadOS {cfg.MIN_IOS} 以降の iPhone または iPad と、macOS {cfg.MIN_MACOS} 以降の Mac が必要です。Mac には Mac アプリ「{HOST}」を入れます。</p>"),
        ("Windows や Android でも使えますか？",
         "<p>現在は、iPhone・iPad から Mac を操作する組み合わせに対応しています。</p>"),
        ("アカウント登録は必要ですか？",
         "<p>必要ありません。iPhone と Mac をペアリングするだけで使えます。</p>"),
        ("画面や入力の内容はどこかに送られますか？",
         "<p>iPhone と Mac のあいだで直接やりとりします。開発者のサーバーに送られることはありません。</p>"),
        ("通信は暗号化されていますか？",
         "<p>はい。端末間の通信には TLS を使います。はじめて接続するときは、iPhone と Mac に表示される 6 桁のコードを照らし合わせて、正しい Mac であることを確かめてから承認してください。</p>"),
        ("自宅の外から使えますか？",
         "<p>Remones Plus と Tailscale などの VPN を使うと接続できます。<a href=\"~/tailscale/\">外出先から使う</a>をご覧ください。</p>"),
        ("複数の Mac を登録できますか？",
         "<p>はい。Remones Plus で 2 台目以降の Mac を Home から開けます。</p>"),
        ("2 台の iPhone から同時に操作できますか？",
         "<p>1 台の Mac を操作できるのは、同時に 1 台です。ほかの端末で接続中の場合は、そちらを閉じてからもう一度お試しください。</p>"),
        ("画面が真っ黒になります",
         "<p>Mac で画面収録が許可されていない可能性があります。<a href=\"~/mac/#permissions\">権限の許可</a>を確認し、許可したあとに Mac アプリを開き直してください。</p>"),
        ("画面は見えるのに操作できません",
         "<p>Mac で {host} にアクセシビリティを許可してください。</p>".format(host=HOST)),
        ("iPhone から Mac が見つかりません",
         "<p>同じ Wi-Fi につながっているか、iPhone の「設定」→「プライバシーとセキュリティ」→「ローカルネットワーク」で Remones がオンになっているかを確認してください。<a href=\"~/mac/#troubleshooting\">うまくいかないとき</a>にも対処法があります。</p>"),
        ("ペーストのたびに許可を求められます",
         "<p>iPhone でコピーしたテキストを Mac に送るときは、セッションメニューの Input から「ペースト」をタップしてください。この方法なら、iOS の確認なしで送れます。</p>"),
        ("Mac の登録を解除するには？",
         "<p>iPhone では、Home の Mac の「…」メニューから登録を解除します。Mac 上のファイルやアプリは削除されません。Mac 側の承認済み端末も、必要に応じて Mac アプリから削除してください。</p>"),
        ("Remones Plus とは？",
         "<p>外出先からの接続や 2 台目以降の Mac などを使える追加プランです。月額・年額・買い切りから選べます。</p>"),
        ("購入した Plus を iPad でも使えますか？",
         "<p>はい。購入はストアごとで、同じ Apple ID の iPhone・iPad で使えます。別の端末では購入画面の「購入を復元」をタップしてください。</p>"),
    ]
    items = "\n".join(f'<details><summary>{q}</summary><div class="answer">{a}</div></details>' for q, a in faq)
    body = f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">ホーム</a> / サポート</p>
<h1>サポート</h1>
<p class="lead">よくある質問と、問題を報告する方法です。設定の手順は<a href="~/setup/">はじめかた</a>をご覧ください。</p>
</div>
<div class="wrap doc">
<nav class="toc" aria-label="このページの内容"><p class="toc-title">このページの内容</p><ol>
<li><a href="#faq">よくある質問</a></li>
<li><a href="#report">問題を報告する</a></li>
</ol></nav>
<div class="doc-main">
<section id="faq" aria-labelledby="faq-title">
<h2 id="faq-title">よくある質問</h2>
<div class="faq">
{items}
</div>
</section>

<section id="report" aria-labelledby="report-title">
<h2 id="report-title">問題を報告する</h2>
<p>接続できないなどの問題は、次の情報を添えてお知らせください。原因の特定が早くなります。</p>
<ol class="steps">
<li><h3>接続診断をコピー</h3><p>接続に失敗したときに表示される「接続診断をコピー」をタップします。iPhone のクリップボードに 1 行の診断情報がコピーされます。</p><p>診断情報に含まれるのは、アプリのビルド、失敗の種類、どの段階まで接続できたか、といった情報だけです。端末名、IP アドレス、ホスト名、鍵、ペアリングコードは含まれません。</p></li>
<li><h3>状況を書き添える</h3><p>いつ、何をしたときに起きたか。iPhone・iPad の機種と iOS のバージョン、Mac の macOS のバージョン、同じ Wi-Fi か Tailscale か、も書いてください。</p></li>
<li><h3>送る</h3><p>お問い合わせ窓口は準備中です。TestFlight でテストに参加している方は、TestFlight アプリのフィードバックから送ってください。</p></li>
</ol>
<div class="note"><p>ペアリングの鍵やパスワードなどの秘密の情報、必要のない個人情報は送らないでください。</p></div>
</section>
</div>
</div>
"""
    return {"slug": "support", "nav": "support", "title": "サポート",
            "description": "Remones のよくある質問と、問題を報告する方法（接続診断のコピー）。",
            "body": body}


def pages() -> list[dict]:
    return [home(), download(), mac(), setup(), tailscale(), support(), legal_ja.privacy(), legal_ja.terms()]
