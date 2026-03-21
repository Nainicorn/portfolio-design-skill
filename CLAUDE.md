# vanilla-scaffold — CLAUDE.md

> Skill registry name: `vanilla-scaffold`
> Brand / vanilla mode: `if-it-ain't-broke` dont fix it xd
> Stack: Vanilla JS (ESModules) + Handlebars + Native CSS + Vite
> LSP: vscode-langservers-extracted (HTML/CSS)

---

## DX Philosophy

This skill has two users: the **developer installing it** and the **user using the app built using the skill**.
Both deserve the same care. Every friction point for either is a bug.

### DX Non-Negotiables

- Zero-surprise install: one command, clear output, explicit success/failure state
- Every error message tells you what went wrong AND what to do next
- The skill never silently skips a phase or makes assumptions without saying so
- Scaffold output is immediately runnable — `npm install && npm run dev` works on first try
- File structure is self-documenting — a new developer reads the tree and understands the architecture
- Every generated comment is useful. No `// TODO` without a description. No `// This is the Header` noise.
- Escape hatches are documented — if a user wants to deviate from the opinionated defaults, they know exactly what to change and where

---

## What You Are Building

A Claude Code skill that scaffolds a vanilla frontend with:
1. Layout-first architecture (Layout → Header / Body / Footer)
2. Per-component file separation (.hbs / .js / .css) -> view projects "text-to-3D" or "wovenAI" for more detailed reference
3. A design intake system that generates a full design decision doc before any code
4. Native CSS nesting enforced via LSP validation
5. Backend-flexible service layer

---

## Skill Folder Structure

```
vanilla-scaffold/
├── SKILL.md
├── .lsp.json
├── scripts/
│   ├── setup.sh
│   ├── setup.ps1
│   └── scaffold.py
├── references/
│   ├── css-modern-spec.md
│   ├── design-system.md
│   ├── app-type-map.md
│   └── component-conventions.md
└── templates/
    ├── index.html
    ├── vite.config.js
    ├── package.json
    ├── .env.example
    ├── Layout.hbs / Layout.js / Layout.css
    ├── Header.hbs / Header.js / Header.css
    ├── Body.hbs / Body.js / Body.css
    ├── Footer.hbs / Footer.js / Footer.css
    ├── base.css
    └── services/
        ├── apiService.js
        └── routeService.js
```

---

## Phase 1 — SKILL.md

### Frontmatter

```yaml
---
name: vanilla-scaffold
description: >
  Scaffold a vanilla JS + Handlebars + Native CSS frontend using a layout-first
  architecture with per-component file separation (.hbs/.js/.css), an opinionated
  design system generated from 3 intake questions, and native CSS nesting enforced
  via LSP. Use when the user wants to build a clean, minimal-dependency frontend
  from scratch without a framework.
allowed-tools: Bash(npm *), Bash(node *), Bash(python *)
---
```

### Skill Behavior — Three Phases

**Phase 1: Context intake (3 questions, no more)**

Ask the user exactly these three questions before doing anything else:

```
1. What are you building?
   [ ] Portfolio / personal site
   [ ] SaaS dashboard
   [ ] Internal tool
   [ ] Fintech / data app
   [ ] Marketing / landing page
   [ ] Developer tool
   [ ] E-commerce
   [ ] Other (describe)

2. What's the vibe?
   [ ] Editorial / dark editorial
   [ ] Brutalist / raw
   [ ] Glassy / premium
   [ ] Corporate clean
   [ ] Playful / expressive
   [ ] Retro-tech / terminal
   [ ] GovTech / neutral
   [ ] Undecided / Custom (I'll decide for you)

3. Do you want motion or 3D?
   [ ] None — plain CSS transitions only
   [ ] Subtle CSS transitions
   [ ] GSAP (scroll-driven reveals)
   [ ] Three.js animations (hero / background)
   [ ] library for component micro-interactions
   [ ] extra libraries for transitions/animations/structure/etc.
```

**Phase 2: Design decision document (required, before any code)**

After intake, output a design decision doc in this exact format:

