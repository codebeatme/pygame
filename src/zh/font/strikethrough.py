# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载第一个可用的字体
fontname = font.get_fonts()[0]
f = font.Font(font.match_font(fontname))
# 修改为删除线样式
f.strikethrough = True

# 创建游戏窗口，并使用字体对象 f 绘制文字
from pygame import display
w = display.set_mode((800, 600))

# 在游戏窗口中绘制文字
w.blit(f.render('Strikethrough', False, [255, 255, 255]), [300, 300])
display.flip()

# 等待 3 秒
import time
time.sleep(3)