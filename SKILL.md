---
name: vanilla-scaffold
description: "Scaffold a vanilla JS + Handlebars + Native CSS frontend with layout-first architecture, per-component file separation (.hbs/.js/.css), built-in pub/sub messaging, theme system, modal framework, and backend-ready service layer. Generates clean, structured projects from intake questions — not a design tool, a codebase architect."
---

# vanilla-scaffold

> Stack: Vanilla JS (ESModules) + Handlebars + Native CSS + Vite
> Brand: `if-it-ain't-broke`
> Focus: **Structure and architecture** — give someone the exact layout and codebase they need.

---

## What This Skill Does

Generates a production-ready vanilla frontend with:
- Layout-first component architecture (Layout → Header / Body / Footer)
- Per-component file separation (.hbs / .js / .css)
- Framework layer: pub/sub messaging, dark/light theme system, reusable modal
- Backend-flexible service layer with streaming support
- Path aliases (@components, @services, @framework)
- Native CSS nesting with HSL-based color derivation

This is a **structure tool**, not a design tool. It gives you clean architecture with sensible defaults. The user's CLAUDE.md or description drives the specifics.

---

## Behavior — Three Phases

### Phase 1: Context Intake

Use the `AskUserQuestion` tool to present all 3 questions as interactive selections in a single call.
Do not use plain text for these questions — always use the tool so the user gets clickable options.
The user can always select "Other" (added automatically) to describe something custom.

Questions to ask (all in one AskUserQuestion call):

**Question 1 — "What are you building?"**
Header: `App type`
Options (pick 4, "Other" is automatic):
- **Portfolio / personal site** — "Showcase work, bio, case studies, or projects"
- **SaaS / dashboard** — "Data-driven interface with panels, controls, and navigation"
- **Fintech / data app** — "Financial data, charts, transactions, or analytics"
- **Marketing / landing page** — "Conversion-focused brand storytelling or product launch"

**Question 2 — "What's the vibe?"**
Header: `Vibe`
Options (pick 4, "Other" is automatic):
- **Dark editorial** — "High contrast, bold typography, magazine-like layouts"
- **Brutalist / raw** — "Exposed structure, monospace, anti-design aesthetic"
- **Glassy / premium** — "Frosted glass, soft gradients, luxury feel"
- **Playful / expressive** — "Bold colors, organic shapes, personality-driven"

**Question 3 — "Do you want motion or 3D?"**
Header: `Motion`
Options (pick 4, "Other" is automatic):
- **None** — "Plain CSS transitions only, no external libraries"
- **GSAP** — "Scroll-driven reveals and timeline animations"
- **Three.js** — "3D hero scenes or animated backgrounds"
- **Multiple libraries** — "GSAP + micro-interactions + extras"

After the user answers all 3, use a **second AskUserQuestion** call to ask:

**Question 4 — "Anything else I should know?"**
Header: `Context`
Options:
- **I have a CLAUDE.md** — "Read my project's CLAUDE.md for additional context and constraints"
- **I'll describe it** — "Let me give you more detail about what I need"
- **Nope, that's it** — "Proceed with what you have"

If the user selects "I have a CLAUDE.md", read it before proceeding — this is critical context.
If the user selects "I'll describe it", wait for their input. This may include specifics about
their domain, features, backend stack, or preferences that override defaults.

Then ask for the **app name** in a follow-up text message.
Do not proceed to Phase 2 until all selections + any extra context + app name are collected.

---

### Phase 2: Scaffold Plan (required, before any code)

After intake, output a scaffold plan. This is NOT a heavy design document — it's a brief
summary of what will be generated so the user can course-correct before files are created.

```
## Scaffold Plan — [App Name]

**App type:** [answer]
**Vibe direction:** [answer — this sets the default theme hue/saturation in scheme.css]

### Structure
- Components: Layout, Header, Body, Footer + [any additional based on app type]
- Services: apiService, routeService + [any additional based on context]
- Framework: messages (pub/sub), scheme (dark/light themes), modal

### Typography
- Display font: [specific font — never Inter, Roboto, Arial, Space Grotesk]
- Body font: [specific font]

### Color Tokens
- HSL base: --hue: [value], --saturation: [value]
- Scheme: [dark default / light default / both]

### Motion
- [what gets animated, when, how — or "CSS transitions only"]

### Additional Libraries
- [only if selected — include exact npm install command]
```

**Hard stop after Phase 2.** Output the plan then output this line verbatim and wait:

> **Reply "yes" to generate the scaffold, or describe what you want changed.**

