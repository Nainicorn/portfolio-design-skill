# App Type Map — vanilla-scaffold Reference

Maps intake answers (app type + vibe) to concrete design direction.
Used during Phase 2 to generate the design decision document.

---

## Matrix: App Type × Vibe → Design Direction

### Portfolio / Personal Site

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Editorial | Deep navy + warm gold | Cormorant Garamond / Source Sans 3 | Asymmetric scroll, generous whitespace | Scroll-triggered fades |
| Brutalist | Black + white, red accent | Archivo Black / IBM Plex Sans | Harsh grid, visible structure | None or abrupt reveals |
| Glassy | Slate + glass morphism tones | Outfit / Plus Jakarta Sans | Centered hero, layered cards | Subtle parallax |
| Playful | Warm pastels + bold accent | Fredoka / Nunito | Playful grid, rounded elements | Bouncy micro-interactions |
| Retro-tech | Phosphor green on dark | Fira Code / IBM Plex Mono | Terminal layout, monospace blocks | Typing effects |

### SaaS Dashboard

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Corporate clean | Neutral grays + blue accent | DM Sans / Work Sans | Sidebar + main grid | Minimal transitions |
| Glassy | Frosted surfaces + subtle gradients | Satoshi / Plus Jakarta Sans | Floating panels, soft depth | Smooth slide-ins |
| Editorial | Dark surface + contrast text | Playfair Display / Lato | Wide data panels, editorial spacing | Content fades |
| GovTech | High contrast accessible palette | Atkinson Hyperlegible / Public Sans | Dense grid, clear hierarchy | None |

### Internal Tool

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Corporate clean | Light gray surface + navy text | Manrope / Nunito Sans | Compact header, tabbed body | Tab transitions |
| Retro-tech | Dark bg + amber/green text | JetBrains Mono / IBM Plex Sans | Utility-dense, monospace tables | None |
| GovTech | White surface + dark text, blue links | Public Sans / Atkinson Hyperlegible | Form-heavy, accessible labels | None |

### Fintech / Data App

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Corporate clean | Deep blue + mint accent | DM Sans / Work Sans | Data grid center, KPI cards top | Number count-ups |
| Editorial | Charcoal + warm amber | Cormorant Garamond / Source Sans 3 | Wide charts, editorial commentary | Scroll reveals |
| Glassy | Dark glass + neon green accent | General Sans / Plus Jakarta Sans | Floating data panels | Smooth data transitions |

### Marketing / Landing Page

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Playful | Bright primaries + warm secondary | Baloo 2 / Varela Round | Hero + benefit blocks + CTA | Scroll-triggered animations |
| Glassy | Premium dark + glass cards | Outfit / Plus Jakarta Sans | Full-width sections, breathing room | Parallax hero |
| Editorial | Cream + charcoal + accent | Playfair Display / Lato | Long-scroll editorial sections | Fade-in blocks |
| Brutalist | High contrast + raw edges | Space Mono / IBM Plex Sans | Grid-breaking, intentional roughness | Abrupt section cuts |

### Developer Tool

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Retro-tech | Terminal dark + green/amber | Fira Code / IBM Plex Mono | Code-block centric, minimal chrome | Typing/cursor effects |
| Brutalist | Black + white + red error | JetBrains Mono / IBM Plex Sans | Dense, no-nonsense layout | None |
| Glassy | Dark slate + soft blue glow | Victor Mono / Plus Jakarta Sans | Panel-based, IDE-inspired | Subtle panel slides |

### E-commerce

| Vibe | Color Direction | Font Pairing | Layout | Motion |
|---|---|---|---|---|
| Corporate clean | White + accent CTA color | Manrope / Work Sans | Card grid, sticky filters | Hover lifts |
| Playful | Warm tones + pop accent | Quicksand / Nunito | Rounded cards, playful badges | Cart bounce |
| Glassy | Premium dark + glass cards | Satoshi / Plus Jakarta Sans | Masonry grid, floating details | Image zoom transitions |
| Editorial | Cream + dark text + gold accent | Cormorant Garamond / Lato | Magazine-style product layout | Scroll fades |

---

## Motion Library Selection

Based on intake question 3:

| Selection | Library | npm Install | Init File |
|---|---|---|---|
| None | — | — | — |
| Subtle CSS transitions | — (pure CSS) | — | — |
| GSAP | gsap | `npm install gsap` | `src/lib/gsapInit.js` |
| Three.js | three | `npm install three` | `src/lib/threeInit.js` |
| Micro-interactions | — (CSS + JS) | — | — |
| Extra libraries | Per user request | Per selection | Per selection |

---

## "Undecided / Custom" Vibe Fallback

When the user selects "Undecided", pick the vibe based on app type:

| App Type | Default Vibe |
|---|---|
| Portfolio | Editorial |
| SaaS dashboard | Corporate clean |
| Internal tool | GovTech |
| Fintech | Corporate clean |
| Marketing | Glassy |
| Developer tool | Retro-tech |
| E-commerce | Corporate clean |
| Other | Glassy |
