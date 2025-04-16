# 匯入 cursors 模組，Cursor 類別
from pygame import cursors, Cursor

# 表示十字的字串元組
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
# 使用 compile 建置對應的遮罩
(xormarks, andmarks) = cursors.compile(cross_strings, '+', '-')

# 建立表示十字的 Cursor 物件，大小 8x8，作用點在 4 4
Cursor((8, 8), (4, 4), xormarks, andmarks)
