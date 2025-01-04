from pygame import Rect

# 建立一個矩形，並填入到其他幾個矩形中
r1 = Rect(0, 0, 100, 100)
print(r1.fit(100, 100, 100, 50))
print(r1.fit((-20, -50), (200, 300)))