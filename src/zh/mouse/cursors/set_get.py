# 在运行脚本前，请将命令行跳转至 set_get.py 所在的目录

# 导入 mouse 模块和其他相关内容，并创建游戏窗口
from pygame import mouse, image, display, event, QUIT
display.set_mode((400, 300))

# 加载大小为 32x32 的图像
candy = image.load('candy.png')
# 将图像设置为鼠标指针，作用点在图像的中心
mouse.set_cursor((16, 16), candy)
print(mouse.get_cursor())

# 处理游戏中的事件
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
