# 导入模块 display 和 event，并创建游戏窗口
from pygame import display, event
w = display.set_mode([800, 600])

# 导入表示退出，窗口移动，窗口最大化的变量
from pygame import QUIT, WINDOWMOVED, WINDOWMAXIMIZED
running = True

while running:
    # 获取队列中的退出，窗口移动事件
    for e in event.get((QUIT, WINDOWMOVED)):
        # 根据事件的类型进行不同的处理
        if e.type == QUIT:
            # 结束游戏循环
            running = False
            print(f'请求退出游戏')
        elif e.type == WINDOWMOVED:
            print(f'窗口位置：{e.x} {e.y}')
    
    # 获取队列中的其他事件，除了窗口最大化
    es = event.get(exclude=WINDOWMAXIMIZED)
    print(es)