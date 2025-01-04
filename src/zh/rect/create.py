# 导入 Rect，Vector2 对象
from pygame import Rect, Vector2

# 创建不同的矩形，浮点数会被转换为整数
# X 坐标 10，Y 坐标 20，宽度 50，高度 99
r1 = Rect(10.5, 20.5, 50.9, 99.9)
# X 坐标 110，Y 坐标 100，宽度 20，高度 25
r2 = Rect((110, 100), [20, 25])
# X 坐标 200，Y 坐标 210，宽度 20，高度 50
r3 = Rect(Vector2(200, 210), Vector2(20, 50.5))
# X 坐标 300，Y 坐标 100，宽度 40，高度 45
r4 = Rect([(300, 100), [40, 45]])

# 创建游戏窗口，并使用矩形进行绘制
from pygame import display, draw
s = display.set_mode((800, 600))
draw.rect(s, 0xff0000, r1)
draw.rect(s, 0x00ff00, r2)
draw.rect(s, 0xff00ff, r3)
draw.rect(s, 0x0000ff, r4)
display.flip()

import time
time.sleep(2)