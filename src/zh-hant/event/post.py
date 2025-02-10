# 匯入相關內容，並建立遊戲視窗
from pygame import display, event, QUIT, WINDOWLEAVE, MOUSEBUTTONDOWN
w = display.set_mode([800, 600])

# 封鎖結束事件
event.set_blocked(QUIT)

running = True
while running:
    for e in event.get():
        if e.type == WINDOWLEAVE:
            # 當滑鼠離開視窗時，取消封鎖結束事件
            event.set_allowed(QUIT)
        elif e.type == MOUSEBUTTONDOWN:
            # 按下滑鼠時，引發結束事件
            event.post(event.Event(QUIT))
        elif e.type == QUIT:
            # 結束遊戲迴圈
            running = False