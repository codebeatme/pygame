# 匯入並初始化 font 模組
from pygame import font
font.init()

# 將文字整形設定為阿拉伯文
f = font.Font()
f.set_script('Arab')