# 导入相关模块，创建游戏窗口
from pygame import display, event, mouse
display.set_mode((800, 600))

count = 0
focused = True
while True:
    # 显式的调用 pump 函数
    event.pump()

    # 判断鼠标是否离开了显示区域
    if focused and not mouse.get_focused():
        focused = False
        count += 1
        print('鼠标离开了显示区域')

    # 判断鼠标是否进入了显示区域
    if not focused and mouse.get_focused():
        focused = True
        count += 1
        print('鼠标进入了显示区域')

    # 切换次数达到 5 次时，结束游戏
    if count == 5:
        break