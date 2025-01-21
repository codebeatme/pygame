from pygame import Surface

s1 = Surface([800, 600])
s1.fill('white', [0, 0, 100, 100])
print(f'是否需要鎖定：{s1.mustlock()}')
# 鎖定表面兩次
s1.lock()
s1.lock()
print(f'是否已經鎖定：{s1.get_locked()}')
print(f'已經存在的鎖定：{s1.get_locks()}')

s2 = Surface([800, 600])
# ERROR 無法繪製被鎖定的表面
s2.blit(s1, [0, 0])