# 匯入 cursors 模組，Cursor 類別和其他相關內容
from pygame import cursors, Cursor, SYSTEM_CURSOR_WAIT

# 建立表示系統等候指標的 Cursor 物件
c1 = Cursor(SYSTEM_CURSOR_WAIT)
# 根據預先定義的 Cursor 物件建立 Cursor 物件
c2 = Cursor(cursors.ball)

# 顯示 Cursor 物件 c1，c2 的型別和資料
print(c1.type, c1.data)
print(c2.type, c2.data)

# 複製之前建立的 Cursor 物件 c1
print(c1.copy())