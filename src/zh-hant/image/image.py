from pygame import image

sky = image.load('sky.webp')

data = open('candy.png')
candy = image.load(data, '.png')

from pygame import display, SCALED
w = display.set_mode([800, 600], SCALED)
w.blit(sky, (0, 0))
w.blit(candy, (200, 200))
display.update()

import time
time.sleep(1)
