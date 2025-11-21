# Jekyll 草稿管理指南

## 什么是草稿？

Jekyll 的草稿（Drafts）功能允许你在 `_drafts` 目录中编写未发布的文章，这些文章默认不会出现在生成的网站中，只有在预览时才会显示。

## 草稿 vs 正式文章

| 特性 | 草稿 (_drafts) | 正式文章 (_posts) |
|------|---------------|------------------|
| 目录 | `_drafts/` | `_posts/` |
| 文件名格式 | `title.md` | `YYYY-MM-DD-title.md` |
| 默认显示 | ❌ 否 | ✅ 是 |
| 需要日期 | ❌ 否（可选） | ✅ 是 |
| 预览方式 | `--drafts` 参数 | 默认显示 |

## 使用草稿

### 1. 创建草稿目录

```bash
mkdir _drafts
```

### 2. 创建草稿文件

在 `_drafts` 目录中创建 markdown 文件，**文件名不需要日期前缀**：

```bash
# ✅ 正确 - 草稿文件名
_drafts/my-new-post.md
_drafts/tutorial-draft.md
_drafts/ideas-for-blog.md

# ❌ 不需要 - 草稿不需要日期前缀
_drafts/2025-01-01-my-post.md
```

### 3. 编写草稿

草稿文件的 front matter 格式与正式文章相同：

```markdown
---
title: "我的草稿文章"
layout: post
tags: [Jekyll, Tutorial]
---

这里是草稿内容...
```

### 4. 预览草稿

使用 `--drafts` 参数启动 Jekyll 服务器：

```bash
# 预览草稿
bundle exec jekyll serve --drafts

# 或者使用简写
jekyll s --drafts
```

访问 `http://localhost:4000` 即可看到草稿文章。

### 5. 发布草稿

当草稿完成后，将文件移动到 `_posts` 目录并添加日期前缀：

```bash
# 手动移动
mv _drafts/my-new-post.md _posts/2025-11-21-my-new-post.md

# 或使用脚本（见下文）
```

## 草稿的日期处理

### 草稿的发布日期

- 如果草稿的 front matter 中**没有** `date` 字段，Jekyll 会使用**文件的修改时间**作为发布日期
- 如果草稿的 front matter 中**有** `date` 字段，则使用指定的日期

```yaml
---
title: "我的草稿"
layout: post
date: 2025-11-21 10:00:00  # 可选：指定日期
---
```

### 草稿排序

在预览时，草稿会按照日期排序显示在文章列表中。

## 实用脚本

### 发布草稿脚本

创建 `publish_draft.sh` 脚本来简化发布流程：

```bash
#!/bin/bash
# 发布草稿脚本

if [ -z "$1" ]; then
    echo "用法: ./publish_draft.sh <草稿文件名>"
    echo "示例: ./publish_draft.sh my-draft.md"
    exit 1
fi

DRAFT_FILE="_drafts/$1"
DATE=$(date +%Y-%m-%d)
FILENAME=$(basename "$1" .md)
POST_FILE="_posts/${DATE}-${FILENAME}.md"

if [ ! -f "$DRAFT_FILE" ]; then
    echo "❌ 错误: 草稿文件不存在: $DRAFT_FILE"
    exit 1
fi

# 验证草稿
echo "🔍 验证草稿..."
./validate.sh "$DRAFT_FILE"

if [ $? -ne 0 ]; then
    echo "❌ 草稿验证失败，请先修复错误"
    exit 1
fi

# 移动文件
mv "$DRAFT_FILE" "$POST_FILE"
echo "✅ 草稿已发布: $POST_FILE"

# 可选：自动提交
read -p "是否提交到 Git? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    git add "$POST_FILE"
    git commit -m "Publish: $FILENAME"
    echo "✅ 已提交到 Git"
fi
```

使用方法：

```bash
chmod +x publish_draft.sh
./publish_draft.sh my-draft.md
```

### 创建草稿脚本

创建 `new_draft.sh` 脚本快速创建新草稿：

