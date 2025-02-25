# 匯入相關模組，並建立遊戲視窗
from pygame import display, event
w = display.set_mode((400, 300))

# 匯入與鍵盤事件相關的變數
from pygame import KEYDOWN, KEYUP, KEYMAPCHANGED, K_UP, K_DOWN, K_LEFT, K_RIGHT, KMOD_RCTRL

running = True
while running:
    for e in event.get():
        if e.type == KEYDOWN:
            print('按下鍵盤', e)
            
            # 判斷按下的鍵是哪一個
            if e.key == K_UP:
                print('上方向鍵')
            elif e.key == K_DOWN:
                print('下方向鍵')
            elif e.key == K_LEFT:
                print('左方向鍵')
            elif e.key == K_RIGHT:
                print('右方向鍵')
            
            if e.mod & KMOD_RCTRL:
                # 按下右 Ctrl 鍵，則結束遊戲迴圈
                running = False

        elif e.type == KEYUP:
            print('放開鍵盤', e)
        elif e.type == KEYMAPCHANGED:
            print('鍵盤布局改變', e)
