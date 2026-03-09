---
name: unique-design
description: Create truly unique, niche-specific frontend designs that look nothing like AI-generated templates. Builds distinctive websites for any industry — healthcare, law, fintech, marine, automotive, AI, government, personal brands, and more. Focuses on creative animations, intentional UX, and production-ready code. Supports vanilla JS, React, Vue, Svelte, Next.js, and any modern stack. Uses inspiration from tools like ReactBits, Aceternity UI, GSAP, Framer Motion, and award-winning design patterns.
license: MIT
---

# Unique Frontend Design

Build frontend interfaces so distinctive they could never be mistaken for AI-generated. Every design is one-of-a-kind — shaped by the user's vision, niche, and personality.

## Philosophy

**No AI slop. No generic templates. No cookie-cutter layouts. Every design is a creative act.**

This skill creates frontends that:

- Feel like they were designed by a top-tier creative agency
- Are tailored to the specific niche and audience (healthcare feels different from fintech feels different from a Bridgerton fan site)
- Use animations and interactions that serve the story, not just decorate
- Reference real-world design inspiration — Awwwards winners, Dribbble trends, creative component libraries
- Give the user complete creative control over every decision

**The user drives the vision. The skill brings it to life.**

## Core Constraints (How This Skill Operates)

Adopted from battle-tested development workflows:

- **Step by step** — break every design into sub-tasks, complete each before moving on
- **Ask before proceeding** — never assume stylistic choices. Ask the user
- **Handle every edge case** — loading states, empty states, error states, responsive breakpoints, reduced motion. Leave nothing unhandled
- **No bias** — give honest recommendations based on the actual project needs, not generic best practices. If a user's idea is better than yours, say so
- **The UI must look like a startup product**, not an AI-generated template
- **Simple stack, simple patterns** — don't overcomplicate with unnecessary abstractions
- **Design for the niche** — a law firm site should feel authoritative, a marine biology site should feel like the ocean, a fintech dashboard should feel precise and trustworthy

## Workflow

### Phase 1: Deep Discovery (ASK EVERYTHING)

**This is the most important phase. Do NOT rush through it. Ask the user detailed questions.**

**Round 1 — The Big Picture:**

1. **What is this for?** What's the purpose of this site/app? Who's the audience?
2. **What niche/industry?** Healthcare, law, fintech, marine, automotive, AI, government, e-commerce, personal brand, startup, restaurant, music, gaming, education, nonprofit, real estate, fashion, fitness, etc.
3. **What's the vibe?** Ask them to describe the feeling in 3-5 words. Examples:
   - "Clean, futuristic, trustworthy"
   - "Dark, mysterious, cinematic"
   - "Warm, inviting, handcrafted"
   - "Bold, rebellious, loud"
   - "Elegant, refined, timeless"
   - "Playful, colorful, energetic"
4. **Any visual inspiration?** Websites they love, movies, shows (Bridgerton, Blade Runner, Wes Anderson), art styles, brands, physical spaces, nature
5. **What tech stack?** Ask explicitly:
   - Vanilla HTML/CSS/JS (zero dependencies, maximum simplicity)
   - React (+ which meta-framework? Next.js, Remix, Vite?)
   - Vue (+ Nuxt?)
   - Svelte (+ SvelteKit?)
   - Other preferences?

**Round 2 — Stylistic Deep Dive:**

6. **Typography feel?** Show options:
   - Serif (elegant, editorial, trustworthy)
   - Sans-serif (modern, clean, tech-forward)
   - Monospace (developer, technical, terminal)
   - Display/decorative (bold personality, specific aesthetic)
   - Handwritten (organic, personal, playful)
   - Mixed? (e.g., serif headings + sans body)
7. **Color direction?** Don't just ask for hex codes. Ask:
   - Dark mode or light mode or both?
   - Warm or cool tones?
   - High contrast or subtle?
   - Any brand colors that must be included?
   - Mood-based: "ocean blues", "forest earth tones", "neon night", "pastel sunrise"
