# Portfolio Theme Catalog

20+ themes with code patterns. Each includes: visual traits, typography, colors, layout, animation approach.

---

## 1. Modern Minimal

**For:** Designers, UX professionals
**Visual:** 60% whitespace, subtle transitions, bento grid
**Typography:** Inter/Outfit, 48-72px headings, 16-18px body
**Colors:** White bg, dark gray text, one accent color
**Layout:** Asymmetric grid, generous padding (80-120px)
**Animation:** Fade-in on scroll (0.4s), hover scale (1.02x)

```css
:root {
  --bg: #FFFFFF;
  --text: #1A1A1A;
  --accent: #0066FF;
}
.section { opacity: 0; transition: opacity 0.4s; }
.section.visible { opacity: 1; }
```

---

## 2. Neo-Brutalist

**For:** Developers, bold personalities
**Visual:** Heavy borders (3-5px black), high contrast, geometric
**Typography:** Bold (700-900), 64-96px, uppercase
**Colors:** Black + white + 2-3 saturated accents (yellow, red, blue)
**Layout:** Blocky, overlapping elements, thick borders
**Animation:** Linear transitions, glitch on hover, no easing

```css
:root { --black: #000; --white: #FFF; --yellow: #FF0; }
.card {
  border: 4px solid var(--black);
  background: var(--yellow);
  transition: transform 0.1s linear;
}
.card:hover { transform: translate(-4px, -4px); }
```

---

## 3. Retro 90s Web

**For:** Nostalgic developers, playful creatives
**Visual:** Bright colors, pixel fonts, GIF-style animations
**Typography:** Press Start 2P / VT323 (pixel fonts)
**Colors:** Hot pink, cyan, lime, yellow on black
**Layout:** Centered content, tiled backgrounds, marquee
**Animation:** Blink, marquee scroll, low framerate (steps())

```css
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P');
body {
  font-family: 'Press Start 2P', monospace;
  background: #000;
  color: #0FF;
}
.blink { animation: blink 1s steps(2) infinite; }
@keyframes blink { 50% { opacity: 0; } }
```

---

## 4. Comic Book

**For:** Illustrators, creative professionals
**Visual:** Bold black outlines, halftone patterns, speech bubbles
**Typography:** Bangers/Bungee (comic fonts), uppercase
**Colors:** Red, yellow, blue primaries + black outlines
**Layout:** Rotated panels (5-10deg), overlapping
**Animation:** Pop effects, shake on hover, explosion transitions

```css
.panel {
  border: 4px solid #000;
  box-shadow: 8px 8px 0 #000;
  transform: rotate(-2deg);
}
.halftone {
  background: radial-gradient(circle, #000 1px, transparent 1px);
  background-size: 4px 4px;
}
```

---

## 5. Terminal / Hacker

