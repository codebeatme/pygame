# 在執行腳本前，請將命令列跳躍至 set_get.py 所在的目錄

# 匯入 mouse 模組和其他相關內容，並建立遊戲視窗
from pygame import mouse, image, display, event, QUIT
display.set_mode((400, 300))

# 載入大小為 32x32 的影像
candy = image.load('candy.png')
# 將影像設定為滑鼠指標，作用點在影像的中心
mouse.set_cursor((16, 16), candy)
print(mouse.get_cursor())

# 處理遊戲中的事件
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
