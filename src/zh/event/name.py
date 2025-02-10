# 导入模块 event 和一些与事件相关的变量
from pygame import event, NOEVENT, USEREVENT

# 获取与系统相关的事件的名称
for i in range(NOEVENT + 1, USEREVENT):
    name = event.event_name(i)

    # 不显示未知事件
    if name != 'Unknown':
        print(name)