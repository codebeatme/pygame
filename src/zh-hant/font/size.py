# 匯入並初始化 font 模組
from pygame import font
font.init()

# 載入預設字型，字型大小 24
f = font.Font(size=24)
print(f'繪製 A 所需的空間大小：{f.size('A')}')
# 繪製空間不會增加一個行的高度
print(f'繪製 A\\n 所需的空間大小：{f.size('A\n')}')
# 繪製空間不會增加一個定位寬度
print(f'繪製 A\\t\\n 所需的空間大小：{f.size('A\t\n')}')

# 載入字型 tahoma
f = font.Font(font.match_font('tahoma'))
# 計算一次性繪製所需的空間寬度
print(f'一次性繪製 Appearance 所需的空間寬度：{f.size("Appearance")[0]}')

# 計算單獨繪製每個字元所需的空間寬度
width = 0
for i in 'Appearance':
	width += f.size(i)[0]

print(f'單獨繪製 Appearance 中的每個字元所需的空間寬度：{width}')
