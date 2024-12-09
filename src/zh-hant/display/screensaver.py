# 匯入並初始化 display 模組
from pygame import display
display.init()

# 取得和設定是否允許熒幕保護程式在遊戲執行階段啟動
print(f'允許熒幕保護程式啟動？{display.get_allow_screensaver()}')
display.set_allow_screensaver()
print(f'允許熒幕保護程式啟動？{display.get_allow_screensaver()}')
