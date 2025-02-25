from pygame import display, event, QUIT
display.set_mode((400, 300))

from pygame import joystick
joystick.init()

from pygame import JOYDEVICEADDED, JOYDEVICEREMOVED

jss = []
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            jss.append(j)

            print('添加控制器', j.get_id(), j.get_instance_id())
        elif e.type == JOYDEVICEREMOVED:
            for j in jss:
                if j.get_instance_id() == e.instance_id:
                    jss.remove(j)

                    print('移除控制器', j.get_id(), j.get_instance_id())
                    break