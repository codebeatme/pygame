from pygame import Rect

# 建立一個矩形
r1 = Rect(0, 0, 10, 10)
# 矩形的寬度增加 3，高度增加 2
r2 = r1.inflate(3, 2)
print(r2)
# 調整矩形 r1 自身的大小
r1.inflate_ip((-20, -30))
print(r1)

# 建立一個矩形
r3 = Rect(0, 0, 10, 10)
# 矩形的寬度和高度增加一倍
r4 = r3.scale_by(2)
print(r4)
# 縮放矩形 r3 自身
r3.scale_by_ip(2.5, 3.5)
print(r3)
