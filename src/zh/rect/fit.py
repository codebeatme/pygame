from pygame import Rect

# 创建一个矩形，并填充到其他几个矩形中
r1 = Rect(0, 0, 100, 100)
print(r1.fit(100, 100, 100, 50))
print(r1.fit((-20, -50), (200, 300)))