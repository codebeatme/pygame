# 匯入 Color 物件
from pygame import Color

# 建立不同的色彩
red1 = Color([255, 0, 0])
red2 = Color([255, 0, 0, 100])
green1 = Color('#00FF00')
green2 = Color('#00FF99')
blue = Color('blue')

# 建立遊戲視窗，使用色彩進行繪製，並等待 2 秒鐘
from pygame import display, draw, Surface, SRCALPHA
s = display.set_mode((800, 600))
# 建立表面，繪製矩形，填入色彩
area = Surface((400, 400), SRCALPHA)
draw.rect(area, red1, [0, 0, 100, 100])
draw.rect(area, red2, [0, 100, 100, 100])
draw.rect(area, green1, [100, 0, 100, 100])
draw.rect(area, green2, [100, 100, 100, 100])
draw.rect(area, blue, [200, 200, 100, 100])

s.blit(area, (0, 0))
display.flip()

import time
time.sleep(2)