from pygame import key, event, display, KEYDOWN, KEYUP, QUIT
display.set_mode((400, 300))

key.set_repeat(1000, 500)
print(key.get_repeat())

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            print('按下', e)
        elif e.type == KEYUP:
            print('释放', e)