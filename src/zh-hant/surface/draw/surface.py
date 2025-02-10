from pygame import display, Surface

s = Surface([100, 100])
s.fill('green')

w = display.set_mode([400, 300])
w.blit(s, [100, 100])
display.flip()

import time
time.sleep(3)