# 匯入並初始化相關模組，建立遊戲視窗
from pygame import display, event, joystick, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 匯入與控製器事件相關的變數
from pygame import JOYAXISMOTION
# 儲存 JoystickType 物件的串列
jss = []

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYAXISMOTION:
            print(e)
            # 判斷觸發事件的軸裝置是否為右扳機鍵
            if e.axis == 5:
                # 判斷右扳機鍵的移動程度，是否足以發動攻擊
                if e.value > -0.3:
                    print('攻擊')
                else:
                    print('停止攻擊')