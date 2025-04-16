# 匯入並初始化相關模組，建立遊戲視窗
from pygame import display, event, joystick, JOYDEVICEADDED, QUIT
display.set_mode((800, 600))
joystick.init()

# 匯入與控製器事件相關的變數
from pygame import JOYHATMOTION
# 儲存 JoystickType 物件的串列
jss = []
# 表示水平和垂直的移動方向
h = 0
v = 0

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYDEVICEADDED:
            jss.append(joystick.Joystick(e.device_index))
        elif e.type == JOYHATMOTION:
            # 取得十字鍵的按下狀態
            (x, y) = e.value

            # 根據十字鍵的按下狀態，設定遊戲角色的移動方向
            if x == 1:
                h = 1
                print('開始向右移動')
            elif x == -1:
                h = -1
                print('開始向左移動')
            elif h != 0:
                h = 0
                print('取消水平移動')
            
            if y == 1:
                v = 1
                print('開始向上移動')
            elif y == -1:
                v = -1
                print('開始向下移動')
            elif v != 0:
                v = 0
                print('取消垂直移動')