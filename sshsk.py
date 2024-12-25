import argparse
from ssh_client.client import login_to_server, upload_file, download_file, start_session
from developer_only.author import init



def main():
    parser = argparse.ArgumentParser(description='SSHShark - 一个友好的SSH客户端工具')
    
    # 添加参数解析逻辑
    parser.add_argument('--login', action='store_true', help='登录到服务器')
    parser.add_argument('--upload', type=str, help='上传文件到服务器')
    parser.add_argument('--download', type=str, help='从服务器下载文件')
    
    args = parser.parse_args()
    
    if args.login:  # 登录
        client = login_to_server()
        if client:
            start_session(client)
    elif args.upload:  # 上传
        upload_file(args.upload)
    elif args.download:  # 下载
        download_file(args.download)
    else:  # 显示帮助
        parser.print_help()


if __name__ == '__main__':
    # init()  # 开发者初始化(用户名非sinvon的用户不执行)
    main()
