# 匯入相關模組和變數，建立遊戲視窗
from pygame import display, event, mouse, QUIT, MOUSEBUTTONUP, BUTTON_LEFT, BUTTON_RIGHT
display.set_mode((800, 600))

running = True
while running:
    # 隱含的呼叫 pump 函式
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONUP:
            if e.button == BUTTON_LEFT:
                # 取得滑鼠的可見狀態，並反轉
                v = mouse.get_visible()
                mouse.set_visible(not v)
            elif e.button == BUTTON_RIGHT:
                # 結束遊戲迴圈
                running = False