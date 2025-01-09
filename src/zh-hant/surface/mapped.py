from pygame import Surface

# 建立色彩深度為 8 的表面
s1 = Surface([400, 300], depth=8)
# 兩個不同色彩的對映整數相同
m1 = s1.map_rgb([255, 0, 0])
print(m1, s1.unmap_rgb(m1))
m2 = s1.map_rgb([250, 5, 5])
print(m2, s1.unmap_rgb(m2))
# 對映整數不考慮透明度
m3 = s1.map_rgb([255, 0, 0, 100])
print(m3, s1.unmap_rgb(m3))

# 建立色彩深度為 32 的表面
s2 = Surface([400, 300], depth=32)
# 相同的色彩在 s1 和 s2 中的對映整數不同
m3 = s2.map_rgb([255, 0, 0])
print(m3, s2.unmap_rgb(m3))
