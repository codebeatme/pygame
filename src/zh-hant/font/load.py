# 匯入並初始化 font 模組
from pygame import font
font.init()

# 取得字型檔案的路徑，並建立一個字型物件
path = font.match_font('Microsoft JhengHei')
# 字型將采用預設大小 12
f = font.Font(path)

# 建立遊戲視窗，並使用字型物件 f 繪製文字
from pygame import display
w = display.set_mode((800, 600))

# 在遊戲視窗中繪製文字
ts = f.render('你好！', False, [255, 255, 255])
w.blit(ts, [200, 200])
display.flip()

# 等待 3 秒
import time
time.sleep(3)