**For:** Backend engineers, CLI enthusiasts
**Visual:** Monospace fonts, green/amber on black, cursor blink
**Typography:** Fira Code / JetBrains Mono, 14-16px
**Colors:** Green (#0F0) or amber (#F90) on black
**Layout:** Full-width terminal, left-aligned, line numbers
**Animation:** Typing effect, cursor blink, scan lines

```css
body {
  font-family: 'Fira Code', monospace;
  background: #0A0A0A;
  color: #0F0;
}
.cursor {
  display: inline-block;
  width: 10px;
  background: #0F0;
  animation: blink 1s step-end infinite;
}
```

---

## 6. Glassmorphic

**For:** Modern designers, UI specialists
**Visual:** Frosted glass (backdrop-filter), soft shadows
**Typography:** Inter/SF Pro, light to medium weights
**Colors:** Soft muted, low opacity backgrounds (rgba)
**Layout:** Floating cards, overlapping layers
**Animation:** Smooth blur intensity changes, gentle floating

```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
}
```

---

## 7. Cyberpunk / Neon

**For:** Game developers, futuristic brands
**Visual:** Neon glowing text, dark bg, glitch effects
**Typography:** Orbitron/Rajdhani (futuristic), all-caps
**Colors:** Cyan, magenta, yellow on dark (#0a0a0f)
**Layout:** Angular sections, grid backgrounds, corner accents
**Animation:** Glitch on hover, neon flicker, scan lines

```css
.neon-text {
  color: #0FF;
  text-shadow: 0 0 10px #0FF, 0 0 20px #0FF, 0 0 30px #0FF;
  animation: flicker 3s infinite;
}
.neon-box {
  border: 2px solid #F0F;
  box-shadow: 0 0 10px #F0F, inset 0 0 10px rgba(255,0,255,0.1);
}
```

---

## 8. Hand-Drawn / Sketch

**For:** Illustrators, playful brands
**Visual:** Imperfect lines, doodles, paper texture
**Typography:** Caveat/Patrick Hand (handwriting fonts)
**Colors:** Soft muted OR bold crayon colors, off-white bg
**Layout:** Asymmetric, rotated elements, overlapping
**Animation:** Hand-drawn line (SVG path), wiggle on hover

```css
.sketch-box::before {
  border: 3px solid #2C2C2C;
  border-radius: 255px 15px 225px 15px/15px 225px 15px 255px;
}
@keyframes wiggle {
  0%, 100% { transform: rotate(-1deg); }
  25% { transform: rotate(1deg); }
}
```

---

## 9. Art Deco / Gatsby

**For:** Elegant portfolios, luxury brands
**Visual:** Geometric patterns, gold/black, symmetrical
**Typography:** Playfair Display (serif), Poiret One (deco)
**Colors:** Black, cream, gold (#D4AF37)
**Layout:** Centered, symmetrical, vertical elegance
**Animation:** Slow elegant transitions, gold shimmer

```css
.gold-text {
  background: linear-gradient(90deg, #D4AF37 0%, #FFD700 50%, #D4AF37 100%);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  color: transparent;
  animation: shimmer 3s ease infinite;
}
```

---

## 10. Swiss / International

**For:** Minimalists, designers, typographers
**Visual:** Perfect grid, ultra-minimal, mathematical precision
**Typography:** Helvetica/Inter, strict hierarchy, left-aligned
**Colors:** Black and white, one accent (red/blue) sparingly
**Layout:** 12-column grid, asymmetric balance, generous margins
**Animation:** None or minimal fades only

```css
:root {
  --text-base: 16px;
  --text-2xl: 32px;
  --space-4: 32px;
}
.container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
}
```

---

## 11. Vaporwave

**For:** Artistic, nostalgic creatives
**Visual:** Pastels (pink, cyan, purple), Greek statues, VHS glitch
**Typography:** Outrun/retro fonts with gradients
**Colors:** #FF71CE (pink), #01CDFE (cyan), #B967FF (purple)
**Layout:** Full-screen sections, palm trees, sunsets
**Animation:** VHS distortion, glitch, slow motion

---

## 12. Dark Mode Luxury

**For:** Premium brands, elegant portfolios
**Visual:** Pure black (#000), gold/silver accents
**Typography:** Elegant serif, thin weights
**Colors:** Black bg, gold (#D4AF37) or silver (#C0C0C0)
**Layout:** Spacious, centered, minimal
**Animation:** Subtle, slow, premium feel

---

## 13. Newspaper / Editorial

**For:** Writers, journalists, content creators
**Visual:** Multi-column, serif fonts, print-inspired
**Typography:** Times-style serif, drop caps
**Colors:** Black text on white, red for accents
**Layout:** 3-4 columns, newspaper grid
**Animation:** Minimal, page turn effects

---

## 14. Bento Box / Card Grid

**For:** Versatile, modern aesthetic
**Visual:** Grid of varied-size cards
**Typography:** Clean sans-serif
**Colors:** Flexible (colorful or minimal)
**Layout:** CSS Grid with different sized cards
**Animation:** Subtle hover lifts

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
}
.card { aspect-ratio: 1; }
.card.wide { grid-column: span 2; }
```

---

## 15. Terminal Code Editor

**For:** Developers, technical portfolios
**Visual:** VSCode/Sublime aesthetic, syntax highlighting
**Typography:** Monospace (Fira Code), ligatures
**Colors:** Dark theme (Dracula, One Dark, Monokai)
**Layout:** Editor-style tabs, line numbers
**Animation:** Typing, cursor blink

---

## 16. Memphis Design

**For:** Energetic, playful creatives
**Visual:** Bold geometric shapes, 80s postmodern
**Typography:** Bold sans-serif, geometric fonts
**Colors:** Bright, clashing primaries
**Layout:** Chaotic but intentional, patterns everywhere
**Animation:** Bouncy, energetic

---

## 17. Portfolio-as-Resume

**For:** Traditional industries, conservative
**Visual:** Literally looks like a resume
**Typography:** Professional serif/sans
**Colors:** Black on white, minimal color
**Layout:** Standard resume sections
**Animation:** Minimal or none, PDF download prominent

---

## 18. Photography-Focused

**For:** Photographers, visual artists
**Visual:** Full-bleed images, minimal text
**Typography:** Clean sans-serif, small
**Colors:** From images
**Layout:** Gallery-style, lightbox
**Animation:** Smooth image transitions

---

## 19. Experimental / Avant-Garde

**For:** Artists, boundary-pushers
**Visual:** Breaking all rules intentionally
**Typography:** Unusual, rotated, overlapping
**Colors:** Unexpected combinations
**Layout:** Non-standard navigation, artistic
**Animation:** Complex, interactive, surprising

---

## 20. One-Page Parallax

**For:** Storytellers, narrative portfolios
**Visual:** Sections scroll at different speeds
**Typography:** Varies by section
**Colors:** Varies by section theme
**Layout:** Full-screen sections, vertical narrative
**Animation:** Parallax scroll, smooth transitions

---

## Hybrid Themes

Combine any two themes (60/40 split recommended):

**Examples:**
- Retro + Brutalist: Pixel fonts + heavy borders + neon colors
- Swiss + Terminal: Perfect grid + monospace + minimal
- Glassmorphic + Cyberpunk: Frosted neon panels + glowing edges
- Art Deco + Dark Mode: Gold on black + geometric patterns

**Process:**
1. Pick primary theme (60% of visual language)
2. Pick secondary theme (40% of accent elements)
3. Merge color palettes carefully
4. Combine layout approaches
5. Balance, don't clash