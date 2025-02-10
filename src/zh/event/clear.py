# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示退出的变量
from pygame import QUIT

while True:
    # 如果存在退出事件，则结束游戏循环
    es = event.get(QUIT)
    if len(es):
        break

    # 清除队列中剩余的事件
    event.clear()