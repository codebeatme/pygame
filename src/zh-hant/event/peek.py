# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 匯入表示結束，滑鼠進入，滑鼠離開的變數
from pygame import QUIT, WINDOWENTER, WINDOWLEAVE
running = True

while running:
    # 判斷事件滑鼠進入視窗或滑鼠離開視窗是否存在
    if event.peek([WINDOWENTER, WINDOWLEAVE]):
        print('滑鼠進入或滑鼠離開')

    # 判斷結束事件是否存在
    if event.peek(QUIT):
        running = False

    # 取得並顯示所有的事件
    es = event.get()
    if len(es):
        print(es)