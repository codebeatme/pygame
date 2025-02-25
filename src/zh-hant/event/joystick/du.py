from pygame import display, event
display.set_mode((400, 300))

from pygame import joystick, JOYDEVICEADDED
joystick.init()

from pygame import JOYBUTTONDOWN, JOYBUTTONUP

jss = []
running = True
while running:
    for e in event.get():
        if e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYBUTTONDOWN:
            
            
            if e.instance_id == 0:
                print('按鍵', e.button)

        elif e.type == JOYBUTTONUP:
            
            if e.instance_id == 1 and e.button == 7:
                running = False