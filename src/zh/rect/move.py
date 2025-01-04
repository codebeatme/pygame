from pygame import Rect, Vector2

# 创建一个矩形，并计算移动后的矩形
r1 = Rect(0, 0, 10, 20)
r2 = r1.move(11, 9)
print(r2)

# 移动矩形 r1 自身
r1.move_ip(Vector2(5, 5))
print(r1)