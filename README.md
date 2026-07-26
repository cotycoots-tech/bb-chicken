# bbc-laugh

**Live site (GitHub Pages):**  
https://cotycoots-tech.github.io/bbc-laugh/

Repo: [cotycoots-tech/bbc-laugh](https://github.com/cotycoots-tech/bbc-laugh)

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

## Web app (GitHub Pages only)

Static mobile gallery in `docs/`. No Render or other hosts.

| Item | Value |
|------|--------|
| Site name | `bbc-laugh` |
| Live URL | https://cotycoots-tech.github.io/bbc-laugh/ |
| Pages source | `main` branch → **`/docs`** |

### Enable GitHub Pages

1. Repo → **Settings → Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `main` / folder **`/docs`**
4. **Custom domain:** leave **empty** for now (use the `github.io` URL)
5. Save

You should see the site at https://cotycoots-tech.github.io/bbc-laugh/ without a DNS error.

### Why “DNS check failed” happened

Public DNS reports **`bbc-laugh.com` → NXDOMAIN** (domain not found). That means either:

1. The domain is **not registered** yet, or  
2. It’s registered but **no nameservers / zone** are set up.

GitHub can only pass the DNS check **after** the domain exists and points at GitHub Pages. Adding a custom domain before that always fails.

### Custom domain later (`bbc-laugh.com`)

**Do this only after you own the domain and DNS works.**

1. **Register** `bbc-laugh.com` (Namecheap, Google Domains/Squarespace, Cloudflare, GoDaddy, etc.).
2. At the registrar (or Cloudflare DNS), create:

| Type | Name | Value |
|------|------|--------|
| `A` | `@` | `185.199.108.153` |
| `A` | `@` | `185.199.109.153` |
| `A` | `@` | `185.199.110.153` |
| `A` | `@` | `185.199.111.153` |
| `CNAME` | `www` | `cotycoots-tech.github.io` |

3. Wait until this succeeds (not NXDOMAIN):

   ```bash
   dig +short A bbc-laugh.com
   # should list the four 185.199.x.x addresses
   ```

4. In the repo, add `docs/CNAME` with a single line:

   ```text
   bbc-laugh.com
   ```

5. Commit/push, then in **Settings → Pages** set custom domain to `bbc-laugh.com`, wait for DNS check, enable **Enforce HTTPS**.

Until step 3 works, keep the custom domain field empty.

### Local preview

```bash
python3 -m http.server 5050 --directory docs
```

Visit `http://127.0.0.1:5050`.

Optional Flask mirror:

```bash
python3 -m pip install -e '.[test]'
bbc-laugh
python3 -m pytest
```

### Project structure

- `docs/` — published web app (GitHub Pages)
- `src/bbc_laugh/` — optional local Flask mirror
- `tests/` — unit tests
- `pyproject.toml` — local package metadata (`bbc-laugh` / `bbc_laugh`)
