from pygame import Surface, image, display

img = image.load('stone.png')

s1 = Surface([300, 120])
s1.blit(img, (0, 0))

s2 = Surface([300, 120])
s2.blit(img, (0, 0))
s2.set_colorkey('#C0C0C0')
print(s2.get_colorkey())

w = display.set_mode((800, 600))
w.blit(s1, (100, 100))
w.blit(s2, (100, 220))
display.flip()
import time
time.sleep(4)