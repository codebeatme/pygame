from pygame import Color

blue = Color(0, 0, 255, 100)
# 由於沒有提供參數 a，因此透明度不會發生變化
blue.update(0, 255, 0)
print(f'透明度：{blue.a}')
# 透明度會發生變化
blue.update('red')
print(f'透明度：{blue.a}')