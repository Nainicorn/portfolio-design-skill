// messages.js
// Pub/sub system using BroadcastChannel for cross-component communication.
// Components publish events after state changes. Other components subscribe
// to react without direct imports — keeps components fully decoupled.
//
// Usage:
//   import messages from '@framework/messages/messages';
//   const unsub = messages.subscribe('chatAdded', (msg, data) => { ... });
//   messages.publish('chatAdded', { id: 123 });
//   unsub(); // cleanup

const channel = new BroadcastChannel('app-messages');
const handlers = new Map();

const messages = {
  init() {
    channel.onmessage = (e) => {
      const { msg, data } = e.data;
      this._dispatch(msg, data);
    };
  },

  subscribe(msg, handler) {
    // If called with one arg, subscribe to all messages
    if (typeof msg === 'function') {
      handler = msg;
      msg = '*';
    }

    if (!handlers.has(msg)) {
      handlers.set(msg, new Set());
    }
    handlers.get(msg).add(handler);

    // Return unsubscribe function for cleanup
    return () => handlers.get(msg)?.delete(handler);
  },

  publish(msg, data = null) {
    channel.postMessage({ msg, data });
    this._dispatch(msg, data);
  },

  _dispatch(msg, data) {
    // Notify topic-specific handlers
    handlers.get(msg)?.forEach((fn) => fn(msg, data));
    // Notify wildcard handlers
    if (msg !== '*') {
      handlers.get('*')?.forEach((fn) => fn(msg, data));
    }
  },
};

export default messages;
