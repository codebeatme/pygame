# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示沒有事件的變數
from pygame import NOEVENT

while True:
    # 取得佇列中的所有事件
    event.get()
    # 等待一個新的事件，逾時時間為 5 秒
    e = event.wait(5000)
    
    # 如果佇列中沒有事件，則結束
    if e.type == NOEVENT:
        break