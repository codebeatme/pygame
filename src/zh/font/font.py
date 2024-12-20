# 导入模块 font
from pygame import font

# 初始化
font.init()
print(f'font 已经初始化？{font.get_init()}')

# 获取所有可用字体的名称
print(font.get_fonts())
# 获取默认字体的文件名称
print(font.get_default_font())

# 获取字体文件的路径
print(font.match_font('tahoma,Sitka Text', True, True))
