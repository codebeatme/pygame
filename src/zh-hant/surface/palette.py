from pygame import Surface, Color

# 建立色彩深度為 8 的表面
s = Surface((800, 600), depth=8)
# 取得調色板
print(s.get_palette())

# 設定調色板中的第一個色彩（黑色）
s.set_palette([(255, 0, 0)])

# 取得調色板中的第一個色彩
c = s.get_palette_at(0)
print(c)

# 設定調色板中的第二個色彩
s.set_palette_at(1, Color('#00FF00'))

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)
