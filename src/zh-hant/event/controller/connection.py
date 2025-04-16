# 匯入相關內容，建立遊戲視窗，初始化模組
from pygame import display, event, joystick, QUIT
display.set_mode((800, 600))
joystick.init()

# 匯入與控製器事件相關的變數
from pygame import JOYDEVICEADDED, JOYDEVICEREMOVED
# 儲存 JoystickType 物件的串列
jss = []

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            # 根據裝置索引建立 JoystickType 物件，並新增至 jss
            js = joystick.Joystick(e.device_index)
            jss.append(js)

            print('新增控製器', e.device_index)
        elif e.type == JOYDEVICEREMOVED:
            # 根據執行個體 ID，將 JoystickType 物件從 jss 移除
            for js in jss:
                if js.get_instance_id() == e.instance_id:
                    jss.remove(js)

                    print('移除控製器', e.instance_id)
                    break