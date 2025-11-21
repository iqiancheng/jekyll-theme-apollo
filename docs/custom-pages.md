# Creating Custom Pages

This guide shows you how to create custom pages like About, Tags, Categories, etc.

## Basic Page Structure

Custom pages should be placed in the **root directory** of your Jekyll site, alongside `_posts/`, `_includes/`, etc.

### Example: About Page

Create `about.md` in the root directory:

```markdown
---
layout: default
title: About
permalink: /about/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">About Me</h1>
        
        <div class="post-content">
            <p>Your content here...</p>
        </div>
    </article>
</div>
```

**Key Points:**
- `layout: default` - Uses the default theme layout
- `permalink: /about/` - Sets the URL path
- HTML structure matches the post style for consistency

## Common Blog Pages

### 1. Tags Page

Create `tags.html` in the root directory:

```html
---
layout: default
title: Tags
permalink: /tags/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">Tags</h1>
        
        <div class="post-content">
            {% assign tags = site.tags | sort %}
            {% for tag in tags %}
                <h2 id="{{ tag[0] | slugify }}">{{ tag[0] }}</h2>
                <ul>
                {% for post in tag[1] %}
                    <li>
                        <a href="{{ post.url }}">{{ post.title }}</a>
                        <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
                    </li>
                {% endfor %}
                </ul>
            {% endfor %}
        </div>
    </article>
</div>
```

### 2. Categories Page

Create `categories.html` in the root directory:

```html
---
layout: default
title: Categories
permalink: /categories/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">Categories</h1>
        
        <div class="post-content">
            {% assign categories = site.categories | sort %}
            {% for category in categories %}
                <h2 id="{{ category[0] | slugify }}">{{ category[0] }}</h2>
                <ul>
                {% for post in category[1] %}
                    <li>
                        <a href="{{ post.url }}">{{ post.title }}</a>
                        <span class="post-date">{{ post.date | date: "%b %d, %Y" }}</span>
                    </li>
                {% endfor %}
                </ul>
            {% endfor %}
        </div>
    </article>
</div>
```

### 3. Projects Page

Create `projects.md` in the root directory:

```markdown
---
layout: default
title: Projects
permalink: /projects/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">My Projects</h1>
        
        <div class="post-content">
            <h2>Open Source</h2>
            <ul>
                <li><a href="https://github.com/user/project1">Project 1</a> - Description</li>
                <li><a href="https://github.com/user/project2">Project 2</a> - Description</li>
            </ul>
            
            <h2>Personal</h2>
            <ul>
                <li><strong>Project 3</strong> - Description</li>
            </ul>
        </div>
    </article>
</div>
```

## Adding Pages to Navigation

After creating a page, add it to your navigation menu in `_config.yml`:

```yaml
menu:
  - name: Blog
    link: /
  - name: Archive
    link: /archive/
  - name: Tags
    link: /tags/
  - name: Categories
    link: /categories/
  - name: Projects
    link: /projects/
  - name: About
    link: /about/
```

## File Structure

```
jekyll-theme-apollo/
├── _posts/              # Blog posts
├── _includes/           # Reusable components
├── _layouts/            # Page layouts
├── about.md             # About page
├── tags.html            # Tags page
├── categories.html      # Categories page
├── projects.md          # Projects page
├── archive.html         # Archive page (already exists)
└── _config.yml          # Site configuration
```

## Tips

1. **Use `.md` for Markdown content** and `.html` for pages with Liquid logic
2. **Keep the HTML structure consistent** with existing pages for uniform styling
3. **Test locally** before deploying: `bundle exec jekyll serve`
4. **Permalinks** should end with `/` for clean URLs
