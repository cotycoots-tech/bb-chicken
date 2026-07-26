from __future__ import annotations

import os
import time
from pathlib import Path

from flask import Flask, render_template_string, request, url_for

app = Flask(__name__, static_folder="static", static_url_path="/static")

# Public web app identity / domain branding.
SITE_NAME = os.environ.get("BBC_LAUGH_SITE_NAME", "bbc-laugh")
# Default to GitHub Pages URL until a real custom domain has working DNS.
SITE_DOMAIN = os.environ.get(
    "BBC_LAUGH_DOMAIN", "cotycoots-tech.github.io/bbc-laugh"
)
# Dev-only live-reload polling (disabled in production).
DEV_MODE = os.environ.get("FLASK_DEBUG", "").lower() in {"1", "true", "yes"} or (
    os.environ.get("BBC_LAUGH_ENV", os.environ.get("ENV", "development")).lower()
    not in {"production", "prod"}
)

# Changes whenever the process restarts (used for browser auto-refresh).
BOOT_ID = f"{os.getpid()}-{time.time()}"

# Gallery assets from the project README (GitHub user-attachments).
metadata_items = [
    {"label": "Title", "value": SITE_NAME},
    # Story + former Boxing Chicken image (combined)
    {
        "label": "Story",
        "value": "big belly chicken vs big black cat",
        "media_type": "image",
        "media_url": "https://github.com/user-attachments/assets/73c75b27-cd64-461b-9ee7-1cf879c0ef82",
        "show_caption": True,
    },
    {
        "label": "Belly Busting Chicken",
        "value": "https://github.com/user-attachments/assets/9965d439-0e58-489c-b3b5-9d41f924c0e5",
        "media_type": "image",
    },
    {
        "label": "Belly Busting Chicken (video)",
        "value": "https://github.com/user-attachments/assets/805e5236-a004-4572-ad29-5e91558eca3b",
        "media_type": "video",
    },
    {
        "label": "Training — Big Black Cat",
        "value": "https://github.com/user-attachments/assets/d31d2edf-8238-440e-b658-b7a1f6563d66",
        "media_type": "image",
    },
    {
        "label": "Training — Big Black Cat (video)",
        "value": "https://github.com/user-attachments/assets/1e5902c6-4a94-4543-a2cb-e1d9e2b9af42",
        "media_type": "video",
    },
    {
        "label": "Boxing Chicken vs Black Cat (video)",
        "value": "https://github.com/user-attachments/assets/1b37c9b1-8d7b-46af-864c-520e5cd26a34",
        "media_type": "video",
    },
    {
        "label": "Showdown (video)",
        "value": "https://github.com/user-attachments/assets/ed79628c-8a78-4273-ae61-f2f47b5b1bce",
        "media_type": "video",
    },
    {
        "label": "Finale (video)",
        "value": "https://github.com/user-attachments/assets/83801bd3-82e3-48ab-8a42-a94e4475199b",
        "media_type": "video",
    },
    # Final slide (image)
    {
        "label": "Big Bucket Chicken",
        "value": "https://github.com/user-attachments/assets/ded7ac9b-5b20-4258-9060-95d0e8b4837e",
        "media_type": "image",
        "final": True,
    },
]

PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <meta name="application-name" content="{{ site_name }}">
  <meta name="description" content="{{ site_name }} — big belly chicken vs big black cat">
  <meta property="og:title" content="{{ site_name }}">
  <meta property="og:site_name" content="{{ site_name }}">
  <meta property="og:description" content="big belly chicken vs big black cat">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://{{ site_domain }}/">
  <link rel="canonical" href="https://{{ site_domain }}/">
  <title>{{ site_name }}</title>
  <style>
    :root {
      color-scheme: light;
      color: #111;
      background: #f8f4ef;
      font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      --safe-top: env(safe-area-inset-top, 0px);
      --safe-right: env(safe-area-inset-right, 0px);
      --safe-bottom: env(safe-area-inset-bottom, 0px);
      --safe-left: env(safe-area-inset-left, 0px);
    }
    * { box-sizing: border-box; }
    html, body {
      margin: 0;
      height: 100%;
      height: 100dvh;
      overflow: hidden;
    }
    body {
      display: flex;
      align-items: center;
      justify-content: center;
      padding:
        max(0.5rem, var(--safe-top))
        max(0.5rem, var(--safe-right))
        max(0.5rem, var(--safe-bottom))
        max(0.5rem, var(--safe-left));
    }
    .card {
      width: min(100%, 720px);
      max-height: 100%;
      min-height: 0;
      background: linear-gradient(180deg, #ffffff 0%, #fcf7f1 100%);
      border: 1px solid rgba(17, 17, 17, 0.08);
      border-radius: 20px;
      padding: 0.9rem 1rem 0.85rem;
      box-shadow: 0 28px 60px rgba(0, 0, 0, 0.08);
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      overflow: hidden;
    }
    .card--media {
      height: 100%;
      align-self: stretch;
    }
    .card-header {
      flex: 0 0 auto;
    }
    .label {
      font-size: 0.8rem;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #6c5e53;
      margin-bottom: 0.15rem;
    }
    .value {
      margin: 0;
      font-size: clamp(1.6rem, 5vw, 2.6rem);
      line-height: 1.05;
      color: #1d1b19;
      word-break: break-word;
    }
    .card--media .value {
      font-size: clamp(1.1rem, 3.5vw, 1.55rem);
      line-height: 1.2;
    }
    .message {
      margin: 0;
      color: #5b5248;
      font-size: 0.95rem;
      line-height: 1.5;
      flex: 0 0 auto;
    }
    .media-frame {
      flex: 1 1 auto;
      min-height: 0;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 16px;
      background: #111;
      overflow: hidden;
    }
    .media {
      display: block;
      width: auto;
      height: auto;
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      background: #000;
    }
    .card:not(.card--media) .media-frame {
      display: none;
    }
    .card--media .message {
      display: none;
    }
    .actions {
      display: grid;
      gap: 0.5rem;
      flex: 0 0 auto;
      justify-items: center;
    }
    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0.85rem 1.1rem;
      width: 100%;
      border: none;
      border-radius: 999px;
      background: #2f7c47;
      color: #fff;
      font-size: 1rem;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
    }
    .button:hover,
    .button:focus-visible {
      transform: translateY(-1px);
      box-shadow: 0 18px 30px rgba(47, 124, 71, 0.24);
      outline: none;
    }
    .button.button--hat {
      position: relative;
      width: min(100%, 280px);
      height: 118px;
      padding: 0;
      border-radius: 0;
      background: transparent;
      box-shadow: none;
      color: #1a1a1a;
      overflow: visible;
    }
    .button.button--hat:hover,
    .button.button--hat:focus-visible {
      transform: translateY(-2px) scale(1.03);
      box-shadow: none;
      filter: drop-shadow(0 14px 18px rgba(30, 70, 40, 0.28));
    }
    .button.button--hat .hat-svg {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      display: block;
    }
    .button.button--hat .hat-label {
      position: relative;
      z-index: 1;
      margin-top: -18px;
      font-size: 0.92rem;
      font-weight: 800;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #fff;
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.45);
      pointer-events: none;
    }
    .footer {
      margin: 0;
      color: #827970;
      font-size: 0.85rem;
      text-align: center;
      flex: 0 0 auto;
    }
    @media (max-height: 700px) {
      .card { padding: 0.65rem 0.75rem; gap: 0.5rem; border-radius: 16px; }
      .button:not(.button--hat) { padding: 0.7rem 1rem; }
      .button.button--hat { height: 100px; width: min(100%, 240px); }
      .button.button--hat .hat-label { font-size: 0.8rem; margin-top: -14px; }
      .label { font-size: 0.72rem; }
    }
  </style>
</head>
<body>
  <main class="card{% if media_type %} card--media{% endif %}" role="main">
    <div class="card-header">
      <div class="label">{{ label }}</div>
      {% if show_caption or not media_type %}
      <h1 class="value">{{ value }}</h1>
      {% endif %}
    </div>
    {% if media_type == 'image' %}
      <div class="media-frame">
        <img class="media" src="{{ media_url }}" alt="{{ label }}" loading="lazy" />
      </div>
    {% elif media_type == 'video' %}
      <div class="media-frame">
        <video class="media" id="step-video" controls autoplay loop playsinline>
          <source src="{{ media_url }}" type="video/mp4" />
          Your browser does not support embedded video.
        </video>
      </div>
      <script>
        (function () {
          const video = document.getElementById("step-video");
          if (!video) return;
          // Preset audio on for media with sound.
          video.muted = false;
          video.defaultMuted = false;
          video.volume = 1;
          const playWithSound = () => {
            video.muted = false;
            video.volume = 1;
            return video.play();
          };
          playWithSound().catch(function () {
            const unlock = function () {
              playWithSound().finally(function () {
                document.removeEventListener("pointerdown", unlock, true);
                document.removeEventListener("keydown", unlock, true);
              });
            };
            document.addEventListener("pointerdown", unlock, true);
            document.addEventListener("keydown", unlock, true);
          });
        })();
      </script>
    {% endif %}
    {% if not media_type %}
    <p class="message">{{ message }}</p>
    {% endif %}
    <div class="actions">
      {% if is_final %}
      <a class="button button--hat" href="{{ next_url }}" aria-label="Start over">
        <svg class="hat-svg" viewBox="0 0 280 118" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="hatCrown" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#3fa85a"/>
              <stop offset="100%" stop-color="#246b38"/>
            </linearGradient>
            <linearGradient id="hatBrim" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#2f8a47"/>
              <stop offset="100%" stop-color="#1c522b"/>
            </linearGradient>
          </defs>
          <ellipse cx="140" cy="92" rx="118" ry="18" fill="url(#hatBrim)"/>
          <ellipse cx="140" cy="88" rx="110" ry="12" fill="#1a4a28" opacity="0.35"/>
          <path d="M48 88 C52 42 90 18 140 18 C190 18 228 42 232 88 Z" fill="url(#hatCrown)"/>
          <path d="M62 86 C70 52 100 34 140 34 C180 34 210 52 218 86" fill="none" stroke="#8fd49e" stroke-width="2" opacity="0.45"/>
          <path d="M140 22 V78" stroke="#1a4a28" stroke-width="2" opacity="0.25"/>
          <circle cx="140" cy="20" r="7" fill="#f2e6c8"/>
          <circle cx="140" cy="20" r="3.5" fill="#d4c08a"/>
          <ellipse cx="140" cy="94" rx="90" ry="6" fill="#6fbf82" opacity="0.25"/>
        </svg>
        <span class="hat-label">Start over</span>
      </a>
      {% else %}
      <a class="button" href="{{ next_url }}">{{ button_text }}</a>
      {% endif %}
    </div>
    <p class="footer">Step {{ step }} of {{ total }} · {{ site_name }}</p>
  </main>
  {% if dev_mode %}
  <script>
    // Auto-refresh the browser when the Flask reloader restarts the app (dev only).
    (function () {
      let bootId = null;
      async function pollBoot() {
        try {
          const response = await fetch("/__boot", { cache: "no-store" });
          if (!response.ok) return;
          const nextId = await response.text();
          if (bootId === null) {
            bootId = nextId;
          } else if (bootId !== nextId) {
            location.reload();
          }
        } catch (_) {
          // Server may be briefly down during reload; keep polling.
        }
      }
      setInterval(pollBoot, 1000);
      pollBoot();
    })();
  </script>
  {% endif %}
