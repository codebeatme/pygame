# 导入模块 pygame
import pygame

# 初始化其他模块
pygame.init()

# 是否已经初始化？
print(f'初始化？{pygame.get_init()}')

# 定义一个退出函数
def my_quit():
    print('游戏结束了？')
# 注册退出函数
pygame.register_quit(my_quit)

# 引发异常
try:
    raise pygame.error('无中生有的错误！')
except RuntimeError as e:
    print(e, type(e))

# 设置错误消息
pygame.set_error('哪里有错？！')
# 显示错误消息
print(pygame.get_error())

# 获取 Pygame 版本
print(pygame.version.ver)
print(pygame.version.vernum)

# 获取 SDL 版本
print(f'当前使用的 SDL 版本：{pygame.get_sdl_version()}')
print(f'编译时针对的 SDL 版本：{pygame.get_sdl_version(False)}')

# 获取 SDL 的字节序
print(pygame.get_sdl_byteorder())

# 取消初始化
pygame.quit()
