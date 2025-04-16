# 导入并初始化相关模块，创建游戏窗口
from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 保存控制器对象的列表
js = []

running = True
while running:
    # 处理控制器连接事件，退出事件
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            js.append(j)

    # 角色索引
    pi = 0

    # 遍历所有的控制器
    for j in js:
        pi += 1
        
        # 如果按下第一个按键，则视为攻击命令
        if j.get_numbuttons() > 0 and j.get_button(0):
            print(f'角色 {pi} 攻击')

        # 根据第一个方向键来移动角色
        if j.get_numhats() > 0:
            (x, y) = j.get_hat(0)
            
            if x == -1:
                print(f'角色 {pi} 向左')
            elif x == 1:
                print(f'角色 {pi} 向右')

            if y == -1:
                print(f'角色 {pi} 向下')
            elif y == 1:
                print(f'角色 {pi} 向上')

        # 根据右扳机键判断是否跳跃，假设 5 对应了右扳机键
        if j.get_numaxes() > 5 and j.get_axis(5) > 0.2:
            print(f'角色 {pi} 跳跃')
