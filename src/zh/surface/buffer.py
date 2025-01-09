from pygame import Surface

s = Surface((100, 100))
# 获取表面的缓冲区对象
b = s.get_buffer()
# 获取表面缓冲区的地址
print(f'缓冲区地址：{s._pixels_address}')