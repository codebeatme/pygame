# 导入模块 event 和一些与事件相关的变量
from pygame import event, QUIT, USEREVENT

# 创建系统事件对象
e1 = event.Event(QUIT)
print(e1)

# 创建自定义事件对象，其 id 为 2
e2 = event.Event(USEREVENT + 100, {'id': 1, 'message': '这是自定义事件！'}, id=2)
print(e2)