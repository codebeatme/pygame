# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载 Pygame 默认字体，字体大小 30
f = font.Font(size=30)
# 修改为下划线样式
f.set_underline(True)

# 创建游戏窗口，并使用字体对象 f 绘制文字
from pygame import display
w = display.set_mode((800, 600))

# 在游戏窗口中绘制文字
w.blit(f.render('Underline', False, [255, 0, 255]), [200, 200])
display.flip()

# 等待 3 秒
import time
time.sleep(3)