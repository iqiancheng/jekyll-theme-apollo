# Image Optimization Guide

## Overview

This guide explains how to optimize images for your Jekyll blog while maintaining compatibility with GitHub Pages.

## Supported Formats

| Format | Compression | Browser Support | Recommended Use |
|--------|-------------|-----------------|-----------------|
| **AVIF** | Best (50% smaller than JPEG) | 95% (all modern browsers) | Primary choice |
| **WebP** | Good (25-35% smaller than JPEG) | 97% (universal) | Fallback for AVIF |
| **JPEG/PNG** | Standard | 100% | Final fallback |

## Quick Start

### 1. Install Dependencies (One-time)

```bash
brew install libvips imagemagick libheif
```

### 2. Convert Images

```bash
# Convert all images in assets/images/
./recipes/scripts/convert-images.sh assets/images

# Convert images in a specific directory
./recipes/scripts/convert-images.sh path/to/images
```

### 3. Use in Your Posts

#### Option A: HTML `<picture>` Tag (Recommended)

```html
<picture>
  <source srcset="/assets/images/photo.avif" type="image/avif">
  <source srcset="/assets/images/photo.webp" type="image/webp">
  <img src="/assets/images/photo.jpg" alt="Description" loading="lazy">
</picture>
```

#### Option B: Markdown (Simple)

```markdown
![Description](/assets/images/photo.jpg)
```

Then manually create `.webp` and `.avif` versions.

## Manual Conversion

### Using vips (Command Line)

```bash
# Convert to WebP
vips copy input.jpg output.webp[Q=80]

# Convert to AVIF
vips copy input.jpg output.avif[Q=75]

# Resize and convert
vips thumbnail input.jpg output.webp 1200 --size=down
```

### Using Online Tools

- **[Squoosh](https://squoosh.app/)** - Best for single images, supports AVIF/WebP
- **[TinyPNG](https://tinypng.com/)** - PNG/JPG compression
- **[Cloudinary](https://cloudinary.com/)** - Full-featured image CDN

## Best Practices

### File Organization

```
assets/images/
├── hero.jpg       # Original (fallback)
├── hero.webp      # WebP version
├── hero.avif      # AVIF version (smallest)
└── thumbnails/
    ├── thumb.jpg
    ├── thumb.webp
    └── thumb.avif
```

### Quality Settings

- **AVIF**: 70-75 quality (excellent compression)
- **WebP**: 75-85 quality (good balance)
- **JPEG**: 80-90 quality (fallback)

### Image Sizes

Recommended maximum widths:
- **Hero images**: 1920px
- **Content images**: 1200px
- **Thumbnails**: 400px

### Lazy Loading

Always add `loading="lazy"` to images below the fold:

```html
<img src="image.jpg" alt="Description" loading="lazy">
```

## GitHub Pages Compatibility

✅ **What Works:**
- Hosting WebP, AVIF, JPEG, PNG files
- Using `<picture>` tags in HTML
- Manual image optimization

❌ **What Doesn't Work:**
- Jekyll plugins like `jekyll-picture-tag` (not supported by GitHub Pages)
- Automatic image conversion during build

## Troubleshooting

### Images Not Converting

```bash
# Check if vips is installed
vips --version

# Reinstall if needed
brew reinstall libvips
```

### Browser Not Showing AVIF/WebP

- Check browser support at [caniuse.com](https://caniuse.com/)
- Ensure fallback `<img>` tag is present
- Verify file paths are correct

## File Size Comparison

Example for a 1MB original PNG:

```
Original PNG:    1000 KB  ████████████████████
JPEG (80%):       400 KB  ████████
WebP (80%):       280 KB  █████▌
AVIF (75%):       220 KB  ████▍
```

## Resources

- [libvips Documentation](https://www.libvips.org/)
- [WebP Browser Support](https://caniuse.com/webp)
- [AVIF Browser Support](https://caniuse.com/avif)
- [MDN: Responsive Images](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)
