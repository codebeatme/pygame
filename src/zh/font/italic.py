# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载一个斜体字体文件
f = font.Font(font.match_font('Arial', italic=True), 30)

# 无法将斜体修改为非斜体
f.set_italic(False)
print(f'斜体？{f.get_italic()}')

# 创建游戏窗口，并使用字体对象 f 绘制文字
from pygame import display
w = display.set_mode([800, 600])

# 在游戏窗口中绘制文字
ts = f.render('Draw in italic style', True, (0, 255, 0))
w.blit(ts, (200, 200))
display.flip()

# 等待 3 秒
import time
time.sleep(3)