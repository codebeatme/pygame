# 导入相关模块，并创建游戏窗口
from pygame import display, event
w = display.set_mode((400, 300))

# 导入与键盘事件相关的变量
from pygame import KEYDOWN, KEYUP, KEYMAPCHANGED, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_LSHIFT

running = True
while running:
    for e in event.get():
        if e.type == KEYDOWN:
            print('按下键盘', e)
            
            # 判断按下的键是哪一个
            if e.key == K_UP:
                print('上方向键')
            elif e.key == K_DOWN:
                print('下方向键')
            elif e.key == K_LEFT:
                print('左方向键')
            elif e.key == K_RIGHT:
                print('右方向键')
            elif e.key == K_LSHIFT:
                # 结束游戏循环
                running = False

        elif e.type == KEYUP:
            print('释放键盘', e)
        elif e.type == KEYMAPCHANGED:
            print('键盘布局改变', e)
