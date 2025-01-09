from pygame import Surface, Color

# 创建颜色深度为 8 的表面
s = Surface((800, 600), depth=8)
# 获取调色板
print(s.get_palette())

# 设置调色板中的第一个颜色（黑色）
s.set_palette([(255, 0, 0)])

# 获取调色板中的第一个颜色
c = s.get_palette_at(0)
print(c)

# 设置调色板中的第二个颜色
s.set_palette_at(1, Color('#00FF00'))

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
