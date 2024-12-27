import os
import shutil
import sys
import getpass
import platform

def copy_files(src_dir, dest_dir):
    """
    复制文件并排除 .git 文件夹
    """
    # 如果目标目录不存在，创建它
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # 复制文件
    for item in os.listdir(src_dir):
        s = os.path.join(src_dir, item)
        d = os.path.join(dest_dir, item)
        
        # 排除 .git 文件夹
        if '.git' in s:
            continue

        if os.path.isdir(s):
            shutil.copytree(s, d, ignore=shutil.ignore_patterns('.git'))
        else:
            shutil.copy2(s, d)

def main():
    """
    主函数：安装 SSHShark
    """
    # 获取当前用户的用户名
    username = getpass.getuser()

    # 判断操作系统
    current_platform = platform.system()
    
    # 设置默认安装路径
    if current_platform == "Windows":
        default_install_dir = f"C:\\Users\\{username}\\SSHShark"
    else:
        default_install_dir = f"/home/{username}/SSHShark"  # 默认路径在 UNIX 系统下
    
    print("正在运行安装程序...")
    print("SSHShark 安装程序")
    
    # 获取用户输入的安装目录
    install_dir = input(f"请输入安装目录 (默认 {default_install_dir}): ").strip()
    
    # 如果用户没有输入，使用默认路径
    if not install_dir:
        install_dir = default_install_dir
    
    # 创建目标目录
    print(f"正在创建目录 {install_dir} ...")
    
    try:
        copy_files(os.getcwd(), install_dir)
    except PermissionError:
        print(f"错误: 无权限将文件写入 {install_dir}. 请确保您有写权限，或者选择一个其他目录.")
        sys.exit(1)
    
    print(f"文件已成功安装到 {install_dir}.")

    # 提示用户是否添加到环境变量
    add_to_env = input("是否将 SSHShark 添加到系统环境变量中? (Y/N): ").strip().lower()
    
    if add_to_env == "y":
        if current_platform == "Windows":
            # 添加 sshsk.bat 到 Windows 系统环境变量
            os.system(f'setx PATH "%PATH%;{install_dir}"')
            print("SSHShark 已添加到系统环境变量.")
        else:
            # 提示用户手动编辑 shell 配置文件以设置 PATH
            print("请手动将以下行添加到您的 shell 配置文件 (例如 ~/.bashrc, ~/.zshrc):")
            print(f'export PATH="{install_dir}:$PATH"')
            print("修改完成后请重新加载配置文件或重启终端以生效.")
    
    print("安装完成!")
    input("请按任意键继续...")

if __name__ == '__main__':
    main()
