from pygame import display

# 建立並最小化遊戲視窗
display.set_mode([800, 600])
print(f'最小化成功？{display.iconify()}')
