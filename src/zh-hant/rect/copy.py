from pygame import Rect

# 建立一個矩形，然後複製他
r1 = Rect(0, 0, 100, 100)
r2 = r1.copy()
# 對第一個矩形進行修改，並不會影響第二個矩形
r1.bottomright = (200, 200)

print(f'第一個矩形：{r1}')
print(f'第二個矩形：{r2}')