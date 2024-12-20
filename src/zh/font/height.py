# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载默认字体，字体大小 120
f = font.Font(size=120)
# 获取字体行高
print(f'字体行高：{f.get_linesize()}')
# 获取字体高度
print(f'字体高度：{f.get_height()}')
