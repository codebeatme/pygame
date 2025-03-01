# 导入初始化相关模块，创建游戏窗口
from pygame import display, event, joystick, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 导入与控制器事件相关的变量
from pygame import JOYHATMOTION
# 保存 JoystickType 对象的列表
jss = []
# 表示水平和垂直的移动方向
h = 0
v = 0

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYHATMOTION:
            # 获取十字键的按下状态
            (x, y) = e.value

            # 根据十字键的按下状态，设置游戏角色的移动方向
            if x == 1:
                h = 1
                print('开始向右移动')
            elif x == -1:
                h = -1
                print('开始向左移动')
            elif h != 0:
                h = 0
                print('取消水平移动')
            
            if y == 1:
                v = 1
                print('开始向上移动')
            elif y == -1:
                v = -1
                print('开始向下移动')
            elif v != 0:
                v = 0
                print('取消垂直移动')