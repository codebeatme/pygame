from pygame import Surface, SRCALPHA

# 创建支持透明度的表面
s = Surface([400, 300], SRCALPHA)
# 通过 & 判断表面是否支持透明度
f = s.get_flags()
print(f'表面支持颜色透明度？{f & SRCALPHA == SRCALPHA}')