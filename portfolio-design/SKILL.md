---
name: portfolio-design
description: Create highly customizable, distinctive personal portfolio websites using HTML, CSS, and Vanilla JavaScript. Use when users want to build portfolio websites, transform resume content into web format, choose from diverse design themes (modern, retro, brutalist, comic book, glassmorphic, terminal, etc.). Focuses on anti-AI-slop aesthetics, complete customizability, manual control, and production-ready content.
license: MIT
---

# Portfolio Design

Build distinctive, fully customizable portfolio websites with vanilla HTML/CSS/JS. Zero framework bloat, maximum control.

## Philosophy

**No AI slop. No generic templates. Complete customization.**

This skill guides users through building portfolios that:

- Look intentionally designed, not AI-generated
- Use vanilla web technologies for simplicity and performance
- Provide complete control over every design decision
- Deploy easily to production hosting

**User provides detail → Skill provides quality.** The more structured input the user gives, the better the output.

## Workflow

### Phase 1: Gather Requirements

**Ask the user to complete this input checklist:**

1. **Theme selection** - See `references/theme-catalog.md` for ALL available themes

   - User can pick one theme or request a hybrid (e.g., "retro + brutalist")
   - Unique themes available: retro 90s, comic book, terminal/hacker, glassmorphic, neo-brutalist, art deco, cyberpunk, hand-drawn/sketch, vaporwave, Swiss/International style, etc.

2. **Color scheme** - See `references/color-systems.md`

   - User can specify exact hex codes, color mood, or request generation
   - Must meet WCAG AA contrast requirements

3. **Resume content** - See `references/resume-input-format.md`

   - Provide a **structured format template** for user to fill out
   - Format includes: projects (with impact metrics), experience, skills, education, contact
   - The more detail here, the better the narrative transformation

**Critical: Do NOT proceed until user provides at least theme + color scheme + basic resume content.**

### Phase 2: Design Consultation

Based on user's theme choice:

1. **Present theme details** from `references/theme-catalog.md`:

   - Visual characteristics
   - Typography recommendations
   - Layout approach
   - Animation style
   - Example code patterns

2. **Refine color palette** using `references/color-systems.md`:

   - Generate palette based on their colors
   - Validate contrast ratios
   - Provide CSS custom properties setup

3. **Plan layout structure**:
   - Based on content volume (heavy projects vs. heavy experience)
   - Single-page vs. multi-page
   - Section organization

### Phase 3: Content Transformation

Transform user's resume input into web-appropriate content:

**Use the structured format from `references/resume-input-format.md` to:**

- Convert experience bullets → narrative with context and impact
- Transform project descriptions → case study format with tech stack, problem, solution, results
- Skills → organized by category with visual treatment matching theme
- Timeline data → visual chronology
- Contact info → clear CTA section

**Key principle:** Web ≠ Resume. Expand context, add personality, show thinking process.

### Phase 4: Code Generation

Generate complete, production-ready code:

**File structure:**

```
portfolio/
├── index.html
├── css/
│   ├── reset.css
│   ├── variables.css (colors, spacing, typography)
│   ├── base.css
│   ├── components.css
│   └── theme.css (theme-specific styles)
├── js/
│   ├── main.js
│   ├── animations.js
│   └── components/ (if needed)
├── assets/
│   ├── images/
│   └── fonts/ (if custom fonts)
└── README.md
```

**Code standards:**

- Semantic HTML5 (proper heading hierarchy, landmarks, etc.)
- CSS custom properties for theming
- Vanilla JavaScript (ES6+, no jQuery)
- Mobile-first responsive design
- Accessibility built-in (ARIA labels, keyboard navigation, focus states)
- Performance optimized (lazy loading, minimal dependencies)

**Reference:**

- `assets/templates/base-structure/` for starter code
- `assets/templates/components/` for reusable components (nav, project cards, contact forms, etc.)
- `references/animation-patterns.md` for vanilla JS animation code

### Phase 5: Customization Guidance

**Provide clear instructions for manual customization:**

