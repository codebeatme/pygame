# 匯入並初始化 display 模組
from pygame import display
display.init()

# 判斷顯示模式是否可用
print(display.mode_ok([1024, 768], depth=8, display=1))