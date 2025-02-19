from pygame import display, event
w = display.set_mode((400, 300))

from pygame import MOUSEMOTION

running = True
while running:
    for e in event.get():
        if e.type == MOUSEMOTION:
            print('位置', e.pos)

            (right, down) = e.rel
            if right == 1:
                print('右移')
            else:
                print('左移')

            if down == 1:
                print('下移')
            else:
                print('上移')

            (l, m, r) = e.buttons
            print(l, m, r)
            if m == 1:
                running = False