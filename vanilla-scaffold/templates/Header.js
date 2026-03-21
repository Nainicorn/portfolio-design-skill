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
  const menuToggle = container.querySelector('.header__menu-toggle');
  const nav = container.querySelector('.header__nav');

  if (menuToggle && nav) {
    menuToggle.addEventListener('click', () => {
      nav.classList.toggle('header__nav--open');
    });
  }
}
