// vite.config.js
// Path aliases let components import services and framework modules
// without fragile relative paths. assetsInclude is required for .hbs?raw imports.
import { defineConfig } from 'vite';
import path from 'path';

export default defineConfig({
  assetsInclude: ['**/*.hbs'],
  resolve: {
    alias: {
      '@components': path.resolve(__dirname, 'src/components'),
      '@services': path.resolve(__dirname, 'src/services'),
      '@framework': path.resolve(__dirname, 'src/framework'),
    },
  },
});
