from colorama import Fore, Back, Style


def cut_line():
    """ 分割线 """
    print(Fore.WHITE + Style.BRIGHT + "═" * 78 + Style.RESET_ALL)


def cut_line_msg(msg):
    """ 文本居中分割线 """
    msg_length = len(msg)
    side_length = (78 - msg_length) // 2
    print(Fore.WHITE + Style.BRIGHT + "═" * side_length + " " + msg + " " + "═" * side_length + Style.RESET_ALL)
