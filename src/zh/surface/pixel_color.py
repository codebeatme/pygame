from pygame import Surface

# 创建表面，并获取坐标为 0 0 的像素的颜色
s = Surface((800, 600))
print(f'坐标 0 0 处的颜色：{s.get_at((0, 0))}')

# 绘制一条白色的线段
for i in range(100, 700):
    s.set_at([i, 300], 'white')
print(f'坐标 100 300 处的颜色：{hex(s.get_at_mapped([100, 300]))}')

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
