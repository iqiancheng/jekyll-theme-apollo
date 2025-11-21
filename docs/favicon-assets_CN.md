# Favicon 和图标资源

本文档说明各种 favicon 和图标文件的作用，以及它们在主题中的推荐存放位置。

## 概述

浏览器和设备会根据不同的用途请求不同的图标文件。本主题支持多种图标格式，以确保在所有平台上的兼容性。

## 必需的资源文件

### 1. `favicon.ico`

**作用：** 经典的 favicon 格式，浏览器会自动请求  
**路径：** `/assets/favicon.ico`  
**尺寸：** 16x16、32x32 或多尺寸 ICO 文件  
**用途：** 旧版浏览器支持、浏览器标签页、书签

**为什么浏览器会请求它：**
- 浏览器会自动在网站根目录查找 `/favicon.ico`
- 即使没有明确的 `<link>` 标签，浏览器也会尝试获取此文件
- 为旧版浏览器提供后备支持

### 2. `apple-touch-icon.png`

**作用：** iOS/iPadOS 主屏幕和 Safari 书签的图标  
**路径：** `/assets/apple-touch-icon.png`  
**尺寸：** 180x180 像素（PNG 格式）  
**用途：** 当用户将您的网站添加到 iOS 主屏幕时使用

**为什么 iOS 会请求它：**
- iOS Safari 在保存 Web 应用时会自动查找此文件
- 用于 iPhone 和 iPad 上的主屏幕快捷方式
- 为 Apple 设备提供高质量图标

### 3. `apple-touch-icon-precomposed.png`

**作用：** 旧版 iOS 图标（iOS 7 之前）  
**路径：** `/assets/apple-touch-icon-precomposed.png`  
**尺寸：** 180x180 像素（PNG 格式）  
**用途：** 较旧的 iOS 版本（iOS 7 之前）

**为什么存在：**
- 旧版 iOS 默认会为图标添加光泽效果
- `-precomposed` 后缀告诉 iOS 不要添加效果
- 现代 iOS 会忽略此文件，但旧设备仍会请求它

## 推荐的文件结构

```
jekyll-theme-apollo/
├── assets/
│   ├── favicon.ico                    # 16x16 或 32x32 ICO 格式
│   ├── favicon.png                    # 当前主题默认（任意尺寸）
│   ├── favicon-16x16.png              # 可选：16x16 PNG
│   ├── favicon-32x32.png              # 可选：32x32 PNG
│   ├── apple-touch-icon.png           # 180x180 用于 iOS
│   └── apple-touch-icon-precomposed.png  # 180x180 用于旧版 iOS
```

## 如何添加这些文件

### 方案 1：快速设置（最小化）

创建以下三个文件以消除错误：

1. **favicon.ico** - 将您的 logo 转换为 ICO 格式（16x16 或 32x32）
2. **apple-touch-icon.png** - 180x180 PNG 版本的 logo
3. **apple-touch-icon-precomposed.png** - apple-touch-icon.png 的副本

将所有文件放在 `assets/` 目录中。

### 方案 2：完整设置（推荐）

为了获得最佳的跨平台支持，在 `_includes/head.html` 中添加这些 `<link>` 标签：

```html
<!-- Favicon -->
<link rel="icon" type="image/x-icon" href="{{ '/assets/favicon.ico' | relative_url }}">
<link rel="icon" type="image/png" sizes="32x32" href="{{ '/assets/favicon-32x32.png' | relative_url }}">
<link rel="icon" type="image/png" sizes="16x16" href="{{ '/assets/favicon-16x16.png' | relative_url }}">

<!-- Apple Touch Icons -->
<link rel="apple-touch-icon" sizes="180x180" href="{{ '/assets/apple-touch-icon.png' | relative_url }}">
```

## 当前配置

主题目前使用：

```yaml
# _config.yml
favicon: /assets/favicon.png
```

在 `_includes/head.html` 中引用：

```html
<link rel="icon" href="{{ site.favicon | relative_url }}">
```

这样可以工作，但浏览器仍会自动请求缺失的文件，导致日志中出现 404 错误。

## 生成图标

您可以使用在线工具从单个图像生成所有所需格式：

- [RealFaviconGenerator](https://realfavicongenerator.net/) - 综合 favicon 生成器
- [Favicon.io](https://favicon.io/) - 简单的 favicon 生成器
- ImageMagick（命令行）：
  ```bash
  # 将 PNG 转换为 ICO
  convert favicon.png -define icon:auto-resize=16,32,48 favicon.ico
  
  # 调整大小为 Apple Touch Icon
  convert favicon.png -resize 180x180 apple-touch-icon.png
  ```

## 为什么会出现这些错误

即使在 HTML 中没有明确的 `<link>` 标签，浏览器和设备也会自动请求这些文件：

- **浏览器** 按照惯例请求 `/favicon.ico`
- **iOS Safari** 在添加书签时请求 `/apple-touch-icon.png`
- **旧版 iOS** 请求 `/apple-touch-icon-precomposed.png`

这些不是您代码中的错误——它们是标准的浏览器行为。添加这些文件将消除服务器日志中的 404 错误。

## 总结

| 文件 | 尺寸 | 用途 | 优先级 |
|------|------|------|--------|
| `favicon.ico` | 16x16 或 32x32 | 浏览器标签页、书签 | 高 |
| `apple-touch-icon.png` | 180x180 | iOS 主屏幕 | 高 |
| `apple-touch-icon-precomposed.png` | 180x180 | 旧版 iOS | 中 |
| `favicon-16x16.png` | 16x16 | 现代浏览器（小） | 可选 |
| `favicon-32x32.png` | 32x32 | 现代浏览器（标准） | 可选 |

**最小设置：** 添加前三个文件以消除 404 错误。  
**推荐设置：** 添加所有文件并更新 `_includes/head.html` 以获得完整的跨平台支持。
