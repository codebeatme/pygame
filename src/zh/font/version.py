from pygame import font

# 获取 SDL_ttf 版本
print(f'当前使用的 SDL_ttf 版本：{font.get_sdl_ttf_version()}')
print(f'编译时针对的 SDL_ttf 版本：{font.get_sdl_ttf_version(False)}')