# 在运行脚本前，请将命令行跳转至 to_bytes.py 所在的目录
from pygame import image

# 将 Surface 对象转换为 bytes，颜色格式为 RGBA
sky = image.load('sky.webp')
bs = image.tobytes(sky, 'RGBA')

# 使用 PIL 读取 bytes，并将图像保存为文件 pil.sky.webp
import PIL.Image
i = PIL.Image.frombytes('RGBA', (729, 1296), bs)
i.save('pil.sky.webp')