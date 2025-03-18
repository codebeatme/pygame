from pygame import key, display, K_CAPSLOCK
# 需要初始化 display 模块
display.init()

# 获取按键名称
n = key.name(K_CAPSLOCK, False)
print(n)

# 获取按键 ID
print(key.key_code(n))
