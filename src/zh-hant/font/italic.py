# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入一個斜體字型檔案
f = font.Font(font.match_font('Arial', italic=True), 30)

# 無法將斜體修改為非斜體
f.set_italic(False)
print(f'斜體？{f.get_italic()}')

# 建立遊戲視窗，並使用字型物件 f 繪製文字
from pygame import display
w = display.set_mode([800, 600])

# 在遊戲視窗中繪製文字
ts = f.render('Draw in italic style', True, (0, 255, 0))
w.blit(ts, (200, 200))
display.flip()

# 等待 3 秒
import time
time.sleep(3)