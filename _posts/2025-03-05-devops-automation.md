---
title: "Automating Deployments: A DevOps Handbook"
layout: post
date: 2025-03-05 16:00:00
tags: [DevOps, CI/CD, Linux, Automation]
---

In the world of DevOps, if you do it twice, automate it. I use this blog to document my scripts and configurations so I never have to reinvent the wheel.

## The Deployment Script

Here is a robust bash script I use for deploying static sites (like this one!) to a remote server.

```bash
#!/bin/bash

# Configuration
SERVER="user@192.168.1.100"
REMOTE_DIR="/var/www/html"
LOCAL_DIR="_site/"

echo "Building Jekyll site..."
bundle exec jekyll build

echo "Deploying to $SERVER..."
rsync -avz --delete $LOCAL_DIR $SERVER:$REMOTE_DIR

echo "Deployment complete!"
```

## GitHub Actions Workflow

Why run scripts manually when GitHub can do it for you? Here is my `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Ruby
      uses: ruby/setup-ruby@v1
      with:
        ruby-version: 3.1
    - name: Build Site
      run: |
        bundle install
        bundle exec jekyll build
```

![Server Room](https://loremflickr.com/800/400/server,tech)

## Why Apollo?

It supports **syntax highlighting** for `bash` and `yaml` out of the box. The copy button is a lifesaver for my readers who want to grab these snippets quickly.
