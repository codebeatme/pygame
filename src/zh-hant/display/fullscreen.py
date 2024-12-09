from pygame import display

# 建立遊戲視窗並在全熒幕模式和視窗模式之間切換
display.set_mode((700, 600))
print(f'切換至全熒幕模式：{display.toggle_fullscreen()}')
print(f'切換至視窗模式：{display.toggle_fullscreen()}')
