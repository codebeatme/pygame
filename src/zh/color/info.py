from pygame import Color

red = Color(255, 0, 0)
print(f'红：{red.r} 绿：{red.g} 蓝：{red.b} 透明度：{red.a}')
# 将颜色改为透明的
red.a = 0
print(f'透明度：{red.a}')

# 以 CMY 格式获取和设置颜色信息
color1 = Color('#3399ff')
print(f'cmy：{color1.cmy} 红：{color1.r} 绿：{color1.g} 蓝：{color1.b}')
color1.cmy = (0.81, 0.4123, 0.0001)
print(f'cmy：{color1.cmy} 红：{color1.r} 绿：{color1.g} 蓝：{color1.b}')

# 显示 HSVA，HSLA，I1I2I3 格式的颜色信息
color2 = Color((200, 100, 50, 25))
print(f'hsva：{color2.hsva}')
print(f'hsla：{color2.hsla}')
print(f'i1i2i3：{color2.i1i2i3}')

# 显示 RGBA 格式的颜色信息
print(Color([50, 150, 250, 100]).normalize())