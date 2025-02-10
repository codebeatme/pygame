# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示結束，視窗移動，視窗最大化的變數
from pygame import QUIT, WINDOWMOVED, WINDOWMAXIMIZED
running = True

while running:
    # 取得佇列中的結束，視窗移動事件
    for e in event.get((QUIT, WINDOWMOVED)):
        # 根據事件的類型進行不同的處理
        if e.type == QUIT:
            # 結束遊戲迴圈
            running = False
            print(f'要求結束遊戲')
        elif e.type == WINDOWMOVED:
            print(f'視窗位置：{e.x} {e.y}')
    
    # 取得佇列中的其他事件，除了視窗最大化
    es = event.get(exclude=WINDOWMAXIMIZED)
    print(es)