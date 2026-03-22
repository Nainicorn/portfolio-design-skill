// scheme.js
// Theme management — dark/light/system with custom theme support.
// Reads from localStorage for persistence. Sets data-scheme and data-theme
// attributes on <body> which scheme.css uses for color derivation.
//
// Usage:
//   import scheme from '@framework/scheme/scheme';
//   scheme.init();                    // Load saved preferences
//   scheme.setScheme('dark');         // 'dark' | 'light' | 'system'
//   scheme.setTheme('ocean');         // Custom theme name
//   scheme.getScheme();               // Current scheme

const STORAGE_KEY_SCHEME = 'app-scheme';
const STORAGE_KEY_THEME = 'app-theme';

const scheme = {
  init() {
    const savedScheme = localStorage.getItem(STORAGE_KEY_SCHEME) || 'dark';
    const savedTheme = localStorage.getItem(STORAGE_KEY_THEME) || 'default';
    this.setScheme(savedScheme);
    this.setTheme(savedTheme);
  },

  setScheme(value) {
    if (value === 'system') {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.body.setAttribute('data-scheme', prefersDark ? 'dark' : 'light');
    } else {
      document.body.setAttribute('data-scheme', value);
    }
    localStorage.setItem(STORAGE_KEY_SCHEME, value);
  },

  setTheme(value) {
    document.body.setAttribute('data-theme', value);
    localStorage.setItem(STORAGE_KEY_THEME, value);
  },

  getScheme() {
    return localStorage.getItem(STORAGE_KEY_SCHEME) || 'dark';
  },

  getTheme() {
    return localStorage.getItem(STORAGE_KEY_THEME) || 'default';
  },
};

export default scheme;
