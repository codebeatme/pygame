# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入第一個可用的字型
fontname = font.get_fonts()[0]
f = font.Font(font.match_font(fontname))
# 修改為刪除線樣式
f.strikethrough = True

# 建立遊戲視窗，並使用字型物件 f 繪製文字
from pygame import display
w = display.set_mode((800, 600))

# 在遊戲視窗中繪製文字
w.blit(f.render('Strikethrough', False, [255, 255, 255]), [300, 300])
display.flip()

# 等候 3 秒
import time
time.sleep(3)