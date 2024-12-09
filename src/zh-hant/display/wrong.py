from pygame import display, SCALED

# 最初沒有采用 SCALED
display.set_mode([700, 500])
# 改為采用 SCALED 將導致例外狀況
display.set_mode((600, 400), SCALED)
