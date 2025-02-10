# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 独占输入设备
event.set_grab(True)
# 独占键盘输入，但 Alt+F4 快捷键依然有效
event.set_keyboard_grab(True)
print(f'独占输入设备？{event.get_grab()}')
print(f'独占键盘输入？{event.get_keyboard_grab()}')

# 在游戏循环中等待结束请求
from pygame import QUIT
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False