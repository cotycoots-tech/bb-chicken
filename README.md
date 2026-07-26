# bbc-laugh

**Live on GitHub Pages** · domain **[bbc-laugh.com](https://bbc-laugh.com)**

Repo: [cotycoots-tech/bb-chicken](https://github.com/cotycoots-tech/bb-chicken)

big belly chicken vs big black cat

<img width="768" height="1152" alt="belly busting chicken" src="https://github.com/user-attachments/assets/9965d439-0e58-489c-b3b5-9d41f924c0e5" />

https://github.com/user-attachments/assets/805e5236-a004-4572-ad29-5e91558eca3b

<img width="768" height="1152" alt="training- big black cat" src="https://github.com/user-attachments/assets/d31d2edf-8238-440e-b658-b7a1f6563d66" />

https://github.com/user-attachments/assets/1e5902c6-4a94-4543-a2cb-e1d9e2b9af42

<img width="832" height="1248" alt="Big - Boxing Chicken vs Black Cat" src="https://github.com/user-attachments/assets/73c75b27-cd64-461b-9ee7-1cf879c0ef82" />

https://github.com/user-attachments/assets/1b37c9b1-8d7b-46af-864c-520e5cd26a34

https://github.com/user-attachments/assets/ed79628c-8a78-4273-ae61-f2f47b5b1bce

https://github.com/user-attachments/assets/83801bd3-82e3-48ab-8a42-a94e4475199b

<img width="768" height="1152" alt="big bucket chicken" src="https://github.com/user-attachments/assets/ded7ac9b-5b20-4258-9060-95d0e8b4837e" />

## Web app (GitHub only)

Static mobile gallery app. Hosted on **GitHub Pages** from the `docs/` folder — no Render, Docker, or external host.

| Item | Value |
|------|--------|
| Site name | `bbc-laugh` |
| Custom domain | `bbc-laugh.com` (`docs/CNAME`) |
| GitHub Pages path | `/docs` on `main` |
| Default Pages URL | https://cotycoots-tech.github.io/bb-chicken/ |

### Enable GitHub Pages

1. Repo → **Settings → Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `main` / folder **`/docs`**
4. Save

After Pages is on, the site is at:

- https://cotycoots-tech.github.io/bb-chicken/
- https://bbc-laugh.com (after DNS — see below)

### Custom domain (`bbc-laugh.com`)

`docs/CNAME` already contains `bbc-laugh.com`.

At your domain registrar, point DNS at GitHub Pages:

| Type | Name | Value |
|------|------|--------|
| `A` | `@` | `185.199.108.153` |
| `A` | `@` | `185.199.109.153` |
| `A` | `@` | `185.199.110.153` |
| `A` | `@` | `185.199.111.153` |
| `CNAME` | `www` | `cotycoots-tech.github.io` |

Then in **Settings → Pages**, confirm custom domain `bbc-laugh.com` and enable **Enforce HTTPS**.

### Local preview

Open the static site:

```bash
# simple static server
python3 -m http.server 5050 --directory docs
```

Visit `http://127.0.0.1:5050`.

Optional Flask mirror (same gallery, for local Python work):

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e '.[test]'
bbc-laugh
# http://127.0.0.1:5050
python3 -m pytest
```

### Project structure

- `docs/` — **published web app** (GitHub Pages)
- `docs/CNAME` — custom domain `bbc-laugh.com`
- `src/bb_chicken/` — optional local Flask mirror
- `tests/` — unit tests for the Flask mirror
- `pyproject.toml` — local package metadata
