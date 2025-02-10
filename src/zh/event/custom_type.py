# 导入模块 event
from pygame import event

# 创建两个自定义事件
e1 = event.Event(event.custom_type())
print(e1.type)
e2 = event.Event(event.custom_type())
print(e2.type)
