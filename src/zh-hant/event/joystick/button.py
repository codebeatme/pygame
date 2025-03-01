# 匯入初始化相關模組，建立遊戲視窗
from pygame import display, event, joystick, JOYDEVICEADDED
display.set_mode((800, 600))
joystick.init()

# 匯入與控製器事件相關的變數
from pygame import JOYBUTTONDOWN, JOYBUTTONUP
# 儲存控製器資訊的字典
cs = {}
# 玩家索引
playerIndex = 0

running = True
while running:
    for e in event.get():
        if e.type == JOYDEVICEADDED:
            js = joystick.Joystick(e.device_index)

            # 將 JoystickType 物件與玩家索引新增至字典，執行個體 ID 為鍵
            playerIndex += 1
            cs[js.get_instance_id()] = [js, playerIndex]
        elif e.type == JOYBUTTONDOWN:
            # 根據執行個體 ID 取得字典中的控製器資訊，顯示玩家索引
            c = cs[e.instance_id]

            print(f'玩家 {c[1]} 按下了 {e.button}')
        elif e.type == JOYBUTTONUP:
            # 如果釋放了開始鍵，則遊戲結束
            if e.button == 7:
                running = False