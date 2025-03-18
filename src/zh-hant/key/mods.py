# 匯入 key 模組和其他相關內容，並建立遊戲視窗
from pygame import key, event, display, K_a, K_q, KMOD_LALT, KMOD_LCTRL
display.set_mode([800, 600])

# 臨時將左 Alt 鍵和左 Ctrl 鍵設定為按下
key.set_mods(KMOD_LALT | KMOD_LCTRL)

while True:
    # 明確的呼叫 pump 函式
    event.pump()
    # 取得所有按鍵和輔助按鍵的按下狀態
    ps = key.get_pressed()
    mods = key.get_mods()

    # 如果按下左 Ctrl 鍵和 A 鍵，則遊戲結束
    if ps[K_a] and (mods & KMOD_LCTRL):
        print('角色攻擊')

    # 如果按下左 Alt 鍵和 Q 鍵，則遊戲結束
    if ps[K_q] and (mods & KMOD_LALT):
        break