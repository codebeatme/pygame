from pygame import Rect

# 创建一个矩形，并更正错误的矩形大小
r = Rect(0, 0, -30, -40)
r.normalize()
print(r)