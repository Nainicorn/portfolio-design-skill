#!/usr/bin/env python3
"""
scaffold.py — generates the vanilla-scaffold project structure.

Usage:
  python scaffold.py <app-name> [--force]

Creates a directory named <app-name> in the current working directory
with the full layout-first component architecture.

Exit codes:
  0 — success
  1 — target directory exists (pass --force to overwrite)
  2 — missing app name argument
"""

import os
import sys
import shutil
import json

# ---------------------------------------------------------------------------
# CLI argument parsing
# ---------------------------------------------------------------------------

def parse_args():
    args = sys.argv[1:]
    force = "--force" in args
    args = [a for a in args if a != "--force"]

    if not args:
        print("❌  Missing app name.")
        print("Usage: python scaffold.py <app-name> [--force]")
        print("Example: python scaffold.py my-cool-app")
        sys.exit(2)

    return args[0], force

# ---------------------------------------------------------------------------
# Template content — loaded from adjacent templates/ directory when available,
# otherwise falls back to inline defaults so the script is self-contained.
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(SCRIPT_DIR, "..", "templates")


def read_template(filename):
    """Read a template file from the templates directory."""
    path = os.path.join(TEMPLATES_DIR, filename)
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    return None


def substitute(content, app_name):
    """Replace {{app-name}} placeholders."""
    return content.replace("{{app-name}}", app_name)


# ---------------------------------------------------------------------------
# File tree definition
# ---------------------------------------------------------------------------

def get_file_tree(app_name):
    """
    Returns a list of (relative_path, content) tuples for every file
    the scaffold generates. Template files are loaded from templates/
    with {{app-name}} substitution applied.
    """
    files = []

    # --- Root files ---
    index_html = read_template("index.html")
    if index_html:
        files.append(("index.html", substitute(index_html, app_name)))

    vite_config = read_template("vite.config.js")
    if vite_config:
        files.append(("vite.config.js", vite_config))

    pkg = read_template("package.json")
    if pkg:
        files.append(("package.json", substitute(pkg, app_name)))

    env_example = read_template(".env.example")
    if env_example:
        files.append((".env.example", env_example))

    # --- src/styles/base.css ---
    base_css = read_template("base.css")
    if base_css:
        files.append(("src/styles/base.css", base_css))

    # --- src/app.js ---
    app_js = read_template("app.js")
    if app_js:
        files.append(("src/app.js", substitute(app_js, app_name)))

    # --- Layout components ---
    layout_components = ["Layout", "Header", "Body", "Footer"]
    for comp in layout_components:
        for ext in ["hbs", "js", "css"]:
            filename = f"{comp}.{ext}"
            content = read_template(filename)
            if content:
                files.append((
                    f"src/components/{comp}/{filename}",
                    substitute(content, app_name)
                ))

    # --- Services ---
    for service in ["apiService.js", "routeService.js"]:
        content = read_template(f"services/{service}")
        if content:
            files.append((f"src/services/{service}", content))

    # --- Placeholder for new components ---
    files.append((
        "src/components/.gitkeep",
        ""
    ))

    # --- src/lib placeholder ---
    files.append((
        "src/lib/.gitkeep",
        ""
    ))

    return files

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    app_name, force = parse_args()
    target = os.path.join(os.getcwd(), app_name)

    # Guard: directory exists
    if os.path.exists(target) and not force:
        print(f"❌  Directory '{app_name}' already exists.")
        print(f"    To overwrite: python scaffold.py {app_name} --force")
        print(f"    Or pick a different name.")
        sys.exit(1)

    if os.path.exists(target) and force:
        print(f"⚠️  --force flag set. Removing existing '{app_name}' directory...")
        shutil.rmtree(target)

    # Generate files
    file_tree = get_file_tree(app_name)
    file_count = 0

    for rel_path, content in file_tree:
        abs_path = os.path.join(target, rel_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        with open(abs_path, "w") as f:
            f.write(content)
        file_count += 1
        print(f"  ✓ Created {rel_path}")

    # Summary
    print("")
    print(f"✅ Scaffold complete — {file_count} files created")
    print("")
    print("To get started:")
    print(f"  cd {app_name}")
    print("  npm install")
    print("  npm run dev")
    print("")
    print("Your app opens at http://localhost:5173")
    print("Add new components under src/components/ to build your first page.")
    print("")


if __name__ == "__main__":
    main()
