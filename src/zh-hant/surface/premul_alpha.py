from pygame import Surface, SRCALPHA, BLEND_PREMULTIPLIED

# 建立一個表面並填入具有透明度的紅色
s = Surface([100, 100], SRCALPHA)
s.fill([255, 0, 0, 100])
# 將表面自身的透明度設定為 50
s.set_alpha(50)

# 預先計算透明度
pa = s.premul_alpha()

# 建立遊戲視窗並繪製 s 和 pa（pa 使用 BLEND_PREMULTIPLIED）
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
w.blit(pa, (100, 100), special_flags=BLEND_PREMULTIPLIED)
display.flip()

import time
time.sleep(3)
