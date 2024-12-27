#!/bin/bash

echo "SSHShark 卸载程序"

# 询问用户安装目录
read -p "请输入安装目录 (默认 /usr/local/SSHShark): " INSTALL_DIR
INSTALL_DIR=${INSTALL_DIR:-/usr/local/SSHShark}

# 删除安装目录中的文件
echo "正在删除 $INSTALL_DIR 中的文件..."
rm -rf "$INSTALL_DIR"

# 删除环境变量中的路径
echo "从环境变量中删除 SSHShark 路径..."
SHELL_TYPE=$(basename "$SHELL")
case "$SHELL_TYPE" in
    bash)
        sed -i '/SSHShark/d' ~/.bashrc
        source ~/.bashrc
        ;;
    zsh)
        sed -i '/SSHShark/d' ~/.zshrc
        source ~/.zshrc
        ;;
    fish)
        sed -i '/SSHShark/d' ~/.config/fish/config.fish
        ;;
    *)
        echo "不支持的 shell 类型: $SHELL_TYPE"
        ;;
esac

echo "卸载完成!"
