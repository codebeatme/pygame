# 导入相关模块，创建游戏窗口
from pygame import display, event, mouse
display.set_mode((800, 600))

while True:
    # 显式的调用 pump 函数
    event.pump()
    # 获取鼠标按键的按下状态
    (l, m, r) = mouse.get_pressed()

    # 如果鼠标左健，右键和滚轮键一同按下，那么游戏循环结束
    if l and r and m:
        break