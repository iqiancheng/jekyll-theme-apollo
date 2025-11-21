# Jekyll 文章验证工具 - 快速开始

## 简介

这个工具可以在发布 markdown 文件到 `_posts` 目录之前，自动检查文件格式，避免 Jekyll 构建错误。

## 快速使用

### 方法 1：使用便捷脚本（推荐）

最简单的方式，自动管理依赖：

```bash
# 验证单个文件
./validate.sh _posts/2025-01-01-example.md

# 验证多个文件
./validate.sh _posts/*.md

# 严格模式
./validate.sh --strict _posts/*.md
```

首次运行会自动创建虚拟环境并安装依赖。

### 方法 2：手动使用

如果你想手动管理环境：

```bash
# 1. 创建虚拟环境（首次）
python3 -m venv .venv

# 2. 激活虚拟环境
source .venv/bin/activate

# 3. 安装依赖（首次）
pip install -r requirements.txt

# 4. 运行验证
python validate_post.py _posts/*.md
```

## 验证内容

✅ **YAML Front Matter**
- 语法正确性
- 必需字段：title, layout, date
- 字段值有效性

✅ **文件命名**
- 格式：`YYYY-MM-DD-title.md`
- 日期有效性

✅ **Markdown 内容**
- 代码块闭合
- 链接格式
- 图片路径

## 输出示例

```
============================================================
验证文件: _posts/2025-01-01-example.md
============================================================

ℹ️  信息:
  • 文件名日期: 2025-01-01
  • 标题: My Example Post
  • 布局: post
  • 文章日期: 2025-01-01 09:00:00
  • 标签: Jekyll, Tutorial
  • 字数统计: 约 150 词

✅ 验证通过！文件格式正确。
```

## 集成到工作流

### 发布前检查

```bash
# 验证所有文章
./validate.sh _posts/*.md

# 如果通过，构建站点
bundle exec jekyll build
```

### Git Pre-commit Hook

创建 `.git/hooks/pre-commit`：

```bash
#!/bin/bash
STAGED_MD=$(git diff --cached --name-only | grep "^_posts/.*\.md$")
if [ -n "$STAGED_MD" ]; then
    ./validate.sh $STAGED_MD || exit 1
fi
```

## 更多信息

详细文档请查看：[docs/validate-posts.md](docs/validate-posts.md)

## 常见问题

**Q: 首次运行很慢？**  
A: 首次运行需要创建虚拟环境和安装依赖，之后会很快。

**Q: 如何只看错误？**  
A: 使用 `--quiet` 参数：`./validate.sh --quiet _posts/*.md`

**Q: 警告必须修复吗？**  
A: 警告是建议，不影响构建。使用 `--strict` 可将警告视为错误。
