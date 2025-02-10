from pygame import Surface

# 创建游戏表面和子表面
s = Surface([800, 600])
c = s.subsurface(0, 0, 10, 10)
cc = c.subsurface(0, 0, 10, 10)

# cc 的父表面为 c
print(cc.get_parent() == c)
# cc 的顶级表面为 s
print(cc.get_abs_parent() == s)
# 获取 s 的父表面和顶级表面
print(s.get_parent())
print(s.get_abs_parent())