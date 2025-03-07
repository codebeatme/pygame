from pygame import mouse, event, display, MOUSEBUTTONDOWN
display.set_mode((400, 300))

running = True
while running:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            (x, y) = mouse.get_rel()

            if x > 0:
                print('向右')
            elif x < 0:
                print('向左')

            if y > 0:
                print('向下')
            elif y < 0:
                print('向上')

            if x == 0 and y == 0:
                running = False