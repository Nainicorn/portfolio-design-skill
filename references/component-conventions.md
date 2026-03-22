# Component Conventions — vanilla-scaffold Reference

Every component follows the same three-file pattern. No exceptions.
All components live flat under `src/components/` — no `layout/` or `features/` subdirs.

---

## File Structure

```
src/
├── app.js                      ← entry point, inits framework + mounts Layout
├── styles/
│   └── base.css                ← reset, typography, spacing tokens
├── framework/
│   ├── messages/
│   │   └── messages.js         ← BroadcastChannel pub/sub
│   ├── scheme/
│   │   ├── scheme.js           ← dark/light/system + custom themes
│   │   └── scheme.css          ← HSL-derived color system
│   └── modal/
│       ├── modal.js            ← reusable modal (open/close/escape)
│       ├── modal.hbs
│       └── modal.css
├── components/                  ← FLAT — all components at same level
│   ├── Layout/
│   │   ├── Layout.hbs
│   │   ├── Layout.js
│   │   └── Layout.css
│   ├── Header/
│   │   ├── Header.hbs
│   │   ├── Header.js
│   │   └── Header.css
│   ├── Body/
│   │   ├── Body.hbs
│   │   ├── Body.js
│   │   └── Body.css
│   ├── Footer/
│   │   ├── Footer.hbs
│   │   ├── Footer.js
│   │   └── Footer.css
│   └── [YourFeature]/
│       ├── [YourFeature].hbs
│       ├── [YourFeature].js
│       └── [YourFeature].css
├── services/
│   ├── apiService.js            ← fetch wrapper + streaming
│   └── routeService.js          ← hash-based routing
└── lib/                         ← motion library init (if selected)
```

---

## Component JS Pattern

```js
// Header.js
// Layout component — rendered once per page load, owns nav and branding.
// To add nav links: update Header.hbs and pass { navItems: [...] } from Layout.js
// To restyle: edit Header.css — color tokens in scheme.css, spacing in base.css

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

---

## Component CSS Pattern

Uses double-underscore prefix for component scoping (matches wovenAI convention).
All colors from scheme.css variables, spacing from base.css tokens.

```css
/* Header.css */
/* Scoped to .__header — native CSS nesting throughout.
   Colors via scheme.css (--primary-bg, --text-color, etc).
   Spacing via base.css (--space-*, --text-*). */

.__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-6);
  background: var(--secondary-bg);
  border-bottom: 1px solid var(--border-color);

  .__header-logo {
    font-family: var(--font-display);
    font-size: var(--text-xl);
    color: var(--text-color);
    cursor: pointer;
  }

  .__header-nav {
    display: flex;
    gap: var(--space-4);

    a {
      color: var(--text-muted);
      font-size: var(--text-sm);

      &:hover {
        color: var(--accent-color);
      }
    }
  }
}
```

---

## Component HBS Pattern

```hbs
{{! Header.hbs }}
{{! Receives: { title, navItems } from Layout.js context }}
<nav class="__header">
  <span class="__header-logo">{{title}}</span>
  <div class="__header-nav">
    {{#each navItems}}
      <a href="{{this.href}}">{{this.label}}</a>
    {{/each}}
  </div>
</nav>
```

---

## Layout.js — The Shell Owner

Layout renders the page shell and calls all child components.
Uses path aliases for imports.

```js
// Layout.js
// Root shell — renders Header, Body, Footer in a fixed page structure.
// Feature components render inside Body, not here.

import Handlebars from 'handlebars';
import template from './Layout.hbs?raw';
import './Layout.css';
import { renderHeader } from '@components/Header/Header.js';
import { renderBody }   from '@components/Body/Body.js';
import { renderFooter } from '@components/Footer/Footer.js';

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
// Initializes framework (scheme, messages, modal), then mounts Layout.

import scheme from '@framework/scheme/scheme';
import messages from '@framework/messages/messages';
import modal from '@framework/modal/modal';
import { renderLayout } from '@components/Layout/Layout.js';

scheme.init();
messages.init();
modal.init();

const root = document.getElementById('app');
renderLayout(root, { title: 'App Name' });
```

---

## Framework Usage in Components

### Pub/Sub Messaging
```js
// In any component — decouple communication
import messages from '@framework/messages/messages';

// Publish after state change
messages.publish('itemAdded', { id: 123 });

// Subscribe to react
const unsub = messages.subscribe('itemAdded', (msg, data) => {
  refreshList();
});
```

### Modal
```js
// In any component — show a modal
import modal from '@framework/modal/modal';

modal.open({ title: 'Confirm', content: '<p>Are you sure?</p>' });
modal.close();
```

### Theme
```js
// In settings component
import scheme from '@framework/scheme/scheme';

scheme.setScheme('light');    // 'dark' | 'light' | 'system'
scheme.setTheme('ocean');     // custom theme name
```

---

## Rules (enforced)

1. **Flat structure** — all components under `src/components/`, no nesting subdirs
2. **Named exports only** — `export function render[Name]`, never `export default`
3. **Sync render** — render functions never `async`. Data comes from services.
4. **Scoped queries** — `container.querySelector()`, never `document.querySelector()`
5. **`?raw` imports** — all `.hbs` imports use `?raw` suffix
6. **No cross-component imports** — use messages.js pub/sub instead
7. **Layout hierarchy** — Layout → Header/Body/Footer. Features inside Body.
8. **Three files always** — `.hbs` + `.js` + `.css`. No component without all three.
9. **Path aliases** — use `@components`, `@services`, `@framework` for cross-directory imports
10. **Double-underscore classes** — `.__componentName` for CSS scoping

---

## Adding a Feature Component

```
1. Create: src/components/YourFeature/
2. Add:    YourFeature.hbs / YourFeature.js / YourFeature.css
3. Import + call from Body.js
4. Add a mount slot in Body.hbs

No registration. No build config changes.
```
