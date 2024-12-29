from pygame import font
font.init()

f = font.Font('NotoSans-italic.ttf', 24)
f.bold = True

from pygame import display
w = display.set_mode([400, 300])
s = f.render('Hello', True, [2, 255, 0])
w.blit(s, (50, 50))
display.flip()

import time
time.sleep(5)