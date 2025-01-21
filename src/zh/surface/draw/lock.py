from pygame import Surface

s1 = Surface([800, 600])
s1.fill('white', [0, 0, 100, 100])
print(f'是否需要锁定：{s1.mustlock()}')
# 锁定表面两次
s1.lock()
s1.lock()
print(f'是否已经锁定：{s1.get_locked()}')
print(f'已经存在的锁：{s1.get_locks()}')

s2 = Surface([800, 600])
# ERROR 无法绘制被锁定的表面
s2.blit(s1, [0, 0])