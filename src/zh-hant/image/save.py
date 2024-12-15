# 在執行腳本前，請將命令列跳躍至 save.py 所在的目錄
from pygame import image, Surface

# 載入影像檔案，並將他們繪製在表面物件 surface 中
sky = image.load('sky.webp')
candy = image.load_extended('candy.png')

surface = Surface((800, 600))
surface.blit(sky, (0, 0))
surface.blit(candy, (100, 100))

# 將 surface 儲存至檔案，影像格式為 jpg
image.save(surface, 'combine.jpg')
