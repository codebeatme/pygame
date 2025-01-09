from pygame import Surface, SRCALPHA

# 创建支持透明度的表面，并设置表面的透明度
s = Surface((800, 600), SRCALPHA)
s.set_alpha(50)
print(f'表面的透明度：{s.get_alpha()}')

# 在表面绘制两个透明度不同的矩形
from pygame import draw
draw.rect(s, '#ff0000', [0, 0, 50, 50])
draw.rect(s, '#ff000099', [50, 0, 50, 50])

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
