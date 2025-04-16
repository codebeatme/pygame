# 匯入並初始化相關模組，建立遊戲視窗
from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
import time
display.set_mode((800, 600))
joystick.init()

# 儲存控製器物件的串列
js = []

running = True
while running:
    # 處理控製器連線事件，結束事件
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            j = joystick.Joystick(e.device_index)
            js.append(j)

            # 嘗試在連線控製器後，啟動其震動回饋
            print('成功啟動震動回饋？', j, j.rumble(0.1, 0.9, 5000))
            time.sleep(1)
            j.stop_rumble()
            print('停止震動回饋', j)