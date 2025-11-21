# Recipes

This directory contains scripts and documentation for maintaining and developing the Jekyll blog.

## 📁 Structure

```
recipes/
├── scripts/              # Utility scripts
│   ├── new_draft.sh     # Create new draft posts
│   ├── publish_draft.sh # Publish drafts to _posts
│   ├── validate.sh      # Validate post syntax
│   ├── validate_post.py # Post validation (Python)
│   ├── check_links.py   # Check for dead links
│   ├── replace_links.py # Replace links in posts
│   ├── convert-images.sh # Convert images to WebP/AVIF
│   └── requirements.txt # Python dependencies
└── docs/                # Documentation
    ├── README-DRAFTS.md        # Draft workflow guide
    ├── README-VALIDATOR.md     # Post validation guide
    └── image-optimization.md   # Image optimization guide
```

## 🚀 Quick Start

### Working with Drafts

```bash
# Create a new draft
./recipes/scripts/new_draft.sh "My Post Title"

# Publish a draft
./recipes/scripts/publish_draft.sh my-draft-file.md
```

### Validating Posts

```bash
# Validate all posts
./recipes/scripts/validate.sh

# Validate specific post
python3 recipes/scripts/validate_post.py _posts/2024-01-01-post.md
```

### Optimizing Images

```bash
# Convert images to modern formats
./recipes/scripts/convert-images.sh assets/images
```

### Checking Links

```bash
# Install Python dependencies first
pip3 install -r recipes/scripts/requirements.txt

# Check for dead links
python3 recipes/scripts/check_links.py

# Replace links
python3 recipes/scripts/replace_links.py
```

## 📚 Documentation

- **[Draft Workflow](docs/README-DRAFTS.md)** - How to work with draft posts
- **[Post Validation](docs/README-VALIDATOR.md)** - Validate post syntax and front matter
- **[Image Optimization](docs/image-optimization.md)** - Optimize images for web
- **[Multi-language Support](docs/i18n.md)** - Configure language settings (EN/简体中文/繁體中文)

## 🛠️ Setup

### Install System Dependencies

```bash
# For image conversion
brew install libvips imagemagick libheif

# For Python scripts
pip3 install -r recipes/scripts/requirements.txt
```

### Make Scripts Executable

```bash
chmod +x recipes/scripts/*.sh
```

## 💡 Tips

- All scripts should be run from the **project root directory**
- Python scripts require Python 3.6+
- Shell scripts are compatible with bash/zsh
- Check individual documentation files for detailed usage

## 🤝 Contributing

When adding new scripts or documentation:

1. Place scripts in `recipes/scripts/`
2. Place documentation in `recipes/docs/`
3. Update this README with usage instructions
4. Add comments to your scripts
5. Make shell scripts executable (`chmod +x`)
