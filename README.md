# Jekyll Theme Apollo

A minimal, clean, and responsive Jekyll theme ported from [Hexo Theme Apollo](https://github.com/pinggod/hexo-theme-apollo).

![hexo-theme-apollo](https://cloud.githubusercontent.com/assets/9530963/13026956/08e76eca-d277-11e5-8bfc-2e80cea20a0d.png)

## Features

- **Minimalist Design**: Focus on content with a clean and distraction-free layout.
- **Responsive**: Looks great on all devices, from desktops to mobiles.
- **Google Analytics**: Built-in support for Google Analytics.
- **Disqus Comments**: Easy integration with Disqus for comments.
- **Syntax Highlighting**: Clean code blocks for your technical posts.
- **MathJax Support**: Render mathematical formulas beautifully.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/iqiancheng/jekyll-theme-apollo.git
    cd jekyll-theme-apollo
    ```

2.  **Install dependencies**:
    ```bash
    bundle install
    ```

3.  **Run the server**:
    ```bash
    bundle exec jekyll serve
    ```

4.  Open [http://localhost:4000](http://localhost:4000) in your browser.

## Configuration

The main configuration is handled in `_config.yml`.

```yaml
title: Apollo
description: A Blog Powered By Jekyll
url: "http://example.com"
baseurl: ""

# Assets
logo: /assets/favicon.png
favicon: /assets/favicon.png

# Comments
disqus: your_disqus_shortname

# Analytics
google_analytics: UA-XXXXXXXX-X
```

For more details, check the [Documentation](docs/configuration.md).

## Writing Posts

Create markdown files in the `_posts` directory with the following format: `YYYY-MM-DD-title.md`.

```yaml
---
layout: post
title: "Hello World"
date: 2023-10-27 12:00:00
---

Your content here...
```

See [Writing Posts](docs/writing-posts.md) for more advanced usage.

## License

MIT
