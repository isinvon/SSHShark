# logUtils.py
import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

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
        handler = TimedRotatingFileHandler(log_file_path, when='midnight', interval=1, backupCount=30)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # 将处理器添加到日志记录器
        logger.addHandler(handler)

    return logger

# -----------------------------------------------------


def logging_and_print(message):
    logger = setup_logger()
    logger.info(message)
    print(message)
    
def logging_and_print_error(message):
    logger = setup_logger()
    logger.error(message)
    print(message)
    
def logging_and_print_warning(message):
    logger = setup_logger()
    logger.warning(message)
    print(message)

# --------------------------------------------------

def logging_no_print(message):
    logger = setup_logger()
    logger.info(message)
    
def logging_no_print_error(message):
    logger = setup_logger()
    logger.error(message)
    
def logging_no_print_warning(message):
    logger = setup_logger()
    logger.warning(message)