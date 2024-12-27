@echo off
echo SSHShark 卸载程序

:: 删除 SSHShark 文件
set /p INSTALL_DIR="请输入安装目录 (默认 C:\Program Files\SSHShark): "
if "%INSTALL_DIR%"=="" set INSTALL_DIR="C:\Program Files\SSHShark"

:: 删除目录中的所有文件
echo 正在删除 %INSTALL_DIR% 中的文件...
rmdir /S /Q "%INSTALL_DIR%"

:: 删除环境变量中的路径
echo 删除系统环境变量中的 SSHShark 路径...
setx PATH "%PATH:;C:\Program Files\SSHShark=%"

echo 卸载完成!
pause
