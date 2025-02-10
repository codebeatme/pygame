from pygame import Surface

# 建立遊戲表面和子表面
s = Surface([800, 600])
c = s.subsurface(100, 200, 50, 50)
cc = c.subsurface(12, 13, 1, 1)

# 取得表面 cc 在父表面和頂層表面中的位置
print(cc.get_offset())
print(cc.get_abs_offset())