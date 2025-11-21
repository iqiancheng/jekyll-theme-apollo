#!/bin/bash
# Jekyll 文章验证便捷脚本
# 自动激活虚拟环境并运行验证

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# 检查虚拟环境是否存在
if [ ! -d ".venv" ]; then
    echo "🔧 首次运行，创建虚拟环境..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -q pyyaml
    echo "✅ 虚拟环境创建完成"
else
    source .venv/bin/activate
fi

# 运行验证
python validate_post.py "$@"
