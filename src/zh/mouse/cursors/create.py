# 导入 cursors 模块，Cursor 类和其他相关内容
from pygame import cursors, Cursor, SYSTEM_CURSOR_WAIT

# 创建表示系统等待指标的 Cursor 对象
c1 = Cursor(SYSTEM_CURSOR_WAIT)
# 根据预先定义的 Cursor 对象创建 Cursor 对象
c2 = Cursor(cursors.ball)

# 显示 Cursor 对象 c1，c2 的类型和数据
print(c1.type, c1.data)
print(c2.type, c2.data)

# 复制之前创建的 Cursor 对象 c1
print(c1.copy())