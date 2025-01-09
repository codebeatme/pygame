from pygame import Surface

# 建立表面，並取得座標為 0 0 的像素的色彩
s = Surface((800, 600))
print(f'座標 0 0 處的色彩：{s.get_at((0, 0))}')

# 繪製一條白色的線段
for i in range(100, 700):
    s.set_at([i, 300], 'white')
print(f'座標 100 300 處的色彩：{hex(s.get_at_mapped([100, 300]))}')

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
