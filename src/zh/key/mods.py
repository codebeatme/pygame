# 导入 key 模块和其他相关内容，并创建游戏窗口
from pygame import key, event, display, K_a, K_q, KMOD_LALT, KMOD_LCTRL
display.set_mode([800, 600])

# 临时将左 Alt 键和左 Ctrl 键设置为按下
key.set_mods(KMOD_LALT | KMOD_LCTRL)

while True:
    # 显式的调用 pump 函数
    event.pump()
    # 获取所有按键和修饰按键的按下状态
    ps = key.get_pressed()
    mods = key.get_mods()

    # 如果按下左 Ctrl 键和 A 键，则游戏结束
    if ps[K_a] and (mods & KMOD_LCTRL):
        print('角色攻击')

    # 如果按下左 Alt 键和 Q 键，则游戏结束
    if ps[K_q] and (mods & KMOD_LALT):
        break