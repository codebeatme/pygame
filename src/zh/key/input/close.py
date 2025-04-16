# 导入 key 模块和其他相关内容，并创建游戏窗口
from pygame import key, display, event, font, TEXTEDITING, TEXTINPUT, QUIT, KEYDOWN, K_SPACE, K_ESCAPE
display.set_mode((400, 300))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                # 如果按下空格键，则打开输入法
                key.start_text_input()
                print('打开输入法')
            elif e.key == K_ESCAPE:
                # 如果按下 Esc 键，则关闭输入法
                key.stop_text_input()
                print('关闭输入法')
        elif e.type == TEXTEDITING:
            print('编辑事件', e)
        elif e.type == TEXTINPUT:
            print('输入事件', e)