8. **Animation philosophy?**
   - Minimal (subtle fades, clean transitions)
   - Moderate (scroll animations, hover effects, page transitions)
   - Heavy/cinematic (parallax, GSAP scroll-driven, 3D elements, complex sequences)
   - Specific ideas? (e.g., "I want the page to open like a garage door", "text should type out like a terminal", "cards should float like they're underwater")
9. **Layout preferences?**
   - Single page or multi-page?
   - How many sections? What content goes where?
   - Full-bleed hero or contained?
   - Grid-based, freeform, asymmetric?
   - Navigation style (sticky header, sidebar, floating, hidden, bottom bar)?
10. **Interactive elements?**
    - Hover effects style
    - Click/tap feedback
    - Scroll behavior (smooth, snap, parallax)
    - Any specific interactions they've seen and loved?

**Round 3 — Content & Structure:**

11. **What content do they have?** Text, images, videos, data, testimonials, case studies, team bios, product info, etc.
12. **Key actions?** What should visitors DO? (Sign up, contact, buy, explore, learn, download)
13. **Special features?** Dark mode toggle, language switching, accessibility controls, filtering, search, forms

**Critical: Do NOT proceed to design until you've asked at least Rounds 1-2. The more you know, the more unique the output.**

### Phase 2: Design Concept

Based on discovery, present a cohesive design concept:

1. **Mood board description** — describe the visual direction in vivid detail
   - Reference specific design inspirations (Awwwards sites, Dribbble shots, real-world aesthetics)
   - Describe how the niche influences the design language
   - Paint the picture: "Imagine opening this site feels like walking into a high-end gallery — dark walls, spotlit content, your cursor leaves a subtle light trail..."

2. **Color palette** — generate using `references/color-systems.md`:
   - Validate WCAG AA contrast ratios
   - Show CSS custom properties
   - Explain the psychology behind choices for their niche

3. **Typography system** — specific font recommendations:
   - Heading font + weight
   - Body font + size
   - Accent/display font if needed
   - Line heights, letter spacing

4. **Animation plan** — specific techniques mapped to their vision:
   - Reference `references/animation-patterns.md` for code patterns
   - Reference `references/creative-libraries-and-patterns.md` for library-specific components
   - Map specific animations to specific sections (hero gets X, cards get Y, nav gets Z)

5. **Layout wireframe** — describe the structure:
   - Section order and purpose
   - Grid system
   - Responsive strategy (mobile-first breakpoints)

6. **Component library recommendations** — based on their stack:
   - If React: suggest ReactBits, Aceternity UI, Magic UI, Motion Primitives, shadcn/ui as appropriate
   - If vanilla: provide copy-paste CSS/JS patterns
   - If Vue/Svelte: adapt patterns to their ecosystem
   - Reference `references/creative-libraries-and-patterns.md` for specifics

**Ask the user to approve, modify, or completely change direction before proceeding.**

### Phase 3: Code Generation

Generate complete, production-ready frontend code:

**Adapt file structure to their chosen stack:**

For vanilla:
```
project/
├── index.html
├── css/
│   ├── reset.css
│   ├── variables.css
│   ├── base.css
│   ├── components.css
│   ├── animations.css
│   └── responsive.css
├── js/
│   ├── main.js
│   ├── animations.js
│   └── components/
└── assets/
    ├── images/
    └── fonts/
```

For React/Next.js:
```
src/
├── components/
│   ├── ui/ (reusable primitives)
│   ├── sections/ (page sections)
│   └── layout/ (nav, footer, wrappers)
├── styles/
│   ├── globals.css
│   └── variables.css
├── hooks/ (custom animation hooks)
├── lib/ (utilities)
└── app/ or pages/
```

**Code standards (ALL stacks):**

