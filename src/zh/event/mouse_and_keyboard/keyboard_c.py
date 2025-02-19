from pygame import display, event
w = display.set_mode((400, 300))

from pygame import KEYDOWN, KEYUP
from pygame import K_w, K_LSHIFT

running = True
while running:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_w:
                print('w 键被按下')
            elif e.key == K_LSHIFT:
                running = False
        elif e.type == KEYUP:
            print(e.unicode)