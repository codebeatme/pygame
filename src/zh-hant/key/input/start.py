# 匯入 key 模組和其他相關內容，並建立遊戲視窗和 Font 物件
from pygame import key, display, event, font, TEXTEDITING, TEXTINPUT, KEYDOWN, K_ESCAPE
w = display.set_mode((400, 300))
font.init()
f = font.SysFont('Microsoft JhengHei', size=30)

# 開啟輸入法（可以忽略 start_text_input 的呼叫）
key.start_text_input()
# 玩家輸入的文字
t = ''
# 玩家書寫的合成文字
c = ''

running = True
while running:
    for e in event.get():
        if e.type == KEYDOWN:
            # 如果按下 Esc，則遊戲迴圈結束
            if e.key == K_ESCAPE:
                running = False
        elif e.type == TEXTEDITING:
            # 記錄玩家書寫的合成文字
            c = e.text
            print('編輯事件', e)
        elif e.type == TEXTINPUT:
            # 累計玩家輸入的文字
            t += e.text
            print('輸入事件', e)

    # 將輸入文字，合成文字顯示在遊戲視窗中
    w.fill('#000000')
    sc = f.render(c, True, '#FF0000')
    tc = f.render(t, True, '#00FF00')
    w.blit(sc, (0, 0))
    w.blit(tc, (0, 50))
    display.flip()