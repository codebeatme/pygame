from pygame import Rect

# 建立一個矩形
r = Rect(10, 20, 30, 40)

# 顯示矩形的位置和大小
print(f'{r.x} {r.y} {r.right} {r.bottom}')
print(f'{r.w} {r.h} {r.size}')

# 顯示矩形的四個頂點的座標
print(f'{r.topleft} {r.topright} {r.bottomright} {r.bottomleft}')
# 顯示矩形的四個邊緣的中點的座標
print(f'{r.midleft} {r.midtop} {r.midright} {r.midbottom}')
# 顯示矩形中心的座標
print(f'{r.centerx} {r.centery} {r.center}')

# 修改矩形的中心位置
r.center = (100, 100)
# 顯示矩形的位置
print(f'{r.x} {r.y} {r.right} {r.bottom}')
