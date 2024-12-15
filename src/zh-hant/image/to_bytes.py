# 在執行腳本前，請將命令列跳躍至 to_bytes.py 所在的目錄
from pygame import image

# 將 Surface 物件轉換為 bytes，色彩格式為 RGBA
sky = image.load('sky.webp')
bs = image.tobytes(sky, 'RGBA')

# 使用 PIL 讀取 bytes，並將影像儲存為檔案 pil.sky.webp
import PIL.Image
i = PIL.Image.frombytes('RGBA', (729, 1296), bs)
i.save('pil.sky.webp')