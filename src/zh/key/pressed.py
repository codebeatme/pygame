# 导入 key 模块和其他相关内容，并创建游戏窗口
from pygame import key, event, display, K_UP, K_RCTRL
display.set_mode([800, 600])

while True:
    # 显式的调用 pump 函数
    event.pump()
    # 获取所有按键的按下状态
    ps = key.get_pressed()

    # 如果同时按下了上方向键和右 Ctrl 键，则游戏结束
    if ps[K_UP] and ps[K_RCTRL]:
        break