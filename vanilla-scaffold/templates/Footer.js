// Footer.js
// Layout component — rendered once per page load, owns copyright and footer links.
// To add footer links: update Footer.hbs and pass context from Layout.js
// To restyle: edit Footer.css — all tokens defined in src/styles/base.css

import Handlebars from 'handlebars';
import template from './Footer.hbs?raw';
import './Footer.css';

const compiledTemplate = Handlebars.compile(template);

export function renderFooter(container, context = {}) {
  container.innerHTML = compiledTemplate(context);
  bindEvents(container);
}

function bindEvents(container) {
  // Footer event listeners scoped to this component's DOM subtree
}
