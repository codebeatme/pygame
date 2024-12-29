from pygame import Color

# 對色彩進行伽瑪校正
c = Color(255, 150, 50, 100)
print(c.correct_gamma(1.5))