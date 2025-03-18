from pygame import key, event, display
display.set_mode((400, 300))

from pygame import K_LCTRL, K_RCTRL
while True:
    event.pump()

    ps = key.get_pressed()
    if ps[K_LCTRL] and ps[K_RCTRL]:
        break