# 匯入相關模組，建立遊戲視窗
from pygame import display, event, mouse
display.set_mode((800, 600))

while True:
    # 明確的呼叫 pump 函式
    event.pump()
    # 取得滑鼠按鍵的按下狀態
    (l, m, r) = mouse.get_pressed()

    # 如果滑鼠左健，右鍵和滾輪鍵一同按下，那麽遊戲迴圈結束
    if l and r and m:
        break