1. **How to modify colors** - Point to CSS variables
2. **How to adjust spacing** - Spacing system documentation
3. **How to add/remove sections** - Modular structure explanation
4. **How to swap fonts** - Typography system
5. **How to debug issues** - Common problems and fixes

**Include inline code comments** explaining what each section does so users can confidently modify.

### Phase 6: Validation & Polish

**If scripts available:**

- Run `scripts/validate_html.py` - Check semantic structure
- Run `scripts/check_accessibility.py` - Basic WCAG validation

**Manual checklist to provide user:**

- [ ] Mobile responsive (test on actual device)
- [ ] Fast load time (< 2s on 3G)
- [ ] All links work
- [ ] Contact form tested (if included)
- [ ] Cross-browser tested (Chrome, Firefox, Safari)
- [ ] Lighthouse score > 90 (performance, accessibility, SEO)
- [ ] No console errors
- [ ] Animations smooth (60fps)

## Quality Standards

### Must-Have:

- ✅ Semantic HTML structure
- ✅ Accessibility (keyboard navigation, screen reader friendly, proper contrast)
- ✅ Mobile-responsive (320px → 4K)
- ✅ Fast performance (minimal JS, optimized images)
- ✅ Clean code with comments
- ✅ Deployment-ready

### Must-Avoid:

- ❌ Framework dependencies (React, Vue, etc.)
- ❌ Generic gradients and particle effects
- ❌ Auto-playing media without controls
- ❌ Resume bullets copied verbatim
- ❌ Inaccessible color combinations
- ❌ JavaScript required for basic functionality
- ❌ Any "AI aesthetic" clichés

## Theme Examples (Brief)

**Full catalog in `references/theme-catalog.md`**

- **Modern Minimal** - Clean, whitespace, sans-serif, subtle animations
- **Neo-Brutalist** - Raw, bold typography, high contrast, geometric shapes
- **Retro 90s** - Bright colors, pixel fonts, GIF-style animations, nostalgic
- **Comic Book** - Bold outlines, halftone patterns, POW/BAM aesthetics, dynamic angles
- **Terminal/Hacker** - Monospace, green/amber on black, typing animations, ASCII art
- **Glassmorphic** - Frosted glass effects, blurs, transparency, soft shadows
- **Cyberpunk** - Neon colors, glitch effects, futuristic, dark backgrounds
- **Hand-Drawn** - Sketch-like, imperfect lines, playful, organic
- **Art Deco** - Geometric patterns, gold accents, elegant, 1920s inspired
- **Swiss/International** - Grid-based, ultra-minimal, perfect alignment, no decoration

(+20 more themes in catalog)

## Troubleshooting

**Common issues and fixes:**

1. **Layout breaking on mobile**

   - Check CSS Grid/Flexbox media queries
   - Verify viewport meta tag
   - Test with browser DevTools device mode

2. **Animations janky**

   - Use `transform` and `opacity` only (GPU-accelerated)
   - Add `will-change` property
   - Reduce animation complexity

3. **Fonts not loading**

   - Check font file paths
   - Verify CORS headers
   - Use font-display: swap

4. **Images slow to load**
   - Compress images (TinyPNG, ImageOptim)
   - Use WebP format with fallbacks
   - Implement lazy loading
   - Set explicit width/height

**For any issues, provide:**

- Exact error message
- Browser/device
- Relevant code snippet
- What you've already tried

## Progressive Enhancement

**For beginners:**

- Start with single theme from catalog
- Use provided base template
- Follow step-by-step customization guide
- Deploy to GitHub Pages (easiest)

**For experienced developers:**

- Hybrid themes
- Custom animation systems
- Advanced layout techniques
- Full control over build process

## Success Criteria

A completed portfolio should:

- Reflect user's unique personality and brand
- Be indistinguishable from professionally designed sites
- Load fast and work everywhere
- Be something the user is proud to share
- **NOT look AI-generated**

---

**Next: User provides theme choice, color preferences, and resume content in specified format.**
