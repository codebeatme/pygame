from pygame import Surface, SRCALPHA

s1 = Surface([100, 100], SRCALPHA)
from pygame import draw
draw.rect(s1, '#ff0000', [0, 0, 50, 50])
draw.rect(s1, '#ff000099', [50, 50, 50, 50])

s2 = Surface((100, 100))
from pygame import image
i = image.load('sky.webp')
s2.blit(i, (0, 0))
s2.set_alpha(120)
s2.get_alpha()

from pygame import display
w = display.set_mode((800, 600))
w.blit(s1, (100, 100))
w.blit(s2, (200, 200))
display.flip()

import time
time.sleep(3)