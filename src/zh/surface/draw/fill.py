from pygame import Surface, SRCALPHA, BLEND_RGBA_ADD

# 创建支持透明度的表面，并设置表面的透明度
s = Surface((800, 600), SRCALPHA)
# 绘制一个不透明矩形
s.fill('#ff0000', [100, 100, 100, 100])
# 绘制一个透明矩形，与不透明矩形部分重叠
s.fill('#ffff0099', [150, 150, 100, 100], BLEND_RGBA_ADD)

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)