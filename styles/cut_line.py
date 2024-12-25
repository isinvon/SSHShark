from colorama import Fore, Back, Style


def cut_line():
    """ 分割线 """
    print(Fore.WHITE + Style.BRIGHT + "-" * 75 + Style.RESET_ALL)
