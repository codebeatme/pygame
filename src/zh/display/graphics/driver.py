# 导入并初始化 display 模块
from pygame import display
display.init()

print(f'当前显示驱动：{display.get_driver()}')