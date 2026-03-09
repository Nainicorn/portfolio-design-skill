# Color Systems

Palette generation, color theory, WCAG accessibility, and niche-specific palettes.

---

## Contrast Requirements (WCAG AA)

**Must meet these ratios:**
- Normal text (< 18px): 4.5:1 minimum
- Large text (≥ 18px or ≥ 14px bold): 3:1 minimum
- UI components and graphics: 3:1 minimum

**Tools to validate:**
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Browser DevTools accessibility panel
- Realtime Colors: https://realtimecolors.com/

**Common failures:**
- Light gray on white (#999 on #FFF = 2.85:1 fail)
- Medium gray on white (#666 on #FFF = 5.74:1 pass)
- Dark gray recommended (#333 on #FFF = 12.63:1 excellent)

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
**Best for:** Minimal, professional, Swiss style, government

### Complementary
Two colors opposite on color wheel.
```css
:root {
  --primary: #0066FF;
  --accent: #FF9500;
  --bg: #FFFFFF;
  --text: #1A1A1A;
}
```
**Best for:** High contrast, energetic, modern, fintech

### Triadic
Three equally spaced colors.
```css
:root { --red: #FF0000; --green: #00FF00; --blue: #0000FF; }
```
**Best for:** Retro, comic book, playful, gaming

### Analogous
3-5 adjacent colors on wheel.
```css
:root { --blue: #0066FF; --cyan: #00CCFF; --teal: #00CCA3; }
```
**Best for:** Harmonious, calming, healthcare, marine

---

## Niche-Specific Palettes

### Healthcare
```css
:root {
  --bg: #FFFFFF;
  --surface: #F0F9FF;
  --primary: #2563EB;      /* Trustworthy blue */
  --secondary: #059669;    /* Healing green */
  --accent: #0891B2;       /* Calming teal */
  --text: #1E293B;
  --text-dim: #64748B;
  --border: #E2E8F0;
  --success: #10B981;
  --warning: #F59E0B;
  --error: #EF4444;
}
```
**Psychology:** Blues and greens = trust, healing, calm. White space = clarity. Avoid red as primary (anxiety trigger in medical context).

### Law / Legal
```css
:root {
  --bg: #FAF8F5;
  --surface: #FFFFFF;
  --primary: #1B2A4A;      /* Navy authority */
  --secondary: #722F37;    /* Burgundy gravitas */
  --accent: #C9A84C;       /* Gold prestige */
  --text: #1A1A1A;
  --text-dim: #6B7280;
  --border: #E5E1D8;
}
```
**Psychology:** Navy = authority, trust. Burgundy = tradition, seriousness. Gold = prestige, success.

### Fintech
```css
:root {
  --bg: #0F172A;
  --surface: #1E293B;
  --primary: #6366F1;      /* Electric indigo */
  --secondary: #0EA5E9;    /* Sky blue */
  --accent: #22C55E;       /* Money green */
  --text: #F1F5F9;
  --text-dim: #94A3B8;
  --border: #334155;
  --positive: #22C55E;     /* Gains */
  --negative: #EF4444;     /* Losses */
}
```
**Psychology:** Dark bg = premium, focused. Green/red = financial performance signals. Indigo = modern tech.

### Marine / Ocean
```css
:root {
  --bg: #0C2340;
  --surface: #1A3A5C;
  --primary: #008B8B;      /* Deep teal */
  --secondary: #00CED1;    /* Aqua */
  --accent: #00FFFF;       /* Bioluminescent cyan */
  --coral: #FF6F61;        /* Coral accent */
  --text: #E8F4F8;
  --text-dim: #94B8C8;
  --border: #2A5070;
}
/* Light variant */
:root[data-theme="light"] {
  --bg: #EFF6FF;
  --surface: #FFFFFF;
  --text: #0C2340;
  --text-dim: #4A7C9B;
}
```
**Psychology:** Deep blues = depth, mystery. Teal = ocean life. Cyan = bioluminescence, wonder.

### Government
```css
:root {
  --bg: #FFFFFF;
  --surface: #F8F9FA;
  --primary: #112E51;      /* Official navy */
  --secondary: #205493;    /* Link blue */
  --accent: #D83933;       /* Alert red */
  --text: #212121;
  --text-dim: #5B616B;
  --border: #D6D7D9;
  --info: #02BFE7;
  --success: #2E8540;
  --warning: #FDB81E;
  --error: #D83933;
}
```
**Based on USWDS.** Maximum contrast. Official colors only. Accessibility-first.

### AI / Tech
```css
:root {
  --bg: #0A0A0F;
  --surface: #111827;
  --primary: #8B5CF6;      /* Purple AI */
  --secondary: #06B6D4;    /* Cyan data */
  --accent: #22C55E;       /* Active/success */
  --glow: #06B6D4;         /* Neon glow color */
  --text: #E5E7EB;
  --text-dim: #6B7280;
  --border: #1F2937;
}
```
**Psychology:** Dark = focus, futuristic. Purple = intelligence, creativity. Cyan = data, processing.

### Automotive
```css
:root {
  --bg: #000000;
  --surface: #111111;
  --primary: #FFFFFF;
  --secondary: #C0C0C0;    /* Metallic silver */
  --accent: #E31837;       /* Brand red (customize per brand) */
  --text: #FFFFFF;
  --text-dim: #888888;
  --border: #333333;
}
```
**Psychology:** Black = premium, power. White text on black = high contrast, modern. Metallic = engineering.

### Restaurant / Food
```css
:root {
  --bg: #FFF8E7;
  --surface: #FFFFFF;
  --primary: #8B4513;      /* Rich brown */
  --secondary: #C2703C;    /* Terracotta */
  --accent: #D4AF37;       /* Golden */
  --green: #7C8C3B;        /* Herb/olive */
  --text: #2C1810;
  --text-dim: #6B5B50;
  --border: #E8DED0;
}
```
**Psychology:** Warm browns = appetite, comfort. Gold = quality. Green = fresh, natural.

### E-Commerce
```css
/* Clean / Minimalist */
:root {
  --bg: #FFFFFF;
  --surface: #FAFAFA;
  --primary: #000000;
  --accent: #FF4444;       /* Sale/CTA red */
  --text: #1A1A1A;
  --text-dim: #6B7280;
  --border: #E5E7EB;
  --sale: #EF4444;
  --new: #8B5CF6;
  --bestseller: #F59E0B;
}
```

### Personal Brand
**No preset — derive from the person.** Ask about:
- Their favorite colors
- Their industry's visual language
- Their personality (bold? subtle? playful? serious?)
- Any existing brand colors

### Gaming
```css
:root {
  --bg: #0D1117;
  --surface: #161B22;
  --primary: #FF4500;      /* Energy orange-red */
  --secondary: #7C3AED;    /* XP purple */
  --accent: #FBBF24;       /* Gold/coin */
  --neon-green: #39FF14;
  --text: #E6EDF3;
  --text-dim: #8B949E;
  --border: #30363D;
}
```

### Fashion / Luxury
```css
:root {
  --bg: #000000;
  --surface: #0A0A0A;
  --primary: #FFFFFF;
  --accent: #D4AF37;       /* Gold */
  --text: #FFFFFF;
  --text-dim: #888888;
  --border: #222222;
}
/* Or pure monochrome: */
:root {
  --bg: #FFFFFF;
  --primary: #000000;
  --text: #000000;
  --text-dim: #666666;
}
```

### Education
```css
:root {
  --bg: #FFFFFF;
  --surface: #F8FAFC;
  --primary: #2563EB;      /* Learning blue */
  --secondary: #7C3AED;    /* Creative purple */
  --accent: #F59E0B;       /* Achievement gold */
  --success: #16A34A;      /* Progress green */
  --text: #1E293B;
  --text-dim: #64748B;
  --border: #E2E8F0;
}
```

### Music
```css
/* Dark/Moody (default) */
:root {
  --bg: #0A0A0A;
  --surface: #1A1A1A;
  --primary: #FF1744;      /* Vibrant red */
  --secondary: #651FFF;    /* Deep purple */
  --accent: #00E5FF;       /* Electric cyan */
  --text: #FAFAFA;
  --text-dim: #9E9E9E;
  --border: #333333;
}
```

---

## Mood-Based Palette Generation

### From Keywords

| User Says | Color Direction |
|-----------|----------------|
| "Clean, professional, trustworthy" | Blues + grays, white bg |
| "Energetic, bold, creative" | Bright saturated + black text |
| "Elegant, luxury, premium" | Dark bg + gold/silver |
| "Calm, nature, organic" | Earth tones, greens, warm whites |
| "Futuristic, tech, dark" | Dark bg + neon accents |
| "Warm, inviting, friendly" | Warm oranges, yellows, cream |
| "Dark, mysterious, cinematic" | Deep blacks, moody purples, red accents |
| "Playful, fun, youthful" | Bright pastels or bold primaries |
| "Minimal, sophisticated, understated" | Monochrome + one accent |
| "Retro, nostalgic, vintage" | Desaturated tones, sepia, muted neons |

### From Visual Inspiration

| Inspiration | Palette Approach |
|-------------|-----------------|
| Bridgerton / period drama | Gold (#D4AF37), cream (#FAF3E0), deep green (#2D5016), burgundy (#722F37) |
| Blade Runner / cyberpunk | Black (#0A0A0F), neon cyan (#00FFFF), magenta (#FF00FF), amber (#FF9500) |
| Wes Anderson | Pastels — pink (#FFB5B5), mustard (#E8B939), sage (#9FB89E), powder blue (#A8D8EA) |
| Studio Ghibli | Nature greens (#4A7C59), sky blue (#87CEEB), warm cream (#FFF5E4), earth (#8B7355) |
| Apple / minimal tech | White (#FFFFFF), black (#000000), one blue (#0071E3) |
| Spotify / music app | Dark (#121212), green (#1DB954), white text |
| Notion / productivity | Off-white (#FFFFFF), tan (#F7F6F3), dark text (#37352F), accents minimal |

---

## CSS Custom Properties Template

**Always structure palettes like this:**

```css
:root {
  /* Brand colors */
  --color-primary: #VALUE;
  --color-secondary: #VALUE;
  --color-accent: #VALUE;

  /* Background and surfaces */
  --color-bg: #VALUE;
  --color-surface: #VALUE;
  --color-surface-hover: #VALUE;

  /* Text colors */
  --color-text: #VALUE;
  --color-text-dim: #VALUE;
  --color-text-inverse: #VALUE;

  /* Borders and dividers */
  --color-border: #VALUE;
  --color-border-strong: #VALUE;

  /* Semantic colors */
  --color-success: #10B981;
  --color-error: #EF4444;
  --color-warning: #F59E0B;
  --color-info: #3B82F6;

  /* Spacing system */
  --space-xs: 4px;
  --space-sm: 8px;
  --space-md: 16px;
  --space-lg: 24px;
  --space-xl: 32px;
  --space-2xl: 48px;
  --space-3xl: 64px;
  --space-section: 80px;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #VALUE;
    --color-surface: #VALUE;
    --color-text: #VALUE;
    --color-text-dim: #VALUE;
    --color-border: #VALUE;
  }
}
```

---

## Accessibility Validation

```javascript
function getContrastRatio(hex1, hex2) {
  function hexToRgb(hex) {
    const r = parseInt(hex.slice(1, 3), 16) / 255;
    const g = parseInt(hex.slice(3, 5), 16) / 255;
    const b = parseInt(hex.slice(5, 7), 16) / 255;
    return [r, g, b].map(c => c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4));
  }
  function luminance([r, g, b]) { return 0.2126 * r + 0.7152 * g + 0.0722 * b; }

  const l1 = luminance(hexToRgb(hex1));
  const l2 = luminance(hexToRgb(hex2));
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}

// Usage:
// getContrastRatio('#1A1A1A', '#FFFFFF') → 17.15 (excellent)
// getContrastRatio('#999999', '#FFFFFF') → 2.85 (fail for normal text)
```

**Deliverable format — always include contrast validation:**

```css
/* Color Palette — [Project Name]
 *
 * Contrast ratios (text on bg):
 * Primary on bg: X.XX:1 ✅/❌
 * Text on bg: X.XX:1 ✅/❌
 * Text-dim on bg: X.XX:1 ✅/❌
 * Accent on bg: X.XX:1 ✅/❌
 */
```

---

## Anti-Patterns

- Generic AI gradients: `linear-gradient(135deg, #667eea, #764ba2)` — overused, screams AI
- Too many colors (> 5 main colors = visual chaos)
- Neon on neon (unreadable): `color: #FF00FF; background: #00FFFF;`
- Inaccessible contrast: `color: #999; background: #FFF;`
- Using color as the ONLY indicator (always pair with icon/text for colorblind users)
- Brand colors that fail accessibility (darken/lighten to meet ratios, don't skip)

---

## Color Psychology Quick Reference

| Color | Feels Like | Common Niches |
|-------|-----------|---------------|
| Blue | Trust, professional, calm | Healthcare, finance, tech, government |
| Green | Growth, health, nature, money | Healthcare, fintech, eco, agriculture |
| Red | Energy, urgency, passion, danger | Gaming, food, sales, emergency |
| Purple | Luxury, creativity, wisdom, AI | AI/tech, luxury, education, creative |
| Orange | Friendly, energetic, adventurous | Startups, food, youth brands |
| Yellow | Optimism, creativity, warning | Education, creative, caution |
| Gold | Prestige, quality, elegance | Law, luxury, restaurant, automotive |
| Black | Sophisticated, powerful, modern | Fashion, automotive, luxury, gaming |
| White | Clean, simple, pure, space | Healthcare, tech, minimal, government |
| Teal/Cyan | Fresh, modern, digital, ocean | Marine, tech, healthcare, AI |
| Pink | Feminine, playful, romantic | Fashion, beauty, lifestyle, music |
