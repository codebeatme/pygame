from pygame import Surface, SRCALPHA

# 建立支援透明度的表面
s = Surface((800, 600), SRCALPHA)

# 在表面繪製不透明與透明度為 1 的矩形
from pygame import draw
draw.rect(s, '#ff0000', [0, 0, 50, 50])
draw.rect(s, '#ff000001', [50, 0, 50, 50])
print(f'表面界限：{s.get_bounding_rect()}')

# 將表面自身的透明度設定為 0
s.set_alpha(0)
print(f'表面界限（透明度大於等於 2）：{s.get_bounding_rect(2)}')