Do not proceed automatically. Only an explicit "yes" or "looks good" triggers Phase 3.
Silence, a slow response, or an unrelated message is not confirmation.

---

### Phase 3: Scaffold Generation

Run `scripts/scaffold.py` with the app name as argument. Then generate all component files per `references/component-conventions.md`.

The generated project structure:

```
[app-name]/
├── index.html
├── vite.config.js              ← path aliases (@components, @services, @framework)
├── package.json
├── .env.example
├── src/
│   ├── app.js                  ← entry point, inits framework + mounts Layout
│   ├── styles/
│   │   └── base.css            ← reset, typography scale, spacing tokens
│   ├── framework/
│   │   ├── messages/
│   │   │   └── messages.js     ← BroadcastChannel pub/sub
│   │   ├── scheme/
│   │   │   ├── scheme.js       ← dark/light/system + custom themes
│   │   │   └── scheme.css      ← HSL-derived color system
│   │   └── modal/
│   │       ├── modal.js        ← open/close, backdrop, Escape key
│   │       ├── modal.hbs
│   │       └── modal.css
│   ├── components/             ← flat structure, no subdirs
│   │   ├── Layout/             ← shell (mounts Header + Body + Footer)
│   │   ├── Header/             ← .hbs + .js + .css
│   │   ├── Body/
│   │   ├── Footer/
│   │   └── [Feature]/          ← user's feature components go here
│   ├── services/
│   │   ├── apiService.js       ← fetch wrapper + streaming support
│   │   └── routeService.js     ← hash-based routing
│   └── lib/                    ← motion library init (if selected)
```

The scaffold script must:
- Print each file as it's created (`✓ Created src/components/Header/Header.js`)
- Exit with a clear error if the target directory already exists — tell the user to pass `--force` or pick a new name
- End with a runnable summary:

```
✅ Scaffold complete — [N] files created

To get started:
  cd [app-name]
  npm install
  npm run dev

Your app opens at http://localhost:5173
```

After generation, run LSP validation on all .css files. Fix any violations before declaring done.

---

## Non-Negotiables

### Architecture
1. Flat component structure. All components under `src/components/` — no `layout/` or `features/` subdirs.
2. Layout owns the shell. Features render inside Body.
3. Service layer is the only thing that touches fetch/storage/auth/routing.
4. Components never import from other components. Only from services, framework, and lib.
5. Framework modules (messages, scheme, modal) are initialized in app.js, used everywhere.
6. Path aliases (@components, @services, @framework) — no fragile relative paths across directories.

### CSS
7. Native CSS nesting always. Flat selectors are a build error.
8. All values via custom properties. No hardcoded hex or px outside `:root` / scheme.css.
9. No SCSS. No preprocessors. Ever.
10. HSL-based color system — scheme.css derives all colors from --hue, --saturation, --lightness.

### JavaScript
11. Always scope `querySelector` to the component's element or container argument, never `document`.
12. Always use `?raw` on `.hbs` imports (or Handlebars Vite plugin if configured).
13. Always named exports from components. No default exports (except framework singletons).
14. Render functions are synchronous. Data fetching is a service concern.
15. Motion library init lives in `src/lib/`. Components never import libraries directly.
16. Cross-component communication via messages.js pub/sub — never direct imports between components.

### UI Quality
17. Zero rogue margins or padding. The base reset kills all browser defaults — if spacing appears, it was intentional via tokens.
18. Every element is explicitly spaced with spacing tokens. No magic numbers — use `--space-*` variables.
19. Alignment is consistent. Header, body, and footer content share the same horizontal gutter.
20. Typography hierarchy is visually obvious. Display → heading → body → caption with clear size/weight contrast.
21. Interactive elements have visible focus states, hover states, and min 44px touch targets.
22. Layout fills the viewport cleanly — no orphaned whitespace, no horizontal overflow.

### Developer Experience
23. Every script is idempotent. Running setup twice must not break anything.
24. Every error message includes what failed AND what to do next. No silent failures.
25. Scaffold output is `npm install && npm run dev` runnable with zero extra steps.
26. Generated comments explain *why*, not *what*. Architecture over annotation.

---

## File References

- `references/css-modern-spec.md` — native nesting, container queries, custom properties
- `references/design-system.md` — banned patterns, font rules, color conventions, spacing/alignment rules
- `references/app-type-map.md` — app type + vibe → library + color direction
- `references/component-conventions.md` — .hbs/.js/.css pattern with examples
- `templates/` — all scaffold file templates including framework/
