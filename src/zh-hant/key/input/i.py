from pygame import key, display, event, font, KEYDOWN, K_ESCAPE
w = display.set_mode((400, 300))
font.init()
f = font.Font(size=30)

from pygame import TEXTINPUT, TEXTEDITING, K_LCTRL
c = ''
t = ''
o = True

running = True
while running:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = False
            elif e.key == K_LCTRL:
                if o:
                    key.stop_text_input()
                else:
                    key.start_text_input()

                o = not o
        elif e.type == TEXTEDITING:
            c = e.text
        elif e.type == TEXTINPUT:
            t += e.text

    w.fill('#000000')
    sc = f.render(c, True, '#FF0000')
    tc = f.render(t, True, '#00FF00')
    w.blit(sc, (0, 0))
    w.blit(tc, (0, 50))
    display.flip()
