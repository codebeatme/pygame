from pygame import Surface, SRCALPHA, BLEND_PREMULTIPLIED

# 创建一个表面并填充具有透明度的红色
s = Surface([100, 100], SRCALPHA)
s.fill([255, 0, 0, 100])
# 将表面自身的透明度设置为 50
s.set_alpha(50)

# 预先计算透明度
pa = s.premul_alpha()

# 创建游戏窗口并绘制 s 和 pa（pa 使用 BLEND_PREMULTIPLIED）
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
w.blit(pa, (100, 100), special_flags=BLEND_PREMULTIPLIED)
display.flip()

import time
time.sleep(3)
