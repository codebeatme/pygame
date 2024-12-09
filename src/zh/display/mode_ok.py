# 导入并初始化 display 模块
from pygame import display
display.init()

# 判断显示模式是否可用
print(display.mode_ok([1024, 768], depth=8, display=1))