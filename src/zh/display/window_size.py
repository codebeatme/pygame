from pygame import display, SCALED

# 创建一个较小的窗口，SCALED 将缩放窗口的表面
s = display.set_mode([300, 200], SCALED)
print(f'显示区域大小：{display.get_window_size()}')
print(f'表面大小：{s.get_size()}')