# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示結束和沒有事件的變數
from pygame import QUIT, NOEVENT
running = True

while running:
    # 使用迴圈取出佇列中的所有事件
    while True:
        e = event.poll()

        # 根據事件的類型進行不同的處理
        if e.type == QUIT:
            print('QUIT')
            # 結束遊戲迴圈
            running = False
            break
        elif e.type == NOEVENT:
            # 佇列中已經沒有事件進入下一個遊戲迴圈
            print('NOEVENT')
            break