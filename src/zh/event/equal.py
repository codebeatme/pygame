# 导入模块 event，USEREVENT
from pygame import event, USEREVENT

# 创建一些事件对象
e1 = event.Event(USEREVENT + 1)
e2 = event.Event(USEREVENT + 1, message='一个自定义事件')
e3 = event.Event(USEREVENT + 1, {'message': '一个自定义事件'})
e4 = event.Event(USEREVENT + 2, {'message': '一个自定义事件'})
e5 = event.Event(USEREVENT + 2, {'message': '一个自定义事件'}, id=1)

# 判断他们是否相等
print(f'e1 == e2？{e1 == e2}')
print(f'e2 == e3？{e2 == e3}')
print(f'e3 == e4？{e3 == e4}')
print(f'e4 == e5？{e4 == e5}')
