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

// Streaming fetch — reads chunked responses and calls onChunk with each piece.
// Use for SSE, LLM streaming, or any chunked endpoint.
async function stream(path, body, onChunk) {
  const res = await fetch(`${BASE_URL}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    throw new Error(
      `Stream error: POST ${path} returned ${res.status}.\n` +
      `Check your backend is running at ${BASE_URL}.`
    );
  }

  const reader = res.body.getReader();
  const decoder = new TextDecoder('utf-8');

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    const chunk = decoder.decode(value, { stream: true });
    if (onChunk) onChunk(chunk);
  }
}

export const api = {
  get:    (path)              => request('GET',    path),
  post:   (path, body)       => request('POST',   path, body),
  put:    (path, body)       => request('PUT',    path, body),
  delete: (path)              => request('DELETE', path),
  stream: (path, body, onChunk) => stream(path, body, onChunk),
};
