# SEO Optimization Guide

This guide covers comprehensive SEO optimization for your Jekyll Apollo theme, including Google Search, social media sharing, and discoverability.

## Overview

The Apollo theme uses the `jekyll-seo-tag` plugin to automatically generate SEO-friendly meta tags, Open Graph tags for social sharing, and Twitter Cards.

## Configuration

### 1. Basic SEO Settings in `_config.yml`

```yaml
# Site Information
title: Your Site Title
description: A concise description of your site (150-160 characters)
url: "https://yourdomain.com"  # IMPORTANT: Must be your actual domain
baseurl: ""  # Leave empty unless using a subdirectory

# Author Information
author:
  name: Your Name
  email: your-email@example.com
  twitter: yourusername

# Twitter Card Settings
twitter:
  username: yourusername
  card: summary_large_image  # Use large image cards

# Social Profiles
social:
  name: Your Name
  links:
    - https://twitter.com/yourusername
    - https://github.com/yourusername
    - https://linkedin.com/in/yourusername

# Default Social Share Image
defaults:
  - scope:
      path: ""
    values:
      image: /assets/default-share.png
```

### 2. Enable SEO Plugins

Ensure these plugins are in your `_config.yml`:

```yaml
plugins:
  - jekyll-feed          # RSS feed
  - jekyll-seo-tag       # SEO meta tags
  - jekyll-sitemap       # XML sitemap
```

### 3. Per-Post SEO Customization

In your post's front matter, you can override defaults:

```yaml
---
title: "Your Post Title"
description: "A specific description for this post"
image: /assets/images/post-featured.jpg
tags: [SEO, Jekyll, Tutorial]
categories: [Web Development]
---
```

## Social Media Optimization

### Open Graph Tags (Facebook, LinkedIn)

The `jekyll-seo-tag` plugin automatically generates:
- `og:title` - Post/page title
- `og:description` - Post excerpt or site description
- `og:image` - Featured image or default
- `og:url` - Canonical URL
- `og:type` - "article" for posts, "website" for pages
- `og:site_name` - Your site title

### Twitter Cards

Automatically generated tags:
- `twitter:card` - Set to `summary_large_image`
- `twitter:title` - Post title
- `twitter:description` - Post description
- `twitter:image` - Featured image
- `twitter:creator` - Author's Twitter handle
- `twitter:site` - Site's Twitter handle

### Image Requirements

**Optimal sizes:**
- **Twitter Large Image Card**: 1200x628px (minimum 300x157px)
- **Open Graph**: 1200x630px
- **Format**: JPG or PNG
- **Max file size**: < 5MB

**Default Image:**
A default share image (`/assets/default-share.png`) is used when a post doesn't specify one.

## Search Engine Optimization

### 1. Sitemap

The `jekyll-sitemap` plugin automatically generates `sitemap.xml` at your site root.

**Submit to Google:**
1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add your property (domain)
3. Submit sitemap: `https://yourdomain.com/sitemap.xml`

**Exclude pages from sitemap:**
Add to front matter:
```yaml
sitemap: false
```

### 2. Robots.txt

A `robots.txt` file is included at the root:

```
User-agent: *
Allow: /

Sitemap: https://yourdomain.com/sitemap.xml
```

**Important:** Update the sitemap URL in `robots.txt` with your actual domain.

### 3. Canonical URLs

The SEO plugin automatically adds canonical URLs to prevent duplicate content issues.

### 4. Structured Data (JSON-LD)

The plugin generates JSON-LD structured data for:
- Articles (blog posts)
- WebSite
- Organization/Person (based on your config)

## GitHub Pages Specific

### Custom Domain Setup

1. Add `CNAME` file to your repository root:
   ```
   yourdomain.com
   ```

2. Configure DNS:
   - **A Records** pointing to GitHub's IPs:
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - **CNAME Record** (for www): `yourusername.github.io`

3. Enable HTTPS in repository settings

### Repository Settings for Discoverability

- Add topics/tags to your repository
- Write a comprehensive README
- Include a description
- Add a website URL

## Testing & Validation

### 1. Twitter Card Validator
- URL: https://cards-dev.twitter.com/validator
- Test your URLs to ensure cards display correctly

### 2. Facebook Sharing Debugger
- URL: https://developers.facebook.com/tools/debug/
- Clear cache and preview how posts appear

### 3. LinkedIn Post Inspector
- URL: https://www.linkedin.com/post-inspector/
- Validate Open Graph tags

### 4. Google Rich Results Test
- URL: https://search.google.com/test/rich-results
- Check structured data

### 5. PageSpeed Insights
- URL: https://pagespeed.web.dev/
- Optimize performance (affects SEO ranking)

## Best Practices

### Content

1. **Unique Titles**: Each page should have a unique, descriptive title (50-60 characters)
2. **Meta Descriptions**: Write compelling descriptions (150-160 characters)
3. **Headings**: Use proper heading hierarchy (H1 → H2 → H3)
4. **Alt Text**: Add descriptive alt text to all images
5. **Internal Links**: Link between related posts
6. **Fresh Content**: Update regularly

### Technical

1. **Mobile-Friendly**: Apollo is responsive by default
2. **Fast Loading**: Minimize images, use lazy loading
3. **HTTPS**: Always use HTTPS (free with GitHub Pages)
4. **Clean URLs**: Use descriptive permalinks
5. **XML Sitemap**: Auto-generated, submit to search engines

### Images

1. **Compress**: Use tools like TinyPNG
2. **Responsive**: Provide multiple sizes if needed
3. **WebP Format**: Consider modern formats for better compression
4. **Lazy Loading**: Implement for below-fold images

## Monitoring

### Google Search Console

Track:
- Indexing status
- Search queries
- Click-through rates
- Mobile usability
- Core Web Vitals

### Google Analytics

Monitor:
- Traffic sources
- User behavior
- Bounce rates
- Popular content

## Checklist

- [ ] Configure `url` in `_config.yml` with your actual domain
- [ ] Add author and social information
- [ ] Create/customize default share image
- [ ] Update `robots.txt` with your domain
- [ ] Submit sitemap to Google Search Console
- [ ] Verify Twitter Cards
- [ ] Test Open Graph tags
- [ ] Set up Google Analytics
- [ ] Add alt text to images
- [ ] Write unique meta descriptions for key pages
- [ ] Enable HTTPS
- [ ] Test mobile responsiveness
- [ ] Check page load speed

## Additional Resources

- [Jekyll SEO Tag Documentation](https://github.com/jekyll/jekyll-seo-tag)
- [Google Search Central](https://developers.google.com/search)
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards Guide](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
