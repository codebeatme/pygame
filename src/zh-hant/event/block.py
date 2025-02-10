# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示結束，滑鼠進入的變數
from pygame import QUIT, WINDOWENTER
# 封鎖滑鼠進入事件
event.set_blocked(WINDOWENTER)

while True:
    # 檢查佇列中是否出現了滑鼠進入事件
    if event.peek(WINDOWENTER):
        print('居然存在滑鼠進入？！')

    # 一次取出一個事件，並判斷是否需要結束迴圈
    if event.poll().type == QUIT:
        break