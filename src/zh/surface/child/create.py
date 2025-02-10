from pygame import Surface, SRCALPHA

# 创建游戏表面和子表面
s = Surface([800, 600], SRCALPHA)
c = s.subsurface(0, 0, 100, 100)

s.fill('#ffff0099', [0, 0, 800, 600])

# 将子表面的透明颜色键设置为红色，但不会达到预期效果
c.set_colorkey('#ff0000')
c.fill('#ff0000', [0, 0, 100, 100])
# 查看父表面的像素是否已经被修改
print(s.get_at([0, 0]))

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)