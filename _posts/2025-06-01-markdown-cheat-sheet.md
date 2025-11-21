---
title: "The Ultimate Markdown Cheat Sheet"
layout: post
date: 2025-06-01 09:00:00
tags: [Markdown, Guide, Reference]
---

This post serves as a comprehensive test suite for the Apollo theme's Markdown rendering capabilities.

## 1. Typography

**Bold Text** and *Italic Text* and ***Bold Italic***.
~~Strikethrough~~ is also supported.

> This is a blockquote.
>
> > Nested blockquotes look like this.

## 2. Lists

### Unordered List
*   Item 1
*   Item 2
    *   Sub-item 2.1
    *   Sub-item 2.2
*   Item 3

### Ordered List
1.  First step
2.  Second step
    1.  Sub-step A
    2.  Sub-step B
3.  Third step

### Task List
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task

## 3. Tables

| Feature | Support | Notes |
| :--- | :---: | ---: |
| Tables | Yes | Left, Center, Right aligned |
| MathJax | Yes | $E=mc^2$ |
| Mermaid | Yes | Diagrams |

## 4. Code

Inline code: `const x = 10;`

```javascript
// JavaScript Block
function hello() {
  console.log("Hello World");
}
```

```python
# Python Block
def add(a, b):
    return a + b
```

## 5. Footnotes

Here is a sentence with a footnote.[^1]

## 6. Definition Lists

Markdown
:   Text-to-HTML conversion tool for web writers.

Apollo
:   A beautiful Jekyll theme.

## 7. Horizontal Rule

---

## 8. Images

![Test Image](https://loremflickr.com/800/400/abstract,geometry)

[^1]: This is the footnote content.
