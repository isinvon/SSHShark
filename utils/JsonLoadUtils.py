import json
from typing import Any, Dict, List, Union
import os

class JsonLoadUtils:
    def __init__(self, file_path: str = 'config/config.json'):
        """
        初始化JsonLoader类并自动加载JSON文件内容。
        
        :param file_path: JSON 文件路径，默认为 'config/config.json'
        """
        self.file_path = file_path
        self.data = None  # 用于存储加载的数据
        
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        
        # 在初始化时自动加载数据
        self.load()

    def load(self) -> Union[Dict, List]:
        """
        加载并解析JSON文件内容到Python对象（字典或列表）。
        
        :return: 解析后的Python对象
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return self.data
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON from {self.file_path}. Details: {e}")
        except Exception as e:
            raise e
        
    def get_all_data(self) -> Union[Dict, List]:
        """Get all data from the JSON file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return self.data
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to decode JSON from {self.file_path}. Details: {e}")
        except Exception as e:
            raise e
    
    def save(self, data: Any, indent: int = 4, ensure_ascii: bool = False) -> None:
        """
        将Python对象保存为JSON格式到文件中。
        
        :param data: 要保存的数据（字典或列表）
        :param indent: 缩进级别，默认4个空格
        :param ensure_ascii: 是否确保ASCII编码，默认False
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=indent, ensure_ascii=ensure_ascii)
        except Exception as e:
            raise e
    
    def get_data(self, *keys: str) -> Any:
        """
        获取当前加载的数据。如果传入了键，则返回对应嵌套字典中的值。
        
        :param keys: 可选的键路径，用于获取嵌套字典中的值
        :return: 当前加载的数据（字典或列表），或根据键路径获取的值
        
        例如：
        >>> json_load.get_data('key1', 'key2')
        
        示例:
        >>> 有这么一个文件中的json数据
            {
                "key1": {
                    "key2": "value"
                }
            }
        
            json_load = JsonLoadUtils()
            json_load.get_all_data()
            print(json_load.get_data('key1','key2'))
            
            得到：value

        """
        if self.data is None:
            raise ValueError("Data has not been loaded yet. Call load() first.")
        
        current_data = self.data
        for key in keys:
            if isinstance(current_data, dict) and key in current_data:
                current_data = current_data[key]
            else:
                raise KeyError(f"Key '{key}' not found in the data.")
        
        return current_data
    
    def update_data(self, updates: Dict) -> None:
        """
        更新部分数据（仅适用于字典类型的数据）。
        
        :param updates: 包含更新项的字典
        """
        if not isinstance(self.data, dict):
            raise TypeError("The current data is not a dictionary and cannot be updated with this method.")
        
        for key, value in updates.items():
            if isinstance(value, dict) and key in self.data and isinstance(self.data[key], dict):
                self.data[key].update(value)  # 深度更新字典
            else:
                self.data[key] = value
    
    def add_to_list(self, list_key: str, item: Any) -> None:
        """
        向指定键对应的列表添加新元素（仅适用于列表类型的数据）。
        
        :param list_key: 对应列表的键名
        :param item: 要添加的新元素
        """
        if not isinstance(self.data.get(list_key), list):
            raise KeyError(f"The key '{list_key}' does not correspond to a list.")
        
        self.data[list_key].append(item)

# 使用示例
# if __name__ == "__main__":
#     try:
#         # 创建 JsonLoader 实例时自动加载数据
#         json_load = JsonLoader()
        
#         # 获取加载的数据
#         data = json_load.get_data()
#         print("Loaded Data:", data)
        
#         # 修改数据
#         json_load.update_data({"new_field": "value"})
#         json_load.add_to_list("employees", {"name": "David", "age": 32, "occupation": "Analyst"})
        
#         # 保存修改后的数据
#         json_load.save(json_load.get_data())
        
#     except Exception as e:
#         print(f"An error occurred: {e}")