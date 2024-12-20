# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入預設字型，字型大小 120
f = font.Font(size=120)
# 取得每個字元的量值
print(f'{f.metrics('Aep')}')