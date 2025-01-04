# 匯入 Rect，Vector2 物件
from pygame import Rect, Vector2

# 建立不同的矩形，浮點數會被轉換為整數
# X 座標 10，Y 座標 20，寬度 50，高度 99
r1 = Rect(10.5, 20.5, 50.9, 99.9)
# X 座標 110，Y 座標 100，寬度 20，高度 25
r2 = Rect((110, 100), [20, 25])
# X 座標 200，Y 座標 210，寬度 20，高度 50
r3 = Rect(Vector2(200, 210), Vector2(20, 50.5))
# X 座標 300，Y 座標 100，寬度 40，高度 45
r4 = Rect([(300, 100), [40, 45]])

# 建立遊戲視窗，並使用矩形進行繪製
from pygame import display, draw
s = display.set_mode((800, 600))
draw.rect(s, 0xff0000, r1)
draw.rect(s, 0x00ff00, r2)
draw.rect(s, 0xff00ff, r3)
draw.rect(s, 0x0000ff, r4)
display.flip()

import time
time.sleep(2)