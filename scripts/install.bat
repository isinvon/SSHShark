@echo off
echo SSHShark 安装程序

:: 询问用户安装路径
set /p INSTALL_DIR="请输入安装目录 (默认 C:\Program Files\SSHShark): "
if "%INSTALL_DIR%"=="" set INSTALL_DIR="C:\Program Files\SSHShark"

:: 创建安装目录
if not exist "%INSTALL_DIR%" (
    mkdir "%INSTALL_DIR%"
)

:: 复制文件到安装目录
echo 正在复制文件到 %INSTALL_DIR% ...
xcopy /E /I /H . "%INSTALL_DIR%\"

:: 设置环境变量（添加到系统环境变量）
echo 将 sshsk.bat 添加到系统路径中以便在任何地方使用
set /p ENV_PATH="是否将 SSHShark 添加到系统环境变量中? (Y/N): "
if /I "%ENV_PATH%"=="Y" (
    setx PATH "%PATH%;%INSTALL_DIR%"
    echo SSHShark 已添加到系统环境变量
)

echo 安装完成!
pause
