# 匯入模組 event 和一些與事件相關的變數
from pygame import event, NOEVENT, USEREVENT

# 取得與系統相關的事件的名稱
for i in range(NOEVENT + 1, USEREVENT):
    name = event.event_name(i)

    # 不顯示未知事件
    if name != 'Unknown':
        print(name)