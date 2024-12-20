# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载默认字体，字体大小 120
f = font.Font(size=120)
# 获取每个字符的度量值
print(f'{f.metrics('Aep')}')