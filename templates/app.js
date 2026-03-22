// app.js
// Application entry point — initializes framework systems, then mounts Layout.
// Scheme handles dark/light/theme persistence. Messages enables pub/sub
// between components. Modal is available globally after init.

import scheme from '@framework/scheme/scheme';
import messages from '@framework/messages/messages';
import modal from '@framework/modal/modal';
import { renderLayout } from '@components/Layout/Layout.js';

// Initialize framework
scheme.init();
messages.init();
modal.init();

// Mount app
const root = document.getElementById('app');
renderLayout(root, { title: '{{app-name}}' });
