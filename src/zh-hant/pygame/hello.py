# 匯入模組 pygame
import pygame

# 初始化其他模組
pygame.init()

# 是否已經初始化？
print(f'初始化？{pygame.get_init()}')

# 定義一個結束函式
def my_quit():
    print('遊戲結束了？')
# 註冊結束函式
pygame.register_quit(my_quit)

# 引發例外狀況
try:
    raise pygame.error('無中生有的錯誤！')
except RuntimeError as e:
    print(e, type(e))

# 設定錯誤訊息
pygame.set_error('哪裏有錯？！')
# 顯示錯誤訊息
print(pygame.get_error())

# 取得 Pygame 版本
print(pygame.version.ver)
print(pygame.version.vernum)

# 取得 SDL 版本
print(f'目前使用的 SDL 版本：{pygame.get_sdl_version()}')
print(f'編譯階段針對的 SDL 版本：{pygame.get_sdl_version(False)}')

# 取得 SDL 的位元組排列方式
print(pygame.get_sdl_byteorder())

# 結束
pygame.quit()
