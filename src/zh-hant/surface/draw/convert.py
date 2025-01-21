# 匯入並建立遊戲視窗
from pygame import display, Surface, SRCALPHA
w = display.set_mode((800, 600))

# 建立支援透明度的表面物件，填入具有透明度的紅色正方形
s = Surface([100, 100], SRCALPHA)
s.fill('#ff000099', [0, 0, 100, 100])

# 轉換像素格式，新表面不支援透明度
cs = s.convert(16, SRCALPHA)
print(f'cs 特性：{cs.get_flags()}')
# 轉換像素格式，新表面支援透明度
cas = s.convert_alpha()
print(f'cas 特性：{cas.get_flags()}')

# 在遊戲視窗中繪製 cs 和 cas
w.blit(cs, (0, 0))
w.blit(cas, (100, 100))
display.flip()

import time
time.sleep(3)