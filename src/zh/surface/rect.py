from pygame import Surface

# 创建大小为 800x600 的表面
s = Surface((800, 600))
# 根据表面创建矩形，并设置左上角坐标为 10 10
print(s.get_rect(topleft=(10, 10)))