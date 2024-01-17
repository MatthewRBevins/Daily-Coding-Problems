#(x^2+y^2)^2*pi=A

#A/(x^2+y^2)^2=pi

#pi = 4 * (area of circle/area of square)

from random import random

square_area = 0
circle_area = 0
for i in range(1000000):
    x = random()
    y = random()
    # if the point is inside the circle
    if pow(x, 2) + pow(y, 2) <= 1:
        circle_area += 1
    square_area += 1
print(round(4 * circle_area / square_area, 3))
