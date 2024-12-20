# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入預設字型，字型大小 120
f = font.Font(size=120)
print(f'字型上移量：{f.get_ascent()}，字型下移量：{f.get_descent()}')
print(f'字型高度：{f.get_height()}')