# 匯入模組 joystick
from pygame import joystick

# 初始化
joystick.init()
print(f'joystick 已經初始化？{joystick.get_init()}')

print(f'控製器個數：{joystick.get_count()}')