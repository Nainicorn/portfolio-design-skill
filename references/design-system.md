# Design System — vanilla-scaffold Reference

This document defines the design constraints every scaffold project must follow.
The design decision document (Phase 2) populates values within these constraints.

---

## Font Rules

### Banned Fonts
These fonts are banned because they signal "AI-generated generic template":
- Inter
- Roboto
- Arial
- Space Grotesk

### Font Selection Guide

Pick fonts that match the vibe. Every project gets exactly two fonts: display + body.

| Vibe | Display Font Direction | Body Font Direction |
|---|---|---|
| Editorial / dark editorial | High-contrast serif (e.g., Playfair Display, Cormorant Garamond) | Clean humanist sans (e.g., Source Sans 3, Lato) |
| Brutalist / raw | Monospace or industrial (e.g., JetBrains Mono, Space Mono, Archivo Black) | System mono or tight sans (e.g., IBM Plex Sans) |
| Glassy / premium | Geometric display (e.g., Outfit, Satoshi, General Sans) | Neutral sans with good weight range (e.g., Plus Jakarta Sans) |
| Corporate clean | Professional sans (e.g., DM Sans, Manrope) | Readable sans (e.g., Nunito Sans, Work Sans) |
| Playful / expressive | Rounded or quirky (e.g., Fredoka, Baloo 2, Quicksand) | Friendly sans (e.g., Nunito, Varela Round) |
| Retro-tech / terminal | Monospace (e.g., Fira Code, IBM Plex Mono, Victor Mono) | Monospace or tight sans (e.g., IBM Plex Sans Condensed) |
| GovTech / neutral | Accessible sans (e.g., Atkinson Hyperlegible, Public Sans) | Same family or high-legibility sans |

### Loading
All fonts loaded via Google Fonts `<link>` in `index.html`. Define as custom properties:
```css
:root {
  --font-display: 'Outfit', sans-serif;
  --font-body: 'Plus Jakarta Sans', sans-serif;
}
```

---

## Color Conventions

### Required Tokens
Every project defines exactly these 7 color tokens on `:root`:
```
--color-primary   — brand action color (buttons, links, focus rings)
--color-surface   — card/panel backgrounds
--color-accent    — secondary highlight (badges, indicators, hover states)
--color-muted     — disabled text, borders, dividers
--color-error     — error states, destructive actions
--color-text      — primary text color
--color-bg        — page background
```

### Banned Color Patterns
- Purple gradients (signals "AI template")
- Blue CTA button on white background (signals "Bootstrap default")
- Neon on dark without sufficient contrast (accessibility fail)
- More than 2 gradient stops anywhere

### Contrast Requirements
- Text on background: minimum 4.5:1 (WCAG AA)
- Large text on background: minimum 3:1
- Interactive elements: minimum 3:1 against adjacent colors

---

## Spacing

Base unit: 4px. Scale defined as custom properties:
```
--space-1:  0.25rem  (4px)
--space-2:  0.5rem   (8px)
--space-3:  0.75rem  (12px)
--space-4:  1rem     (16px)
--space-5:  1.25rem  (20px)
--space-6:  1.5rem   (24px)
--space-8:  2rem     (32px)
--space-12: 3rem     (48px)
--space-16: 4rem     (64px)
```

Components use spacing tokens exclusively. No magic numbers.

### Spacing Rules (enforced)
- Every margin and padding must use a `--space-*` token. No `12px`, no `1.5em`, no arbitrary values.
- Consistent section spacing: use `--space-12` or `--space-16` between major sections, `--space-4` to `--space-6` within components.
- Padding on containers must be symmetric unless the design intentionally breaks symmetry.
- No element should rely on browser-default margins. The global reset strips them — re-add intentionally or not at all.

### Alignment Rules (enforced)
- Page content must have a consistent horizontal gutter (e.g., `--space-6` or `--space-8` on body/main containers).
- Header content, body content, and footer content must share the same horizontal alignment — left edges line up.
- Grid and flex gaps use spacing tokens. No unitless or arbitrary gap values.
- Vertically, no orphaned whitespace. Footer hugs the bottom of content or viewport (whichever is taller).

### Interactive Element Rules
- Buttons: min-height 44px, horizontal padding `--space-4` to `--space-6`, visible hover + focus states.
- Inputs: same height as buttons, consistent border radius, clear focus ring using `--color-accent`.
- Links: distinguishable from body text via color or underline. Hover state required.
- Touch targets: minimum 44x44px for any clickable/tappable element.

---

## Layout Patterns

| App Type | Recommended Layout |
|---|---|
| Portfolio | Asymmetric, scroll-driven sections, generous whitespace |
| SaaS dashboard | Sidebar + main content grid, dense information hierarchy |
| Internal tool | Compact header, tabbed body, utility-first spacing |
| Fintech | Data-grid centered, monospace numbers, tight vertical rhythm |
| Marketing | Full-width sections, hero-driven, breathing room between blocks |
| Developer tool | Terminal-inspired, monospace-heavy, minimal chrome |
| E-commerce | Card grid, sticky filters, clear CTA hierarchy |

---

## What Gets Generated vs What Gets Decided

| Aspect | Generated (fixed) | Decided (Phase 2) |
|---|---|---|
| File structure | Always the same | — |
| CSS nesting | Always native | — |
| Typography scale | Token names fixed | Font families + weights chosen per vibe |
| Color tokens | Token names fixed | Hex values chosen per vibe |
| Spacing scale | Fixed values | — |
| Motion | — | Chosen in intake, plan written in Phase 2 |
