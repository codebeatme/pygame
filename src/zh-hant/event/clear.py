# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示結束的變數
from pygame import QUIT

while True:
    # 如果存在結束事件，則結束遊戲迴圈
    es = event.get(QUIT)
    if len(es):
        break

    # 清除佇列中剩余的事件
    event.clear()