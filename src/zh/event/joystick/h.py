from pygame import display, event, QUIT
display.set_mode((400, 300))

from pygame import joystick, JOYDEVICEADDED
joystick.init()
jss = []

from pygame import JOYHATMOTION

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYHATMOTION:
            if e.instance_id == 0:
                (x, y) = e.value

                if x == 1:
                    print('开始向右移动')
                elif x == -1:
                    print('开始向左移动')
                else:
                    print('结束水平移动')
                
                if y == 1:
                    print('开始向上移动')
                elif y == -1:
                    print('开始向下移动')
                else:
                    print('结束垂直移动')