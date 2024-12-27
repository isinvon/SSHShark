#!/bin/bash
# SSHShark - Linux/MacOS 启动脚本

# 设置 Python 环境（如果有虚拟环境，替换路径）
PYTHON_PATH="python3"

# 检查是否传递了参数
if [ "$#" -eq 0 ]; then
    echo "请传入参数运行 SSHShark"
    echo "例如: ./sshsk.sh --login"
    exit 1
fi

# 执行 Python 主脚本
$PYTHON_PATH sshsk.py "$@"