```
## Design Decisions — [App Name]

**App type:** [answer]
**Vibe:** [answer]

### Typography
- Display font: [specific font + why — never Inter, Roboto, Arial, Space Grotesk]
- Body font: [specific font + why]
- Scale: --text-xs through --text-5xl as CSS custom properties

### Color System (all as CSS custom properties on :root)
- --color-primary: [hex + rationale]
- --color-surface: [hex]
- --color-accent: [hex]
- --color-muted: [hex]
- --color-error: [hex]
- --color-text: [hex]
- --color-bg: [hex]

### Spacing Scale
- --space-1 through --space-8 (base: 4px)

### Layout Direction
- [describe the structural pattern: asymmetric / centered / grid-breaking / etc.]

### Motion Plan
- [what gets animated, when, how — or explicitly "none"]

### Libraries
- [only if selected in question 3 — include exact npm install command]

### Banned in this project
- No purple gradients
- No blue CTA on white
- No Inter / Roboto / Arial / Space Grotesk
- No flat CSS selectors (always nest with &)
- No SCSS or preprocessor syntax
- No hardcoded hex values outside :root
```

**Hard stop after Phase 2.** Output the design doc then output this line verbatim and wait:

> **Reply "yes" to generate the scaffold, or describe what you want changed.**

Claude must not proceed automatically. Only an explicit "yes" or "looks good" triggers Phase 3.
Silence, a slow response, or an unrelated message is not confirmation.

**Phase 3: Scaffold generation**

Run `scripts/scaffold.py` with app name as argument. Then generate all component files per `references/component-conventions.md`.

The scaffold script must:
- Print each file as it's created (`✓ Created src/components/layout/Header/Header.js`)
- Exit with a clear error if the target directory already exists — tell the user to pass `--force` or pick a new name
- End with a runnable summary:

```
✅ Scaffold complete — 24 files created

To get started:
  cd your-app-name
  npm install
  npm run dev

Your app opens at http://localhost:5173
Edit src/components/features/ to build your first page.
```

After generation, run LSP validation on all .css files. Fix any violations before declaring done:

```
⚠️  LSP found 2 CSS issues — fixing before handoff:
  src/components/layout/Header/Header.css:14 — flat selector detected
  src/components/features/MainPage/MainPage.css:8 — hardcoded color value
✓  Fixed. All CSS passes LSP validation.
```

---

## Phase 2 — Required Entry-Point Templates

These four files are generated by `scaffold.py` before any component files.
If any are missing the project does not run.

### templates/index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{{app-name}}</title>
    <link rel="stylesheet" href="/src/styles/base.css" />
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/app.js"></script>
  </body>
</html>
```

### templates/vite.config.js

```js
// vite.config.js
// Required for .hbs?raw imports to work. Do not remove assetsInclude.
import { defineConfig } from 'vite';

export default defineConfig({
  assetsInclude: ['**/*.hbs'],
});
```

### templates/package.json

```json
{
  "name": "{{app-name}}",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "handlebars": "^4.7.8"
  },
  "devDependencies": {
    "vite": "^5.0.0"
  }
}
```

for dependencies, handlebars should be included as well as material library icons and any others you may think necessary

Claude must not add any other dependencies unless a motion library was explicitly chosen in intake:
- GSAP selected → add `"gsap": "^3.12.0"` to dependencies
- Three.js selected → add `"three": "^0.163.0"` to dependencies
- Nothing else. Ever.

### templates/.env.example

```
# Backend API base URL — update this to point at your backend
# Copy this file to .env before running npm run dev
VITE_API_URL=http://localhost:8000/api
```

---

## Phase 3 — CSS Rules (Gotchas — highest priority)

These rules are non-negotiable. Claude must follow them on every file it touches.

### Native CSS Nesting — Always

```css
/* WRONG — never do this */
.card .title { font-size: var(--text-lg); }
.card .title:hover { color: var(--color-accent); }
@media (max-width: 768px) { .card { padding: var(--space-2); } }

