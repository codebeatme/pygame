# 在运行脚本前，请将命令行跳转至 from_buffer.py 所在的目录
from pygame import image, display

# 使用 PIL 读取图像文件，并转换为 bytes 对象
import PIL.Image
bs = PIL.Image.open('sky.webp').tobytes()

# 将 bytes 对象转换为 Surface 对象
sky = image.frombuffer(bs, (729, 1296), 'RGB', True)

# 创建游戏窗口，绘制天空，并等待 2 秒钟
s = display.set_mode((800, 600))
s.blit(sky, (0, 0))
display.flip()

import time
time.sleep(2)