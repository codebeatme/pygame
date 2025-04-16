# 匯入相關內容，並建立遊戲視窗
from pygame import joystick, display, event, QUIT, JOYBUTTONDOWN
display.set_mode([800, 600])

# 初始化 joystick 模組
joystick.init()

js = []
# 取得所有已經連線的控製器
for i in range(joystick.get_count()):
    j = joystick.Joystick(i)
    js.append(j)

    print(f'控製器 {i} 已經初始化？{j.get_init()}')

# 處理結束事件，控製器按鍵的按下事件
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == JOYBUTTONDOWN:
            print(e)