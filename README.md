# vanilla-scaffold

> Scaffold a vanilla JS + Handlebars + Native CSS frontend with layout-first architecture — no frameworks, no bloat, no generic AI templates.

**Claude Code skill** that generates opinionated, production-ready frontend projects from 3 questions.

---

## Install

```bash
# Copy to Claude Code skills directory
cp -r vanilla-scaffold ~/.claude/skills/

# Run setup (installs LSP, checks Node version)
bash ~/.claude/skills/vanilla-scaffold/scripts/setup.sh
```

Or install as a plugin:
```
/plugin install nainicorn/ui-kit
```

---

## Usage

In Claude Code, run:

```
/vanilla-scaffold
```

The skill walks you through 3 questions:
1. **What are you building?** (portfolio, SaaS, fintech, etc.)
2. **What's the vibe?** (editorial, brutalist, glassy, etc.)
3. **Motion or 3D?** (none, GSAP, Three.js, etc.)

Then it generates a **design decision document** with typography, colors, spacing, and layout direction — all tailored to your answers. Review it, say "yes", and the scaffold generates.

```
✅ Scaffold complete — 24 files created

To get started:
  cd your-app-name
  npm install
  npm run dev
```

Zero extra steps. Works on first run.

---

## What You Get

```
your-app/
├── index.html
├── vite.config.js
├── package.json
├── .env.example
├── src/
│   ├── app.js
│   ├── styles/
│   │   └── base.css              ← design tokens
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Layout/           ← shell (Header + Body + Footer)
│   │   │   ├── Header/           ← .hbs + .js + .css
│   │   │   ├── Body/
│   │   │   └── Footer/
│   │   └── features/             ← your components go here
│   ├── services/
│   │   ├── apiService.js         ← fetch wrapper, any backend
│   │   └── routeService.js       ← hash-based routing
│   └── lib/                      ← motion library init (if selected)
```

Every component = 3 files: `.hbs` (markup) + `.js` (logic) + `.css` (styles). No exceptions.

---

## Architecture

- **Layout-first**: Layout.js owns the shell. Features live inside Body.
- **Native CSS nesting**: No SCSS, no preprocessors. `& .child {}` everywhere.
- **Custom properties only**: All colors, fonts, spacing from `:root` tokens.
- **Scoped queries**: `container.querySelector()`, never `document.querySelector()`.
- **Sync renders**: Components render synchronously. Data fetching is a service concern.
- **Backend-flexible**: Change `VITE_API_URL` in `.env` to point at any backend.

---

## Escape Hatches

| Default | How to change |
|---|---|
| Handlebars templating | Swap `.hbs` for `.html` + update `?raw` import in component `.js` |
| Hash-based routing | In `routeService.js`: `hashchange` → `popstate`, `location.hash` → `location.pathname` |
| Vite | Any ESM bundler works — Parcel, Rollup, esbuild. Swap `vite.config.js`. |
| `VITE_API_URL` env var | Hardcode `BASE_URL` in `apiService.js` if you don't need env management |

---

## Adding a Feature Component

```
1. Create: src/components/features/YourFeature/
2. Add:    YourFeature.hbs / YourFeature.js / YourFeature.css
3. Import + call from Body.js
4. Add a mount slot in Body.hbs

No registration. No build config changes.
```

---

## Adding a Service

```
1. Create src/services/yourService.js
2. Named exports only — no default exports
3. Import directly into any component that needs it
4. Never import one service from another — keep them flat
```

---

## Stack

- Vanilla JS (ESModules)
- Handlebars (templating)
- Native CSS (nesting, custom properties, container queries)
- Vite (dev server + build)
- Material Icons (icon set)

---

## Requirements

- Node.js 18+
- Claude Code CLI

---

## License

MIT — Sreenaina Koujala
