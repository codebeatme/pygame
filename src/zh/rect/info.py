from pygame import Rect

# 创建一个矩形
r = Rect(10, 20, 30, 40)

# 显示矩形的位置和大小
print(f'{r.x} {r.y} {r.right} {r.bottom}')
print(f'{r.w} {r.h} {r.size}')

# 显示矩形的四个顶点的坐标
print(f'{r.topleft} {r.topright} {r.bottomright} {r.bottomleft}')
# 显示矩形的四个边缘的中点的坐标
print(f'{r.midleft} {r.midtop} {r.midright} {r.midbottom}')
# 显示矩形中心的坐标
print(f'{r.centerx} {r.centery} {r.center}')

# 修改矩形的中心位置
r.center = (100, 100)
# 显示矩形的位置
print(f'{r.x} {r.y} {r.right} {r.bottom}')
