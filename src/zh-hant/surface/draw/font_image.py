# 匯入模組並進行初始化
from pygame import font, image
font.init()

# 使用 Pygame 預設字型繪製文字 Hello
f = font.Font(size=30)
ts = f.render('Hello', True, [2, 255, 0], '#ffffff')

# 載入影像檔案
img = image.load('candy.png')

# 建立遊戲視窗並繪製 ts 和 img
from pygame import display
w = display.set_mode([800, 600])
w.blit(ts, (50, 50))
w.blit(img, (100, 100))
display.flip()

import time
time.sleep(3)