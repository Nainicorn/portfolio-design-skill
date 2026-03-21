// app.js
// Application entry point — mounts the Layout shell into #app.
// Data fetching and service init happens here before render.
// To add global state or service initialization, do it here before renderLayout.

import { renderLayout } from './components/layout/Layout/Layout.js';

const root = document.getElementById('app');
renderLayout(root, { title: '{{app-name}}' });
