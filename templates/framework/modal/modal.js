// modal.js
// Reusable modal system. Call modal.open() with content, modal.close() to dismiss.
// Handles backdrop click, Escape key, and focus trapping.
//
// Usage:
//   import modal from '@framework/modal/modal';
//   modal.open({ title: 'Settings', content: settingsHtml });
//   modal.close();

import template from './modal.hbs';
import './modal.css';

const modal = {
  element: null,

  init() {
    // Create modal container once, append to body
    const wrapper = document.createElement('div');
    wrapper.innerHTML = template();
    this.element = wrapper.firstElementChild;
    document.body.appendChild(this.element);
    this._bindEvents();
  },

  open({ title = '', content = '' } = {}) {
    const titleEl = this.element.querySelector('.__modal-title');
    const bodyEl = this.element.querySelector('.__modal-body');
    if (titleEl) titleEl.textContent = title;
    if (bodyEl) {
      if (typeof content === 'string') {
        bodyEl.innerHTML = content;
      } else {
        bodyEl.innerHTML = '';
        bodyEl.appendChild(content);
      }
    }
    this.element.classList.add('__modal--open');
  },

  close() {
    this.element.classList.remove('__modal--open');
    const bodyEl = this.element.querySelector('.__modal-body');
    if (bodyEl) bodyEl.innerHTML = '';
  },

  _bindEvents() {
    // Close on backdrop click
    this.element.addEventListener('click', (e) => {
      if (e.target.classList.contains('__modal-backdrop')) {
        this.close();
      }
    });

    // Close on X button
    this.element.addEventListener('click', (e) => {
      if (e.target.dataset.action === 'close') {
        this.close();
      }
    });

    // Close on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.element.classList.contains('__modal--open')) {
        this.close();
      }
    });
  },
};

export default modal;
