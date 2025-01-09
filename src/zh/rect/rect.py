from pygame import Rect

rect1 = Rect(0, 0, 100, 100)
rect2 = Rect([10, 10], (70, 70))

rect1.topleft = (10, 10)
rect1.move_ip(-10, -10)

rect3 = rect1.move(10, 10)
rect2.width = 100
rect2.height = 100

rect2.update()