from pygame import Rect

# 建立一個矩形，並更正錯誤的矩形大小
r = Rect(0, 0, -30, -40)
r.normalize()
print(r)