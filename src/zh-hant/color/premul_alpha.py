from pygame import Color

# 預先計算透明度
c = Color(150, 20, 200, 50)
print(c.premul_alpha())
