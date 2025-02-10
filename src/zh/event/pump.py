# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

count = 0

while True:
    # 让 Pygame 自动处理事件
    event.pump()

    # 不断加 1，使窗口显示一段时间
    count += 1
    if count == 10000000:
        # 跳出循环会使程序结束，窗口也将关闭
        break