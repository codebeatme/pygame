# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入一個非粗體字型檔案，字型大小 24
f = font.Font(font.match_font('Microsoft JhengHei'), 24)

# 修改為粗體樣式
f.bold = True
print(f'粗體？{f.get_bold()}')

# 建立遊戲視窗，並使用字型物件 f 繪製文字
from pygame import display
w = display.set_mode((800, 600))

# 在遊戲視窗中繪製文字
ts = f.render('以粗體樣式繪製', False, [255, 0, 0])
w.blit(ts, [50, 50])
display.flip()

# 等待 3 秒
import time
time.sleep(3)