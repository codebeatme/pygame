from pygame import Surface, SRCALPHA

# 创建表面对象
s1 = Surface((800, 600))
# 将坐标 0 0 的像素设置为透明的红色
s1.set_at((0, 0), (255, 50, 0, 100))
print(f'坐标 0 0 处的颜色：{hex(s1.get_at_mapped((0, 0)))}')

# 创建支持透明度的表面对象
s2 = Surface((800, 600), SRCALPHA)
# 将坐标 0 0 的像素设置为透明的红色
s2.set_at((0, 0), (255, 50, 0, 100))
print(f'坐标 0 0 处的颜色：{hex(s2.get_at_mapped((0, 0)))}')
