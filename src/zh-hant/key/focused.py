# 匯入 key 模組和其他相關內容，並建立遊戲視窗
from pygame import key, event, display, QUIT
display.set_mode([800, 600])

running = True
while True:
    # 隱含的呼叫 pump 函式，並處理事件
    for e in event.get():
        if e.type == QUIT:
            running = False

    print('擁有輸入焦點？', key.get_focused())