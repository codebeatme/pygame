# 导入并初始化相关模块，创建游戏窗口
from pygame import display, event, joystick, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 导入与控制器事件相关的变量
from pygame import JOYAXISMOTION
# 保存 JoystickType 对象的列表
jss = []

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYAXISMOTION:
            print(e)
            # 判断触发事件的轴装置是否为右扳机键
            if e.axis == 5:
                # 判断右扳机键的移动程度，是否足以发动攻击
                if e.value > -0.3:
                    print('攻击')
                else:
                    print('停止攻击')