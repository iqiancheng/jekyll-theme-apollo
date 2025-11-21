# 自定义指南

## 样式 (CSS/SCSS)

主题使用 SCSS 编写样式。主入口文件是 `assets/css/main.scss`，它引入了 `_sass/` 目录下的局部文件。

- `_sass/_apollo.scss`: 主题核心样式。
- `_sass/_partial/`: 组件样式（头部、页脚、文章等）。

你可以直接修改这些文件来调整样式。

## 布局 (Layouts)

布局文件位于 `_layouts` 目录。

- `default.html`: 基础布局，包含 `head`、`header`、`footer` 和脚本。
- `post.html`: 文章页面的布局。

## 组件 (Includes)

可复用的组件位于 `_includes` 目录。

- `head.html`: Meta 标签和 CSS 链接。
- `nav.html`: 导航菜单。
- `copyright.html`: 页脚版权信息。
- `scripts.html`: JavaScript 文件 (MathJax, Google Analytics)。

## 404 页面

你可以通过修改根目录下的 `404.html` 来自定义 404 页面。
