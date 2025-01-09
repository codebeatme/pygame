from pygame import Surface

# 创建颜色深度为 8 的表面
s1 = Surface([400, 300], depth=8)
# 两个不同颜色的映射整数相同
m1 = s1.map_rgb([255, 0, 0])
print(m1, s1.unmap_rgb(m1))
m2 = s1.map_rgb([250, 5, 5])
print(m2, s1.unmap_rgb(m2))
# 映射整数不考虑透明度
m3 = s1.map_rgb([255, 0, 0, 100])
print(m3, s1.unmap_rgb(m3))

# 创建颜色深度为 32 的表面
s2 = Surface([400, 300], depth=32)
# 相同的颜色在 s1 和 s2 中的映射整数不同
m3 = s2.map_rgb([255, 0, 0])
print(m3, s2.unmap_rgb(m3))
