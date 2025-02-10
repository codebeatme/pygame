# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

count = 0

while True:
    # 讓 Pygame 自動處理事件
    event.pump()

    # 不斷加 1，使視窗顯示一段時間
    count += 1
    if count == 10000000:
        # 跳出迴圈會使程式結束，視窗也將關閉
        break