from pygame import Rect

# 矩形 r1 作为容器
r1 = Rect(0, 0, 100, 100)

# 矩形 r2 位于 r1 的右上方
r2 = Rect(500, -500, 50, 50)
# 固定在 r1 内部（右上角）
print(r2.clamp(r1))

# 矩形 r3 位于 r1 的左下方
r3 = Rect(-500, 500, 50, 50)
# 固定在 r1 内部（左下角）
print(r3.clamp(r1))

# 矩形 r4 的一部分与 r1 重合
r4 = Rect(-10, -10, 50, 50)
# 固定在 r1 内部（左上角）
print(r4.clamp(r1))

# 矩形 r5 位于 r1 内部，但中心不相同
r5 = Rect(10, 10, 20, 20)
# 不会发生变化
print(r5.clamp(r1))

# 矩形 r6 比 r1 大
r6 = Rect(-1000, -1000, 200, 200)
# r6 的中心将于 r1 相同
r6.clamp_ip(r1)
print(r6.center, r1.center)