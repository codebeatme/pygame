from pygame import Rect

# 判斷矩形 r1 是否能夠完全包含其他矩形
r1 = Rect(0, 0, 10, 10)
r2 = Rect(-10, -10, 10, 10)
print(r1.contains(r2))
print(r1.contains([5, 5], [10, 10]))
print(r1.contains(2, 2, 6, 6))