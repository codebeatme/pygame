# 匯入模組 event
from pygame import event

# 建立兩個自訂事件
e1 = event.Event(event.custom_type())
print(e1.type)
e2 = event.Event(event.custom_type())
print(e2.type)
