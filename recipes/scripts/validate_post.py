#!/usr/bin/env python3
"""
Jekyll Post Validator
验证 Jekyll markdown 文件的语法格式，确保不会导致 Jekyll 报错

使用方法:
    python validate_post.py <file_path>
    python validate_post.py _posts/2025-01-01-example.md
    python validate_post.py _posts/*.md  # 验证多个文件
"""

import sys
import re
import yaml
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Dict, Any
import argparse


class Colors:
    """终端颜色代码"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class ValidationResult:
    """验证结果"""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
    
    def add_error(self, message: str):
        self.errors.append(message)
    
    def add_warning(self, message: str):
        self.warnings.append(message)
    
    def add_info(self, message: str):
        self.info.append(message)
    
    def is_valid(self) -> bool:
        return len(self.errors) == 0
    
    def print_result(self):
        """打印验证结果"""
        print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}验证文件: {self.file_path}{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")
        
        if self.errors:
            print(f"{Colors.RED}{Colors.BOLD}❌ 错误 ({len(self.errors)}):{Colors.RESET}")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {Colors.RED}{error}{Colors.RESET}")
            print()
        
        if self.warnings:
            print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  警告 ({len(self.warnings)}):{Colors.RESET}")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {Colors.YELLOW}{warning}{Colors.RESET}")
            print()
        
        if self.info:
            print(f"{Colors.BLUE}{Colors.BOLD}ℹ️  信息:{Colors.RESET}")
            for info in self.info:
                print(f"  • {Colors.BLUE}{info}{Colors.RESET}")
            print()
        
        if self.is_valid():
            print(f"{Colors.GREEN}{Colors.BOLD}✅ 验证通过！文件格式正确。{Colors.RESET}\n")
        else:
            print(f"{Colors.RED}{Colors.BOLD}❌ 验证失败！请修复上述错误。{Colors.RESET}\n")


class JekyllPostValidator:
    """Jekyll 文章验证器"""
    
    # 必需的 front matter 字段
    REQUIRED_FIELDS = ['title', 'layout', 'date']
    
    # 文件名格式: YYYY-MM-DD-title.md
    FILENAME_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}-.+\.md$')
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.result = ValidationResult(str(file_path))
        self.content = ""
        self.front_matter = {}
        self.body = ""
    
    def validate(self) -> ValidationResult:
        """执行所有验证"""
        # 1. 检查文件是否存在
        if not self.file_path.exists():
            self.result.add_error(f"文件不存在: {self.file_path}")
            return self.result
        
        # 2. 读取文件内容
        try:
            self.content = self.file_path.read_text(encoding='utf-8')
        except Exception as e:
            self.result.add_error(f"无法读取文件: {e}")
            return self.result
        
        # 3. 验证文件名格式
        self._validate_filename()
        
        # 4. 解析和验证 front matter
        self._validate_front_matter()
        
        # 5. 验证 Markdown 内容
        self._validate_markdown()
        
        # 6. 额外的最佳实践检查
        self._validate_best_practices()
        
        return self.result
    
    def _validate_filename(self):
        """验证文件名格式"""
        filename = self.file_path.name
        
        # 检查文件名格式
        if not self.FILENAME_PATTERN.match(filename):
            self.result.add_error(
                f"文件名格式不正确。应为: YYYY-MM-DD-title.md，当前: {filename}"
            )
            return
        
        # 提取日期部分
        date_str = filename[:10]
        try:
            file_date = datetime.strptime(date_str, '%Y-%m-%d')
            self.result.add_info(f"文件名日期: {date_str}")
        except ValueError:
            self.result.add_error(f"文件名中的日期无效: {date_str}")
    
    def _validate_front_matter(self):
        """验证 YAML front matter"""
        # 检查是否有 front matter
        if not self.content.startswith('---'):
            self.result.add_error("缺少 YAML front matter（文件应以 '---' 开头）")
            return
        
        # 提取 front matter
        parts = self.content.split('---', 2)
        if len(parts) < 3:
            self.result.add_error("YAML front matter 格式不正确（缺少结束的 '---'）")
            return
        
        front_matter_str = parts[1]
        self.body = parts[2]
        
        # 解析 YAML
        try:
            self.front_matter = yaml.safe_load(front_matter_str)
            if self.front_matter is None:
                self.front_matter = {}
        except yaml.YAMLError as e:
            self.result.add_error(f"YAML 语法错误: {e}")
            return
        
        # 检查必需字段
        for field in self.REQUIRED_FIELDS:
            if field not in self.front_matter:
                self.result.add_error(f"缺少必需字段: {field}")
            elif not self.front_matter[field]:
                self.result.add_error(f"必需字段不能为空: {field}")
        
        # 验证特定字段
        self._validate_title()
        self._validate_layout()
        self._validate_date()
        self._validate_tags()
    
    def _validate_title(self):
        """验证标题"""
        if 'title' in self.front_matter:
            title = self.front_matter['title']
            if isinstance(title, str):
                if len(title.strip()) == 0:
                    self.result.add_error("标题不能为空字符串")
                elif len(title) > 200:
                    self.result.add_warning(f"标题过长 ({len(title)} 字符)，建议少于 200 字符")
                self.result.add_info(f"标题: {title}")
    
    def _validate_layout(self):
        """验证布局"""
        if 'layout' in self.front_matter:
            layout = self.front_matter['layout']
            if layout not in ['post', 'page', 'default']:
                self.result.add_warning(
                    f"布局 '{layout}' 不是常见值（post, page, default）"
                )
            self.result.add_info(f"布局: {layout}")
    
    def _validate_date(self):
        """验证日期"""
        if 'date' not in self.front_matter:
            return
        
        date_value = self.front_matter['date']
        
        # 尝试解析日期
        try:
            if isinstance(date_value, datetime):
                post_date = date_value
            elif isinstance(date_value, str):
                # 支持多种日期格式
                for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%Y-%m-%d %H:%M:%S %z']:
                    try:
                        post_date = datetime.strptime(date_value.strip(), fmt)
                        break
                    except ValueError:
                        continue
                else:
                    self.result.add_error(
                        f"日期格式不正确: {date_value}。"
                        f"建议格式: YYYY-MM-DD HH:MM:SS"
                    )
                    return
            else:
                self.result.add_error(f"日期类型不正确: {type(date_value)}")
                return
            
            self.result.add_info(f"文章日期: {post_date.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # 检查未来日期
            if post_date > datetime.now():
                self.result.add_warning(
                    f"文章日期是未来时间，可能不会立即显示"
                )
            
            # 检查文件名日期和 front matter 日期是否一致
            filename = self.file_path.name
            file_date_str = filename[:10]
            try:
                file_date = datetime.strptime(file_date_str, '%Y-%m-%d')
                if file_date.date() != post_date.date():
                    self.result.add_warning(
                        f"文件名日期 ({file_date_str}) 与 front matter 日期 "
                        f"({post_date.strftime('%Y-%m-%d')}) 不一致"
                    )
            except ValueError:
                pass
            
        except Exception as e:
            self.result.add_error(f"日期验证失败: {e}")
    
    def _validate_tags(self):
        """验证标签"""
        if 'tags' in self.front_matter:
            tags = self.front_matter['tags']
            if not isinstance(tags, list):
                self.result.add_error("tags 应该是一个列表")
            elif len(tags) == 0:
                self.result.add_warning("tags 列表为空")
            else:
                self.result.add_info(f"标签: {', '.join(str(t) for t in tags)}")
                
                # 检查标签格式
                for tag in tags:
                    if not isinstance(tag, str):
                        self.result.add_warning(f"标签应该是字符串: {tag}")
    
    def _validate_markdown(self):
        """验证 Markdown 内容"""
        if not self.body or not self.body.strip():
            self.result.add_warning("文章内容为空")
            return
        
        # 检查常见的 Markdown 问题
        lines = self.body.split('\n')
        
        # 统计内容
        word_count = len(self.body.split())
        self.result.add_info(f"字数统计: 约 {word_count} 词")
        
        # 检查代码块是否闭合
        code_block_count = self.body.count('```')
        if code_block_count % 2 != 0:
            self.result.add_error("代码块未正确闭合（``` 数量不匹配）")
        
        # 检查图片链接
        img_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
        images = img_pattern.findall(self.body)
        if images:
            self.result.add_info(f"找到 {len(images)} 个图片")
            for img in images:
                if img.startswith('http'):
                    continue  # 外部链接
                elif not img.startswith('/'):
                    self.result.add_warning(
                        f"图片路径建议使用绝对路径（以 / 开头）: {img}"
                    )
        
        # 检查链接
        link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
        links = link_pattern.findall(self.body)
        broken_links = [link for link in links if link.strip() == '']
        if broken_links:
            self.result.add_error(f"发现 {len(broken_links)} 个空链接")
    
    def _validate_best_practices(self):
        """验证最佳实践"""
        # 检查是否有描述/摘要
        if 'description' not in self.front_matter and 'excerpt' not in self.front_matter:
            self.result.add_info(
                "建议添加 'description' 或 'excerpt' 字段以改善 SEO"
            )
        
        # 检查是否有分类
        if 'categories' not in self.front_matter and 'category' not in self.front_matter:
            self.result.add_info("建议添加 'categories' 字段以组织文章")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='验证 Jekyll markdown 文件格式',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s _posts/2025-01-01-example.md
  %(prog)s _posts/*.md
  %(prog)s --strict _posts/2025-01-01-example.md
        """
    )
    parser.add_argument(
        'files',
        nargs='+',
        help='要验证的 markdown 文件路径'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='严格模式：警告也视为错误'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='安静模式：只显示错误'
    )
    
    args = parser.parse_args()
    
    # 展开通配符
    from glob import glob
    all_files = []
    for pattern in args.files:
        matched = glob(pattern)
        if matched:
            all_files.extend(matched)
        else:
            all_files.append(pattern)
    
    if not all_files:
        print(f"{Colors.RED}错误: 没有找到要验证的文件{Colors.RESET}")
        sys.exit(1)
    
    # 验证所有文件
    results = []
    for file_path in all_files:
        validator = JekyllPostValidator(file_path)
        result = validator.validate()
        results.append(result)
        
        if not args.quiet:
            result.print_result()
    
    # 汇总结果
    total = len(results)
    passed = sum(1 for r in results if r.is_valid())
    failed = total - passed
    
    print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}验证汇总{Colors.RESET}")
    print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
    print(f"总文件数: {total}")
    print(f"{Colors.GREEN}通过: {passed}{Colors.RESET}")
    print(f"{Colors.RED}失败: {failed}{Colors.RESET}")
    
    # 严格模式检查
    if args.strict:
        has_warnings = any(len(r.warnings) > 0 for r in results)
        if has_warnings:
            print(f"\n{Colors.YELLOW}严格模式：发现警告，退出码为 1{Colors.RESET}")
            sys.exit(1)
    
    # 返回退出码
    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()
