# 导入 key 模块和其他相关内容，并创建游戏窗口
from pygame import key, event, display, KEYDOWN, KEYUP, QUIT
display.set_mode([800, 600])

# 1 秒后开始重复按下事件，重复事件之间间隔 0.5 秒
key.set_repeat(1000, 500)
print(key.get_repeat())

running = True
while running:
    # 隐式的调用 pump 函数
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            print('按下', e)
        elif e.type == KEYUP:
            print('释放', e)