/* RIGHT — always do this */
.card {
  padding: var(--space-4);

  & .title {
    font-size: var(--text-lg);

    &:hover {
      color: var(--color-accent);
    }
  }

  @media (max-width: 768px) {
    padding: var(--space-2);
  }
}
```

### Custom Properties — Always

```css
/* WRONG */
.btn { background: #6200ea; padding: 12px 24px; }

/* RIGHT */
.btn {
  background: var(--color-primary);
  padding: var(--space-3) var(--space-6);
}
```

### Container Queries Over Media Queries for Component-Level Responsiveness

```css
.card-wrapper { container-type: inline-size; }

.card {
  @container (min-width: 400px) {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
```

### base.css — Always the First File Generated

for css structure for each component, use the structure used in wovenAI project as its nested native structure

```css
:root {
  /* Typography */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;

  /* Spacing (base 4px) */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;

  /* Colors — filled in from design decision doc */
  --color-primary: ;
  --color-surface: ;
  --color-accent: ;
  --color-muted: ;
  --color-error: ;
  --color-text: ;
  --color-bg: ;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: var(--font-body);
  color: var(--color-text);
  background: var(--color-bg);
  line-height: 1.6;
}
```

---

## Phase 4 — JS Gotchas (same priority as CSS gotchas)

### Always scope queries to the container argument

```js
// WRONG — breaks when multiple instances render on the same page
function bindEvents() {
  document.querySelector('.btn').addEventListener('click', handleClick);
}

// RIGHT — scoped to the component's own DOM subtree
function bindEvents(container) {
  container.querySelector('.btn').addEventListener('click', handleClick);
}
```

### Always use ?raw on .hbs imports

```js
// WRONG — Vite tries to process this as a module, fails silently
import template from './Header.hbs';

// RIGHT — Vite passes the file content as a raw string
import template from './Header.hbs?raw';
```

### Always named exports from components

```js
// WRONG
export default function renderHeader(container, context) { ... }

// RIGHT
export function renderHeader(container, context = {}) { ... }
```

### Render functions are synchronous

```js
// WRONG — causes Layout.js to break when it calls renderHeader() without awaiting
export async function renderHeader(container, context = {}) {
  container.innerHTML = compiledTemplate(context);
}

// RIGHT — render is sync. Data fetching belongs in services, called before render.
export function renderHeader(container, context = {}) {
  container.innerHTML = compiledTemplate(context);
  bindEvents(container);
}
```

### Motion library init lives in src/lib/, never in components

```js
// WRONG
import * as THREE from 'three';
const scene = new THREE.Scene(); // never in a component file

// RIGHT — all Three.js / GSAP setup in src/lib/threeInit.js or src/lib/gsapInit.js
// Components import functions from src/lib/, never from the library package directly
```

If a motion library was selected in intake, scaffold.py must create `src/lib/` and the
appropriate init file before generating any component files.

---

## Phase 5 — Component Conventions

Every component lives in its own folder. Three files, always.

```
components/
  layout/
    Header/
      Header.hbs    ← markup only, no logic
      Header.js     ← import/export, event binding, Handlebars compile
      Header.css    ← scoped styles, native nesting only
```

### Every generated file gets a self-documenting header comment

```js
// Header.js
// Layout component — rendered once per page load, owns nav and branding.
// To add nav links: update Header.hbs and pass { navItems: [...] } from Layout.js
// To restyle: edit Header.css — all tokens defined in src/styles/base.css
```

```css
/* Header.css */
/* Scoped to .header — do not style children from other components here.
   Native CSS nesting throughout. All values via custom properties from base.css. */
```

```hbs
{{! Header.hbs }}
{{! Receives: { title, navItems } from Layout.js context }}
```

### Component JS pattern

```js
import Handlebars from 'handlebars';
import template from './Header.hbs?raw';
import './Header.css';

const compiledTemplate = Handlebars.compile(template);

export function renderHeader(container, context = {}) {
  container.innerHTML = compiledTemplate(context);
  bindEvents(container);
}

function bindEvents(container) {
  // event listeners scoped to container
}
```

### Layout.js — owns the shell

```js
import { renderHeader } from '../Header/Header.js';
import { renderBody }   from '../Body/Body.js';
import { renderFooter } from '../Footer/Footer.js';

export function renderLayout(root, context = {}) {
  root.innerHTML = `
    <header id="header"></header>
    <main id="body"></main>
    <footer id="footer"></footer>
  `;
  renderHeader(root.querySelector('#header'), context);
  renderBody(root.querySelector('#body'), context);
  renderFooter(root.querySelector('#footer'), context);
}
```

### app.js — entry point

```js
import { renderLayout } from './components/layout/Layout/Layout.js';

const root = document.getElementById('app');
renderLayout(root, { title: 'App Name' });
```

---

## Phase 6 — Service Layer

No business logic in components. Services are the only thing that touches
fetch, storage, auth, and routing.

```
services/
  apiService.js      ← fetch wrapper, base URL, error handling
  authService.js     ← token storage, login/logout, auth state
  routeService.js    ← hash-based client-side routing
  storageService.js  ← localStorage/sessionStorage wrapper
```

### apiService.js

```js
// apiService.js
// Fetch wrapper — backend-flexible.
// Change VITE_API_URL in .env to point at any backend.
// No changes to this file needed when switching backends.

const BASE_URL = import.meta.env.VITE_API_URL ?? '/api';

async function request(method, path, body = null) {
  const options = {
    method,
    headers: { 'Content-Type': 'application/json' },
  };
  if (body) options.body = JSON.stringify(body);

  try {
    const res = await fetch(`${BASE_URL}${path}`, options);
    if (!res.ok) {
      throw new Error(
        `API error: ${method} ${path} returned ${res.status}.\n` +
        `Check your backend is running at ${BASE_URL}.\n` +
        `To change the base URL, update VITE_API_URL in your .env file.`
      );
    }
    return res.json();
  } catch (err) {
    console.error('[apiService]', err.message);
    throw err;
  }
}

export const api = {
  get:    (path)       => request('GET',    path),
  post:   (path, body) => request('POST',   path, body),
  put:    (path, body) => request('PUT',    path, body),
  delete: (path)       => request('DELETE', path),
};
```

### routeService.js

```js
// routeService.js
// Hash-based client-side routing. No server config required.
// To switch to History API: replace 'hashchange' with 'popstate'
// and window.location.hash with window.location.pathname

const routes = new Map();

export function register(path, renderFn) {
  routes.set(path, renderFn);
}

export function navigate(path) {
  window.location.hash = path;
}

function resolve() {
  const path = window.location.hash.replace('#', '') || '/';
  const renderFn = routes.get(path) ?? routes.get('*');
  if (!renderFn) {
    console.warn(
      `[routeService] No route registered for "${path}". ` +
      `Register a '*' route to handle 404s.`
    );
    return;
  }
  renderFn();
}

export function init() {
  window.addEventListener('hashchange', resolve);
  resolve(); // handle initial load
}
```

---

## Phase 7 — LSP Setup

### .lsp.json

```json
{
  "lspServers": {
    "css": {
      "command": "vscode-css-language-server",
      "args": ["--stdio"],
      "extensionToLanguage": {
        ".css": "css"
      }
    },
    "html": {
      "command": "vscode-html-language-server",
      "args": ["--stdio"],
      "extensionToLanguage": {
        ".hbs": "html",
        ".html": "html"
      }
    }
  }
}
```

### scripts/setup.sh

```bash
#!/bin/bash
set -e

echo ""
echo "🛠  vanilla-scaffold (if-it-ain't-broke) — setup"
echo "──────────────────────────────────────────────────"

NODE_VERSION=$(node -v 2>/dev/null | sed 's/v//' | cut -d. -f1)
if [ -z "$NODE_VERSION" ]; then
  echo "❌  Node.js not found. Install from https://nodejs.org and re-run setup."
  exit 1
fi
if [ "$NODE_VERSION" -lt 18 ]; then
  echo "⚠️  Node.js v$NODE_VERSION detected. v18+ recommended for Vite and ESM support."
fi

if ! command -v vscode-css-language-server &> /dev/null; then
  echo "→  Installing vscode-langservers-extracted (CSS + HTML LSP)..."
  npm install -g vscode-langservers-extracted
  echo "✓  LSP installed"
else
  echo "✓  CSS LSP already installed — skipping"
fi

echo ""
echo "✅  Setup complete."
echo ""
echo "Next steps:"
echo "  1. Open a project folder"
echo "  2. Run: /vanilla-scaffold"
echo "  3. Answer 3 questions — scaffold generates from your answers"
echo ""
```

### scripts/setup.ps1

```powershell
Write-Host ""
Write-Host "🛠  vanilla-scaffold (if-it-ain't-broke) — setup" -ForegroundColor Cyan
Write-Host "──────────────────────────────────────────────────"

try {
  $nodeVersion = (node -v) -replace 'v','' -split '\.' | Select-Object -First 1
  if ([int]$nodeVersion -lt 18) {
    Write-Host "⚠️  Node.js v$nodeVersion detected. v18+ recommended." -ForegroundColor Yellow
  }
} catch {
  Write-Host "❌  Node.js not found. Install from https://nodejs.org" -ForegroundColor Red
  exit 1
}

$lspInstalled = Get-Command vscode-css-language-server -ErrorAction SilentlyContinue
if (-not $lspInstalled) {
  Write-Host "→  Installing vscode-langservers-extracted..."
  npm install -g vscode-langservers-extracted
  Write-Host "✓  LSP installed" -ForegroundColor Green
} else {
  Write-Host "✓  CSS LSP already installed — skipping" -ForegroundColor Green
}

Write-Host ""
Write-Host "✅  Setup complete." -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Open a project folder"
Write-Host "  2. Run: /vanilla-scaffold"
Write-Host "  3. Answer 3 questions — scaffold generates from your answers"
Write-Host ""
```

---

## DX Layer — Escape Hatches & Extension Guide

Generated as part of the project README by scaffold.py.

### Escape hatches

| Default | Why | How to change |
|---|---|---|
| Native CSS nesting | No preprocessor dependency | This is non-negotiable. Use `& .child {}` syntax. |
| Handlebars templating | Markup/logic separation | Swap `.hbs` for `.html` + update `?raw` import in component `.js` |
| Hash-based routing | No server config needed | In `routeService.js`: `hashchange` → `popstate`, `location.hash` → `location.pathname` |
| Vite | Fast ESM dev server | Any ESM bundler works — Parcel, Rollup, esbuild. Swap `vite.config.js`. |
| `VITE_API_URL` env var | Works with any backend | Hardcode `BASE_URL` in `apiService.js` if you don't need env management |

### How to add a feature component

```
1. Create: src/components/features/YourFeature/
2. Add:    YourFeature.hbs / YourFeature.js / YourFeature.css
3. Import + call from Body.js
4. Add a mount slot in Body.hbs

No registration. No build config changes. That's it.
```

### How to add a service

```
1. Create src/services/yourService.js
2. Named exports only — no default exports in services
3. Import directly into any component that needs it
4. Never import one service from another — keep them flat
```

---

## Completed When

### Core skill
- [ ] `SKILL.md` — `vanilla-scaffold` name, all three phases, hard stop after Phase 2
- [ ] `.lsp.json` — HTML + CSS language servers wired
- [ ] `scripts/setup.sh` + `setup.ps1` — Node check, idempotent LSP install, next-steps output
- [ ] `scripts/scaffold.py` — per-file progress, `--force` flag, runnable summary at end

### References
- [ ] `references/css-modern-spec.md` — native nesting, container queries, custom properties
- [ ] `references/design-system.md` — banned patterns, font rules, color conventions
- [ ] `references/app-type-map.md` — app type + vibe → library + color direction
- [ ] `references/component-conventions.md` — .hbs/.js/.css pattern with examples

### Templates
- [ ] `templates/index.html` — `<div id="app">` + `<script type="module">` correct
- [ ] `templates/vite.config.js` — `assetsInclude: ['**/*.hbs']` present
- [ ] `templates/package.json` — `"type": "module"`, handlebars + vite only
- [ ] `templates/.env.example` — VITE_API_URL documented
- [ ] `templates/` — Layout, Header, Body, Footer, base.css with self-documenting headers
- [ ] `templates/services/apiService.js` — descriptive errors with recovery instructions
- [ ] `templates/services/routeService.js` — hash routing + 404 handler

### DX verification
- [ ] `npm install && npm run dev` works on a fresh scaffold with zero extra steps
- [ ] Setup script is idempotent — running it twice produces no errors
- [ ] Setup script exits clearly on Node < 18 with install link
- [ ] Scaffold exits clearly if target directory exists
- [ ] LSP error output shows file + line + what to fix
- [ ] Generated README includes escape hatches table + "how to add a component"

### Quality gates
- [ ] Full flow tested: 3 questions → design doc → "yes" → scaffold → LSP validates → zero flat selectors
- [ ] Read the project cold — can a backend dev understand the structure in under 2 minutes?
- [ ] Run setup twice in a row — stays clean both times

---

## Non-Negotiables

### CSS / Architecture
1. Native CSS nesting always. Flat selectors are a build error.
2. All values via custom properties. No hardcoded hex or px outside `:root`.
3. No SCSS. No preprocessors. Ever.
4. Design decision doc before any code. No exceptions.
5. Service layer is the only thing that touches fetch/storage/auth/routing.
6. Components never import from other components. Only from services and utils.
7. Layout owns the shell. Features live in Body children.
8. LSP validation runs after CSS generation. Fix diagnostics before done.

### JavaScript
9. Always scope `querySelector` to the `container` argument, never `document`.
10. Always use `?raw` on `.hbs` imports.
11. Always named exports from components. No default exports.
12. Render functions are synchronous. Data fetching is a service concern.
13. Motion library init lives in `src/lib/`. Components never import libraries directly.

### Developer Experience
14. Every script is idempotent. Running setup twice must not break anything.
15. Every error message includes what failed AND what to do next. No silent failures.
16. Scaffold output is `npm install && npm run dev` runnable with zero extra steps.
17. Generated comments explain *why*, not *what*. Architecture over annotation.
18. Escape hatches are documented. If a user wants to deviate, they know exactly where.
19. The "Completed When" checklist items are verified, not assumed.