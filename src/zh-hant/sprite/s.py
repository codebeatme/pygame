from pygame import sprite, image, display, event, QUIT
w = display.set_mode([400, 300])

g = sprite.Group()
s = image.load('candy.png')

class Candy(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = s
        self.rect = s.get_rect(topleft=(100, 100))

g.add(Candy())

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    w.fill(0)
    g.draw(w)
    display.flip()