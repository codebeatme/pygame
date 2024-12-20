from pygame import font

# 取得 SDL_ttf 版本
print(f'目前使用的 SDL_ttf 版本：{font.get_sdl_ttf_version()}')
print(f'編譯階段針對的 SDL_ttf 版本：{font.get_sdl_ttf_version(False)}')