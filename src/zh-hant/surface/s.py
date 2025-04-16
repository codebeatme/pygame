from pygame import image

stone = image.load('stone.png')
w = stone.get_width()
h = stone.get_height()
s = stone.get_size()
print(w, h, s)

r = stone.get_rect(width=w - 40, height=h - 40)
print(r)