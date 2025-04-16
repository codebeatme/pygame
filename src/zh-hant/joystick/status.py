# 匯入並初始化相關模組，建立遊戲視窗
from pygame import joystick, display, event, JOYDEVICEADDED, QUIT
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

    # 角色索引
    pi = 0

    # 周遊所有的控製器
    for j in js:
        pi += 1
        
        # 如果按下第一個按鍵，則視為攻擊命令
        if j.get_numbuttons() > 0 and j.get_button(0):
            print(f'角色 {pi} 攻擊')

        # 根據第一個方向鍵來移動角色
        if j.get_numhats() > 0:
            (x, y) = j.get_hat(0)
            
            if x == -1:
                print(f'角色 {pi} 向左')
            elif x == 1:
                print(f'角色 {pi} 向右')

            if y == -1:
                print(f'角色 {pi} 向下')
            elif y == 1:
                print(f'角色 {pi} 向上')

        # 根據右扳機鍵判斷是否跳躍，假設 5 對應了右扳機鍵
        if j.get_numaxes() > 5 and j.get_axis(5) > 0.2:
            print(f'角色 {pi} 跳躍')
