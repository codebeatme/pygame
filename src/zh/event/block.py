# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示退出，鼠标进入的变量
from pygame import QUIT, WINDOWENTER
# 阻止鼠标进入事件
event.set_blocked(WINDOWENTER)

while True:
    # 检查队列中是否出现了鼠标进入事件
    if event.peek(WINDOWENTER):
        print('居然存在鼠标进入？！')

    # 一次取出一个事件，并判断是否需要退出循环
    if event.poll().type == QUIT:
        break