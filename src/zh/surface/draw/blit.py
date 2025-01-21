from pygame import Surface

# 创建一些表面对象
s1 = Surface([100, 100])
s1.fill(0xff0000, [0, 0, 100, 100])
s2 = Surface([50, 50])
s2.fill('green', [0, 0, 50, 50])
s3 = Surface([100, 100])
s3.fill('#0000ff', [0, 0, 100, 100])

# 创建游戏窗口并绘制多个表面
from pygame import display
w = display.set_mode((800, 600))
w.blits([
    (s1, (0, 0)),
    (s2, (100, 0)),
    # 只绘制 s3 的左上角区域
    (s3, (150, 0), [0, 0, 25, 25])
])
display.flip()

# 等待 3 秒钟
import time
time.sleep(3)