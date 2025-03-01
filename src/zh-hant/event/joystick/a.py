from pygame import display, event, joystick, QUIT, JOYDEVICEADDED
display.init()
joystick.init()
display.set_mode((400, 300))

from pygame import JOYAXISMOTION

jss = []
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYAXISMOTION:
            if e.axis == 0 or e.axis == 1:
                print('左搖桿')

                if e.axis == 0:
                    if e.value > 0.3:
                        print('向右移動')
                    elif e.value < -0.3:
                        print('向左移動')
                    else:
                        print('停止水平移動')
                elif e.axis == 1:
                    if e.value > 0.3:
                        print('向下移動')
                    elif e.value < -0.3:
                        print('向上移動')
                    else:
                        print('停止垂直移動')
            elif e.axis == 5:
                print('右扳機鍵')

                if e.value > -0.3:
                    print('攻擊')