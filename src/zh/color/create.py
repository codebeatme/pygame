# 导入 Color 对象
from pygame import Color

# 创建不同的颜色
red1 = Color([255, 0, 0])
red2 = Color([255, 0, 0, 100])
green1 = Color('#00FF00')
green2 = Color('#00FF99')
blue = Color('blue')

# 创建游戏窗口，使用颜色进行绘制，并等待 2 秒钟
from pygame import display, draw, Surface, SRCALPHA
s = display.set_mode((800, 600))
# 创建表面，绘制矩形，填充颜色
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