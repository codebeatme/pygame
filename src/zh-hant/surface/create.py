# 匯入 Surface 物件
from pygame import Surface

# 建立大小為 800x600，色彩深度為 16 的表面
s1 = Surface((800, 600), depth=16)
print(f'色彩深度：{s1.get_bitsize()}')
# 表面 s2 的色彩深度與 s1 相同
s2 = Surface([400, 300], 0, s1)
print(f'色彩深度：{s2.get_bitsize()}')
