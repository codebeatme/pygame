from pygame import display

# 创建游戏窗口并在全屏模式和窗口模式之间切换
display.set_mode((700, 600))
print(f'切换至全屏模式：{display.toggle_fullscreen()}')
print(f'切换至窗口模式：{display.toggle_fullscreen()}')
