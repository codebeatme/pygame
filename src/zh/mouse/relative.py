# 导入相关模块，创建游戏窗口
from pygame import display, event, mouse, MOUSEBUTTONDOWN
display.set_mode((800, 600))

running = True
while running:
    # 隐式的调用 pump 函数
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            # 获取鼠标的移动距离
            (x, y) = mouse.get_rel()
            print('水平移动距离', x, '垂直移动距离', y)

            # 如果实际的移动距离大于 400，则游戏循环结束
            d = (x**2 + y**2) ** 0.5
            print('实际移动距离', d)

            if d > 400:
                running = False