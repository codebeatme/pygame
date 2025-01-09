from pygame import Surface, SRCALPHA

# 创建支持透明度的表面
s = Surface((800, 600), SRCALPHA)

# 在表面绘制不透明与透明度为 1 的矩形
from pygame import draw
draw.rect(s, '#ff0000', [0, 0, 50, 50])
draw.rect(s, '#ff000001', [50, 0, 50, 50])
print(f'表面边界：{s.get_bounding_rect()}')

# 将表面自身的透明度设置为 0
s.set_alpha(0)
print(f'表面边界（透明度大于等于 2）：{s.get_bounding_rect(2)}')