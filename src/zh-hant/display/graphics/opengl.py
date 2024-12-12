# 匯入並初始化 display 模組
from pygame import display
display.init()

from pygame import OPENGL, FULLSCREEN, GL_CONTEXT_MAJOR_VERSION, GL_ACCELERATED_VISUAL, GL_DEPTH_SIZE

# 設定與 OpenGL 相關的屬性
display.gl_set_attribute(GL_CONTEXT_MAJOR_VERSION, 4)
display.gl_set_attribute(GL_ACCELERATED_VISUAL, 0)

# 建立一個采用 OpenGL 的全熒幕遊戲視窗
display.set_mode([0, 0], OPENGL | FULLSCREEN)

# 下面的陳述式不會產生效果
display.gl_set_attribute(GL_DEPTH_SIZE, 32)

# 取得與 OpenGL 相關的屬性
print(f'GL_CONTEXT_MAJOR_VERSION：{display.gl_get_attribute(GL_CONTEXT_MAJOR_VERSION)}')
print(f'GL_ACCELERATED_VISUAL：{display.gl_get_attribute(GL_ACCELERATED_VISUAL)}')
print(f'GL_DEPTH_SIZE：{display.gl_get_attribute(GL_DEPTH_SIZE)}')