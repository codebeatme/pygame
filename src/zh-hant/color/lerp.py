from pygame import Color

# 計算白色與黑色之間的線性插補
c = Color(255, 255, 255)
print(f'amount：{c.lerp("#000000", 0.1)}')
print(f'amount：{c.lerp("#000000", 0.9)}')
