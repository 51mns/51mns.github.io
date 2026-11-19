"""Japanese legal pages, built from remones-legal-drafts.raw.md (2026-11-17).

DRAFT: not legal advice. Every page carries a draft banner and noindex.
Changes from the raw draft are limited to:
- placeholders rendered visibly (effective date, provider, contact, Host licence);
- the Plus price table replaced by a placeholder (prices are a local StoreKit
  configuration, not confirmed App Store Connect values);
- the privacy-policy link pointing at this site's /privacy/ page.
"""

from __future__ import annotations


def _ph(text: str) -> str:
    return f'<span class="placeholder">［{text}］</span>'


def _banner() -> str:
    return ('<div class="draft-banner" role="note"><strong>草案 — 公開前に確認中</strong>'
            'この文書は公開前の草案です。内容は確定しておらず、法的助言ではありません。</div>')


def _head(title: str, crumb: str) -> str:
    return f"""
<div class="wrap page-head">
<p class="breadcrumb"><a href="~/">ホーム</a> / {crumb}</p>
<h1>{title}</h1>
{_banner()}
</div>"""


def _meta() -> str:
    return f"""<ul class="legal-meta">
<li>施行日：{_ph("公開前に記入")}</li>
<li>提供者：{_ph("氏名または法人名を記入")}</li>
<li>お問い合わせ：{_ph("連絡先メールアドレスを記入")}</li>
</ul>"""


