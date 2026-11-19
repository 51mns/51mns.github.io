"""Single place for values that change at launch.

Edit here, then run:  python3 tools/build.py
The generated HTML is committed, so GitHub Pages needs no build step.
"""

# Canonical base URL of the Remones site (trailing slash required).
# Decided 2026-11-19: the site lives in the `remones/` folder of the
# user-site repository 51mns/51mns.github.io.
BASE_URL = "https://51mns.github.io/remones/"

# --- App Store -------------------------------------------------------------
# TODO(launch): set to the real App Store URL once the listing is live,
# e.g. "https://apps.apple.com/jp/app/remones/id0000000000".
# While None, the site shows a disabled "App Store で近日公開" button.
APP_STORE_URL = None

# --- Mac app download --------------------------------------------------------
# Intended download target: the GitHub Releases "latest" page of the
# user-site repository. No release exists yet.
MAC_DOWNLOAD_URL = "https://github.com/51mns/51mns.github.io/releases/latest"
# TODO(launch): flip to True after the first notarized Mac release is published.
MAC_DOWNLOAD_READY = False

# Display name of the companion Mac app. TODO(owner): confirm the final name.
MAC_APP_NAME = "Remones Host"

# Minimum OS versions, from Apps/Prototype/project.yml deploymentTarget.
MIN_IOS = "18"
MIN_MACOS = "15"

# Default Host TCP port (Apps/Prototype/Host/HostViewModel.swift).
DEFAULT_PORT = "7777"

# Privacy Policy / Terms of Use are still drafts (provider, contact and dates
# are placeholders). Keep them out of the published site until approved.
LEGAL_PUBLISHED = False
