from pygame import Rect

# X 座標 10，Y 座標 20，寬度 30，高度 40
r = Rect(10, 20, 30, 40)
# 更新矩形位置和大小，X 和 Y 座標為 0，寬度和高度為 10
r.update([0, 0], (10, 10))