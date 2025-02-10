from pygame import Surface

# 建立遊戲表面和子表面
s = Surface([800, 600])
c = s.subsurface(0, 0, 10, 10)
cc = c.subsurface(0, 0, 10, 10)

# cc 的父表面為 c
print(cc.get_parent() == c)
# cc 的頂層表面為 s
print(cc.get_abs_parent() == s)
# 取得 s 的父表面和頂層表面
print(s.get_parent())
print(s.get_abs_parent())