from pygame import Surface, SRCALPHA

# 创建支持透明度的表面，并将其透明颜色键设置为红色
s = Surface((800, 600), SRCALPHA)
s.set_colorkey(0xff0000)
print(f'透明颜色键：{s.get_colorkey()}')

# 在表面分别绘制红色和黄色的矩形
from pygame import draw
draw.rect(s, '#ff000088', [0, 0, 50, 50])
draw.rect(s, '#ffff0099', [50, 0, 50, 50])

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
