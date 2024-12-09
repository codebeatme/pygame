# 匯入並初始化 display 模組
from pygame import display
display.init()

# 列出全熒幕模式所支援的視窗表面大小
print(f'全熒幕模式支援的表面大小：{display.list_modes()}')
