from pygame import mouse, image, display, event, QUIT
display.set_mode((400, 300))

candy = image.load('candy.png')
mouse.set_cursor((16, 16), candy)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False