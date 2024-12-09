from pygame import display, FULLSCREEN, SCALED

# 全熒幕顯示，表面大小 600x400，可縮放
s = display.set_mode((600, 400), FULLSCREEN | SCALED )
print(f'表面大小：{s.get_size()}')
