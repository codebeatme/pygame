# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示没有事件的变量
from pygame import NOEVENT

while True:
    # 获取队列中的所有事件
    event.get()
    # 等待一个新的事件，超时时间为 5 秒
    e = event.wait(5000)
    
    # 如果队列中没有事件，则退出
    if e.type == NOEVENT:
        break