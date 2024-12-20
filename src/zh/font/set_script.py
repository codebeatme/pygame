# 导入并初始化 font 模块
from pygame import font
font.init()

# 将文字整形设置为阿拉伯文
f = font.Font()
f.set_script('Arab')