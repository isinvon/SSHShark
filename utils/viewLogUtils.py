import curses
import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

from rich.console import Console
from rich.table import Table

logger = None


def setup_logger():
    global logger
    if logger is not None:
        return logger

    # 获取当前日期
    current_date = datetime.now()
    year_month = current_date.strftime('%Y-%m')
    year_month_day = current_date.strftime('%Y-%m-%d')

    # 创建日志文件夹
    log_folder = os.path.join('logs', year_month)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # 日志文件路径
    log_file_path = os.path.join(log_folder, f'{year_month_day}.log')

    # 配置日志记录器
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 检查是否已有处理器
    if not logger.handlers:
        # 创建TimedRotatingFileHandler
        handler = TimedRotatingFileHandler(
            log_file_path, when='midnight', interval=1, backupCount=30)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        logger.addHandler(handler)

    return logger


def display_log(stdscr):
    setup_logger()
    log_folder = os.path.join('logs', datetime.now().strftime('%Y-%m'))
    log_file_path = os.path.join(
        log_folder, f'{datetime.now().strftime("%Y-%m-%d")}.log')

    if not os.path.exists(log_file_path):
        stdscr.addstr("日志文件不存在\n")
        stdscr.refresh()
        stdscr.getch()
        return

    # 打开日志文件
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    # 设置窗口和日志分页
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    page_size = height - 1  # 留一个空行给退出提示
    start_line = 0

    while True:
        stdscr.clear()

        # 显示当前页的日志
        for i in range(start_line, min(start_line + page_size, len(lines))):
            stdscr.addstr(i - start_line, 0, lines[i])

        stdscr.refresh()

        # 用户输入
        key = stdscr.getch()

        # 按键处理
        if key == curses.KEY_UP and start_line > 0:  # 上键，向上翻页
            start_line -= 1
        # 下键，向下翻页
        elif key == curses.KEY_DOWN and start_line < len(lines) - page_size:
            start_line += 1
        elif key == curses.KEY_RIGHT:  # 右键，水平滚动
            # 需要进一步处理日志行的内容宽度，以进行水平滚动
            stdscr.addstr(f"按键 {key} 左右键滚动 - 还未实现水平滚动！")
        elif key == ord('q'):  # 按下q退出
            break
