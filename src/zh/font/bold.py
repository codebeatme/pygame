# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载一个非粗体字体文件，字体大小 24
f = font.Font(font.match_font('Microsoft JhengHei'), 24)

# 修改为粗体样式
f.bold = True
print(f'粗体？{f.get_bold()}')

# 创建游戏窗口，并使用字体对象 f 绘制文字
from pygame import display
w = display.set_mode((800, 600))

# 在游戏窗口中绘制文字
ts = f.render('以粗体样式绘制', False, [255, 0, 0])
w.blit(ts, [50, 50])
display.flip()

# 等待 3 秒
import time
time.sleep(3)