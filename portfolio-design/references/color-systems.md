# Color Systems

Palette generation, color theory, and WCAG accessibility compliance.

---

## Contrast Requirements (WCAG AA)

**Must meet these ratios:**
- Normal text (< 18px): 4.5:1 minimum
- Large text (≥ 18px or ≥ 14px bold): 3:1 minimum
- UI components and graphics: 3:1 minimum

**Tools to validate:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Browser DevTools accessibility panel

**Common failures:**
- Light gray on white (#999 on #FFF = 2.85:1 ❌)
- Medium gray on white (#666 on #FFF = 5.74:1 ✅)
- Dark gray recommended (#333 on #FFF = 12.63:1 ✅✅)

---

## Color Palette Structures

### Monochromatic
One hue with varying lightness/saturation.

```css
:root {
  --primary-900: #1a202c;
  --primary-700: #2d3748;
  --primary-500: #4a5568;
  --primary-300: #a0aec0;
  --primary-100: #edf2f7;
}
```

**Use for:** Minimal, professional, Swiss style

---

### Complementary
Two colors opposite on color wheel (e.g., blue + orange).

```css
:root {
  --primary: #0066FF; /* Blue */
  --accent: #FF9500;  /* Orange */
  --bg: #FFFFFF;
  --text: #1A1A1A;
}
```

**Use for:** High contrast, energetic, modern

---

### Triadic
Three colors equally spaced on wheel (e.g., RGB).

```css
:root {
  --red: #FF0000;
  --green: #00FF00;
  --blue: #0000FF;
  --bg: #000000;
  --text: #FFFFFF;
}
```

**Use for:** Retro, comic book, playful

---

### Analogous
3-5 adjacent colors on wheel (e.g., blue → cyan → teal).

```css
:root {
  --blue: #0066FF;
  --cyan: #00CCFF;
  --teal: #00CCA3;
  --bg: #F8F9FA;
  --text: #1A1A1A;
}
```

**Use for:** Harmonious, calming, professional

---

## Pre-Made Palettes

### Minimal Professional
```css
:root {
  --bg: #FFFFFF;
  --text: #1A1A1A;
  --gray: #6B7280;
  --accent: #0066FF;
  --border: #E5E7EB;
}
```

---

### Dark Mode Premium
```css
:root {
  --bg: #000000;
  --surface: #1A1A1A;
  --text: #FFFFFF;
  --text-dim: #A0A0A0;
  --accent: #D4AF37; /* Gold */
}
```

---

### Retro Neon
```css
:root {
  --bg: #000000;
  --pink: #FF00FF;
  --cyan: #00FFFF;
  --yellow: #FFFF00;
  --lime: #00FF00;
}
```

---

### Brutalist Bold
```css
:root {
  --black: #000000;
  --white: #FFFFFF;
  --yellow: #FFFF00;
  --red: #FF0000;
  --blue: #0000FF;
}
```

---

### Pastel Soft
```css
:root {
  --bg: #FAF9F6;
  --peach: #FFD4B2;
  --lavender: #D4BBDD;
  --mint: #C5E8D5;
  --sky: #BAE1FF;
  --text: #2C2C2C;
}
```

---

### Cyberpunk Neon
```css
:root {
  --bg: #0A0A0F;
  --cyan: #00FFFF;
  --magenta: #FF00FF;
  --yellow: #FFFF00;
  --pink: #FF10F0;
  --blue: #00D9FF;
}
```

---

### Nature Earth Tones
```css
:root {
  --bg: #F4F1E8;
  --forest: #2C5F2D;
  --earth: #8B5A3C;
  --sage: #9CAF88;
  --clay: #C17A59;
  --text: #2C2C2C;
}
```

---

## Generating Custom Palettes

### From User's Brand Color

User provides: `#FF6B35` (coral orange)

**Generate:**
1. **Primary:** User's color
2. **Background:** White (#FFF) or Black (#000) based on theme
3. **Text:** High contrast to background
4. **Accent:** Complementary or analogous to primary
5. **Shades:** Lighter/darker versions of primary

```css
:root {
  --primary: #FF6B35;       /* User's color */
  --primary-light: #FFA985; /* +40% lightness */
  --primary-dark: #CC5528;  /* -20% lightness */
  --bg: #FFFFFF;
  --text: #1A1A1A;
  --accent: #359AFF;        /* Complementary (blue) */
}
```

---

### From Mood/Keywords

**User says:** "Calm, professional, trustworthy"
**Generate:** Blues and grays

```css
:root {
  --primary: #2563EB; /* Blue */
  --bg: #F8FAFC;
  --text: #1E293B;
  --gray: #64748B;
}
```

**User says:** "Energetic, creative, bold"
**Generate:** Bright, saturated colors

```css
:root {
  --primary: #EC4899; /* Hot pink */
  --accent: #F59E0B;  /* Orange */
  --bg: #FFFFFF;
  --text: #000000;
}
```

**User says:** "Elegant, luxury, premium"
**Generate:** Dark with gold/silver

```css
:root {
  --bg: #000000;
  --text: #FFFFFF;
  --gold: #D4AF37;
  --silver: #C0C0C0;
}
```

---

## Accessibility Validation

**Before finalizing palette, check:**

```javascript
// Pseudo-code for contrast check
function checkContrast(color1, color2) {
  const ratio = getContrastRatio(color1, color2);
  const normalText = ratio >= 4.5;
  const largeText = ratio >= 3.0;
  
  return { ratio, normalText, largeText };
}

// Example
checkContrast('#666666', '#FFFFFF');
// Returns: { ratio: 5.74, normalText: true, largeText: true }
```

**If fails:**
1. Darken light colors or lighten dark colors
2. Test again
3. Provide both normal and large text versions if needed

---

## CSS Custom Properties Setup

**Always structure like this:**

```css
:root {
  /* Brand colors */
  --color-primary: #0066FF;
  --color-accent: #FF9500;
  
  /* Neutrals */
  --color-bg: #FFFFFF;
  --color-surface: #F8F9FA;
  --color-text: #1A1A1A;
  --color-text-dim: #6B7280;
  --color-border: #E5E7EB;
  
  /* Semantic colors */
  --color-success: #10B981;
  --color-error: #EF4444;
  --color-warning: #F59E0B;
  
  /* Spacing (bonus) */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
}

/* Dark mode (optional) */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #1A1A1A;
    --color-text: #FFFFFF;
  }
}
```

**Benefits:**
- User can change entire palette by editing `:root`
- Easy theme switching
- Consistent colors throughout site

---

## Anti-Patterns to Avoid

❌ **Generic AI gradients**
```css
/* Don't do this */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

❌ **Too many colors** (> 5 colors = chaos)

❌ **Inaccessible contrast**
```css
/* Bad: 2.5:1 ratio */
color: #999;
background: #FFF;
```

❌ **Neon on neon** (unreadable)
```css
/* Bad */
color: #FF00FF;
background: #00FFFF;
```

---

## Color Psychology (Quick Reference)

- **Blue:** Trust, professional, calm (tech, corporate)
- **Red:** Energy, urgency, passion (bold, statements)
- **Green:** Growth, nature, health (environmental, wellness)
- **Yellow:** Optimism, creativity, warning (playful, attention)
- **Purple:** Luxury, creativity, wisdom (premium, artistic)
- **Orange:** Friendly, energetic, adventurous (startups, creative)
- **Black:** Sophisticated, powerful, modern (luxury, minimal)
- **White:** Clean, simple, pure (minimal, modern)

---

## Deliverable Format

When generating a palette, output as:

```css
/* Portfolio Color Palette */
:root {
  /* Primary colors */
  --color-primary: #VALUE;
  --color-accent: #VALUE;
  
  /* Background and surfaces */
  --color-bg: #VALUE;
  --color-surface: #VALUE;
  
  /* Text colors */
  --color-text: #VALUE;
  --color-text-dim: #VALUE;
  
  /* Borders and dividers */
  --color-border: #VALUE;
}

/* Contrast ratios (validation):
 * Primary on bg: X.XX:1 ✅/❌
 * Text on bg: X.XX:1 ✅/❌
 * Accent on bg: X.XX:1 ✅/❌
 */
```