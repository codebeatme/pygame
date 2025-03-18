from pygame import key, display, K_CAPSLOCK
# 需要初始化 display 模組
display.init()

# 取得按鍵名稱
n = key.name(K_CAPSLOCK, False)
print(n)

# 取得按鍵 ID
print(key.key_code(n))
