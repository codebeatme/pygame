from pygame import display, SCALED

# 最初没有采用 SCALED
display.set_mode([700, 500])
# 改为采用 SCALED 将导致异常
display.set_mode((600, 400), SCALED)
