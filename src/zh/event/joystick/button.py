# 导入初始化相关模块，创建游戏窗口
from pygame import display, event, joystick, JOYDEVICEADDED
display.set_mode((800, 600))
joystick.init()

# 导入与控制器事件相关的变量
from pygame import JOYBUTTONDOWN, JOYBUTTONUP
# 保存控制器信息的字典
cs = {}
# 玩家索引
playerIndex = 0

running = True
while running:
    for e in event.get():
        if e.type == JOYDEVICEADDED:
            js = joystick.Joystick(e.device_index)

            # 将 JoystickType 对象与玩家索引添加至字典，实例 ID 为键
            playerIndex += 1
            cs[js.get_instance_id()] = [js, playerIndex]
        elif e.type == JOYBUTTONDOWN:
            # 根据实例 ID 获取字典中的控制器信息，显示玩家索引
            c = cs[e.instance_id]

            print(f'玩家 {c[1]} 按下了 {e.button}')
        elif e.type == JOYBUTTONUP:
            # 如果释放了开始键，则游戏结束
            if e.button == 7:
                running = False