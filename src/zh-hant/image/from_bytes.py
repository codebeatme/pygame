# 在執行腳本前，請將命令列跳躍至 from_bytes.py 所在的目錄
from pygame import image, display

# 使用 PIL 讀取影像檔案，並轉換為 bytes 物件
import PIL.Image
bs = PIL.Image.open('sky.webp').tobytes()

# 將 bytes 物件轉換為 Surface 物件
sky = image.frombytes(bs, (729, 1296), 'RGB', True)

# 建立遊戲視窗，繪製天空，並等待 2 秒鐘
s = display.set_mode((800, 600))
s.blit(sky, (0, 0))
display.flip()

import time
time.sleep(2)