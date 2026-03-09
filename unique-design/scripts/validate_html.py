#!/usr/bin/env python3
"""
HTML Semantic Structure Validator
Checks for proper HTML5 semantics and common issues
"""

import re
import sys
from pathlib import Path

def validate_html(html_path):
    """Validate HTML file for semantic structure"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    warnings = []
    
    # Check for DOCTYPE
    if not re.search(r'<!DOCTYPE html>', content, re.IGNORECASE):
        issues.append("Missing <!DOCTYPE html>")
    
    # Check for lang attribute
    if not re.search(r'<html[^>]*lang=', content):
        issues.append("Missing lang attribute on <html> tag")
    
    # Check for charset
    if not re.search(r'<meta[^>]*charset=', content):
        issues.append("Missing charset meta tag")
    
    # Check for viewport
    if not re.search(r'<meta[^>]*viewport', content):
        issues.append("Missing viewport meta tag (important for mobile)")
    
    # Check for title
    if not re.search(r'<title>', content):
        issues.append("Missing <title> tag")
    
    # Check for semantic elements
    if '<div' in content and not any(tag in content for tag in ['<header', '<nav', '<main', '<section', '<article', '<aside', '<footer']):
        warnings.append("Using <div> but no semantic HTML5 elements (header, nav, main, section, etc.)")
    
    # Check for heading hierarchy
    h1_count = len(re.findall(r'<h1[^>]*>', content))
    if h1_count == 0:
        issues.append("No <h1> heading found (important for SEO and accessibility)")
    elif h1_count > 1:
        warnings.append(f"Multiple <h1> headings found ({h1_count}). Best practice is one per page.")
    
    # Check for alt text on images
    img_tags = re.findall(r'<img[^>]*>', content)
    for img in img_tags:
        if 'alt=' not in img:
            warnings.append(f"Image missing alt attribute: {img[:50]}...")
    
    # Check for aria-label or alt on buttons/links with no text
    button_pattern = r'<button[^>]*>(\s*)<\/button>'
    if re.search(button_pattern, content):
        warnings.append("Found button with no text content. Ensure it has aria-label.")
    
    # Check for inline styles (not critical but not best practice)
    if ' style=' in content:
        warnings.append("Found inline styles. Consider moving to CSS file.")
    
    # Results
    print("=" * 60)
    print(f"HTML Validation Results: {html_path}")
    print("=" * 60)
    
    if not issues and not warnings:
        print("✅ All checks passed! HTML looks good.")
        return True
    
    if issues:
        print("\n❌ ISSUES (must fix):")
        for issue in issues:
            print(f"  - {issue}")
    
    if warnings:
        print("\n⚠️  WARNINGS (recommended to fix):")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("\n" + "=" * 60)
    return len(issues) == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_html.py <path/to/index.html>")
        sys.exit(1)
    
    html_file = Path(sys.argv[1])
    
    if not html_file.exists():
        print(f"Error: File not found: {html_file}")
        sys.exit(1)
    
    success = validate_html(html_file)
    sys.exit(0 if success else 1)