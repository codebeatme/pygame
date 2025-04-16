from pygame import display, event, QUIT
display.set_mode((400, 300))

from pygame import joystick, JOYDEVICEADDED, JOYHATMOTION
joystick.init()
jss = []

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
                    print('開始向右移動')
                elif x == -1:
                    print('開始向左移動')
                else:
                    print('結束水平移動')
                
                if y == 1:
                    print('開始向上移動')
                elif y == -1:
                    print('開始向下移動')
                else:
                    print('結束垂直移動')