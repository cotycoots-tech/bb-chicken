# bbc-laugh

**Domain:** [bbc-laugh.com](https://bbc-laugh.com)

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

## Web app

Mobile-ready Flask gallery app branded as **bbc-laugh**.

| Item | Value |
|------|--------|
| Site name | `bbc-laugh` |
| Domain | `bbc-laugh.com` |
| Health check | `/healthz` |
| Local URL | `http://127.0.0.1:5050` |

### Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e '.[test]'
bbc-laugh
# or: PYTHONPATH=src python3 -m bb_chicken.app
```

Open `http://127.0.0.1:5050`. VS Code/Cursor auto-starts the app on folder open.

```bash
python3 -m pytest
```

### Production (Docker / gunicorn)

```bash
docker build -t bbc-laugh .
docker run --rm -p 8080:8080 -e BB_CHICKEN_ENV=production bbc-laugh
```

Or without Docker:

```bash
pip install -e .
export BB_CHICKEN_ENV=production FLASK_DEBUG=0
gunicorn --bind 0.0.0.0:8080 --workers 2 bb_chicken.app:app
```

### Deploy to Render + custom domain

1. Push this repo to GitHub.
2. In [Render](https://render.com): **New → Blueprint** and select the repo (uses `render.yaml`),  
   or **New → Web Service** with Docker runtime.
3. After the service is live (e.g. `https://bbc-laugh.onrender.com`), open  
   **Settings → Custom Domains → Add** `bbc-laugh.com` (and optionally `www.bbc-laugh.com`).
4. At your domain registrar, add the DNS records Render shows (usually a CNAME or A record).
5. Wait for TLS to provision. Visit `https://bbc-laugh.com`.

Environment variables (already set in `render.yaml`):

- `BB_CHICKEN_ENV=production`
- `BBC_LAUGH_SITE_NAME=bbc-laugh`
- `BBC_LAUGH_DOMAIN=bbc-laugh.com`

### Project structure

- `src/bb_chicken/` — Flask app
- `Dockerfile` / `Procfile` / `render.yaml` — production deploy
- `tests/` — unit tests
- `pyproject.toml` — package + `bbc-laugh` CLI entrypoint
