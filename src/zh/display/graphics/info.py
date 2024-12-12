# 导入 display 模块和 FULLSCREEN，并进行初始化
from pygame import display, FULLSCREEN
display.init()

# 尝试获取默认的图形环境的信息
info = display.Info()
print(f'默认的表面大小：{info.current_w}x{info.current_h}')

# 尝试创建一个表面大小为 400x300 并全屏显示的窗口
s = display.set_mode((400, 300), FULLSCREEN)

# 获取当前的图形环境的信息
info = display.Info()
print(f'表面大小：{info.current_w}x{info.current_h}')
