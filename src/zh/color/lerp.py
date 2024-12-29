from pygame import Color

# 计算白色与黑色之间的线性插值
c = Color(255, 255, 255)
print(f'amount：{c.lerp("#000000", 0.1)}')
print(f'amount：{c.lerp("#000000", 0.9)}')
