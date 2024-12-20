from pygame import image

# 取得 SDL_Image 版本
print(f'目前使用的 SDL_Image 版本：{image.get_sdl_image_version()}')
print(f'編譯階段針對的 SDL_Image 版本：{image.get_sdl_image_version(False)}')