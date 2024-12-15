# 在執行腳本前，請將命令列跳躍至 load.py 所在的目錄
from pygame import image, display

# 通過 IO 物件載入影像檔案 sky.webp
data = open('sky.webp', 'rb')
sky = image.load(data)

# 直接載入影像檔案 candy.png
candy = image.load_extended('candy.png')

# 建立遊戲視窗，繪製天空和糖果，並等待 2 秒鐘
s = display.set_mode((800, 600))
s.blit(sky, (0, 0))
s.blit(candy, (100, 100))
display.flip()

import time
time.sleep(2)