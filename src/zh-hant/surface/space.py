from pygame import Surface

# 建立色彩深度為 15 的表面
s = Surface((100, 100), depth=15)
print(f'一個像素需要 {s.get_bitsize()} 個 bit，{s.get_bytesize()} 個位元組')
print(f'一行像素需要 {s.get_pitch()} 個位元組')