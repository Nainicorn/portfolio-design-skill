// apiService.js
// Fetch wrapper — backend-flexible.
// Change VITE_API_URL in .env to point at any backend.
// No changes to this file needed when switching backends.

const BASE_URL = import.meta.env.VITE_API_URL ?? '/api';

async function request(method, path, body = null) {
  const options = {
    method,
    headers: { 'Content-Type': 'application/json' },
  };
  if (body) options.body = JSON.stringify(body);

  try {
    const res = await fetch(`${BASE_URL}${path}`, options);
    if (!res.ok) {
      throw new Error(
        `API error: ${method} ${path} returned ${res.status}.\n` +
        `Check your backend is running at ${BASE_URL}.\n` +
        `To change the base URL, update VITE_API_URL in your .env file.`
      );
    }
    return res.json();
  } catch (err) {
    console.error('[apiService]', err.message);
    throw err;
  }
}

export const api = {
  get:    (path)       => request('GET',    path),
  post:   (path, body) => request('POST',   path, body),
  put:    (path, body) => request('PUT',    path, body),
  delete: (path)       => request('DELETE', path),
};
