# 导入并初始化 display 模块
from pygame import display
display.init()

# 获取所有桌面的大小
print(f'所有桌面：{display.get_desktop_sizes()}')

# 获取屏幕个数
print(f'屏幕个数：{display.get_num_displays()}')
