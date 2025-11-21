# 创建自定义页面

本指南将教你如何创建自定义页面，如关于页面、标签页、分类页等。

## 基础页面结构

自定义页面应该放在 Jekyll 站点的**根目录**下，与 `_posts/`、`_includes/` 等文件夹平级。

### 示例：关于页面

在根目录创建 `about.md`：

```markdown
---
layout: default
title: About
permalink: /about/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">关于我</h1>
        
        <div class="post-content">
            <p>你的内容...</p>
        </div>
    </article>
</div>
```

**关键点：**
- `layout: default` - 使用默认主题布局
- `permalink: /about/` - 设置 URL 路径
- HTML 结构与文章样式保持一致

## 常见博客页面

### 1. 标签页面

在根目录创建 `tags.html`：

```html
---
layout: default
title: Tags
permalink: /tags/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">标签</h1>
        
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

### 2. 分类页面

在根目录创建 `categories.html`：

```html
---
layout: default
title: Categories
permalink: /categories/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">分类</h1>
        
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

### 3. 项目页面

在根目录创建 `projects.md`：

```markdown
---
layout: default
title: Projects
permalink: /projects/
---

<div class="post">
    <article class="post-block">
        <h1 class="post-title">我的项目</h1>
        
        <div class="post-content">
            <h2>开源项目</h2>
            <ul>
                <li><a href="https://github.com/user/project1">项目 1</a> - 描述</li>
                <li><a href="https://github.com/user/project2">项目 2</a> - 描述</li>
            </ul>
            
            <h2>个人项目</h2>
            <ul>
                <li><strong>项目 3</strong> - 描述</li>
            </ul>
        </div>
    </article>
</div>
```

## 将页面添加到导航栏

创建页面后，在 `_config.yml` 中添加到导航菜单：

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

## 文件结构

```
jekyll-theme-apollo/
├── _posts/              # 博客文章
├── _includes/           # 可复用组件
├── _layouts/            # 页面布局
├── about.md             # 关于页面
├── tags.html            # 标签页面
├── categories.html      # 分类页面
├── projects.md          # 项目页面
├── archive.html         # 归档页面（已存在）
└── _config.yml          # 站点配置
```

## 小贴士

1. **Markdown 内容使用 `.md`**，包含 Liquid 逻辑的页面使用 `.html`
2. **保持 HTML 结构一致**，与现有页面保持统一样式
3. **本地测试**后再部署：`bundle exec jekyll serve`
4. **Permalinks** 应以 `/` 结尾，保持 URL 简洁
