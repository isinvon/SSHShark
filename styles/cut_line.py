from colorama import Style

from styles.Theme import Theme


def cut_line():
    """ 分割线 """
    print(Theme.get_theme() + Style.BRIGHT + "═" * 78 + Style.RESET_ALL)


def cut_line_msg(msg):
    """ 文本居中分割线 """
    msg_length = len(msg)
    side_length = (78 - msg_length) // 2
    print(Theme.get_theme() + Style.BRIGHT + "═" * side_length +
          " " + msg + " " + "═" * side_length + Style.RESET_ALL)
