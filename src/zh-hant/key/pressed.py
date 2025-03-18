# 匯入 key 模組和其他相關內容，並建立遊戲視窗
from pygame import key, event, display, K_UP, K_RCTRL
display.set_mode([800, 600])

while True:
    # 明確的呼叫 pump 函式
    event.pump()
    # 取得所有按鍵的按下狀態
    ps = key.get_pressed()

    # 如果同時按下了上方向鍵和右 Ctrl 鍵，則遊戲結束
    if ps[K_UP] and ps[K_RCTRL]:
        break