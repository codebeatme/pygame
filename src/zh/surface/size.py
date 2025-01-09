from pygame import Surface

# 创建大小为 800x600 的表面
s = Surface((800, 600))
# 显示表面的大小
print(f'宽度：{s.get_width()} 高度：{s.get_height()} 大小：{s.get_size()}')