- Semantic HTML5 (proper heading hierarchy, landmarks, ARIA where needed)
- CSS custom properties for theming (colors, spacing, typography as variables)
- Mobile-first responsive design (320px → 4K)
- Accessibility built-in:
  - Keyboard navigation and visible focus states
  - Screen reader friendly (aria-labels, roles, live regions)
  - `prefers-reduced-motion` respected on ALL animations
  - `prefers-color-scheme` for dark/light mode
  - Touch targets ≥ 44x44px
  - Color contrast ≥ 4.5:1 (normal text), ≥ 3:1 (large text)
- Performance optimized:
  - Lazy loading images
  - Minimal JS bundles (tree-shake, code-split)
  - GPU-accelerated animations (transform + opacity)
  - `will-change` used sparingly
  - No layout thrashing

**Animation implementation:**

Reference these in order of preference based on stack:

1. **Vanilla JS** → `references/animation-patterns.md` (Intersection Observer, GSAP CDN, CSS animations)
2. **React** → Framer Motion, GSAP with React, ReactBits components, Aceternity UI
3. **Vue** → Vue transitions, GSAP with Vue, Motion One
4. **Svelte** → Built-in transitions/animations, GSAP

For complex/cinematic animations, use GSAP ScrollTrigger patterns from `references/creative-libraries-and-patterns.md`.

### Phase 4: Niche-Specific Refinement

Apply niche-specific design intelligence from `references/niche-design-systems.md`:

- **Healthcare** → calming, trust-building, HIPAA-aware form patterns, accessible
- **Law** → authoritative, dignified, serif-heavy, case-study layouts
- **Fintech** → data-driven, precise, real-time feel, security signals
- **Marine/Ocean** → fluid, wave-based, bioluminescent accents, underwater parallax
- **Government** → WCAG AAA, plain language, structured, USWDS/GOV.UK inspired
- **AI/Tech** → futuristic, dark themes, neural patterns, data visualizations
- **Automotive** → premium, cinematic, full-bleed imagery, configurator UX
- **Restaurant** → warm, sensory, menu-focused, reservation CTA
- **Fashion** → editorial, photography-forward, minimal text, lookbook layouts
- **Gaming** → immersive, bold, animated, achievement-driven UI
- **Music** → audio-visual, rhythm-based animations, dark/moody
- **Education** → clear hierarchy, progress tracking, accessible, engaging
- **Personal brand** → personality-driven, unique story, memorable interactions
- **E-commerce** → conversion-optimized, product-focused, trust signals

Each niche has specific anti-patterns to avoid — reference the niche guide.

### Phase 5: Creative Extras

Based on the user's animation philosophy, offer these enhancements:

**Signature interactions** (make the site memorable):
- Custom cursor effects (scale on hover, magnetic buttons, context-aware cursor)
- Page transition animations (clip-path reveals, crossfades, slide)
- Scroll-driven storytelling (content unfolds as narrative)
- Micro-interactions on every interactive element
- Easter eggs or hidden interactions
- Sound design integration (subtle, optional, respectful)

**Unique concepts** (things that make people say "how did they do that?"):
- Garage door opening → site reveal (CSS clip-path + transform animation)
- Bridgerton-themed → ornate borders, serif typography, gold filigree SVG animations, parchment textures
- Underwater dive → parallax depth layers, bubble particles, bioluminescent glows
- Terminal boot sequence → typing animation loading screen into full site
- Book/magazine → page turn transitions, editorial grid, drop caps
- Dashboard → real-time data animations, chart draws, metric counters
- Retro TV → CRT scanline effects, channel switching between pages

**Always ask:** "Want me to add any signature interactions or creative extras?"

### Phase 6: Customization Guidance

Provide clear documentation so the user can modify anything:

1. **Color system** — point to CSS variables, explain how to swap palettes
2. **Typography** — how to change fonts, adjust scale
3. **Animations** — how to adjust timing, disable specific animations, add new ones
4. **Layout** — how to reorder sections, adjust spacing, modify grid
5. **Responsive** — breakpoint system, how to adjust for specific devices
6. **Components** — how each component works, props/options available

