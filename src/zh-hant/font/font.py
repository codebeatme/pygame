# 匯入模組 font
from pygame import font

# 初始化
font.init()
print(f'font 已經初始化？{font.get_init()}')

# 取得所有可用字型的名稱
print(font.get_fonts())
# 取得預設字型的檔案名稱
print(font.get_default_font())

# 取得字型檔案的路徑
print(font.match_font('tahoma,Sitka Text', True, True))
