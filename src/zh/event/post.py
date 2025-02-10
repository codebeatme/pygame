# 导入相关内容，并创建游戏窗口
from pygame import display, event, QUIT, WINDOWLEAVE, MOUSEBUTTONDOWN
w = display.set_mode([800, 600])

# 阻止退出事件
event.set_blocked(QUIT)

running = True
while running:
    for e in event.get():
        if e.type == WINDOWLEAVE:
            # 当鼠标离开窗口时，取消阻止退出事件
            event.set_allowed(QUIT)
        elif e.type == MOUSEBUTTONDOWN:
            # 按下鼠标时，引发退出事件
            event.post(event.Event(QUIT))
        elif e.type == QUIT:
            # 结束游戏循环
            running = False