// routeService.js
// Hash-based client-side routing. No server config required.
// To switch to History API: replace 'hashchange' with 'popstate'
// and window.location.hash with window.location.pathname

const routes = new Map();

export function register(path, renderFn) {
  routes.set(path, renderFn);
}

export function navigate(path) {
  window.location.hash = path;
}

function resolve() {
  const path = window.location.hash.replace('#', '') || '/';
  const renderFn = routes.get(path) ?? routes.get('*');
  if (!renderFn) {
    console.warn(
      `[routeService] No route registered for "${path}". ` +
      `Register a '*' route to handle 404s.`
    );
    return;
  }
  renderFn();
}

export function init() {
  window.addEventListener('hashchange', resolve);
  resolve(); // handle initial load
}
