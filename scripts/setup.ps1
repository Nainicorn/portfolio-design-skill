Write-Host ""
Write-Host "🛠  vanilla-scaffold (if-it-ain't-broke) — setup" -ForegroundColor Cyan
Write-Host "──────────────────────────────────────────────────"

try {
  $nodeVersion = (node -v) -replace 'v','' -split '\.' | Select-Object -First 1
  if ([int]$nodeVersion -lt 18) {
    Write-Host "⚠️  Node.js v$nodeVersion detected. v18+ recommended." -ForegroundColor Yellow
  }
} catch {
  Write-Host "❌  Node.js not found. Install from https://nodejs.org" -ForegroundColor Red
  exit 1
}

$lspInstalled = Get-Command vscode-css-language-server -ErrorAction SilentlyContinue
if (-not $lspInstalled) {
  Write-Host "→  Installing vscode-langservers-extracted..."
  npm install -g vscode-langservers-extracted
  Write-Host "✓  LSP installed" -ForegroundColor Green
} else {
  Write-Host "✓  CSS LSP already installed — skipping" -ForegroundColor Green
}

Write-Host ""
Write-Host "✅  Setup complete." -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Open a project folder"
Write-Host "  2. Run: /vanilla-scaffold"
Write-Host "  3. Answer 3 questions — scaffold generates from your answers"
Write-Host ""
