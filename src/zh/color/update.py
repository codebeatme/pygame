from pygame import Color

blue = Color(0, 0, 255, 100)
# 由于没有提供参数 a，因此透明度不会发生变化
blue.update(0, 255, 0)
print(f'透明度：{blue.a}')
# 透明度会发生变化
blue.update('red')
print(f'透明度：{blue.a}')