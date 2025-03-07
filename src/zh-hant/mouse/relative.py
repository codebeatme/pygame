# 匯入相關模組，建立遊戲視窗
from pygame import display, event, mouse, MOUSEBUTTONDOWN
display.set_mode((800, 600))

running = True
while running:
    # 隱含的呼叫 pump 函式
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            # 取得滑鼠的移動距離
            (x, y) = mouse.get_rel()
            print('水平移動距離', x, '垂直移動距離', y)

            # 如果實際的移動距離大於 400，則遊戲迴圈結束
            d = (x**2 + y**2) ** 0.5
            print('實際移動距離', d)

            if d > 400:
                running = False