def privacy() -> dict:
    body = _head("Remones プライバシーポリシー", "プライバシーポリシー") + f"""
<div class="wrap doc">
<nav class="toc" aria-label="目次"><p class="toc-title">目次</p><ol>
<li><a href="#p1">1. 対象と基本方針</a></li>
<li><a href="#p2">2. 端末間で扱う情報</a></li>
<li><a href="#p3">3. 端末内に保存する情報</a></li>
<li><a href="#p4">4. 決済・外部サービス</a></li>
<li><a href="#p5">5. 広告・解析・診断</a></li>
<li><a href="#p6">6. 選択・保持・削除</a></li>
<li><a href="#p7">7. 安全性</a></li>
<li><a href="#p8">8. お問い合わせ・変更</a></li>
</ol></nav>
<div class="doc-main legal">
{_meta()}
<section id="p1"><h2>1. 対象と基本方針</h2>
<p>本ポリシーは、RemonesのiPhone／iPadアプリとMac Hostに適用されます。</p>
<p>Remonesは、お客様が所有する、または操作する権限を持つMacへ、ローカルネットワークやお客様が用意したVPNを通じて接続するアプリです。Remones独自のアカウント登録や、開発者が運営する共通サーバー・中継サービスは必要ありません。</p>
<p>通常のリモート接続で扱う画面、音声、入力、クリップボードなどを、開発者のサーバーへ送信する仕組みはありません。</p>
</section>
<section id="p2"><h2>2. 端末間で扱う情報</h2>
<p>使用する機能に応じて、接続した端末間で次の情報を処理・送信します。</p>
<ul>
<li>Macの画面・ウインドウ映像、カーソル情報、有効な場合のMacの再生音声。</li>
<li>キーボード入力、入力したテキスト、マウス・タッチ・トラックパッド操作、操作に必要なフォーカス情報。</li>
<li>端末の識別用ID・名称、接続先アドレス、認証情報、接続状態、対応機能、ビルド情報、バッテリー状態など。</li>
<li>Macのアプリ名・識別子・アイコン、実行状態、ウインドウ名・配置など、アプリや画面を選択するための情報。</li>
<li>クリップボード同期を有効にした場合のテキスト・URL。複数Mac対応版では、同期を有効にして接続先を切り替えると、コピーしたテキストが切替先のMacに送られる場合があります。</li>
<li>Mac側でファイル検索を許可した場合の検索語と検索結果。検索はMac上のファイル名などを対象とし、結果には名称、親フォルダー名、種類、開くための一時的な識別子などを含みます。検索結果としてファイル本文や完全なパスを送信する機能ではありません。ただし、開いたファイルの内容は画面映像に含まれます。</li>
</ul>
<p>接続先Macや、そのMacで使用するアプリは、受信した入力・クリップボードなどを処理・保存する場合があります。</p>
<p>確認対象版では、iPhone／iPadのマイク・カメラをMacへ送る実装はありますが、通常のMac Host構成では無効です。有効化した版を提供する場合は、本ポリシーと権限説明を見直します。</p>
</section>
<section id="p3"><h2>3. 端末内に保存する情報</h2>
<p>Remonesは、再接続や表示・設定の復元のために、次の情報を端末内に保存します。</p>
<ul>
<li><strong>Keychain：</strong>クライアント識別用ID、ペアリングした端末の情報、共有秘密鍵など。Mac側にも承認した端末の情報を保存します。</li>
<li><strong>設定領域：</strong>表示・入力・音声・クリップボード等の設定、お気に入り、最近使用した接続対象、ワークスペースの名称・対象・配置など。</li>
<li><strong>アプリ用ファイル：</strong>接続したMacのアプリ一覧、名称・識別子・利用時刻等のメタデータ、アプリアイコン。</li>
<li><strong>Mac側の復旧情報：</strong>ウインドウやシステム設定を復元するための識別子、位置・サイズ、処理状態など。</li>
<li><strong>診断情報：</strong>接続状態、エラー、処理時間などのローカルログ。</li>
</ul>
<p>確認対象版のセッション画面サムネイルはメモリ内で保持され、Remonesが画像ファイルとして永続保存する処理は確認されていません。</p>
<p>OSのバックアップ、システムのクリップボード共有、他のアプリによる保存には、それぞれの設定・ポリシーが適用されます。</p>
</section>
<section id="p4"><h2>4. 決済・外部サービス</h2>
<p>Remones Plusの購入・復元・購読状態の確認にはAppleのStoreKitを使用します。アプリは商品、取引、購読の有効期限・更新状態などを処理します。Remonesがカード番号やApple Accountのパスワードを受け取ることはありません。</p>
<p>Appleによる決済、配信、診断情報等の取り扱いには、<a href="https://www.apple.com/legal/privacy/en-ww/" rel="noopener">Appleのプライバシーポリシー</a>が適用されます。</p>
<p>Mac Hostのダウンロードや公開文書の閲覧でGitHub／GitHub Pagesを利用するときは、IPアドレスなどのアクセス情報がGitHubに処理されます。<a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHubのプライバシー声明</a>をご確認ください。</p>
<p>VPNは任意です。利用するVPN事業者やネットワーク管理者による処理には、そのサービスの条件が適用されます。</p>
</section>
<section id="p5"><h2>5. 広告・解析・診断</h2>
<p>確認対象のアプリ実装には、広告SDK、第三者の利用解析SDK、第三者のクラッシュ送信SDKは確認されていません。Remones独自の広告追跡や、ローカルログの自動アップロード機能はありません。</p>
<p>OSやAppleのサービスを通じた診断情報の共有は、お客様の設定およびAppleの仕組みに従います。</p>
</section>
<section id="p6"><h2>6. 選択・保持・削除</h2>
<p>クリップボード同期は初期状態で無効です。同期や音声、PiPを使用しない場合は、対応する設定を無効にしてください。PiPでは、メイン画面を離れてもMacの映像・音声が続く場合があります。</p>
<p>保存したペアリングやアプリ情報は、対応する「コンピュータを削除」操作で削除できます。最近使用した項目やワークスペースは、別途削除が必要な場合があります。Mac側の承認済み端末も、必要に応じてMac側で解除してください。</p>
<p>端末内の保存情報は、削除・置換されるまで保持される場合があります。ログはOS等の保存管理に従います。アプリを削除しても、Keychain、Mac側のデータ、バックアップ、Appleの購入記録がすべて消えるとは限りません。開発者からお客様の端末内データを遠隔削除する仕組みはありません。</p>
</section>
<section id="p7"><h2>7. 安全性</h2>
<p>端末間の接続にはTLSを使用します。初回接続では両端末の6桁コードを照合し、正しい接続先であることを確認して承認してください。暗号化だけで初回接続先の本人確認が完了するわけではありません。</p>
</section>
<section id="p8"><h2>8. お問い合わせ・変更</h2>
<p>お問い合わせで任意に提供された連絡先、説明、ログ等は、問い合わせ対応・不具合調査のために使用し、対応および法令上必要な期間に限り保持します。秘密鍵や不要な個人情報は送らないでください。</p>
<p>本ポリシーを変更する場合は、このページの施行日と内容を更新します。</p>
</section>
</div>
</div>
"""
    return {"slug": "privacy", "nav": None, "noindex": True,
            "title": "プライバシーポリシー（草案）",
            "description": "Remones のプライバシーポリシー（公開前の草案）。",
            "body": body}


