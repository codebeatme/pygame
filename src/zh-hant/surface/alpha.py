from pygame import Surface, SRCALPHA

# 建立支援透明度的表面，並設定表面的透明度
s = Surface((800, 600), SRCALPHA)
s.set_alpha(50)
print(f'表面的透明度：{s.get_alpha()}')

# 在表面繪製兩個透明度不同的矩形
from pygame import draw
draw.rect(s, '#ff0000', [0, 0, 50, 50])
draw.rect(s, '#ff000099', [50, 0, 50, 50])

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
