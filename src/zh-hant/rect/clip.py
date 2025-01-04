from pygame import Rect

# 建立兩個矩形並計算他們重疊的部分
r1 = Rect(0, 0, 100, 100)
r2 = Rect(-50, -50, 100, 100)
print(r2.clip(r1))

# 矩形 r2 與參數表示的矩形不重疊
print(r2.clip([100, 100], [10, 10]))