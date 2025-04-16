import random
from pygame import sprite, image, display, event, time, QUIT, MOUSEBUTTONUP, BUTTON_LEFT
w = display.set_mode([400, 300])
c = time.Clock()

img_c = image.load('candy.png')
img_l = image.load('laser.png')

class Candy(sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = img_c
        self.rect = img_c.get_rect(center=pos)

class Laser(sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = img_l
        self.rect = img_l.get_rect(center=pos)

    def update(self, *args, **kwargs):
        if not kwargs['stop']:
            self.rect.centery -= 1
        return super().update(*args, **kwargs)

cs = sprite.Group()
cs.add(Candy((50, 50)), [Candy((100, 50)), [Candy((150, 50)), Candy((200, 50))]])
Candy((300, 200)).add(cs)

ls = sprite.Group()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONUP:
            if e.button == BUTTON_LEFT:
                ls.add(Laser(e.pos))

    w.fill(0)
    cs.draw(w)
    ls.update(stop=False if random.randint(1, 100) < 25 else True)
    ls.draw(w)
    display.flip()
    c.tick(60)