from pygame import Rect, Vector2

# 建立一個矩形，並計算線段在該矩形中的部分
r = Rect(0, 0, 100, 100)
# 線段的一部分在矩形中
print(r.clipline(-1, -1, 50, 50))
# 線段完全在矩形中
print(r.clipline((50, 50), [60, 60]))
# 線段穿過了矩形
print(r.clipline(Rect(10, -10, 10, 110)))
# 線段在矩形外
print(r.clipline(Vector2(-1, 0), Vector2(0, 100)))