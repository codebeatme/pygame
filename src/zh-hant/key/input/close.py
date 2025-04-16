# 匯入 key 模組和其他相關內容，並建立遊戲視窗
from pygame import key, display, event, font, TEXTEDITING, TEXTINPUT, QUIT, KEYDOWN, K_SPACE, K_ESCAPE
display.set_mode((400, 300))

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                # 如果按下空格鍵，則開啟輸入法
                key.start_text_input()
                print('開啟輸入法')
            elif e.key == K_ESCAPE:
                # 如果按下 Esc 鍵，則關閉輸入法
                key.stop_text_input()
                print('關閉輸入法')
        elif e.type == TEXTEDITING:
            print('編輯事件', e)
        elif e.type == TEXTINPUT:
            print('輸入事件', e)