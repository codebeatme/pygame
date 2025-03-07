from pygame import mouse, event, display, QUIT, MOUSEBUTTONUP
display.set_mode((400, 300))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONUP:
            v = mouse.get_visible()
            mouse.set_visible(not v)