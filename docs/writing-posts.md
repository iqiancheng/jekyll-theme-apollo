# Writing Posts

## Creating a Post

To create a new post, add a file to the `_posts` directory with the following name format:

`YEAR-MONTH-DAY-title.md`

Example: `2023-10-27-hello-world.md`

## Front Matter

Every post must begin with Front Matter, which is a block of YAML between two triple-dashed lines.

```yaml
---
layout: post
title: "Your Post Title"
date: 2023-10-27 12:00:00
---
```

### Post Excerpts

The theme automatically uses the first paragraph of your post as the excerpt on the home page. You can also define a custom excerpt in the front matter:

```yaml
excerpt: "This is a custom excerpt for the post list."
```

## Formatting

### Headings

The theme is optimized for `h2` and `h3` headings within posts.

```markdown
## Level 2 Heading
### Level 3 Heading
```

### Code Blocks

Use triple backticks for code blocks. You can specify the language for syntax highlighting.

    ```python
    def hello():
        print("Hello World")
    ```

### MathJax

MathJax is enabled by default. You can write LaTeX equations:

$$ E = mc^2 $$
