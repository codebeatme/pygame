from pygame import image

# 获取 SDL_Image 版本
print(f'当前使用的 SDL_Image 版本：{image.get_sdl_image_version()}')
print(f'编译时针对的 SDL_Image 版本：{image.get_sdl_image_version(False)}')