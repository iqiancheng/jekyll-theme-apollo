# Jekyll Theme Apollo

[Hexo Theme Apollo](https://github.com/pinggod/hexo-theme-apollo) 的 Jekyll 移植版本。极简、干净、响应式。

![hexo-theme-apollo](https://cloud.githubusercontent.com/assets/9530963/13026956/08e76eca-d277-11e5-8bfc-2e80cea20a0d.png)

## 特性

- **极简设计**: 专注于内容，无干扰的阅读体验。
- **响应式**: 完美适配桌面和移动端。
- **Google Analytics**: 内置支持。
- **Disqus 评论**: 轻松集成。
- **代码高亮**: 简洁的代码块样式。
- **MathJax**: 支持数学公式渲染。

## 安装

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/iqiancheng/jekyll-theme-apollo.git
    cd jekyll-theme-apollo
    ```

2.  **安装依赖**:
    ```bash
    bundle install
    ```

3.  **启动服务**:
    ```bash
    bundle exec jekyll serve
    ```

4.  浏览器访问 [http://localhost:4000](http://localhost:4000)。

## 配置

主要配置在 `_config.yml` 文件中。

```yaml
title: Apollo
description: A Blog Powered By Jekyll
url: "http://example.com"
baseurl: ""

# 资源
logo: /assets/favicon.png
favicon: /assets/favicon.png

# 评论
disqus: your_disqus_shortname

# 统计
google_analytics: UA-XXXXXXXX-X
```

更多详情请查看 [配置文档](docs/configuration_CN.md)。

## 写文章

在 `_posts` 目录下创建 Markdown 文件，文件名格式：`YYYY-MM-DD-title.md`。

```yaml
---
layout: post
title: "你好，世界"
date: 2023-10-27 12:00:00
---

这里写内容...
```

查看 [写文章指南](docs/writing-posts_CN.md) 了解更多。

## 许可证

MIT
