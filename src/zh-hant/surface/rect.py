from pygame import Surface

# 建立大小為 800x600 的表面
s = Surface((800, 600))
# 根據表面建立矩形，並設定左上角座標為 10 10
print(s.get_rect(topleft=(10, 10)))