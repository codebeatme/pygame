from pygame import Surface

# 创建颜色深度为 15 的表面
s = Surface((100, 100), depth=15)
print(f'一个像素需要 {s.get_bitsize()} 个 bit，{s.get_bytesize()} 个字节')
print(f'一行像素需要 {s.get_pitch()} 个字节')