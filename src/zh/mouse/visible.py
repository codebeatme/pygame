# 导入相关模块和变量，创建游戏窗口
from pygame import display, event, mouse, QUIT, MOUSEBUTTONUP, BUTTON_LEFT, BUTTON_RIGHT
display.set_mode((800, 600))

running = True
while running:
    # 隐式的调用 pump 函数
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONUP:
            if e.button == BUTTON_LEFT:
                # 获取鼠标的可见状态，并反转
                v = mouse.get_visible()
                mouse.set_visible(not v)
            elif e.button == BUTTON_RIGHT:
                # 退出游戏循环
                running = False