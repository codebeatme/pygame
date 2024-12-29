from pygame import Color

red = Color(255, 0, 0)
print(f'紅：{red.r} 綠：{red.g} 藍：{red.b} 透明度：{red.a}')
# 將色彩改為透明的
red.a = 0
print(f'透明度：{red.a}')

# 以 CMY 格式取得和設定色彩資訊
color1 = Color('#3399ff')
print(f'cmy：{color1.cmy} 紅：{color1.r} 綠：{color1.g} 藍：{color1.b}')
color1.cmy = (0.81, 0.4123, 0.0001)
print(f'cmy：{color1.cmy} 紅：{color1.r} 綠：{color1.g} 藍：{color1.b}')

# 顯示 HSVA，HSLA，I1I2I3 格式的色彩資訊
color2 = Color((200, 100, 50, 25))
print(f'hsva：{color2.hsva}')
print(f'hsla：{color2.hsla}')
print(f'i1i2i3：{color2.i1i2i3}')

# 顯示 RGBA 格式的色彩資訊
print(Color([50, 150, 250, 100]).normalize())