# 匯入並初始化相關模組，建立遊戲視窗
from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 儲存控製器物件的串列
js = []

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            # 控製器連線事件
            j = joystick.Joystick(e.device_index)
            js.append(j)
            print(f'控製器執行個體 ID：{j.get_instance_id()}')
            print(f'控製器名稱：{j.get_name()}')
            print(f'控製器電量：{j.get_power_level()}')
            print(f'控製器 GUID：{j.get_guid()}')
