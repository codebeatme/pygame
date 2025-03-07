# 匯入相關模組，建立遊戲視窗
from pygame import display, event, mouse
display.set_mode((800, 600))

count = 0
focused = True
while True:
    # 明確的呼叫 pump 函式
    event.pump()

    # 判斷滑鼠是否離開了顯示區域
    if focused and not mouse.get_focused():
        focused = False
        count += 1
        print('滑鼠離開了顯示區域')

    # 判斷滑鼠是否進入了顯示區域
    if not focused and mouse.get_focused():
        focused = True
        count += 1
        print('滑鼠進入了顯示區域')

    # 切換次數達到 5 次時，結束遊戲
    if count == 5:
        break