from pygame import Color

color1 = Color(100, 120, 200)
color2 = Color([50, 200, 90, 100])

# 在色彩物件之間，進行加，減，乘運算
print(f'{color1} + {color2} = {color1 + color2}')
print(f'{color1} - {color2} = {color1 - color2}')
print(f'{color1} * {color2} = {color1 * color2}')

# 在色彩物件之間，進行整除運算
print(f'{color1} // {color2} = {color1 // color2}')

# 在色彩物件之間，進行取余運算
print(f'{color1} % {color2} = {color1 % color2}')

# 比較兩個色彩
color3 = Color(100, 120, 200, 200)
print(f'{color1} == {color3} {color1 == color3}')
print(f'{color1} != {color2} {color1 != color2}')