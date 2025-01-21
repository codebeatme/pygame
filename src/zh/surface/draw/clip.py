from pygame import Surface

s = Surface([800, 600])
# 绘制一个白色的正方形并将其设置为剪辑区域
s.fill('white', ((100, 100), (100, 100)))
s.set_clip((100, 100), (100, 100))
print(f'当前剪辑区域：{s.get_clip()}')

# 绘制一个与白色正方形部分重叠的绿色正方形
s.fill('#00ff00', (150, 150, 100, 100))

# 将整个表面设置为剪辑区域
s.set_clip(None)
print(f'当前剪辑区域：{s.get_clip()}')

# 绘制一个与白色正方形部分重叠的蓝色正方形
s.fill('#0000ff', [50, 50, 100, 100])

# 创建游戏窗口并绘制 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)