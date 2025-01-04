from pygame import Rect, Vector2

# 创建一个矩形，并计算线段在该矩形中的部分
r = Rect(0, 0, 100, 100)
# 线段的一部分在矩形中
print(r.clipline(-1, -1, 50, 50))
# 线段完全在矩形中
print(r.clipline((50, 50), [60, 60]))
# 线段穿过了矩形
print(r.clipline(Rect(10, -10, 10, 110)))
# 线段在矩形外
print(r.clipline(Vector2(-1, 0), Vector2(0, 100)))