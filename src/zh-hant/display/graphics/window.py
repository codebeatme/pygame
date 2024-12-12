# 匯入並初始化 display 模組
from pygame import display
display.init()

# 取得由作業系統提供的關於遊戲視窗的資訊
print(f'遊戲視窗資訊：{display.get_wm_info()}')