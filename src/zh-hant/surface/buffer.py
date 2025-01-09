from pygame import Surface

s = Surface((100, 100))
# 取得表面的緩沖區物件
b = s.get_buffer()
# 取得表面緩沖區的位址
print(f'緩沖區位址：{s._pixels_address}')