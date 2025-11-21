#!/bin/bash
# 创建新草稿脚本

set -e

if [ -z "$1" ]; then
    echo "用法: ./new_draft.sh <标题>"
    echo "示例: ./new_draft.sh 'My New Post'"
    exit 1
fi

TITLE="$1"
# 转换标题为文件名：小写、空格转连字符、移除特殊字符
FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')
DRAFT_FILE="_drafts/${FILENAME}.md"

# 创建 _drafts 目录（如果不存在）
mkdir -p _drafts

# 检查文件是否已存在
if [ -f "$DRAFT_FILE" ]; then
    echo "❌ 错误: 草稿已存在: $DRAFT_FILE"
    read -p "是否打开现有草稿? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        code "$DRAFT_FILE" 2>/dev/null || echo "📝 请手动打开: $DRAFT_FILE"
    fi
    exit 1
fi

# 创建草稿文件
cat > "$DRAFT_FILE" << EOF
---
title: "$TITLE"
layout: post
tags: []
---

在这里开始写作...

## 大纲

- 
- 
- 

## 主要内容

### 小节 1

### 小节 2

## 总结

EOF

echo "✅ 草稿已创建: $DRAFT_FILE"
echo ""
echo "下一步:"
echo "  1. 编辑草稿: code $DRAFT_FILE"
echo "  2. 预览草稿: bundle exec jekyll serve --drafts"
echo "  3. 验证草稿: ./validate.sh $DRAFT_FILE"
echo "  4. 发布草稿: ./publish_draft.sh ${FILENAME}.md"
echo ""

# 可选：自动打开编辑器
read -p "是否立即打开编辑器? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    code "$DRAFT_FILE" 2>/dev/null || vim "$DRAFT_FILE" 2>/dev/null || echo "请手动打开文件"
fi
