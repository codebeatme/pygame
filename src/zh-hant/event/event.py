# 匯入模組 event 和一些與事件相關的變數
from pygame import event, QUIT, USEREVENT

# 建立系統事件物件
e1 = event.Event(QUIT)
print(e1)

# 建立自訂事件物件，其 id 為 2
e2 = event.Event(USEREVENT + 100, {'id': 1, 'message': '這是自訂事件！'}, id=2)
print(e2)