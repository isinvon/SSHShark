from enum import Enum

from colorama import Fore

from utils.JsonLoadUtils import JsonLoadUtils


class Theme(Enum):
    """ 主题颜色 """

    # background
    black = Fore.BLACK  # \033[40m
    red = Fore.RED  # \033[41m
    green = Fore.GREEN  # \033[42m
    yellow = Fore.YELLOW  # \033[43m
    blue = Fore.BLUE  # \033[44m
    magenta = Fore.MAGENTA  # \033[45m
    cyan = Fore.CYAN  # \033[46m
    white = Fore.RESET  # 由于Fore.WHITE和Fore.LIGHTWHITE_EX效果相同, 所以使用Fore.RESET代替作为默认的主题颜色

    # background - height light
    lightblack = Fore.LIGHTBLACK_EX  # \033[100m
    lightred = Fore.LIGHTRED_EX  # \033[101m
    lightgreen = Fore.LIGHTGREEN_EX  # \033[102m
    lightyellow = Fore.LIGHTYELLOW_EX  # \033[103m
    lightblue = Fore.LIGHTBLUE_EX  # \033[104m
    lightmagenta = Fore.LIGHTMAGENTA_EX  # \033[105m
    lightcyan = Fore.LIGHTCYAN_EX  # \033[106m
    lightwhite = Fore.LIGHTWHITE_EX  # \033[107m

    def __str__(self) -> str:
        return self.value

    @classmethod
    def get_names(cls) -> list[str]:
        """ 获取所有枚举名称 """
        return [member.name for member in cls]

    @classmethod
    def get_values(cls) -> list[str]:
        """ 获取所有枚举值 """
        return [member.value for member in cls]

    @classmethod
    def get_theme(cls):
        """ 获取主题颜色 """
        theme_name = cls._read_config_file()
        for member in cls:
            if member.name == theme_name:
                return member.value
        return Fore.RESET  # 如果找不到匹配项，则返回默认值

    @staticmethod
    def _read_config_file() -> str:
        """ 从配置文件中读取主题颜色 """
        # 注意：这里需要确保JsonLoadUtils已经正确定义并且可以导入。
        json_load = JsonLoadUtils()
        theme = json_load.get_data('style', 'theme')
        return theme

    @classmethod
    def fore_reset(cls):
        """ 临时重置颜色 """
        return Fore.RESET
