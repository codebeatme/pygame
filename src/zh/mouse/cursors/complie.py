# 导入 cursors 模块，Cursor 类
from pygame import cursors, Cursor

# 表示十字的字符串元组
cross_strings = (
    "   ++   ",
    "   --   ",
    "   --   ",
    "+--++--+",
    "+--++--+",
    "   --   ",
    "   --   ",
    "   ++   ",
)
# 使用 compile 生成对应的掩码
(xormarks, andmarks) = cursors.compile(cross_strings, '+', '-')

# 创建表示十字的 Cursor 对象，大小 8x8，作用点在 4 4
Cursor((8, 8), (4, 4), xormarks, andmarks)
