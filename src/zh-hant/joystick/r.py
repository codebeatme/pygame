from pygame import joystick, display, event, JOYDEVICEADDED, JOYBUTTONDOWN, QUIT
display.set_mode((400, 300))
joystick.init()

js = []
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            js.append(j)

            if j.rumble(0.5, 1, 3000):
                print('震動回饋已啓動')
        elif e.type == JOYBUTTONDOWN:
            for j in js:
                if j.get_instance_id() == e.instance_id:
                    j.stop_rumble()
                    print('震動回饋已停止')