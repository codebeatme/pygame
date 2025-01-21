# 导入模块并进行初始化
from pygame import font, image
font.init()

# 使用 Pygame 默认字体绘制文本 Hello
f = font.Font(size=30)
ts = f.render('Hello', True, [2, 255, 0], '#ffffff')

# 加载图像文件
img = image.load('candy.png')

# 创建游戏窗口并绘制 ts 和 img
from pygame import display
w = display.set_mode([800, 600])
w.blit(ts, (50, 50))
w.blit(img, (100, 100))
display.flip()

import time
time.sleep(3)