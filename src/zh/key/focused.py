# 导入 key 模块和其他相关内容，并创建游戏窗口
from pygame import key, event, display, QUIT
display.set_mode([800, 600])

running = True
while True:
    # 隐式的调用 pump 函数，并处理事件
    for e in event.get():
        if e.type == QUIT:
            running = False

    print('拥有输入焦点？', key.get_focused())