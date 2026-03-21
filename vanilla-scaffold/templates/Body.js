// Body.js
// Main content area — feature components are imported and rendered here.
// To add a feature: import its render function and call it on a mount point.
// Body owns the content layout; features own their internal structure.

import Handlebars from 'handlebars';
import template from './Body.hbs?raw';
import './Body.css';

const compiledTemplate = Handlebars.compile(template);

export function renderBody(container, context = {}) {
  container.innerHTML = compiledTemplate(context);
  bindEvents(container);
}

function bindEvents(container) {
  // Feature-level event delegation can be wired here
}
