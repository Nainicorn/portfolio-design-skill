// Layout.js
// Root shell — renders Header, Body, Footer in a fixed page structure.
// Feature components are rendered inside Body, not here.
// To change page structure: edit Layout.hbs and the mount selectors below.

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
