from pygame import event, display
w = display.set_mode([400, 300])

from pygame import QUIT, WINDOWMOVED
running = True
while running:
    es = event.get(QUIT)

    for e in es:
        if e.type == QUIT:
            running = False
        elif e.type == WINDOWMOVED:
            print(e.x, e.y)