from pygame import display

# 建立遊戲視窗
display.set_mode((800, 600))
print(f'活動狀態？{display.get_active()}')
# 最小化遊戲視窗後，視窗處於非活動狀態
display.iconify()
print(f'活動狀態？{display.get_active()}')

