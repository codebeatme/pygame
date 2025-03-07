# 导入相关模块，创建游戏窗口
from pygame import display, event, mouse
display.set_mode((800, 600))

while True:
    # 显式的调用 pump 函数
    event.pump()
    # 获取鼠标位置
    (x, y) = mouse.get_pos()

    # 当鼠标位于窗口左上角时，他将被移至中心
    if x < 100 and y < 100:
        mouse.set_pos([400, 300])

    # 当鼠标位于窗口右下角时，结束游戏循环
    if x > 700 and x < 800 and y > 500 and y < 600:
        break