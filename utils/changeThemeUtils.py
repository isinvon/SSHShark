
from styles.Theme import Theme
from utils import logUtils
from utils.JsonLoadUtils import JsonLoadUtils

""" 颜色主题切换 """

def _update_theme(new_theme: str) -> None:
    """ 切换主题色 """
    if new_theme not in Theme.get_names():
        print(f"无效的主题 : {new_theme}")
        return
    json_load = JsonLoadUtils()
    # 更新配置文件
    json_load.update_data(
        {
            "style": {
                "theme": new_theme
            }
        }
    )
    # 保存修改后的数据(不调用save的话不会保存修改)
    json_load.save(json_load.data)
    logUtils.logging_and_print(f"主题已被切换为 {new_theme}")




def list_theme_and_select():
    """ 列出所有主题色 """
    list = Theme.get_names()
    for index, theme in enumerate(list, start=1):
        print(f"{index}. {theme}")
    # 选择主题色
    selected_index = int(
        input("请选择要使用的主题色编号: "))
    # 获取并更新
    selected_theme = list[selected_index - 1]
    # 更新主题色
    _update_theme(new_theme=selected_theme)
