// vite.config.js
// Required for .hbs?raw imports to work. Do not remove assetsInclude.
import { defineConfig } from 'vite';

export default defineConfig({
  assetsInclude: ['**/*.hbs'],
});
