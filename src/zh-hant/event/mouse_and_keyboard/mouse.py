# 匯入相關模組，並建立遊戲視窗
from pygame import display, event
w = display.set_mode((400, 300))

# 匯入與滑鼠事件相關的變數
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, MOUSEWHEEL

running = True
while running:
    for e in event.get():
        # 顯示不同滑鼠事件的資訊
        if e.type == MOUSEBUTTONDOWN:
            print('按下滑鼠', e)
        elif e.type == MOUSEBUTTONUP:
            print('放開滑鼠', e)
        elif e.type == MOUSEMOTION:
            print('移動滑鼠', e)
        elif e.type == MOUSEWHEEL:
            # 當玩家捲動滾輪時，結束遊戲迴圈
            print('捲動滾輪', e)
            running = False
