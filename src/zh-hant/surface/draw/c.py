from pygame import display, Surface, SRCALPHA

s = Surface([50, 50], SRCALPHA)
s.fill('#00FF0099', [0, 0, 50, 50])
w = display.set_mode([400, 300])
cs = s.convert()
csa = s.convert_alpha()

w.blit(cs, (0, 0))
w.blit(csa, (100, 100))
display.flip()

import time
time.sleep(3)