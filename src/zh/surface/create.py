# 导入 Surface 对象
from pygame import Surface

# 创建大小为 800x600，颜色深度为 16 的表面
s1 = Surface((800, 600), depth=16)
print(f'颜色深度：{s1.get_bitsize()}')
# 表面 s2 的颜色深度与 s1 相同
s2 = Surface([400, 300], 0, s1)
print(f'颜色深度：{s2.get_bitsize()}')
