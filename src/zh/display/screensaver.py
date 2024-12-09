# 导入并初始化 display 模块
from pygame import display
display.init()

# 获取和设置是否允许屏幕保护程序在游戏运行时启动
print(f'允许屏幕保护程序启动？{display.get_allow_screensaver()}')
display.set_allow_screensaver()
print(f'允许屏幕保护程序启动？{display.get_allow_screensaver()}')
