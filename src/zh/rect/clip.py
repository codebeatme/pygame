from pygame import Rect

# 创建两个矩形并计算他们重叠的部分
r1 = Rect(0, 0, 100, 100)
r2 = Rect(-50, -50, 100, 100)
print(r2.clip(r1))

# 矩形 r2 与参数表示的矩形不重叠
print(r2.clip([100, 100], [10, 10]))