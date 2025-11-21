# 写文章指南

## 创建文章

在 `_posts` 目录下新建文件，命名格式如下：

`年-月-日-标题.md`

示例：`2023-10-27-hello-world.md`

## Front Matter (前置元数据)

每篇文章必须以 Front Matter 开头，即两行 `---` 之间的 YAML 块。

```yaml
---
layout: post
title: "文章标题"
date: 2023-10-27 12:00:00
---
```

### 文章摘要

主题默认使用文章的第一段作为首页显示的摘要。你也可以在 Front Matter 中自定义：

```yaml
excerpt: "这是自定义的摘要内容，将显示在文章列表中。"
```

## 格式规范

### 标题

文章内建议使用二级 `##` 和三级 `###` 标题。

```markdown
## 二级标题
### 三级标题
```

### 代码块

使用三个反引号包裹代码，并指定语言以启用高亮。

    ```python
    def hello():
        print("Hello World")
    ```

### 数学公式 (MathJax)

默认已启用 MathJax。你可以直接编写 LaTeX 公式：

$$ E = mc^2 $$
