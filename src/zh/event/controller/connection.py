# 导入相关内容，创建游戏窗口，初始化模块
from pygame import display, event, joystick, QUIT
display.set_mode((800, 600))
joystick.init()

# 导入与控制器事件相关的变量
from pygame import JOYDEVICEADDED, JOYDEVICEREMOVED
# 保存 JoystickType 对象的列表
jss = []

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            # 根据设备索引创建 JoystickType 对象，并添加至 jss
            js = joystick.Joystick(e.device_index)
            jss.append(js)

            print('添加控制器', e.device_index)
        elif e.type == JOYDEVICEREMOVED:
            # 根据实例 ID，将 JoystickType 对象从 jss 移除
            for js in jss:
                if js.get_instance_id() == e.instance_id:
                    jss.remove(js)

                    print('移除控制器', e.instance_id)
                    break