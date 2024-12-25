import os


def get_username():
    """ 获取当前用户名 """
    try:
        # 尝试使用 os.getlogin() 获取用户名
        return os.getlogin()
    except OSError:
        # 如果 os.getlogin() 失败（例如在某些情况下它可能无法正确工作），我们可以尝试从环境变量中获取
        return os.getenv('USERNAME') or os.getenv('USER')


def install_and_import_pretty_errors():
    """ 安装python开发环境报错美化工具 """
    if 'pretty_errors' in globals():  # 如果已经导入了pretty_errors，则直接返回
        return
    # 执行命令
    os.system('pip install pretty_errors')
    # 启动工具
    os.system('python - m pretty_errors')
    try:
        import pretty_errors
    except ImportError:
        print('pretty_errors 安装失败，请手动安装pretty_errors')


def init():
    """ 初始化 """
    username = get_username()
    if username == 'sinvon':  # 仅对本项目的开发者sinvon<2021469084@qq.com>开启错误美化工具
        install_and_import_pretty_errors()
