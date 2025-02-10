from pygame import Surface, SRCALPHA

# 建立遊戲表面和子表面
s = Surface([800, 600], SRCALPHA)
c = s.subsurface(0, 0, 100, 100)

s.fill('#ffff0099', [0, 0, 800, 600])

# 將子表面的透明色彩鍵設定為紅色，但不會達到預期效果
c.set_colorkey('#ff0000')
c.fill('#ff0000', [0, 0, 100, 100])
# 檢視父表面的像素是否已經被修改
print(s.get_at([0, 0]))

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)