# 配置指南

`_config.yml` 是站点的核心配置文件。

## 基础设置

| 选项 | 描述 |
|---- | ----------- |
| `title` | 网站标题。 |
| `description` | 网站描述（用于 meta 标签）。 |
| `url` | 网站的基础域名。 |
| `baseurl` | 网站子路径（例如 `/blog`）。 |
| `language` | 语言设置（默认：`en`）。 |

## 资源

| 选项 | 描述 |
|---- | ----------- |
| `logo` | 网站 Logo 路径（如 `/assets/favicon.png`）。 |
| `favicon` | 网站 Favicon 路径。 |

## 导航菜单

导航链接在 `_config.yml` 的 `menu` 键下定义。你可以自定义顺序、添加或删除菜单项：

```yaml
menu:
  - name: Blog
    link: /
  - name: Archive
    link: /archive/
  - name: GitHub
    link: https://github.com/yourusername
  - name: RSS
    link: /feed.xml
  - name: About
    link: /about/
```

**注意事项：**
- 以 `http://` 或 `https://` 开头的链接会在新标签页打开
- 内部链接（以 `/` 开头）会在当前标签页打开
- YAML 文件中的顺序决定了导航栏中的显示顺序

## 评论系统

要启用 Disqus 评论，在 `_config.yml` 中添加你的 shortname：

```yaml
disqus: your_disqus_shortname
```

## 统计分析

要启用 Google Analytics，在 `_config.yml` 中添加你的追踪 ID：

```yaml
google_analytics: UA-XXXXXXXX-X
```
