# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入預設字型，字型大小 120
f = font.Font(size=120)
# 取得字型行高
print(f'字型行高：{f.get_linesize()}')
# 取得字型高度
print(f'字型高度：{f.get_height()}')