```bash
#!/bin/bash
# 创建新草稿脚本

if [ -z "$1" ]; then
    echo "用法: ./new_draft.sh <标题>"
    echo "示例: ./new_draft.sh 'My New Post'"
    exit 1
fi

TITLE="$1"
FILENAME=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | sed 's/[^a-z0-9-]//g')
DRAFT_FILE="_drafts/${FILENAME}.md"

if [ -f "$DRAFT_FILE" ]; then
    echo "❌ 错误: 草稿已存在: $DRAFT_FILE"
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

## 内容

EOF

echo "✅ 草稿已创建: $DRAFT_FILE"
echo "📝 开始编辑: code $DRAFT_FILE"

# 可选：自动打开编辑器
# code "$DRAFT_FILE"  # VS Code
# vim "$DRAFT_FILE"   # Vim
```

使用方法：

```bash
chmod +x new_draft.sh
./new_draft.sh "My Awesome Post"
```

## 草稿工作流

### 推荐工作流程

```bash
# 1. 创建新草稿
./new_draft.sh "My New Article"

# 2. 编辑草稿
code _drafts/my-new-article.md

# 3. 预览草稿
bundle exec jekyll serve --drafts
# 访问 http://localhost:4000

# 4. 验证草稿
./validate.sh _drafts/my-new-article.md

# 5. 发布草稿
./publish_draft.sh my-new-article.md

# 6. 推送到远程
git push
```

### 使用 Makefile

在 `Makefile` 中添加草稿相关命令：

```makefile
.PHONY: draft serve-drafts publish-draft

# 预览草稿
serve-drafts:
	@echo "🚀 启动服务器（包含草稿）..."
	@bundle exec jekyll serve --drafts --livereload

# 列出所有草稿
list-drafts:
	@echo "📝 当前草稿列表:"
	@ls -1 _drafts/ 2>/dev/null || echo "  (无草稿)"

# 验证所有草稿
validate-drafts:
	@echo "🔍 验证所有草稿..."
	@./validate.sh _drafts/*.md 2>/dev/null || echo "  (无草稿)"
```

使用：

```bash
make serve-drafts      # 预览草稿
make list-drafts       # 列出草稿
make validate-drafts   # 验证草稿
```

## 高级技巧

### 1. 草稿分类

在 `_drafts` 中创建子目录来组织草稿：

```
_drafts/
  ├── tutorials/
  │   └── jekyll-guide.md
  ├── reviews/
  │   └── book-review.md
  └── ideas/
      └── future-topics.md
```

### 2. 草稿模板

创建 `_drafts/_template.md` 作为模板：

```markdown
---
title: "文章标题"
layout: post
tags: []
categories: []
description: "文章简介"
---

## 概述

## 主要内容

### 小节 1

### 小节 2

## 总结
```

### 3. 未来文章

在草稿中设置未来日期，即使移动到 `_posts` 也不会立即发布：

```yaml
---
title: "未来文章"
layout: post
date: 2025-12-31 10:00:00  # 未来日期
---
```

Jekyll 默认不会显示未来日期的文章，除非使用 `--future` 参数：

```bash
bundle exec jekyll serve --future
```

## Git 管理

### 是否提交草稿？

**选项 1: 提交草稿**（推荐用于个人博客）
```bash
# .gitignore 中不排除 _drafts
git add _drafts/
git commit -m "Add draft: my-new-post"
```

优点：
- 草稿有版本控制
- 可以在不同设备间同步
- 有备份

**选项 2: 不提交草稿**（推荐用于团队博客）
```bash
# .gitignore 中添加
echo "_drafts/" >> .gitignore
```

优点：
- 草稿保持私密
- 仓库更干净

## 常见问题

### Q: 草稿可以有日期前缀吗？

A: 可以，但不推荐。草稿的优势就是不需要日期前缀，更灵活。

### Q: 草稿会被构建到生产环境吗？

A: 不会。只有在使用 `--drafts` 参数时才会包含草稿。生产环境构建时不会包含。

### Q: 如何批量发布多个草稿？

A: 可以写一个脚本遍历 `_drafts` 目录，或者手动移动多个文件。

### Q: 草稿可以使用验证工具吗？

A: 可以！验证工具对草稿和正式文章都有效：

```bash
./validate.sh _drafts/my-draft.md
```

## 总结

Jekyll 的草稿功能提供了：

✅ **灵活的写作环境** - 不需要立即确定发布日期  
✅ **安全的预览** - 草稿不会出现在生产环境  
✅ **简单的发布流程** - 移动文件即可发布  
✅ **版本控制** - 可选择是否提交草稿到 Git  

现在你可以自由地创建和管理草稿，在准备好之前不用担心文章被发布！


