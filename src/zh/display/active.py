from pygame import display

# 创建游戏窗口
display.set_mode((800, 600))
print(f'活动状态？{display.get_active()}')
# 最小化游戏窗口后，窗口处于非活动状态
display.iconify()
print(f'活动状态？{display.get_active()}')

