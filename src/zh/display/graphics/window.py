# 导入并初始化 display 模块
from pygame import display
display.init()

# 获取由操作系统提供的关于游戏窗口的信息
print(f'游戏窗口信息：{display.get_wm_info()}')