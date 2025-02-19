# 导入相关模块，并创建游戏窗口
from pygame import display, event
w = display.set_mode((400, 300))

# 导入与鼠标事件相关的变量
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, MOUSEWHEEL

running = True
while running:
    for e in event.get():
        # 显示不同鼠标事件的信息
        if e.type == MOUSEBUTTONDOWN:
            print('按下鼠标', e)
        elif e.type == MOUSEBUTTONUP:
            print('释放鼠标', e)
        elif e.type == MOUSEMOTION:
            print('移动鼠标', e)
        elif e.type == MOUSEWHEEL:
            # 当玩家滚动滚轮时，结束游戏循环
            print('滚动滚轮', e)
            running = False
