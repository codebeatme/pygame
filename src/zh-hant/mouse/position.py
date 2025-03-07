# 匯入相關模組，建立遊戲視窗
from pygame import display, event, mouse
display.set_mode((800, 600))

while True:
    # 明確的呼叫 pump 函式
    event.pump()
    # 取得滑鼠位置
    (x, y) = mouse.get_pos()

    # 當滑鼠位於視窗左上角時，他將被移至中心
    if x < 100 and y < 100:
        mouse.set_pos([400, 300])

    # 當滑鼠位於視窗右下角時，結束遊戲迴圈
    if x > 700 and x < 800 and y > 500 and y < 600:
        break