from pygame import display, SCALED

# 建立一個較小的視窗，SCALED 將縮放視窗的表面
s = display.set_mode([300, 200], SCALED)
print(f'顯示區域大小：{display.get_window_size()}')
print(f'表面大小：{s.get_size()}')