# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示結束，視窗關閉，滑鼠進入的變數
from pygame import QUIT, WINDOWCLOSE, WINDOWENTER
running = True

# 封鎖結束和視窗關閉事件
event.set_blocked([QUIT, WINDOWCLOSE])

while running:
    for e in event.get():
        # 當滑鼠進入視窗並且結束事件被封鎖時，解除對結束和視窗關閉事件的封鎖
        if e.type == WINDOWENTER and event.get_blocked(QUIT):
            event.set_allowed((QUIT, WINDOWCLOSE))

        # 根據事件的類型進行不同的處理
        if e.type == WINDOWCLOSE:
            print('視窗關閉')
        elif e.type == QUIT:
            print('結束')
            running = False