import random
from pygame import sprite, image, display, event, time, QUIT, MOUSEBUTTONUP, BUTTON_LEFT
w = display.set_mode([400, 300])
c = time.Clock()

img_c = image.load('candy.png')
img_l = image.load('laser.png')
img_dlc = image.load('doors_leaf_closed.png')

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
        self.rect.centery -= 1
        return super().update(*args, **kwargs)

class Door(sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = img_dlc
        self.rect = img_dlc.get_rect(center=pos)

cs = sprite.Group()
cs.add(Candy((50 * i, 50)) for i in range(1, 8))
cs.add(Candy((50 * i + 10, 70)) for i in range(1, 8))

ls = sprite.Group()

door = Door((200, 150))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONUP:
            if e.button == BUTTON_LEFT:
                ls.add(Laser(e.pos))

    w.fill(0)
    ls.update()

    for l in ls.sprites():
        if sprite.collide_rect(l, door):
            l.kill()

        # rcs = sprite.spritecollide(l, cs, False)
        # if rcs:
        #     l.remove(ls)
        #     cs.remove(rcs)

    sprite.groupcollide(ls, cs, True, True)

    cs.draw(w)
    w.blit(door.image, door.rect)
    ls.draw(w)
    display.flip()
    c.tick(60)