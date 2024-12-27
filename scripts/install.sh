#!/bin/bash

echo "SSHShark 安装程序"

# 询问用户安装目录
read -p "请输入安装目录 (默认 /usr/local/SSHShark): " INSTALL_DIR
INSTALL_DIR=${INSTALL_DIR:-/usr/local/SSHShark}

# 创建安装目录
if [ ! -d "$INSTALL_DIR" ]; then
    mkdir -p "$INSTALL_DIR"
fi

# 复制文件到安装目录
echo "正在复制文件到 $INSTALL_DIR ..."
cp -r ./* "$INSTALL_DIR"

# 设置环境变量
echo "将 sshsk.sh 添加到环境变量以便在任何地方使用"
read -p "是否将 SSHShark 添加到 shell 环境变量中? (Y/N): " ENV_PATH
if [[ "$ENV_PATH" =~ ^[Yy]$ ]]; then
    # 检查用户使用的 shell 类型
    SHELL_TYPE=$(basename "$SHELL")
    
    case "$SHELL_TYPE" in
        bash)
            echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.bashrc
            source ~/.bashrc
            ;;
        zsh)
            echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.zshrc
            source ~/.zshrc
            ;;
        fish)
            echo "set -Ux PATH $INSTALL_DIR \$PATH" >> ~/.config/fish/config.fish
            ;;
        *)
            echo "不支持的 shell 类型: $SHELL_TYPE"
            ;;
    esac
    echo "SSHShark 已成功添加到 shell 环境变量中"
fi

echo "安装完成!"
