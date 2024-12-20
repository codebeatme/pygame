# 导入并初始化 font 模块
from pygame import font
font.init()

# 加载默认字体，字体大小 24
f = font.Font(size=24)
print(f'绘制 A 所需的空间大小：{f.size('A')}')
# 绘制空间不会增加一个行的高度
print(f'绘制 A\\n 所需的空间大小：{f.size('A\n')}')
# 绘制空间不会增加一个制表宽度
print(f'绘制 A\\t\\n 所需的空间大小：{f.size('A\t\n')}')

# 加载字体 tahoma
f = font.Font(font.match_font('tahoma'))
# 计算一次性绘制所需的空间宽度
print(f'一次性绘制 Appearance 所需的空间宽度：{f.size("Appearance")[0]}')

# 计算单独绘制每个字符所需的空间宽度
width = 0
for i in 'Appearance':
	width += f.size(i)[0]

print(f'单独绘制 Appearance 中的每个字符所需的空间宽度：{width}')
