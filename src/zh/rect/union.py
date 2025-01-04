from pygame import Rect

# 创建一个矩形，并计算与其他矩形的并集
r = Rect(0, 0, 10, 10)
print(r.union(30, 30, 10, 10))
print(r.unionall([(30, 30, 10, 10), [[-10, -10], [5, 5]]]))
r.union_ip((-10, -10, 15, 15))
print(r)