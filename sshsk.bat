@echo off
rem SSHShark - Windows 启动脚本

rem 设置 Python 环境（如果有虚拟环境，替换路径）
set PYTHON_PATH=python

rem 检查是否传递了参数
if "%~1"=="" (
    echo 请传入参数运行 SSHShark
    echo 例如: sshsk.bat --login
    goto end
)

rem 执行 Python 主脚本
%PYTHON_PATH% sshsk.py %*

:end
pause
