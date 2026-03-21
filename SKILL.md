---
name: vanilla-scaffold
description: >
  Scaffold a vanilla JS + Handlebars + Native CSS frontend using a layout-first
  architecture with per-component file separation (.hbs/.js/.css), an opinionated
  design system generated from 3 intake questions, and native CSS nesting enforced
  via LSP. Use when the user wants to build a clean, minimal-dependency frontend
  from scratch without a framework.
---

# vanilla-scaffold

> Stack: Vanilla JS (ESModules) + Handlebars + Native CSS + Vite
> Brand: `if-it-ain't-broke`

---

## Behavior — Three Phases

### Phase 1: Context Intake (3 questions, no more)

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

After the user answers all 3, ask for the **app name** in a follow-up text message.
Do not proceed to Phase 2 until all 3 selections + app name are collected.

---

### Phase 2: Design Decision Document (required, before any code)

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

Do not proceed automatically. Only an explicit "yes" or "looks good" triggers Phase 3.
Silence, a slow response, or an unrelated message is not confirmation.

---

### Phase 3: Scaffold Generation

Run `scripts/scaffold.py` with the app name as argument. Then generate all component files per `references/component-conventions.md`.

The scaffold script must:
- Print each file as it's created (`✓ Created src/components/layout/Header/Header.js`)
- Exit with a clear error if the target directory already exists — tell the user to pass `--force` or pick a new name
- End with a runnable summary:

```
✅ Scaffold complete — [N] files created

To get started:
  cd your-app-name
  npm install
  npm run dev

Your app opens at http://localhost:5173
Edit src/components/features/ to build your first page.
```

After generation, run LSP validation on all .css files. Fix any violations before declaring done:

```
⚠️  LSP found [N] CSS issues — fixing before handoff:
  src/components/layout/Header/Header.css:14 — flat selector detected
  src/components/features/MainPage/MainPage.css:8 — hardcoded color value
✓  Fixed. All CSS passes LSP validation.
```

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

---

## File References

- `references/css-modern-spec.md` — native nesting, container queries, custom properties
- `references/design-system.md` — banned patterns, font rules, color conventions
- `references/app-type-map.md` — app type + vibe → library + color direction
- `references/component-conventions.md` — .hbs/.js/.css pattern with examples
- `templates/` — all scaffold file templates
