# 导入并初始化相关模块，创建游戏窗口
from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 保存控制器对象的列表
js = []

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            # 控制器连接事件
            j = joystick.Joystick(e.device_index)
            js.append(j)
            print(f'控制器实例 ID：{j.get_instance_id()}')
            print(f'控制器名称：{j.get_name()}')
            print(f'控制器电量：{j.get_power_level()}')
            print(f'控制器 GUID：{j.get_guid()}')
