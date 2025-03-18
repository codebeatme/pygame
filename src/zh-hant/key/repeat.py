# 匯入 key 模組和其他相關內容，並建立遊戲視窗
from pygame import key, event, display, KEYDOWN, KEYUP, QUIT
display.set_mode([800, 600])

# 1 秒後開始重複按下事件，重複事件之間間隔 0.5 秒
key.set_repeat(1000, 500)
print(key.get_repeat())

running = True
while running:
    # 隱含的呼叫 pump 函式
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            print('按下', e)
        elif e.type == KEYUP:
            print('釋放', e)