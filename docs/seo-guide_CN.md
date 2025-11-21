# SEO 优化指南

本指南涵盖 Jekyll Apollo 主题的全面 SEO 优化，包括 Google 搜索、社交媒体分享和可发现性。

## 概述

Apollo 主题使用 `jekyll-seo-tag` 插件自动生成 SEO 友好的 meta 标签、用于社交分享的 Open Graph 标签和 Twitter Cards。

## 配置

### 1. `_config.yml` 中的基础 SEO 设置

```yaml
# 站点信息
title: 你的站点标题
description: 站点的简洁描述（150-160 字符）
url: "https://yourdomain.com"  # 重要：必须是你的实际域名
baseurl: ""  # 除非使用子目录，否则留空

# 作者信息
author:
  name: 你的名字
  email: your-email@example.com
  twitter: yourusername

# Twitter Card 设置
twitter:
  username: yourusername
  card: summary_large_image  # 使用大图卡片

# 社交资料
social:
  name: 你的名字
  links:
    - https://twitter.com/yourusername
    - https://github.com/yourusername
    - https://linkedin.com/in/yourusername

# 默认社交分享图片
defaults:
  - scope:
      path: ""
    values:
      image: /assets/default-share.png
```

### 2. 启用 SEO 插件

确保这些插件在你的 `_config.yml` 中：

```yaml
plugins:
  - jekyll-feed          # RSS 订阅
  - jekyll-seo-tag       # SEO meta 标签
  - jekyll-sitemap       # XML 站点地图
```

### 3. 单篇文章的 SEO 自定义

在文章的 front matter 中，你可以覆盖默认值：

```yaml
---
title: "你的文章标题"
description: "这篇文章的特定描述"
image: /assets/images/post-featured.jpg
tags: [SEO, Jekyll, 教程]
categories: [Web 开发]
---
```

## 社交媒体优化

### Open Graph 标签（Facebook、LinkedIn）

`jekyll-seo-tag` 插件自动生成：
- `og:title` - 文章/页面标题
- `og:description` - 文章摘要或站点描述
- `og:image` - 特色图片或默认图片
- `og:url` - 规范 URL
- `og:type` - 文章为 "article"，页面为 "website"
- `og:site_name` - 你的站点标题

### Twitter Cards

自动生成的标签：
- `twitter:card` - 设置为 `summary_large_image`
- `twitter:title` - 文章标题
- `twitter:description` - 文章描述
- `twitter:image` - 特色图片
- `twitter:creator` - 作者的 Twitter 账号
- `twitter:site` - 站点的 Twitter 账号

### 图片要求

**最佳尺寸：**
- **Twitter 大图卡片**：1200x628px（最小 300x157px）
- **Open Graph**：1200x630px
- **格式**：JPG 或 PNG
- **最大文件大小**：< 5MB

**默认图片：**
当文章未指定图片时，使用默认分享图片（`/assets/default-share.png`）。

## 搜索引擎优化

### 1. 站点地图

`jekyll-sitemap` 插件会在站点根目录自动生成 `sitemap.xml`。

**提交到 Google：**
1. 访问 [Google Search Console](https://search.google.com/search-console)
2. 添加你的资源（域名）
3. 提交站点地图：`https://yourdomain.com/sitemap.xml`

**从站点地图中排除页面：**
在 front matter 中添加：
```yaml
sitemap: false
```

### 2. Robots.txt

根目录包含 `robots.txt` 文件：

```
User-agent: *
Allow: /

Sitemap: https://yourdomain.com/sitemap.xml
```

**重要：** 在 `robots.txt` 中更新站点地图 URL 为你的实际域名。

### 3. 规范 URL

SEO 插件会自动添加规范 URL，防止重复内容问题。

### 4. 结构化数据（JSON-LD）

插件为以下内容生成 JSON-LD 结构化数据：
- 文章（博客文章）
- 网站
- 组织/个人（基于你的配置）

## GitHub Pages 专用

### 自定义域名设置

1. 在仓库根目录添加 `CNAME` 文件：
   ```
   yourdomain.com
   ```

2. 配置 DNS：
   - **A 记录** 指向 GitHub 的 IP：
     - 185.199.108.153
     - 185.199.109.153
     - 185.199.110.153
     - 185.199.111.153
   - **CNAME 记录**（用于 www）：`yourusername.github.io`

3. 在仓库设置中启用 HTTPS

### 提高仓库可发现性的设置

- 为仓库添加主题/标签
- 编写详细的 README
- 添加描述
- 添加网站 URL

## 测试与验证

### 1. Twitter Card 验证器
- URL：https://cards-dev.twitter.com/validator
- 测试你的 URL 以确保卡片正确显示

### 2. Facebook 分享调试器
- URL：https://developers.facebook.com/tools/debug/
- 清除缓存并预览文章显示效果

### 3. LinkedIn Post Inspector
- URL：https://www.linkedin.com/post-inspector/
- 验证 Open Graph 标签

### 4. Google 富媒体结果测试
- URL：https://search.google.com/test/rich-results
- 检查结构化数据

### 5. PageSpeed Insights
- URL：https://pagespeed.web.dev/
- 优化性能（影响 SEO 排名）

## 最佳实践

### 内容

1. **唯一标题**：每个页面都应有唯一、描述性的标题（50-60 字符）
2. **Meta 描述**：编写引人注目的描述（150-160 字符）
3. **标题层级**：使用正确的标题层级（H1 → H2 → H3）
4. **Alt 文本**：为所有图片添加描述性 alt 文本
5. **内部链接**：在相关文章之间建立链接
6. **新鲜内容**：定期更新

### 技术

1. **移动友好**：Apollo 默认响应式
2. **快速加载**：压缩图片，使用懒加载
3. **HTTPS**：始终使用 HTTPS（GitHub Pages 免费提供）
4. **简洁 URL**：使用描述性永久链接
5. **XML 站点地图**：自动生成，提交到搜索引擎

### 图片

1. **压缩**：使用 TinyPNG 等工具
2. **响应式**：必要时提供多种尺寸
3. **WebP 格式**：考虑使用现代格式以获得更好的压缩
4. **懒加载**：为首屏以下的图片实现懒加载

## 监控

### Google Search Console

跟踪：
- 索引状态
- 搜索查询
- 点击率
- 移动可用性
- Core Web Vitals

### Google Analytics

监控：
- 流量来源
- 用户行为
- 跳出率
- 热门内容

## 检查清单

- [ ] 在 `_config.yml` 中配置实际域名的 `url`
- [ ] 添加作者和社交信息
- [ ] 创建/自定义默认分享图片
- [ ] 用你的域名更新 `robots.txt`
- [ ] 向 Google Search Console 提交站点地图
- [ ] 验证 Twitter Cards
- [ ] 测试 Open Graph 标签
- [ ] 设置 Google Analytics
- [ ] 为图片添加 alt 文本
- [ ] 为关键页面编写唯一的 meta 描述
- [ ] 启用 HTTPS
- [ ] 测试移动响应性
- [ ] 检查页面加载速度

## 其他资源

- [Jekyll SEO Tag 文档](https://github.com/jekyll/jekyll-seo-tag)
- [Google 搜索中心](https://developers.google.com/search)
- [Open Graph 协议](https://ogp.me/)
- [Twitter Cards 指南](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
