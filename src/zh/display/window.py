# 导入模块 display
from pygame import display

# 初始化
display.init()
print(f'display 已经初始化？{display.get_init()}')

# 设置游戏窗口的标题
display.set_caption('一个 Pygame 游戏')
print(display.get_caption())

# 在运行脚本前，请将命令行跳转至 window.py 所在的目录
from pygame import image
# 设置游戏窗口的图标
display.set_icon(image.load('python.ico'))

from pygame import RESIZABLE, FULLSCREEN
# 创建一个表面 700x500，可以改变大小的窗口
s = display.set_mode([700, 500], RESIZABLE)
print(f'表面大小：{s.get_size()}')
# 更改为全屏显示，表面大小 600x400
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