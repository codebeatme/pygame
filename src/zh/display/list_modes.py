# 导入并初始化 display 模块
from pygame import display
display.init()

# 列出全屏模式所支持的窗口表面大小
print(f'全屏模式支持的表面大小：{display.list_modes()}')
