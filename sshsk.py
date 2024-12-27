import argparse
from database.db import record_login
from ssh_client.client import login_to_server, download_file, start_session, upload_file_with_selection
from developer_only.author import init
from styles import cut_line
import curses
from utils import aboutUtils, changeThemeUtils, viewLogUtils


def main():
    parser = argparse.ArgumentParser(description='SSHShark - 一个友好的SSH客户端工具')
    
    # 添加参数解析逻辑
    parser.add_argument('--login', action='store_true', help='登录到服务器')
    # parser.add_argument('--upload', type=str, help='上传文件到服务器')
    parser.add_argument('--upload', action='store_true', help='上传文件到服务器')
    parser.add_argument('--download', type=str, help='从服务器下载文件')
    parser.add_argument('--log', action='store_true', help='显示日志')
    parser.add_argument('--theme', action='store_true', help='切换主题')
    parser.add_argument('--about', action='store_true', help='关于信息')
    
    args = parser.parse_args()
    
    if args.login:  # 登录
        client,host,username = login_to_server()
        if client:
            record_login(host=host,username=username)
            cut_line.cut_line()
            start_session(client)
    elif args.upload:  # 上传
        # upload_file(args.upload)
        upload_file_with_selection()
    elif args.download:  # 下载
        download_file(args.download)
    elif args.log:  # 显示日志
        cut_line.cut_line()
        curses.wrapper(viewLogUtils.display_log)  # 使用 curses.wrapper 执行日志查看功能
        cut_line.cut_line()
    elif args.theme:
        cut_line.cut_line()
        changeThemeUtils.list_theme_and_select()
        cut_line.cut_line()
    elif args.about:  # 显示关于
        aboutUtils.print_about_table()
    else:  # 显示帮助
        parser.print_help()


if __name__ == '__main__':
    # init()  # 开发者初始化(用户名非sinvon的用户不执行)
    main()
