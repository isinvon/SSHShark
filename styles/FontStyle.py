from enum import Enum

from colorama import Style


class FontStyle(Enum):
    """ 字体样式 """

    # font style
    bright = Style.BRIGHT  # \033[1m
    dim = Style.DIM  # \033[2m
    normal = Style.NORMAL  # \033[22m

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
