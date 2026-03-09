#!/usr/bin/env python3
"""
Deployment Configuration Generator
Creates platform-specific config files for deployment
"""

import sys
import json
from pathlib import Path

VERCEL_CONFIG = """{
  "version": 2,
  "builds": [
    {
      "src": "index.html",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/$1"
    }
  ]
}
"""

AMPLIFY_CONFIG = """version: 1
frontend:
  phases:
    build:
      commands:
        - echo "No build step needed for static HTML"
  artifacts:
    baseDirectory: /
    files:
      - '**/*'
  cache:
    paths: []
"""

GITHUB_ACTIONS_CONFIG = """name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Pages
        uses: actions/configure-pages@v3
      
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: '.'
      
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
"""

README_TEMPLATE = """# {project_name}

Built by {author_name}.

## Deployment

Deployed on {platform}.

### Local Development

1. Clone this repository
2. Open `index.html` in your browser (or run your framework's dev server)
3. Make changes and see them live

### Making Changes

1. Edit the HTML, CSS, or JS files
2. Commit and push to GitHub
3. {deploy_note}

## Customization

### Colors

Edit your CSS variables file to change the color scheme:

```css
:root {{
  --color-primary: #VALUE;
  --color-accent: #VALUE;
  /* ... more colors */
}}
```

### Content

Update your HTML/components with your content.

### Styling

Modify your theme-specific styles to customize the design.

## License

© {year} {author_name}. All rights reserved.
"""

def generate_configs(platform, output_dir='.', project_name='Portfolio', author_name='Your Name'):
    """Generate deployment configuration files"""
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    from datetime import datetime
    year = datetime.now().year
    
    files_created = []
    
    if platform.lower() == 'vercel':
        vercel_file = output_path / 'vercel.json'
        with open(vercel_file, 'w') as f:
            f.write(VERCEL_CONFIG)
        files_created.append(str(vercel_file))
        
        deploy_note = "Changes auto-deploy on push to main branch"
        
    elif platform.lower() == 'amplify':
        amplify_file = output_path / 'amplify.yml'
        with open(amplify_file, 'w') as f:
            f.write(AMPLIFY_CONFIG)
        files_created.append(str(amplify_file))
        
        deploy_note = "Changes auto-deploy via AWS Amplify CI/CD"
        
    elif platform.lower() == 'github' or platform.lower() == 'github-pages':
        workflows_dir = output_path / '.github' / 'workflows'
        workflows_dir.mkdir(parents=True, exist_ok=True)
        
        actions_file = workflows_dir / 'deploy.yml'
        with open(actions_file, 'w') as f:
            f.write(GITHUB_ACTIONS_CONFIG)
        files_created.append(str(actions_file))
        
        deploy_note = "GitHub Actions will automatically deploy to GitHub Pages"
        
    else:
        print(f"Error: Unknown platform '{platform}'")
        print("Supported platforms: vercel, amplify, github-pages")
        return False
    
    # Create README
    readme_content = README_TEMPLATE.format(
        project_name=project_name,
        author_name=author_name,
        platform=platform.title(),
        deploy_note=deploy_note,
        year=year
    )
    
    readme_file = output_path / 'README.md'
    with open(readme_file, 'w') as f:
        f.write(readme_content)
    files_created.append(str(readme_file))
    
    # Print results
    print("=" * 60)
    print(f"✅ Deployment Configuration Generated for {platform.title()}")
    print("=" * 60)
    print("\nFiles created:")
    for file in files_created:
        print(f"  ✓ {file}")
    
    print("\n" + "=" * 60)
    print(f"Next steps for {platform.title()} deployment:")
    print("=" * 60)
    
    if platform.lower() == 'vercel':
        print("""
1. Install Vercel CLI: npm install -g vercel
2. Run: vercel
3. Follow the prompts
4. Your site will be live in ~30 seconds!

OR use Vercel dashboard:
1. Go to vercel.com
2. Import your GitHub repository
3. Deploy!
""")
    
    elif platform.lower() == 'amplify':
        print("""
1. Go to AWS Amplify Console
2. Connect your GitHub repository
3. AWS will detect amplify.yml automatically
4. Deploy!
""")
    
    elif platform.lower() in ['github', 'github-pages']:
        print("""
1. Push these files to GitHub:
   git add .
   git commit -m "Add deployment config"
   git push

2. Go to repo Settings > Pages
3. Enable GitHub Pages (source: GitHub Actions)
4. Wait for Actions workflow to complete
5. Your site will be live at username.github.io/repo-name
""")
    
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_deployment_config.py <platform> [output_dir] [project_name] [author_name]")
        print("\nPlatforms: vercel, amplify, github-pages")
        print("\nExample:")
        print("  python generate_deployment_config.py vercel . 'My Portfolio' 'John Doe'")
        sys.exit(1)
    
    platform = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else '.'
    project_name = sys.argv[3] if len(sys.argv) > 3 else 'My Project'
    author_name = sys.argv[4] if len(sys.argv) > 4 else 'Your Name'
    
    success = generate_configs(platform, output_dir, project_name, author_name)
    sys.exit(0 if success else 1)