# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载默认字体，字体大小 120
f = font.Font(size=120)
print(f'字体上移量：{f.get_ascent()}，字体下移量：{f.get_descent()}')
print(f'字体高度：{f.get_height()}')