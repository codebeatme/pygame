# 导入并初始化 display 模块
from pygame import display
display.init()

from pygame import OPENGL, FULLSCREEN, GL_CONTEXT_MAJOR_VERSION, GL_ACCELERATED_VISUAL, GL_DEPTH_SIZE

# 设置与 OpenGL 相关的属性
display.gl_set_attribute(GL_CONTEXT_MAJOR_VERSION, 4)
display.gl_set_attribute(GL_ACCELERATED_VISUAL, 0)

# 创建一个采用 OpenGL 的全屏游戏窗口
display.set_mode([0, 0], OPENGL | FULLSCREEN)

# 下面的语句不会产生效果
display.gl_set_attribute(GL_DEPTH_SIZE, 32)

# 获取与 OpenGL 相关的属性
print(f'GL_CONTEXT_MAJOR_VERSION：{display.gl_get_attribute(GL_CONTEXT_MAJOR_VERSION)}')
print(f'GL_ACCELERATED_VISUAL：{display.gl_get_attribute(GL_ACCELERATED_VISUAL)}')
print(f'GL_DEPTH_SIZE：{display.gl_get_attribute(GL_DEPTH_SIZE)}')