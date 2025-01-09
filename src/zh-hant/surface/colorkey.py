from pygame import Surface, SRCALPHA

# 建立支援透明度的表面，並將其透明色彩鍵設定為紅色
s = Surface((800, 600), SRCALPHA)
s.set_colorkey(0xff0000)
print(f'透明色彩鍵：{s.get_colorkey()}')

# 在表面分別繪製紅色和黃色的矩形
from pygame import draw
draw.rect(s, '#ff000088', [0, 0, 50, 50])
draw.rect(s, '#ffff0099', [50, 0, 50, 50])

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
