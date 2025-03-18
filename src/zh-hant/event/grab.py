# 匯入模組 display 和 event，並建立遊戲視窗
from pygame import display, event
w = display.set_mode([800, 600])

# 獨占輸入裝置
event.set_grab(True)
# 獨占鍵盤輸入，但 Alt+F4 快速鍵依然有效
event.set_keyboard_grab(True)
print(f'獨占輸入裝置？{event.get_grab()}')
print(f'獨占鍵盤輸入？{event.get_keyboard_grab()}')

# 在遊戲迴圈中等候結束要求
from pygame import QUIT
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False