**Include inline code comments** explaining decisions so users can confidently modify.

### Phase 7: Validation & Polish

**Run validation (if scripts available):**

- `scripts/validate_html.py` — semantic structure check
- `scripts/check_accessibility.py` — WCAG validation

**Quality checklist (provide to user):**

- [ ] Mobile responsive (test 320px, 375px, 768px, 1024px, 1440px, 4K)
- [ ] All animations smooth (60fps, no jank)
- [ ] `prefers-reduced-motion` works (animations disabled)
- [ ] Keyboard navigation works (tab through everything)
- [ ] Screen reader tested (meaningful content order)
- [ ] Color contrast passes WCAG AA
- [ ] Images lazy loaded with proper alt text
- [ ] No console errors
- [ ] Fast load time (< 2s on 3G)
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Lighthouse score > 90 (performance, accessibility, SEO, best practices)
- [ ] The design feels unique — show it to someone and ask "does this look AI-generated?"

## Quality Standards

### Must-Have:
- Semantic HTML structure
- Accessibility (keyboard nav, screen reader, proper contrast, reduced motion)
- Mobile-responsive (320px → 4K)
- Fast performance
- Clean, commented code
- Unique visual identity that matches the niche

### Must-Avoid:
- Generic AI gradients (the purple-to-blue gradient of death)
- Cookie-cutter hero sections with stock photos
- Particle.js backgrounds on everything
- Generic card grids with no personality
- "AI aesthetic" cliches (glass cards + gradient bg + sans-serif = boring)
- Inaccessible color combinations
- JavaScript required for basic content visibility
- Framework bloat when vanilla would suffice
- Over-engineering simple interactions
- Animations that serve no UX purpose

## External Inspiration & Tools

**Always encourage users to browse these for inspiration:**

- **ReactBits** (reactbits.dev) — 110+ creative React components, copy-paste ready
- **Aceternity UI** (ui.aceternity.com) — 200+ stunning animated components
- **Magic UI** (magicui.design) — 150+ motion-first components
- **Motion Primitives** (motion-primitives.com) — shadcn-compatible animated components
- **Awwwards** (awwwards.com) — award-winning website designs
- **Dribbble** — visual design trends and niche-specific inspiration
- **GSAP** (gsap.com) — industry-standard animation library with ScrollTrigger
- **Framer Motion / Motion** (motion.dev) — React animation library

See `references/creative-libraries-and-patterns.md` for detailed component lists and usage patterns.

## Niche Examples (Brief)

**Full niche guides in `references/niche-design-systems.md`**

- **Healthcare** — Calming blues/greens, ample whitespace, trust signals, subtle animations
- **Law Firm** — Dark navy/burgundy, serif typography, authoritative, dignified motion
- **Fintech** — Data-driven, dark mode dashboards, precise animations, security-first
- **Marine/Ocean** — Deep blues/teals, wave shapes, underwater parallax, bioluminescent glow
- **Government** — Maximum accessibility, structured grids, plain language, minimal animation
- **AI Application** — Dark + neon, neural patterns, futuristic typography, data flow animations
- **Automotive** — Premium black + metallic, cinematic reveals, full-bleed imagery, configurator UX
- **Restaurant** — Warm tones, sensory imagery, menu typography, reservation-focused
- **Personal Brand** — Personality-driven, unique story, memorable signature interactions
- **E-commerce** — Product-focused, trust signals, smooth cart UX, conversion-optimized

## Success Criteria

A completed frontend should:

- Be immediately recognizable as belonging to its niche
- Have at least one "wow" interaction that makes it memorable
- Be indistinguishable from a professionally designed site
- Load fast and work everywhere
- Be something the user is genuinely excited to show people
- **NOT look AI-generated**

---

**Next: Ask the user what they want to build. Start with Phase 1 discovery questions.**
