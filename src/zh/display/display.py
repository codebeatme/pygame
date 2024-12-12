from pygame import display, NOFRAME, SCALED

display.set_caption('Pygame')
display.set_mode([800, 600], SCALED)

import time
time.sleep(1)

display.toggle_fullscreen()

time.sleep(3)