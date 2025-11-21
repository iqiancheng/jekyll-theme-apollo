# Favicon and Icon Assets

This document explains the purpose of various favicon and icon files, and where they should be placed in the theme.

## Overview

Browsers and devices request different icon files for different purposes. This theme supports multiple icon formats to ensure compatibility across all platforms.

## Required Assets

### 1. `favicon.ico`

**Purpose:** The classic favicon format, automatically requested by browsers  
**Path:** `/assets/favicon.ico`  
**Size:** 16x16, 32x32, or multi-size ICO file  
**Usage:** Legacy browser support, browser tabs, bookmarks

**Why browsers request it:**
- Browsers automatically look for `/favicon.ico` at the site root
- Even without explicit `<link>` tags, browsers will try to fetch this file
- Provides fallback support for older browsers

### 2. `apple-touch-icon.png`

**Purpose:** Icon for iOS/iPadOS home screen and Safari bookmarks  
**Path:** `/assets/apple-touch-icon.png`  
**Size:** 180x180 pixels (PNG format)  
**Usage:** When users add your site to their iOS home screen

**Why iOS requests it:**
- iOS Safari automatically looks for this file when saving a web app
- Used for home screen shortcuts on iPhone and iPad
- Provides a high-quality icon for Apple devices

### 3. `apple-touch-icon-precomposed.png`

**Purpose:** Legacy iOS icon (pre-iOS 7)  
**Path:** `/assets/apple-touch-icon-precomposed.png`  
**Size:** 180x180 pixels (PNG format)  
**Usage:** Older iOS versions (before iOS 7)

**Why it exists:**
- Older iOS versions added gloss effects to icons by default
- The `-precomposed` suffix tells iOS not to add effects
- Modern iOS ignores this, but older devices still request it

## Recommended File Structure

```
jekyll-theme-apollo/
├── assets/
│   ├── favicon.ico                    # 16x16 or 32x32 ICO format
│   ├── favicon.png                    # Current theme default (any size)
│   ├── favicon-16x16.png              # Optional: 16x16 PNG
│   ├── favicon-32x32.png              # Optional: 32x32 PNG
│   ├── apple-touch-icon.png           # 180x180 for iOS
│   └── apple-touch-icon-precomposed.png  # 180x180 for legacy iOS
```

## How to Add These Files

### Option 1: Quick Setup (Minimal)

Create these three files to eliminate the errors:

1. **favicon.ico** - Convert your logo to ICO format (16x16 or 32x32)
2. **apple-touch-icon.png** - 180x180 PNG version of your logo
3. **apple-touch-icon-precomposed.png** - Copy of apple-touch-icon.png

Place all files in the `assets/` directory.

### Option 2: Complete Setup (Recommended)

For best cross-platform support, add these `<link>` tags to `_includes/head.html`:

```html
<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="{{ '/assets/favicon.ico' | relative_url }}">
<link rel="icon" type="image/png" sizes="32x32" href="{{ '/assets/favicon-32x32.png' | relative_url }}">
<link rel="icon" type="image/png" sizes="16x16" href="{{ '/assets/favicon-16x16.png' | relative_url }}">

<!-- Apple Touch Icons -->
<link rel="apple-touch-icon" sizes="180x180" href="{{ '/assets/apple-touch-icon.png' | relative_url }}">
```

## Current Configuration

The theme currently uses:

```yaml
# _config.yml
favicon: /assets/favicon.png
```

Referenced in `_includes/head.html`:

```html
<link rel="icon" href="{{ site.favicon | relative_url }}">
```

This works, but browsers will still automatically request the missing files, causing 404 errors in the logs.

## Generating Icons

You can use online tools to generate all required formats from a single image:

- [RealFaviconGenerator](https://realfavicongenerator.net/) - Comprehensive favicon generator
- [Favicon.io](https://favicon.io/) - Simple favicon generator
- ImageMagick (command line):
  ```bash
  # Convert PNG to ICO
  convert favicon.png -define icon:auto-resize=16,32,48 favicon.ico
  
  # Resize for Apple Touch Icon
  convert favicon.png -resize 180x180 apple-touch-icon.png
  ```

## Why These Errors Appear

Even without explicit `<link>` tags in your HTML, browsers and devices will automatically request these files:

- **Browsers** request `/favicon.ico` by convention
- **iOS Safari** requests `/apple-touch-icon.png` when bookmarking
- **Legacy iOS** requests `/apple-touch-icon-precomposed.png`

These are not errors in your code—they're standard browser behavior. Adding the files will eliminate the 404 errors in your server logs.

## Summary

| File | Size | Purpose | Priority |
|------|------|---------|----------|
| `favicon.ico` | 16x16 or 32x32 | Browser tabs, bookmarks | High |
| `apple-touch-icon.png` | 180x180 | iOS home screen | High |
| `apple-touch-icon-precomposed.png` | 180x180 | Legacy iOS | Medium |
| `favicon-16x16.png` | 16x16 | Modern browsers (small) | Optional |
| `favicon-32x32.png` | 32x32 | Modern browsers (standard) | Optional |

**Minimum setup:** Add the first three files to eliminate 404 errors.  
**Recommended setup:** Add all files and update `_includes/head.html` for complete cross-platform support.
