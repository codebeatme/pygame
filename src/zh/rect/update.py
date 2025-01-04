from pygame import Rect

# X 坐标 10，Y 坐标 20，宽度 30，高度 40
r = Rect(10, 20, 30, 40)
# 更新矩形位置和大小，X 和 Y 坐标为 0，宽度和高度为 10
r.update([0, 0], (10, 10))