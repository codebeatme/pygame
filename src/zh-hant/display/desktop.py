# 匯入並初始化 display 模組
from pygame import display
display.init()

# 取得所有桌面的大小
print(f'所有桌面：{display.get_desktop_sizes()}')

# 取得熒幕個數
print(f'熒幕個數：{display.get_num_displays()}')
