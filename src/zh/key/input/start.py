# 导入 key 模块和其他相关内容，并创建游戏窗口和 Font 对象
from pygame import key, display, event, font, TEXTEDITING, TEXTINPUT, KEYDOWN, K_ESCAPE
w = display.set_mode((400, 300))
font.init()
f = font.SysFont('Microsoft JhengHei', size=30)

# 打开输入法（可以忽略 start_text_input 的调用）
key.start_text_input()
# 玩家输入的文本
t = ''
# 玩家书写的合成文本
c = ''

running = True
while running:
    for e in event.get():
        if e.type == KEYDOWN:
            # 如果按下 Esc，则游戏循环结束
            if e.key == K_ESCAPE:
                running = False
        elif e.type == TEXTEDITING:
            # 记录玩家书写的合成文本
            c = e.text
            print('编辑事件', e)
        elif e.type == TEXTINPUT:
            # 累计玩家输入的文本
            t += e.text
            print('输入事件', e)

    # 将输入文本，合成文本显示在游戏窗口中
    w.fill('#000000')
    sc = f.render(c, True, '#FF0000')
    tc = f.render(t, True, '#00FF00')
    w.blit(sc, (0, 0))
    w.blit(tc, (0, 50))
    display.flip()