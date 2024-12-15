# 在執行腳本前，請將命令列跳躍至 reload.py 所在的目錄
from pygame import image

# 將 surface 儲存至 IO 物件
import io
bs = io.BytesIO()
sky = image.load('sky.webp')
# 指定影像格式為 png
image.save(sky, bs, '.png')

# 重新載入 IO 物件之前，需要將指標移動至開頭
bs.seek(0)
new_sky = image.load(bs, '.png')
