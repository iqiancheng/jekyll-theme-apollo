# Configuration

The `_config.yml` file is where you configure your site settings.

## Basic Settings

| Option | Description |
|----- | ----------- |
| `title` | Your site title. |
| `description` | A short description of your site (used in meta tags). |
| `url` | The base hostname and protocol for your site. |
| `baseurl` | The subpath of your site (e.g. `/blog`). |
| `language` | The language of your site (default: `en`). |

## Assets

| Option | Description |
|----- | ----------- |
| `logo` | Path to your site logo (e.g. `/assets/favicon.png`). |
| `favicon` | Path to your favicon (e.g. `/assets/favicon.png`). |

## Menu

Navigation links are defined in `_config.yml` under the `menu` key. You can customize the order, add, or remove items:

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

**Notes:**
- Links starting with `http://` or `https://` will open in a new tab
- Internal links (starting with `/`) will open in the same tab
- The order in the YAML file determines the display order in the navigation bar

## Comments

To enable Disqus comments, add your shortname to `_config.yml`:

```yaml
disqus: your_disqus_shortname
```

## Analytics

To enable Google Analytics, add your tracking ID to `_config.yml`:

```yaml
google_analytics: UA-XXXXXXXX-X
```
