from pygame import mouse, event, display
display.set_mode((400, 300))

while True:
    event.pump()
    (l, m, r) = mouse.get_pressed()

    if l and r and not m:
        break