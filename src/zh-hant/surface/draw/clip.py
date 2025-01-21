from pygame import Surface

s = Surface([800, 600])
# 繪製一個白色的正方形並將其設定為裁剪區域
s.fill('white', ((100, 100), (100, 100)))
s.set_clip((100, 100), (100, 100))
print(f'目前裁剪區域：{s.get_clip()}')

# 繪製一個與白色正方形部分重疊的綠色正方形
s.fill('#00ff00', (150, 150, 100, 100))

# 將整個表面設定為裁剪區域
s.set_clip(None)
print(f'目前裁剪區域：{s.get_clip()}')

# 繪製一個與白色正方形部分重疊的藍色正方形
s.fill('#0000ff', [50, 50, 100, 100])

# 建立遊戲視窗並繪製 s
from pygame import display
w = display.set_mode((800, 600))
w.blit(s, (0, 0))
display.flip()

import time
time.sleep(3)