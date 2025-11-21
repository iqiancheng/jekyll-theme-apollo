#!/bin/bash
# 发布草稿脚本 - 将草稿移动到 _posts 目录并添加日期前缀

set -e

if [ -z "$1" ]; then
    echo "用法: ./publish_draft.sh <草稿文件名>"
    echo "示例: ./publish_draft.sh my-draft.md"
    echo ""
    echo "当前草稿列表:"
    ls -1 _drafts/ 2>/dev/null || echo "  (无草稿)"
    exit 1
fi

DRAFT_FILE="_drafts/$1"
DATE=$(date +%Y-%m-%d)
FILENAME=$(basename "$1" .md)
POST_FILE="_posts/${DATE}-${FILENAME}.md"

# 检查草稿是否存在
if [ ! -f "$DRAFT_FILE" ]; then
    echo "❌ 错误: 草稿文件不存在: $DRAFT_FILE"
    exit 1
fi

# 检查目标文件是否已存在
if [ -f "$POST_FILE" ]; then
    echo "⚠️  警告: 目标文件已存在: $POST_FILE"
    read -p "是否覆盖? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ 取消发布"
        exit 1
    fi
fi

# 验证草稿（如果验证脚本存在）
if [ -f "validate.sh" ]; then
    echo "🔍 验证草稿..."
    ./validate.sh "$DRAFT_FILE"
    
    if [ $? -ne 0 ]; then
        echo ""
        read -p "⚠️  验证失败，是否仍要发布? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "❌ 取消发布"
            exit 1
        fi
    fi
fi

# 移动文件
mv "$DRAFT_FILE" "$POST_FILE"
echo "✅ 草稿已发布: $POST_FILE"

# 可选：自动提交到 Git
if git rev-parse --git-dir > /dev/null 2>&1; then
    read -p "是否提交到 Git? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git add "$POST_FILE"
        git commit -m "Publish: $FILENAME"
        echo "✅ 已提交到 Git"
        
        read -p "是否推送到远程? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git push
            echo "✅ 已推送到远程"
        fi
    fi
fi

echo ""
echo "🎉 发布完成！"
echo "📝 文件位置: $POST_FILE"
