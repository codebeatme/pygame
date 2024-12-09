from pygame import display

# 创建并最小化游戏窗口
display.set_mode([800, 600])
print(f'最小化成功？{display.iconify()}')
