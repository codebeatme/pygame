from pygame import Rect, Vector2

# 建立一個矩形，並計算移動後的矩形
r1 = Rect(0, 0, 10, 20)
r2 = r1.move(11, 9)
print(r2)

# 移動矩形 r1 自身
r1.move_ip(Vector2(5, 5))
print(r1)