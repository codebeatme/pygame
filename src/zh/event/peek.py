# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示退出，鼠标进入，鼠标离开的变量
from pygame import QUIT, WINDOWENTER, WINDOWLEAVE
running = True

while running:
    # 判断事件鼠标进入窗口或鼠标离开窗口是否存在
    if event.peek([WINDOWENTER, WINDOWLEAVE]):
        print('鼠标进入或鼠标离开')

    # 判断退出事件是否存在
    if event.peek(QUIT):
        running = False

    # 获取并显示所有的事件
    es = event.get()
    if len(es):
        print(es)