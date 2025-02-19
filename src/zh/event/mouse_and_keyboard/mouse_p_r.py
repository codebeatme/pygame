from pygame import display, event
w = display.set_mode((400, 300))

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from pygame import BUTTON_LEFT, BUTTON_RIGHT, BUTTON_MIDDLE

running = True
while running:
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button == BUTTON_LEFT:
                print(f'鼠标位置：{e.pos}')
        elif e.type == MOUSEBUTTONUP:
            if e.button == BUTTON_RIGHT:
                print(f'结束')
                running = False