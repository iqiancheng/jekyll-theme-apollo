# Customization

## Styles

The theme uses SCSS for styling. The main entry point is `assets/css/main.scss`, which imports partials from `_sass/`.

- `_sass/_apollo.scss`: Main theme styles.
- `_sass/_partial/`: Component-specific styles (header, footer, post, etc.).

To customize styles, you can edit these files directly.

## Layouts

Layouts are located in the `_layouts` directory.

- `default.html`: The base layout containing the `head`, `header`, `footer`, and scripts.
- `post.html`: The layout for individual blog posts.

## Includes

Reusable components are in `_includes`.

- `head.html`: Meta tags and CSS links.
- `nav.html`: The navigation menu.
- `copyright.html`: The footer copyright section.
- `scripts.html`: JavaScript files (MathJax, Google Analytics).

## 404 Page

You can customize the 404 page by editing `404.html` in the root directory.
