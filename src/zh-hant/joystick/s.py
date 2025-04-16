from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
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

    for i in range(j.get_numaxes()):
        d = j.get_axis(i)
        if 1 - d < 0.1:
            print('最下|最右|扳機鍵最大幅度', d, i)

    if j.get_numhats() > 0:
        (x, y) = j.get_hat(0)
        if x or y:
            print('方向鍵被按下', x, y)
            
    for j in js:
        for i in range(j.get_numbuttons()):
            if j.get_button(i):
                print('按鍵被按下', i)
