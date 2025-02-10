# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示退出，窗口关闭，鼠标进入的变量
from pygame import QUIT, WINDOWCLOSE, WINDOWENTER
running = True

# 阻止退出和窗口关闭事件
event.set_blocked([QUIT, WINDOWCLOSE])

while running:
    for e in event.get():
        # 当鼠标进入窗口并且退出事件被阻止时，解除对退出和窗口关闭事件的阻止
        if e.type == WINDOWENTER and event.get_blocked(QUIT):
            event.set_allowed((QUIT, WINDOWCLOSE))

        # 根据事件的类型进行不同的处理
        if e.type == WINDOWCLOSE:
            print('窗口关闭')
        elif e.type == QUIT:
            print('退出')
            running = False