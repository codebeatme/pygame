from pygame import Color

color1 = Color(100, 120, 200)
color2 = Color([50, 200, 90, 100])

# 在颜色对象之间，进行加，减，乘运算
print(f'{color1} + {color2} = {color1 + color2}')
print(f'{color1} - {color2} = {color1 - color2}')
print(f'{color1} * {color2} = {color1 * color2}')

# 在颜色对象之间，进行整除运算
print(f'{color1} // {color2} = {color1 // color2}')

# 在颜色对象之间，进行取余运算
print(f'{color1} % {color2} = {color1 % color2}')

# 比较两个颜色
color3 = Color(100, 120, 200, 200)
print(f'{color1} == {color3} {color1 == color3}')
print(f'{color1} != {color2} {color1 != color2}')

# 除数为 0 的情况
print(Color(0xFFFFFFFF) // Color(0x00000000))
print(Color(0xFFFFFFFF) % Color(0x00000000))