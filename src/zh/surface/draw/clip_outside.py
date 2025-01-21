from pygame import Surface

s = Surface([100, 100])
# 剪辑区域超出了表面的大小
s.set_clip((0, 0, 110, 120))
print(f'当前剪辑区域：{s.get_clip()}')