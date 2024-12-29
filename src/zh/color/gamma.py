from pygame import Color

# 对颜色进行伽玛校正
c = Color(255, 150, 50, 100)
print(c.correct_gamma(1.5))