# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入 Pygame 預設字型，字型大小 30
f = font.Font(size=30)
# 修改為底線樣式
f.set_underline(True)

# 建立遊戲視窗，並使用字型物件 f 繪製文字
from pygame import display
w = display.set_mode((800, 600))

# 在遊戲視窗中繪製文字
w.blit(f.render('Underline', False, [255, 0, 255]), [200, 200])
display.flip()

# 等待 3 秒
import time
time.sleep(3)