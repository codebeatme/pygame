from pygame import mouse, event, display
display.set_mode((400, 300))

running = True
while running:
    event.pump()
    (x, y) = mouse.get_pos()

    if x > 200 and y > 150:
        running = False

    if x > 200 and y < 150:
        mouse.set_pos(x - 200, y)