def terms() -> dict:
    body = _head("Remones 利用条件", "利用条件") + f"""
<div class="wrap doc">
<nav class="toc" aria-label="目次"><p class="toc-title">目次</p><ol>
<li><a href="#t1">1. 適用される契約</a></li>
<li><a href="#t2">2. 利用できるコンピュータと禁止事項</a></li>
<li><a href="#t3">3. 動作環境と操作</a></li>
<li><a href="#t4">4. Remones Plus</a></li>
<li><a href="#t5">5. 保証と責任</a></li>
<li><a href="#t6">6. Mac Hostとソースコード</a></li>
<li><a href="#t7">7. プライバシーと変更</a></li>
</ol></nav>
<div class="doc-main legal">
{_meta()}
<section id="t1"><h2>1. 適用される契約</h2>
<p>App Storeで配布するRemonesのiPhone／iPadアプリには、<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" rel="noopener">Apple標準使用許諾契約（Standard EULA）</a>を使用します。本書はRemones固有の利用条件と購読条件を補足します。標準EULAや強行法規上の権利を制限するものではありません。</p>
</section>
<section id="t2"><h2>2. 利用できるコンピュータと禁止事項</h2>
<p>Remonesは、お客様が所有する、または正当な操作権限を持つコンピュータにのみ使用してください。</p>
<p>無断アクセス、本人の同意を欠く監視、認証・承認機能の回避、他者の情報の不正取得、権利侵害、その他違法な目的で使用してはなりません。</p>
<p>お客様は、接続先、入力内容、クリップボード共有、Mac上で実行する操作を確認し、必要な権限や同意を確保してください。</p>
</section>
<section id="t3"><h2>3. 動作環境と操作</h2>
<p>お客様がMac Host、端末、ネットワーク、必要なOS権限を用意・管理します。VPNは任意です。ネットワークや他のアプリによる料金はお客様の負担です。</p>
<p>リモート入力は、ファイル変更、送信、購入等の操作につながる場合があります。重要な操作は接続先と結果を確認し、必要なバックアップを用意してください。</p>
<p>Windows／Android等への将来対応は、本書による提供の約束ではありません。</p>
</section>
<section id="t4"><h2>4. Remones Plus</h2>
<p>Remones Plusは任意の自動更新購読です。確認対象版の有料内容は、有料アイコンカラーと対応するアプリ内アクセントカラーです。</p>
<p>{_ph("プラン・価格・無料体験の表：App Store Connect の本番設定が確定したあとに記入")}</p>
<p>実際の価格、通貨、税、提供内容、無料体験の適用は、購入時のアプリ表示とAppleの購入確認画面で確認してください。年額プランは月払いではありません。</p>
<ul>
<li>購入はApple Accountを通じて処理されます。</li>
<li>無料体験はAppleが対象と判定したお客様に適用されます。体験終了前に解約しなければ、表示された年額料金の有料購読へ移行します。</li>
<li>購読は解約するまで同じ期間で自動更新されます。更新・体験終了による請求を避けるには、終了の少なくとも24時間前までにAppleの購読管理から解約してください。</li>
<li>管理・解約は、iPhone／iPadの「設定」→お客様の名前→「サブスクリプション」、または<a href="https://apps.apple.com/account/subscriptions" rel="noopener">Appleの購読管理</a>で行えます。アプリの削除だけでは解約されません。</li>
<li>解約後の利用期限はAppleの購読画面で確認してください。無料体験は解約により利用が終了する場合があります。</li>
<li>購入の復元には、購入時と同じApple Accountを使用してください。</li>
<li>価格変更はAppleの通知・同意手続きおよび適用法に従います。</li>
</ul>
<p>Appleとの取引には、<a href="https://www.apple.com/legal/internet-services/itunes/jp/terms.html" rel="noopener">Appleメディアサービス利用規約</a>も適用されます。返金は<a href="https://reportaproblem.apple.com/" rel="noopener">Appleの返金申請窓口</a>で申請してください。返金可否はAppleの条件と適用法に従い、法定の権利は制限されません。<a href="https://support.apple.com/en-us/118223" rel="noopener">Appleの返金案内</a></p>
</section>
<section id="t5"><h2>5. 保証と責任</h2>
<p>適用法で認められる範囲で、Remonesは現状有姿・提供可能な状態で提供されます。接続の継続、特定環境での互換性、無停止・無障害の動作を保証しません。保証および責任にはApple標準EULAの該当条項が適用されます。</p>
<p>本書は、消費者保護法その他の強行法規により排除・制限できない権利や責任を除外しません。</p>
</section>
<section id="t6"><h2>6. Mac Hostとソースコード</h2>
<p>Mac HostはApp Store版クライアントとは別に配布されます。ソースコードや同梱コンポーネントの使用・変更・再配布には、それぞれに適用されるライセンス条件を確認してください。ソースコードが公開されていることだけで、任意の再利用権が付与されるものではありません。</p>
<p>{_ph("Mac Host のライセンス名称・本文・対象範囲・URL：確定後に記入")}</p>
</section>
<section id="t7"><h2>7. プライバシーと変更</h2>
<p>情報の取り扱いは<a href="~/privacy/">プライバシーポリシー</a>をご確認ください。</p>
<p>本条件を変更する場合は、変更内容・施行日を公開し、必要な通知・同意手続きを行います。購読条件の変更にはAppleの手続きも適用されます。</p>
</section>
</div>
</div>
"""
    return {"slug": "terms", "nav": None, "noindex": True,
            "title": "利用条件（草案）",
            "description": "Remones の利用条件（公開前の草案）。",
            "body": body}
