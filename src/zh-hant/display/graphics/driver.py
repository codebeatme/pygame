# 匯入並初始化 display 模組
from pygame import display
display.init()

print(f'目前顯示驅動：{display.get_driver()}')