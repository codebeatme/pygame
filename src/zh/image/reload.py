# 在运行脚本前，请将命令行跳转至 reload.py 所在的目录
from pygame import image

# 将 surface 保存至 IO 对象
import io
bs = io.BytesIO()
sky = image.load('sky.webp')
# 指定图像格式为 png
image.save(sky, bs, '.png')

# 重新加载 IO 对象之前，需要将指针移动至开头
bs.seek(0)
new_sky = image.load(bs, '.png')
