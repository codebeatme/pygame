from pygame import Surface

# 建立大小為 800x600 的表面
s = Surface((800, 600))
# 顯示表面的大小
print(f'寬度：{s.get_width()} 高度：{s.get_height()} 大小：{s.get_size()}')