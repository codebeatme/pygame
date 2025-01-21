# 导入并创建游戏窗口
from pygame import display, Surface, SRCALPHA
w = display.set_mode((800, 600))

# 创建支持透明度的表面对象，填充具有透明度的红色正方形
s = Surface([100, 100], SRCALPHA)
s.fill('#ff000099', [0, 0, 100, 100])

# 转换像素格式，新表面不支持透明度
cs = s.convert(16, SRCALPHA)
print(f'cs 特性：{cs.get_flags()}')
# 转换像素格式，新表面支持透明度
cas = s.convert_alpha()
print(f'cas 特性：{cas.get_flags()}')

# 在游戏窗口中绘制 cs 和 cas
w.blit(cs, (0, 0))
w.blit(cas, (100, 100))
display.flip()

import time
time.sleep(3)