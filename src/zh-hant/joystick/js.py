from pygame import joystick, display, event, JOYDEVICEADDED, JOYDEVICEREMOVED, QUIT
display.set_mode((400, 300))
joystick.init()

js = []
# for i in range(joystick.get_count()):
#     j = joystick.Joystick(i)
#     js.append(j)
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            js.append(j)
            print('新增控制器', j.get_instance_id(), j.get_name(), j.get_power_level(), joystick.get_count())
        elif e.type == JOYDEVICEREMOVED:
            for j in js:
                if j.get_instance_id() == e.instance_id:
                    js.remove(j)
                    print('移除控制器', e.instance_id)
                    break
        