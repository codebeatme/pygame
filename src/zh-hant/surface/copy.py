from pygame import Surface, SRCALPHA

# 建立一個表面，然後複製他
s1 = Surface([400, 300], SRCALPHA, 16)
s1.set_colorkey('#ff0000')
s1.set_alpha(100)
s2 = s1.copy()

# s2 的透明色彩鍵為 None，與 s1 不同
print(f'複製的表面：{s2.get_size()} {s2.get_flags()} {s2.get_bitsize()} {s2.get_colorkey()} {s2.get_alpha()}')