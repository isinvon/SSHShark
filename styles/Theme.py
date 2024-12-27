from enum import Enum

from colorama import Fore


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
    white = Fore.WHITE  # \033[47m

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

# if __name__ == '__main__':
    # theme = Theme
    # 获取所有枚举名称
    # print(theme.get_names())
