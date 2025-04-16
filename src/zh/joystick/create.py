# 导入相关内容，并创建游戏窗口
from pygame import joystick, display, event, QUIT, JOYBUTTONDOWN
display.set_mode([800, 600])

# 初始化 joystick 模块
joystick.init()

js = []
# 获取所有已经连接的控制器
for i in range(joystick.get_count()):
    j = joystick.Joystick(i)
    js.append(j)

    print(f'控制器 {i} 已经初始化？{j.get_init()}')

# 处理退出事件，控制器按键的按下事件
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYBUTTONDOWN:
            print(e)