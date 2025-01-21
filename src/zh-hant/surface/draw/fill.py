from pygame import Surface, SRCALPHA, BLEND_RGBA_ADD

# 建立支援透明度的表面，並設定表面的透明度
s = Surface((800, 600), SRCALPHA)
# 繪製一個不透明矩形
s.fill('#ff0000', [100, 100, 100, 100])
# 繪製一個透明矩形，與不透明矩形部分重疊
s.fill('#ffff0099', [150, 150, 100, 100], BLEND_RGBA_ADD)

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)