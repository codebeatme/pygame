from pygame import Rect

# 创建一个矩形，然后复制他
r1 = Rect(0, 0, 100, 100)
r2 = r1.copy()
# 对第一个矩形进行修改，并不会影响第二个矩形
r1.bottomright = (200, 200)

print(f'第一个矩形：{r1}')
print(f'第二个矩形：{r2}')