#!/bin/bash
set -e

echo ""
echo "🛠  vanilla-scaffold (if-it-ain't-broke) — setup"
echo "──────────────────────────────────────────────────"

NODE_VERSION=$(node -v 2>/dev/null | sed 's/v//' | cut -d. -f1)
if [ -z "$NODE_VERSION" ]; then
  echo "❌  Node.js not found. Install from https://nodejs.org and re-run setup."
  exit 1
fi
if [ "$NODE_VERSION" -lt 18 ]; then
  echo "⚠️  Node.js v$NODE_VERSION detected. v18+ recommended for Vite and ESM support."
fi

if ! command -v vscode-css-language-server &> /dev/null; then
  echo "→  Installing vscode-langservers-extracted (CSS + HTML LSP)..."
  npm install -g vscode-langservers-extracted
  echo "✓  LSP installed"
else
  echo "✓  CSS LSP already installed — skipping"
fi

echo ""
echo "✅  Setup complete."
echo ""
echo "Next steps:"
echo "  1. Open a project folder"
echo "  2. Run: /vanilla-scaffold"
echo "  3. Answer 3 questions — scaffold generates from your answers"
echo ""
