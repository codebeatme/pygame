from pygame import font, image, display
w = display.set_mode([400, 300])

img = image.load('candy.png')

font.init()
f = font.Font(size=30)
ts = f.render('Hello', True, [2, 255, 0], '#ffffff')

w.blit(ts, (50, 50))
w.blit(img, (100, 100))

display.flip()
import time
time.sleep(3)