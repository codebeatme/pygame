# 匯入 display 模組和 FULLSCREEN，並進行初始化
from pygame import display, FULLSCREEN
display.init()

# 嘗試取得預設的圖形環境的資訊
info = display.Info()
print(f'預設的表面大小：{info.current_w}x{info.current_h}')

# 嘗試建立一個表面大小為 400x300 並全熒幕顯示的視窗
s = display.set_mode((400, 300), FULLSCREEN)

# 取得目前的圖形環境的資訊
info = display.Info()
print(f'表面大小：{info.current_w}x{info.current_h}')
