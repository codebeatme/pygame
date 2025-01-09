from pygame import Surface

# 建立色彩深度為 16 的表面
s = Surface((100, 100), depth=16)
print(f'一個像素需要 {s.get_bytesize()} 個位元組')