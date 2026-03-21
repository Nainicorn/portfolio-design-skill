# CSS Modern Spec — vanilla-scaffold Reference

This document defines the CSS rules enforced in every vanilla-scaffold project.
LSP validation checks against these rules after scaffold generation.

---

## Native CSS Nesting — Always

Every selector must be nested using `&`. Flat selectors are treated as build errors.

```css
/* WRONG — flat selector, never do this */
.card .title { font-size: var(--text-lg); }
.card .title:hover { color: var(--color-accent); }
@media (max-width: 768px) { .card { padding: var(--space-2); } }

/* RIGHT — nested with & */
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

---

## Custom Properties — Always

No hardcoded hex, rgb, or px values outside `:root`. Every value references a custom property.

```css
/* WRONG */
.btn { background: #6200ea; padding: 12px 24px; }

/* RIGHT */
.btn {
  background: var(--color-primary);
  padding: var(--space-3) var(--space-6);
}
```

---

## Container Queries Over Media Queries (Component-Level)

Use container queries for component-level responsiveness. Media queries are reserved
for page-level layout shifts only.

```css
.card-wrapper {
  container-type: inline-size;
}

.card {
  @container (min-width: 400px) {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}
```

---

## :root Custom Property Structure

All design tokens live on `:root`. Components never define their own tokens — they
consume from `:root`.

### Typography Scale
```
--text-xs:   0.75rem
--text-sm:   0.875rem
--text-base: 1rem
--text-lg:   1.125rem
--text-xl:   1.25rem
--text-2xl:  1.5rem
--text-3xl:  1.875rem
--text-4xl:  2.25rem
--text-5xl:  3rem
```

### Spacing Scale (base: 4px)
```
--space-1:  0.25rem
--space-2:  0.5rem
--space-3:  0.75rem
--space-4:  1rem
--space-5:  1.25rem
--space-6:  1.5rem
--space-8:  2rem
--space-12: 3rem
--space-16: 4rem
```

### Color Tokens
```
--color-primary
--color-surface
--color-accent
--color-muted
--color-error
--color-text
--color-bg
```

### Font Tokens
```
--font-display
--font-body
```

---

## Banned Patterns

| Pattern | Why |
|---|---|
| Flat CSS selectors | Breaks nesting convention, harder to trace scope |
| Hardcoded hex outside `:root` | Breaks theming, makes design changes expensive |
| SCSS / preprocessor syntax | Unnecessary — native CSS nesting covers all use cases |
| `!important` | Indicates a specificity problem — fix the cascade instead |
| `@import` in CSS files | Use `<link>` in HTML or JS imports — `@import` blocks rendering |