</body>
</html>
"""


from urllib.parse import urlparse


def get_media_info(value: str, media_type: str | None = None) -> tuple[str | None, str]:
    """Resolve media type and URL for a metadata value.

    Prefer an explicit ``media_type`` (needed for GitHub user-attachment
    URLs that have no file extension). Otherwise infer from the path suffix.
    """

    def suffix_from_url(url: str) -> str:
        parsed = urlparse(url)
        return Path(parsed.path).suffix.lower()

    if media_type in {"image", "video"}:
        if value.startswith(("http://", "https://")):
            return media_type, value
        return media_type, url_for("static", filename=value)

    if value.startswith(("http://", "https://")):
        suffix = suffix_from_url(value)
        if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
            return "image", value
        if suffix == ".mp4":
            return "video", value
        return None, value

    suffix = Path(value).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        return "image", url_for("static", filename=value)
    if suffix == ".mp4":
        return "video", url_for("static", filename=value)
    return None, value


@app.get("/healthz")
def healthz() -> tuple[str, int]:
    """Lightweight health check for hosting platforms."""
    return "ok", 200


@app.get("/__boot")
def boot_id() -> str:
    """Return a process boot id so the browser can auto-refresh on reload."""
    return BOOT_ID


@app.get("/")
def index() -> str:
    raw_index = request.args.get("index", "0")
    try:
        current_index = max(0, int(raw_index))
    except ValueError:
        current_index = 0

    total = len(metadata_items)
    # Clamp past-the-end navigations onto the final image slide.
    current_index = min(max(0, current_index), total - 1)
    item = metadata_items[current_index]
    label = item["label"]
    value = item["value"]
    step = current_index + 1
    media_src = item.get("media_url") or value
    media_type, media_url = get_media_info(media_src, item.get("media_type"))
    show_caption = bool(item.get("show_caption"))
    is_final = current_index == total - 1 or bool(item.get("final"))
    if is_final:
        button_text = "Start over"
        next_url = url_for("index", index=0)
        message = "That’s the end — tap to begin again."
    else:
        button_text = "Next"
        next_url = url_for("index", index=current_index + 1)
        message = "Tap the button to move to the next entry."

    return render_template_string(
        PAGE_TEMPLATE,
        label=label,
        value=value,
        message=message,
        next_url=next_url,
        button_text=button_text,
        step=step,
        total=total,
        media_type=media_type,
        media_url=media_url,
        show_caption=show_caption,
        is_final=is_final,
        site_name=SITE_NAME,
        site_domain=SITE_DOMAIN,
        dev_mode=DEV_MODE,
    )


def main() -> None:
    """Run the bbc-laugh web app (dev server with auto-reload)."""
    host = os.environ.get("BBC_LAUGH_HOST", "127.0.0.1")
    # Default 5050 avoids macOS AirPlay Receiver on port 5000.
    # Production hosts set PORT (and usually HOST 0.0.0.0 via gunicorn).
    port = int(os.environ.get("PORT", os.environ.get("BBC_LAUGH_PORT", "5050")))
    debug = DEV_MODE
    print(f"{SITE_NAME} is running at http://{host}:{port} ({SITE_DOMAIN})")
    if debug:
        print("Debug auto-reload is on — save a file to refresh the app and browser.")
    app.run(host=host, port=port, debug=debug, use_reloader=debug)


def welcome_message() -> str:
    """Return a welcome message for the package."""
    return f"Welcome to {SITE_NAME}!"


if __name__ == "__main__":
    main()
