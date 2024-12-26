import paramiko
from tqdm import tqdm
from database.db import save_password, get_password, get_server_list, record_login
from utils import logUtils
from utils.encryption import decrypt_password
import os
import select
import sys
from colorama import Fore, Back, Style
from styles import cut_line
from tabulate import tabulate

# 检测操作系统类型
IS_WINDOWS = sys.platform.startswith('win')

if not IS_WINDOWS:
    import pty
    import termios
    import tty
    import struct
    import fcntl
else:
    # Windows系统需要使用的模块
    import msvcrt


def connect_to_server(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    return client


def execute_command(client, command):
    try:
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        if error:
            logUtils.logging_and_print_error(f"错误: {error}")
        if output:
            logUtils.logging_and_print(output)
    except Exception as e:
        logUtils.logging_and_print_error(f"执行命令时出错: {str(e)}")


def start_session(client):
    try:
        # 获取远程 shell 通道
        channel = client.invoke_shell()

        if IS_WINDOWS:
            _windows_shell(channel)
        else:
            _unix_shell(channel)

    except KeyboardInterrupt:
        logUtils.logging_no_print("SSH连接已被用户中断")
    except paramiko.SSHException as ssh_ex:
        logUtils.logging_no_print_error(f"SSH 异常: {str(ssh_ex)}")
    except OSError as os_ex:
        logUtils.logging_no_print_error(f"网络异常: {str(os_ex)}")
    except Exception as e:
        logUtils.logging_no_print_error(f"会话错误: {str(e)}")
    finally:
        client.close()
        print("\n")
        cut_line.cut_line_msg("end")
        logUtils.logging_no_print("已退出SSH会话")
def _windows_shell(channel):
    try:
        # 设置终端环境变量 (解决切换bash的时候回话标头乱码的问题)
        channel.send('export TERM=xterm-256color\n')
        channel.send('export LC_ALL=en_US.UTF-8\n')
        channel.send('export LANG=en_US.UTF-8\n')

        while True:
            if channel.recv_ready():
                data = channel.recv(1024)
                try:
                    # 使用 utf-8 解码，忽略无法解码的字符
                    sys.stdout.buffer.write(data)
                    sys.stdout.buffer.flush()
                except UnicodeDecodeError:
                    # 如果解码失败，直接输出原始字节
                    sys.stdout.buffer.write(data)
                    sys.stdout.buffer.flush()

            if msvcrt.kbhit():
                char = msvcrt.getch()
                channel.send(char)

            if channel.exit_status_ready():
                break
    except Exception as e:
        logUtils.logging_and_print_error(f"会话错误: {str(e)}")


def _unix_shell(channel):
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        channel.settimeout(0.0)

        # 原来的Unix系统相关的代码
        term_size = struct.pack('HHHH', 0, 0, 0, 0)
        term_size = fcntl.ioctl(sys.stdout.fileno(),
                                termios.TIOCGWINSZ, term_size)
        channel.resize_pty(*struct.unpack('HHHH', term_size))

        while True:
            r, w, e = select.select([channel, sys.stdin], [], [])
            if channel in r:
                try:
                    x = channel.recv(1024)
                    if len(x) == 0:
                        break
                    sys.stdout.write(x.decode())
                    sys.stdout.flush()
                except Exception:
                    break
            if sys.stdin in r:
                x = sys.stdin.read(1)
                if len(x) == 0:
                    break
                channel.send(x)
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


def display_server_list():
    servers = get_server_list()
    if servers:
        # 普通格式列表 ------------start-------------
        # cut_line.cut_line() # 分割线
        # for idx, (host, username, login_count, last_login) in enumerate(servers, 1):
        #     print(
        #         f"{idx:<6}{host:<20}{username:<16}{login_count:<10}{last_login or '从未登录'}")
        # cut_line.cut_line() # 分割线
        # 普通格式列表 ------------end---------------
        
        # 使用了表格格式 ----------start-------------
        table = []
        for idx, (host, username, login_count, last_login) in enumerate(servers, 1):
            table.append([idx, host, username, login_count, last_login or '从未登录'])
        
        headers = ["序号", "主机地址", "用户名", "登录次数", "最后登录时间"]
        print(tabulate(table, headers, tablefmt="fancy_grid"))
        # 使用了表格格式 ----------end---------------
        try:
            choice = input("\n请选择服务器序号 (或按Enter手动输入新服务器): ")
            if choice.strip():
                idx = int(choice) - 1
                if 0 <= idx < len(servers):
                    logUtils.logging_no_print(f"已选择服务器序号: {idx+1}")
                    return servers[idx][0], servers[idx][1]
        except ValueError:
            pass

    return None, None


def login_to_server():
    try:
        # 显示服务器列表并获取选择
        selected_host, selected_username = display_server_list()

        # 如果没有选择已有服务器，要求手动输入
        host = selected_host or input("输入服务器地址: ")
        username = selected_username or input("输入用户名: ")

        # 尝试从数据库获取保存的密码
        saved_password = get_password(host, username)
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if saved_password:
            try:
                logUtils.logging_and_print("使用已保存的密码尝试连接...")
                client.connect(hostname=host, username=username,
                               password=saved_password)
                logUtils.logging_and_print("登录成功!")
                save_password(host, username, saved_password)
                logUtils.logging_and_print("已经将密码更新到数据库")
                return client,host,username
            except Exception as e:
                logUtils.logging_and_print_error(f"使用保存的密码登录失败: {str(e)}")
                password = input("请输入新的密码: ")
        else:
            password = input("请输入密码: ")

        try:
            client.connect(hostname=host, username=username, password=password)
            logUtils.logging_and_print("登录成功!")
            save_password(host, username, password)  # 保存新密码和登录记录
            return client,host,username
        except Exception as e:
            logUtils.logging_and_print_error(f"登录失败: {str(e)}")
            return None,None,None

    except KeyboardInterrupt:
        print("\n")
        cut_line.cut_line_msg("end")
        logUtils.logging_no_print("程序已被用户中断")
        return None,None,None


def upload_file(file_path):
    host = input("Enter the server host: ")
    username = input("Enter your username: ")
    password = get_password(host, username)

    if not password:
        password = input("Enter your password: ")
        save_password(host, username, password)

    try:
        client = connect_to_server(host, username, password)

        sftp = client.open_sftp()
        remote_path = input("Enter the remote path to upload the file: ")
        with tqdm(total=100, desc="Uploading", unit="%", ncols=100) as pbar:
            sftp.put(file_path, remote_path)
            pbar.update(100)

        sftp.close()
        client.close()
        print("File uploaded successfully!")
    except Exception as e:
        print(f"Failed to upload file: {e}")


def download_file(file_path):
    host = input("Enter the server host: ")
    username = input("Enter your username: ")
    password = get_password(host, username)

    if not password:
        password = input("Enter your password: ")
        save_password(host, username, password)

    try:
        client = connect_to_server(host, username, password)

        sftp = client.open_sftp()
        local_path = input("Enter the local path to save the file: ")
        with tqdm(total=100, desc="Downloading", unit="%", ncols=100) as pbar:
            sftp.get(file_path, local_path)
            pbar.update(100)

        sftp.close()
        client.close()
        print("File downloaded successfully!")
    except Exception as e:
        print(f"Failed to download file: {e}")
