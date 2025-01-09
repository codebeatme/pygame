from pygame import Surface

s = Surface((100, 100))
# 获取表面的缓冲区对象
print(s.get_view('1'))