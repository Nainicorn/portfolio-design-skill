#!/usr/bin/env python3
"""
Basic Accessibility Checker
Validates common WCAG AA compliance issues
"""

import re
import sys
from pathlib import Path

def rgb_to_relative_luminance(r, g, b):
    """Convert RGB to relative luminance for contrast calculation"""
    def adjust(channel):
        c = channel / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def hex_to_rgb(hex_color):
    """Convert hex color to RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def calculate_contrast_ratio(color1, color2):
    """Calculate WCAG contrast ratio between two hex colors"""
    try:
        rgb1 = hex_to_rgb(color1)
        rgb2 = hex_to_rgb(color2)
        
        l1 = rgb_to_relative_luminance(*rgb1)
        l2 = rgb_to_relative_luminance(*rgb2)
        
        lighter = max(l1, l2)
        darker = min(l1, l2)
        
        return (lighter + 0.05) / (darker + 0.05)
    except:
        return None

def check_accessibility(html_path, css_path=None):
    """Check for common accessibility issues"""
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    css_content = ""
    if css_path and Path(css_path).exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
    
    issues = []
    warnings = []
    
    # 1. Check for alt text on images
    img_tags = re.findall(r'<img[^>]*>', html_content)
    missing_alt = 0
    for img in img_tags:
        if 'alt=' not in img:
            missing_alt += 1
    
    if missing_alt > 0:
        issues.append(f"{missing_alt} image(s) missing alt attributes")
    
    # 2. Check for form labels
    input_tags = re.findall(r'<input[^>]*>', html_content)
    for input_tag in input_tags:
        if 'type="text"' in input_tag or 'type="email"' in input_tag:
            input_id = re.search(r'id="([^"]*)"', input_tag)
            if input_id:
                label_pattern = f'<label[^>]*for="{input_id.group(1)}"'
                if not re.search(label_pattern, html_content):
                    warnings.append(f"Input field possibly missing associated label: {input_tag[:50]}...")
    
    # 3. Check heading hierarchy
    headings = re.findall(r'<h([1-6])', html_content)
    if headings:
        prev_level = 0
        for heading in headings:
            level = int(heading)
            if prev_level > 0 and level > prev_level + 1:
                warnings.append(f"Heading hierarchy skips level (h{prev_level} to h{level})")
            prev_level = level
    
    # 4. Check for empty links or buttons
    if re.search(r'<a[^>]*>\s*</a>', html_content):
        issues.append("Found empty link(s). All links need text or aria-label")
    
    if re.search(r'<button[^>]*>\s*</button>', html_content):
        issues.append("Found empty button(s). All buttons need text or aria-label")
    
    # 5. Basic color contrast check (from CSS variables if available)
    if css_content:
        # Extract color variables
        bg_color = re.search(r'--color-bg:\s*(#[0-9A-Fa-f]{6})', css_content)
        text_color = re.search(r'--color-text:\s*(#[0-9A-Fa-f]{6})', css_content)
        
        if bg_color and text_color:
            ratio = calculate_contrast_ratio(bg_color.group(1), text_color.group(1))
            if ratio:
                if ratio < 4.5:
                    issues.append(f"Text contrast ratio {ratio:.2f}:1 fails WCAG AA (needs 4.5:1 minimum)")
                elif ratio >= 4.5 and ratio < 7:
                    print(f"✓ Text contrast ratio: {ratio:.2f}:1 (passes AA, below AAA)")
                else:
                    print(f"✓ Text contrast ratio: {ratio:.2f}:1 (passes AAA)")
    
    # 6. Check for tab index abuse
    if re.search(r'tabindex="[^0-]', html_content):
        warnings.append("Found positive tabindex values. This can break keyboard navigation.")
    
    # 7. Check for language attribute
    if not re.search(r'<html[^>]*lang=', html_content):
        issues.append("Missing lang attribute on <html> tag (required for screen readers)")
    
    # Results
    print("=" * 60)
    print(f"Accessibility Check Results: {html_path}")
    print("=" * 60)
    
    if not issues and not warnings:
        print("✅ No major accessibility issues found!")
        print("\nNote: This is a basic check. For comprehensive testing, use:")
        print("  - axe DevTools browser extension")
        print("  - WAVE accessibility tool")
        print("  - Lighthouse in Chrome DevTools")
        return True
    
    if issues:
        print("\n❌ ACCESSIBILITY ISSUES (must fix for WCAG AA):")
        for issue in issues:
            print(f"  - {issue}")
    
    if warnings:
        print("\n⚠️  WARNINGS (recommended to fix):")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("\n" + "=" * 60)
    print("For full accessibility audit, use browser tools:")
    print("  • Chrome: Lighthouse (DevTools > Lighthouse)")
    print("  • Firefox: Accessibility Inspector")
    print("  • axe DevTools extension")
    print("=" * 60)
    
    return len(issues) == 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_accessibility.py <path/to/index.html> [path/to/variables.css]")
        sys.exit(1)
    
    html_file = Path(sys.argv[1])
    css_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    
    if not html_file.exists():
        print(f"Error: File not found: {html_file}")
        sys.exit(1)
    
    success = check_accessibility(html_file, css_file)
    sys.exit(0 if success else 1)