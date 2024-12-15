# 在运行脚本前，请将命令行跳转至 load.py 所在的目录
from pygame import image, display

# 通过 IO 对象加载图像文件 sky.webp
data = open('sky.webp', 'rb')
sky = image.load(data)

# 直接加载图像文件 candy.png
candy = image.load_extended('candy.png')

# 创建游戏窗口，绘制天空和糖果，并等待 2 秒钟
s = display.set_mode((800, 600))
s.blit(sky, (0, 0))
s.blit(candy, (100, 100))
display.flip()

import time
time.sleep(2)