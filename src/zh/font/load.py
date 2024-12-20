# 导入并初始化 font 模块
from pygame import font
font.init()

# 获取字体文件的路径，并创建一个字体对象
path = font.match_font('Microsoft JhengHei')
# 字体将采用默认大小 12
f = font.Font(path)

# 创建游戏窗口，并使用字体对象 f 绘制文字
from pygame import display
w = display.set_mode((800, 600))

# 在游戏窗口中绘制文字
ts = f.render('你好！', False, [255, 255, 255])
w.blit(ts, [200, 200])
display.flip()

# 等待 3 秒
import time
time.sleep(3)