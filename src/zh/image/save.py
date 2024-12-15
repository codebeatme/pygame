# 在运行脚本前，请将命令行跳转至 save.py 所在的目录
from pygame import image, Surface

# 加载图像文件，并将他们绘制在表面对象 surface 中
sky = image.load('sky.webp')
candy = image.load_extended('candy.png')

surface = Surface((800, 600))
surface.blit(sky, (0, 0))
surface.blit(candy, (100, 100))

# 将 surface 保存至文件，图像格式为 jpg
image.save(surface, 'combine.jpg')
