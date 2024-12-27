import os
import shutil
import sys
import getpass
import platform

def remove_from_env(install_dir):
    """ 从系统环境变量中移除指定的路径 """
    try:
        current_platform = platform.system()
        if current_platform == "Windows":
            # Windows 系统环境变量移除
            path = os.getenv('PATH', '')
            if install_dir in path:
                new_path = path.replace(install_dir + ";", "").replace(install_dir, "")
                os.system(f'setx PATH "{new_path}"')
                print(f"已从系统环境变量中移除 {install_dir}.")
            else:
                print("没有找到安装目录在系统环境变量中.")
        else:
            # UNIX 系统环境变量移除
            home_dir = os.path.expanduser("~")
            shell_config_files = [".bashrc", ".zshrc", ".bash_profile", ".profile"]
            
            for shell_config_file in shell_config_files:
                config_path = os.path.join(home_dir, shell_config_file)
                if os.path.exists(config_path):
                    with open(config_path, "r") as f:
                        lines = f.readlines()
                    with open(config_path, "w") as f:
                        for line in lines:
                            if install_dir not in line:
                                f.write(line)
                    print(f"已从 {shell_config_file} 中移除 {install_dir}.")
                    break
            else:
                print("未找到适用的 shell 配置文件.")
    except Exception as e:
        print(f"无法移除环境变量: {e}")

def delete_directory(install_dir):
    """ 删除指定目录及其所有内容 """
    if os.path.exists(install_dir):
        try:
            shutil.rmtree(install_dir)  # 递归删除目录
            print(f"已删除目录 {install_dir}.")
        except PermissionError:
            print(f"删除目录时发生权限错误: {install_dir}，请尝试使用 sudo 权限。")
            sys.exit(1)
        except Exception as e:
            print(f"删除目录时发生错误: {e}")
            sys.exit(1)
    else:
        print("指定的目录不存在.")

def main():
    """ 主程序，卸载 SSHShark """
    username = getpass.getuser()
    
    current_platform = platform.system()
    
    # 设置默认卸载路径
    if current_platform == "Windows":
        default_install_dir = f"C:\\Users\\{username}\\SSHShark"
    else:
        default_install_dir = f"/home/{username}/SSHShark"  # UNIX 系统默认路径
    
    print("正在运行卸载程序...")
    print("SSHShark 卸载程序")

    # 获取用户输入的卸载目录
    uninstall_dir = input(f"请输入要卸载的目录 (默认 {default_install_dir}): ").strip()
    
    # 如果用户没有输入，使用默认路径
    if not uninstall_dir:
        uninstall_dir = default_install_dir
    
    # 确认删除目录
    confirm = input(f"确认要卸载 SSHShark 并删除目录 {uninstall_dir} 吗？(Y/N): ").strip().lower()
    if confirm == 'y':
        delete_directory(uninstall_dir)
        # 删除环境变量中的路径
        remove_from_env(uninstall_dir)
        print("卸载完成!")
    else:
        print("卸载已取消.")
    
    input("请按任意键继续...")

if __name__ == '__main__':
    main()
