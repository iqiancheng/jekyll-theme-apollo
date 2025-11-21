# Jekyll 草稿快速参考

## 快速开始

### 预览草稿
```bash
# 启动服务器并显示草稿
bundle exec jekyll serve --drafts

# 访问
http://localhost:4000
```

### 创建草稿
```bash
# 方法 1: 使用脚本
./new_draft.sh "我的新文章"

# 方法 2: 手动创建
# 在 _drafts/ 目录创建 .md 文件（不需要日期前缀）
```

### 发布草稿
```bash
# 使用脚本（推荐）
./publish_draft.sh my-draft.md

# 手动发布
mv _drafts/my-draft.md _posts/2025-11-21-my-draft.md
```

## 草稿 vs 正式文章

| 项目 | 草稿 | 正式文章 |
|------|------|---------|
| 位置 | `_drafts/` | `_posts/` |
| 文件名 | `title.md` | `YYYY-MM-DD-title.md` |
| 预览 | 需要 `--drafts` | 默认显示 |

## 常用命令

```bash
# 创建新草稿
./new_draft.sh "文章标题"

# 预览草稿
bundle exec jekyll serve --drafts

# 验证草稿
./validate.sh _drafts/my-draft.md

# 发布草稿
./publish_draft.sh my-draft.md

# 列出所有草稿
ls _drafts/
```

## 工作流程

```
创建草稿 → 编辑内容 → 预览效果 → 验证格式 → 发布文章
   ↓          ↓          ↓          ↓          ↓
new_draft  编辑器    serve      validate   publish
```

## 提示

- ✅ 草稿文件名**不需要**日期前缀
- ✅ 草稿**不会**出现在生产环境
- ✅ 可以随时编辑草稿而不影响已发布内容
- ✅ 发布时会自动添加当前日期

详细文档: [docs/drafts-guide.md](docs/drafts-guide.md)
