# Jekyll 文章验证工具

这个工具可以在发布 markdown 文件到 `_posts` 目录之前，检查文件是否符合 Jekyll 的语法格式要求，避免导致 Jekyll 报错。

## 功能特性

✅ **YAML Front Matter 验证**
- 检查 YAML 语法是否正确
- 验证必需字段（title, layout, date）
- 检查字段值的有效性

✅ **文件名格式验证**
- 确保文件名符合 `YYYY-MM-DD-title.md` 格式
- 验证日期的有效性
- 检查文件名日期与 front matter 日期是否一致

✅ **Markdown 内容验证**
- 检查代码块是否正确闭合
- 验证图片和链接格式
- 统计字数

✅ **最佳实践建议**
- SEO 优化建议（description, excerpt）
- 内容组织建议（categories, tags）

## 安装依赖

```bash
pip install pyyaml
```

或者使用项目的 requirements.txt（如果有的话）。

## 使用方法

### 基本用法

验证单个文件：
```bash
python validate_post.py _posts/2025-01-01-example.md
```

验证多个文件：
```bash
python validate_post.py _posts/2025-01-01-post1.md _posts/2025-01-02-post2.md
```

使用通配符验证所有文章：
```bash
python validate_post.py _posts/*.md
```

### 高级选项

**严格模式**（警告也视为错误）：
```bash
python validate_post.py --strict _posts/2025-01-01-example.md
```

**安静模式**（只显示错误）：
```bash
python validate_post.py --quiet _posts/*.md
```

### 查看帮助

```bash
python validate_post.py --help
```

## 输出示例

### 验证通过
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

### 验证失败
```
============================================================
验证文件: _posts/2025-01-01-bad-post.md
============================================================

❌ 错误 (2):
  1. 缺少必需字段: title
  2. 代码块未正确闭合（``` 数量不匹配）

⚠️  警告 (1):
  1. tags 列表为空

❌ 验证失败！请修复上述错误。
```

## 验证规则

### 必需的 Front Matter 字段
- `title`: 文章标题（不能为空）
- `layout`: 布局类型（建议使用 post, page, default）
- `date`: 发布日期（格式：YYYY-MM-DD HH:MM:SS）

### 可选但推荐的字段
- `tags`: 标签列表
- `categories`: 分类
- `description` 或 `excerpt`: 文章摘要（用于 SEO）

### 文件名规则
- 格式：`YYYY-MM-DD-title.md`
- 日期必须有效
- 建议文件名日期与 front matter 日期一致

## 集成到工作流

### Git Pre-commit Hook

创建 `.git/hooks/pre-commit` 文件：

```bash
#!/bin/bash
# 验证所有即将提交的 markdown 文件

# 获取所有暂存的 .md 文件
STAGED_MD_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep "^_posts/.*\.md$")

if [ -n "$STAGED_MD_FILES" ]; then
    echo "验证 Jekyll 文章..."
    python validate_post.py $STAGED_MD_FILES
    
    if [ $? -ne 0 ]; then
        echo "❌ 验证失败！请修复错误后再提交。"
        exit 1
    fi
    
    echo "✅ 所有文章验证通过！"
fi

exit 0
```

然后添加执行权限：
```bash
chmod +x .git/hooks/pre-commit
```

### 发布前检查脚本

创建 `check_before_publish.sh`：

```bash
#!/bin/bash
# 发布前检查所有文章

echo "🔍 检查所有文章..."
python validate_post.py _posts/*.md --strict

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ 所有文章验证通过！可以安全发布。"
    echo ""
    echo "运行 Jekyll 构建测试..."
    bundle exec jekyll build --strict_front_matter
    
    if [ $? -eq 0 ]; then
        echo "✅ Jekyll 构建成功！"
    else
        echo "❌ Jekyll 构建失败，请检查错误信息。"
        exit 1
    fi
else
    echo "❌ 文章验证失败，请先修复错误。"
    exit 1
fi
```

### Makefile 集成

在项目根目录创建或编辑 `Makefile`：

```makefile
.PHONY: validate validate-strict build publish

# 验证所有文章
validate:
	@echo "验证所有文章..."
	@python validate_post.py _posts/*.md

# 严格模式验证
validate-strict:
	@echo "严格模式验证所有文章..."
	@python validate_post.py _posts/*.md --strict

# 构建站点（包含验证）
build: validate-strict
	@echo "构建 Jekyll 站点..."
	@bundle exec jekyll build --strict_front_matter

# 发布前完整检查
publish: build
	@echo "✅ 所有检查通过，可以发布！"
```

使用方法：
```bash
make validate        # 快速验证
make validate-strict # 严格验证
make build          # 验证并构建
make publish        # 完整发布流程
```

## 其他推荐工具

### 1. Jekyll 内置验证
在 `_config.yml` 中启用严格模式：
```yaml
strict_front_matter: true
```

或在命令行使用：
```bash
bundle exec jekyll build --strict_front_matter
```

### 2. Markdown Linter
安装 markdownlint：
```bash
npm install -g markdownlint-cli
```

使用：
```bash
markdownlint _posts/*.md
```

### 3. YAML Linter
安装 yamllint：
```bash
pip install yamllint
```

使用：
```bash
yamllint _posts/*.md
```

## 故障排除

### 常见错误

**错误：缺少必需字段**
```yaml
---
# ❌ 错误：缺少 title
layout: post
date: 2025-01-01
---

# ✅ 正确
---
title: "My Post"
layout: post
date: 2025-01-01 09:00:00
---
```

**错误：YAML 语法错误**
```yaml
# ❌ 错误：冒号后缺少空格
---
title:"My Post"
---

# ✅ 正确
---
title: "My Post"
---
```

**错误：日期格式不正确**
```yaml
# ❌ 错误
date: 2025/01/01

# ✅ 正确
date: 2025-01-01 09:00:00
```

**错误：代码块未闭合**
````markdown
❌ 错误：
```python
def hello():
    print("Hello")
# 缺少结束的 ```

✅ 正确：
```python
def hello():
    print("Hello")
```
````

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个工具！

## 许可证

MIT License
