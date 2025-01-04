from pygame import Rect

# 建立一個矩形，並計算與其他矩形的並集
r = Rect(0, 0, 10, 10)
print(r.union(30, 30, 10, 10))
print(r.unionall([(30, 30, 10, 10), [[-10, -10], [5, 5]]]))
r.union_ip((-10, -10, 15, 15))
print(r)