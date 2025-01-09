from pygame import Surface, SRCALPHA

# 建立支援透明度的表面
s = Surface([400, 300], SRCALPHA)
# 通過 & 判斷表面是否支援透明度
f = s.get_flags()
print(f'表面支援色彩透明度？{f & SRCALPHA == SRCALPHA}')