
from .JsonLoadUtils import JsonLoadUtils
from utils import logUtils
from tabulate import tabulate

""" 
获取关于信息
"""


def get_about_list():
    """ 获取所有关于信息列表 """
    json_load = JsonLoadUtils()
    return json_load.get_all_data()


def _extract_format_table():
    """ 提炼数据然后用tabulate格式化 """
    json_load = JsonLoadUtils()
    name = json_load.get_data('name')
    version = json_load.get_data('version')
    description = json_load.get_data('description')
    author = json_load.get_data('author')
    license = json_load.get_data('license')
    author_url = json_load.get_data('author_url')
    email = json_load.get_data('email')
    repo = json_load.get_data('repo')
    git = json_load.get_data('git')
    theme = json_load.get_data('style', 'theme')

    table = [
        ["Name", name],
        ["Version", version],
        ["Description", description],
        ["Author", author],
        ["License", license],
        ["Author URL", author_url],
        ["Email", email],
        ["Repo", repo],
        ["Git", git],
        ["Theme", theme]
    ]

    return table


def print_about_table():
    table = _extract_format_table()
    logUtils.logging_no_print("关于信息正在输出...")
    print(tabulate(table, tablefmt="fancy_grid"))
