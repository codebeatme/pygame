# 导入并初始化相关模块，创建游戏窗口
from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
import time
display.set_mode((800, 600))
joystick.init()

# 保存控制器对象的列表
js = []

running = True
while running:
    # 处理控制器连接事件，退出事件
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            js.append(j)

            # 尝试在连接控制器后，启动其震动回馈
            print('成功启动震动回馈？', j, j.rumble(0.1, 0.9, 5000))
            time.sleep(1)
            j.stop_rumble()
            print('停止震动回馈', j)