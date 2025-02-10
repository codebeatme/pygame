# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示退出和没有事件的变量
from pygame import QUIT, NOEVENT
running = True

while running:
    # 使用循环取出队列中的所有事件
    while True:
        e = event.poll()

        # 根据事件的类型进行不同的处理
        if e.type == QUIT:
            print('QUIT')
            # 结束游戏循环
            running = False
            break
        elif e.type == NOEVENT:
            # 队列中已经没有事件进入下一个游戏循环
            print('NOEVENT')
            break