from pygame import sprite, Surface, Rect, image, BLEND_ADD, BLEND_SUB, BLEND_RGBA_MIN, SRCALPHA

class My(sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = Surface((100, 200), SRCALPHA)
        self.image.fill('#FF0000')

        self.rect = Rect(0, 0, 10, 10)
        self.visible = 0
        self.dirty  = 1

class W1(sprite.WeakSprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = Surface((100, 200), SRCALPHA)
        self.image.fill('#0000FF66')

        self.rect = Rect(0, 100, 10, 10)
        self.layer = 200

class W2(sprite.DirtySprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = Surface((200, 200), SRCALPHA)
        self.image.fill('#00FF0099')

        self.rect = Rect(0, 100, 10, 10)
        self.layer = 400
        self.visible = 1
        self.dirty  = 2
        # self.blendmode = BLEND_SUB
        self.source_rect = Rect(0, 0, 150, 150)

class W3(sprite.DirtySprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = candy

        self.rect = Rect(0, 0, 10, 10)
        self.layer = 400
        self.visible = 1
        # self.dirty  = 2
        self.count = 0
        # self.blendmode = BLEND_SUB
        self.source_rect = Rect(0, 0, 10, 20)

    def update(self, *args, **kwargs):
        self.count += 1
        # print(self.count)
        return super().update(*args, **kwargs)

data = open('Z:\\code\\beat\\pygame\\src\\zh\\sprite\\candy.png')
candy = image.load(data, '.png')

from pygame import display
w = display.set_mode((800, 600))
s = Surface((800, 600))

ss = sprite.Sprite()
# ss.image = Surface((300, 300), SRCALPHA)
# ss.image.fill('#FFFF00')
# ss.rect = Rect(300, 300, 100, 100)

g1 = sprite.Group()
g2 = sprite.Group()
g3 = sprite.Group()
m2 = My()
# print(m2.layer)
m2.layer = 1
w1 = W1()
w2 = W2()
w3 = W3()
print(w3.blendmode, w3.source_rect, w3.visible, w3.dirty)
# g1.add(m2)
# m2.layer = 1
g1.add(w2, w3, ss)
print(m2.layer, w2.layer)
# m2.add()

while True:
    # s.fill(0)
    # g1.update()
    # g1.draw(w)
    g1.update()
    # g1.draw(s)

    w.blit(s, (0, 0))
    # print(type(m2.groups()))

    # m2.rect.x += 1

    display.flip()