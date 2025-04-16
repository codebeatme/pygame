from pygame import display, event, joystick, QUIT, JOYDEVICEADDED
display.set_mode((400, 300))
joystick.init()

from pygame import JOYAXISMOTION

jss = []
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            jss.append(j)
            print(j.get_name())
        elif e.type == JOYAXISMOTION:
            if e.axis == 0 or e.axis == 1:
                print('左摇杆')

                if e.axis == 0:
                    if e.value > 0.3:
                        print('向右移动')
                    elif e.value < -0.3:
                        print('向左移动')
                    else:
                        print('停止水平移动')
                elif e.axis == 1:
                    if e.value > 0.3:
                        print('向下移动')
                    elif e.value < -0.3:
                        print('向上移动')
                    else:
                        print('停止垂直移动')
            elif e.axis == 5:
                print('右扳机键')

                if e.value > -0.3:
                    print('攻击')