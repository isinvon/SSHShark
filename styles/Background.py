from enum import Enum
from colorama import Back


class Background(Enum):
    """ 背景颜色 """
    # --------------- 枚举右边需要多个参数的时候开启 ---------start--------
    # def __new__(cls, *args, **kwds):
    #     obj = object.__new__(cls)
    #     obj._value_ = args[0]
    #     return obj

    # def __init__(self, value, type, color, price):
    #     self.type = type
    #     self.color = color
    #     self.price = price
    # --------------- 枚举右边需要多个参数的时候开启 ----------end--------

    # background
    black_back = Back.BLACK  # \033[40m
    red_back = Back.RED  # \033[41m
    green_back = Back.GREEN  # \033[42m
    yellow_back = Back.YELLOW  # \033[43m
    blue_back = Back.BLUE  # \033[44m
    magenta_back = Back.MAGENTA  # \033[45m
    cyan_back = Back.CYAN  # \033[46m
    white_back = Back.WHITE  # \033[47m

    # background - height light
    lightblack_back = Back.LIGHTBLACK_EX  # \033[100m
    lightred_back = Back.LIGHTRED_EX  # \033[101m
    lightgreen_back = Back.LIGHTGREEN_EX  # \033[102m
    lightyellow_back = Back.LIGHTYELLOW_EX  # \033[103m
    lightblue_back = Back.LIGHTBLUE_EX  # \033[104m
    lightmagenta_back = Back.LIGHTMAGENTA_EX  # \033[105m
    lightcyan_back = Back.LIGHTCYAN_EX  # \033[106m
    lightwhite_back = Back.LIGHTWHITE_EX  # \033[107m

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
    # theme = Background
    # 获取所有枚举名称
    # print(theme.get_names())
    # 获取所有枚举值
    # print(theme.get_values())
    
