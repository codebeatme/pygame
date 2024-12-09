# 匯入模組 display
from pygame import display

# 初始化
display.init()
print(f'display 已經初始化？{display.get_init()}')

# 設定遊戲視窗的標題
display.set_caption('一個 Pygame 遊戲')
print(display.get_caption())

# 在執行腳本前，請將命令列跳躍至 window.py 所在的目錄
from pygame import image
# 設定遊戲視窗的圖示
display.set_icon(image.load('python.ico'))

from pygame import RESIZABLE, FULLSCREEN
# 建立一個表面 700x500，可以改變大小的視窗
s = display.set_mode([700, 500], RESIZABLE)
print(f'表面大小：{s.get_size()}')
# 變更為全熒幕顯示，表面大小 600x400
s = display.set_mode((600, 400), FULLSCREEN)
print(f'表面大小：{s.get_size()}')

# 等待 3 秒
import time
time.sleep(3)



# clock = pygame.time.Clock()
# running = True
# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     s.fill("purple")
    
#     pygame.draw.line(s, (255,0,0), (0, 200), (270, 200), 10)

#     # RENDER YOUR GAME HERE

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60
# # display.quit()



# # display.set_mode((1024, 500))
# print(display.list_modes(depth=16, flags=pygame.SHOWN))
# for m in display.list_modes(depth=16, flags=pygame.SHOWN):
#     print(m)

# time.sleep(3)