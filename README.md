# TerrAgrox global — Static Export Website

Static multi-page website for **TerrAgrox global** (Salem, Tamil Nadu), built with the same layout/structure style as `avinternationalexim.com`, but with TerrAgrox branding, products, and WhatsApp-first enquiries.

## Tech stack

- HTML5 + CSS3 + Vanilla JavaScript
- Bootstrap 5 (CDN)
- Font Awesome 6 (CDN)
- Google Fonts: **Cormorant Garamond** (headings) + **DM Sans** (body)
- AOS.js (CDN)
- **No backend**. Contact form redirects to WhatsApp.
- Hosting: Vercel

## Structure

```
index.html
about-us.html
founder.html
products.html
herbal-powders.html
spices.html
jaggery.html
contact-us.html
vercel.json
assets/
  css/style.css
  js/main.js
  img/ (optional if you later replace Unsplash URLs)
```

## Run locally

### Option A: Python server

From the project root:

```bash
python3 -m http.server 8000 --directory "/Users/prateeka/terragroxglobal"
```

Open:
- `http://127.0.0.1:8000/index.html`

If port `8000` is busy, change it (e.g. `8010`).

### Option B: Any static server

You can use any static server (VS Code Live Server, etc.). Just make sure it serves the project root.

## WhatsApp number update

The WhatsApp number is defined in:
- `assets/js/main.js` → `WA_NUMBER`

## Swap Unsplash images to local files later

Replace any `src="https://images.unsplash.com/..."` with a local path under `assets/img/...`.

## Deploy to Vercel

1. Push the folder to GitHub
2. Import the repo in Vercel
3. Deploy (no build step needed)

The included `vercel.json` enables clean routes like:
- `/products` → `/products.html`
- `/herbal-powders` → `/herbal-powders.html`
- `/contact` → `/contact-us.html`

