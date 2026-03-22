# vanilla-scaffold

> Scaffold a vanilla JS + Handlebars + Native CSS frontend with layout-first architecture — no frameworks, no bloat, no generic AI templates.

**Claude Code skill** that generates structured, production-ready frontend projects from a few questions.

---

## Install

```
/plugin marketplace add nainicorn/vanilla-scaffold
/plugin install vanilla-scaffold
```

Or install locally:
```bash
git clone https://github.com/nainicorn/vanilla-scaffold.git ~/.claude/skills/vanilla-scaffold
bash ~/.claude/skills/vanilla-scaffold/scripts/setup.sh
```

---

## Usage

In Claude Code (VS Code extension or CLI):

```
/vanilla-scaffold
```

Or just describe what you want to build — the skill triggers automatically.

The skill asks a few questions about your app type, vibe, and motion preferences, then generates the full project.

```
npm install && npm run dev
```

Works on first try. Zero extra steps.

---

## What You Get

```
your-app/
├── index.html
├── vite.config.js               ← path aliases (@components, @services, @framework)
├── package.json
├── .env.example
├── src/
│   ├── app.js                   ← entry point, inits framework + mounts Layout
│   ├── styles/
│   │   └── base.css             ← reset, typography, spacing tokens
│   ├── framework/
│   │   ├── messages/
│   │   │   └── messages.js      ← pub/sub (BroadcastChannel)
│   │   ├── scheme/
│   │   │   ├── scheme.js        ← dark/light/system themes
│   │   │   └── scheme.css       ← HSL-derived color system
│   │   └── modal/
│   │       ├── modal.js         ← reusable modal (open/close/escape)
│   │       ├── modal.hbs
│   │       └── modal.css
│   ├── components/              ← flat structure, no nesting
│   │   ├── Layout/              ← shell (Header + Body + Footer)
│   │   ├── Header/              ← .hbs + .js + .css
│   │   ├── Body/
│   │   ├── Footer/
│   │   └── YourFeature/         ← your components go here
│   ├── services/
│   │   ├── apiService.js        ← fetch wrapper + streaming
│   │   └── routeService.js      ← hash-based routing
│   └── lib/                     ← motion library init (if selected)
```

Every component = 3 files: `.hbs` (markup) + `.js` (logic) + `.css` (styles).

---

## Architecture

- **Layout-first**: Layout.js owns the shell. Features live inside Body.
- **Flat components**: All under `src/components/` — no subdirectories.
- **Framework layer**: Pub/sub messaging, theme system, reusable modal — all initialized at app start.
- **Native CSS nesting**: No SCSS, no preprocessors. `& .child {}` everywhere.
- **HSL color system**: All colors derived from hue + saturation. Dark/light handled automatically.
- **Path aliases**: `@components`, `@services`, `@framework` — no fragile relative paths.
- **Scoped queries**: `container.querySelector()`, never `document.querySelector()`.
- **Sync renders**: Components render synchronously. Data fetching is a service concern.
- **Backend-flexible**: Change `VITE_API_URL` in `.env` or use Vite proxy. Streaming support built in.

---

## Escape Hatches

| Default | How to change |
|---|---|
| Handlebars templating | Swap `.hbs` for `.html` + update `?raw` import in component `.js` |
| Hash-based routing | In `routeService.js`: `hashchange` → `popstate`, `location.hash` → `location.pathname` |
| Vite | Any ESM bundler works — Parcel, Rollup, esbuild. Swap `vite.config.js`. |
| `VITE_API_URL` env var | Hardcode `BASE_URL` in `apiService.js` if you don't need env management |
| HSL color system | Replace scheme.css variables with hex values if you prefer static colors |

---

## Adding a Feature Component

```
1. Create: src/components/YourFeature/
2. Add:    YourFeature.hbs / YourFeature.js / YourFeature.css
3. Import + call from Body.js
4. Add a mount slot in Body.hbs

No registration. No build config changes.
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
- Claude Code

---

## License

MIT — Sreenaina Koujala
