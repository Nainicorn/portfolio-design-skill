# Component Conventions — vanilla-scaffold Reference

Every component follows the same three-file pattern. No exceptions.

---

## File Structure

```
components/
  layout/
    Layout/
      Layout.hbs    ← shell markup
      Layout.js     ← imports + renders child components
      Layout.css    ← shell styles
    Header/
      Header.hbs    ← markup only, no logic
      Header.js     ← import/export, event binding, Handlebars compile
      Header.css    ← scoped styles, native nesting only
    Body/
      Body.hbs
      Body.js
      Body.css
    Footer/
      Footer.hbs
      Footer.js
      Footer.css
  features/
    [FeatureName]/
      [FeatureName].hbs
      [FeatureName].js
      [FeatureName].css
```

---

## File Roles

### `.hbs` — Markup Only
- Pure Handlebars template
- No logic, no helpers, no inline styles
- Documents its expected context in a comment at the top
- Uses semantic HTML elements

```hbs
{{! Header.hbs }}
{{! Receives: { title, navItems } from Layout.js context }}
<nav class="header">
  <a class="header__logo" href="#">{{title}}</a>
  <ul class="header__nav">
    {{#each navItems}}
      <li><a href="{{this.href}}">{{this.label}}</a></li>
    {{/each}}
  </ul>
</nav>
```

### `.js` — Logic + Binding
- Imports Handlebars, compiles the template
- Uses `?raw` on `.hbs` imports (required for Vite)
- Named export only (`export function render[Component]`)
- Render function is synchronous
- All `querySelector` calls scoped to `container` argument
- Self-documenting header comment

```js
// Header.js
// Layout component — rendered once per page load, owns nav and branding.
// To add nav links: update Header.hbs and pass { navItems: [...] } from Layout.js
// To restyle: edit Header.css — all tokens defined in src/styles/base.css

import Handlebars from 'handlebars';
import template from './Header.hbs?raw';
import './Header.css';

const compiledTemplate = Handlebars.compile(template);

export function renderHeader(container, context = {}) {
  container.innerHTML = compiledTemplate(context);
  bindEvents(container);
}

function bindEvents(container) {
  // Event listeners scoped to this component's DOM subtree
}
```

### `.css` — Scoped Styles
- Native CSS nesting throughout
- All values via custom properties from `base.css`
- Never styles children from other components
- Self-documenting header comment

```css
/* Header.css */
/* Scoped to .header — do not style children from other components here.
   Native CSS nesting throughout. All values via custom properties from base.css. */

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-6);
  background: var(--color-surface);

  & .header__logo {
    font-family: var(--font-display);
    font-size: var(--text-xl);
    color: var(--color-text);
    text-decoration: none;
  }

  & .header__nav {
    display: flex;
    gap: var(--space-4);
    list-style: none;

    & a {
      color: var(--color-text);
      text-decoration: none;
      font-size: var(--text-sm);

      &:hover {
        color: var(--color-accent);
      }
    }
  }
}
```

---

## Layout.js — The Shell Owner

Layout.js is special: it renders the page shell and calls all layout children.

```js
// Layout.js
// Root shell — renders Header, Body, Footer in a fixed page structure.
// Feature components are rendered inside Body, not here.
// To change page structure: edit the innerHTML template below.

import Handlebars from 'handlebars';
import template from './Layout.hbs?raw';
import './Layout.css';
import { renderHeader } from '../Header/Header.js';
import { renderBody }   from '../Body/Body.js';
import { renderFooter } from '../Footer/Footer.js';

const compiledTemplate = Handlebars.compile(template);

export function renderLayout(root, context = {}) {
  root.innerHTML = compiledTemplate(context);
  renderHeader(root.querySelector('#header'), context);
  renderBody(root.querySelector('#body'), context);
  renderFooter(root.querySelector('#footer'), context);
}
```

---

## app.js — Entry Point

```js
// app.js
// Application entry point — mounts the Layout shell into #app.
// Data fetching and service init happens here before render.

import { renderLayout } from './components/layout/Layout/Layout.js';

const root = document.getElementById('app');
renderLayout(root, { title: 'App Name' });
```

---

## Rules (enforced)

1. **Named exports only** — `export function render[Name]`, never `export default`
2. **Sync render** — render functions never `async`. Data comes from services before render.
3. **Scoped queries** — `container.querySelector()`, never `document.querySelector()`
4. **`?raw` imports** — all `.hbs` imports use `?raw` suffix
5. **No cross-component imports** — components import from services and utils only
6. **Layout hierarchy** — Layout → Header/Body/Footer. Features live inside Body.
7. **Three files always** — `.hbs` + `.js` + `.css`. No component without all three.
8. **Self-documenting headers** — every file starts with a comment explaining its role and how to modify it

---

## Adding a Feature Component

```
1. Create: src/components/features/YourFeature/
2. Add:    YourFeature.hbs / YourFeature.js / YourFeature.css
3. Import + call from Body.js
4. Add a mount slot in Body.hbs

No registration. No build config changes. That's it.
```
