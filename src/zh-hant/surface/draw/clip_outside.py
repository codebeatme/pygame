from pygame import Surface

s = Surface([100, 100])
# 裁剪區域超出了表面的大小
s.set_clip((0, 0, 110, 120))
print(f'目前裁剪區域：{s.get_clip()}')