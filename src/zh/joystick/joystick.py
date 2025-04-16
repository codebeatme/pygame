# 导入模块 joystick
from pygame import joystick

# 初始化
joystick.init()
print(f'joystick 已经初始化？{joystick.get_init()}')

print(f'控制器个数：{joystick.get_count()}')