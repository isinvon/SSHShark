from enum import Enum

from colorama import Fore


class Theme(Enum):
    """ 主题颜色 """

    # background
    black_back = Fore.BLACK  # \033[40m
    red_back = Fore.RED  # \033[41m
    green_back = Fore.GREEN  # \033[42m
    yellow_back = Fore.YELLOW  # \033[43m
    blue_back = Fore.BLUE  # \033[44m
    magenta_back = Fore.MAGENTA  # \033[45m
    cyan_back = Fore.CYAN  # \033[46m
    white_back = Fore.WHITE  # \033[47m

    # background - height light
    lightblack_back = Fore.LIGHTBLACK_EX  # \033[100m
    lightred_back = Fore.LIGHTRED_EX  # \033[101m
    lightgreen_back = Fore.LIGHTGREEN_EX  # \033[102m
    lightyellow_back = Fore.LIGHTYELLOW_EX  # \033[103m
    lightblue_back = Fore.LIGHTBLUE_EX  # \033[104m
    lightmagenta_back = Fore.LIGHTMAGENTA_EX  # \033[105m
    lightcyan_back = Fore.LIGHTCYAN_EX  # \033[106m
    lightwhite_back = Fore.LIGHTWHITE_EX  # \033[107m

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
