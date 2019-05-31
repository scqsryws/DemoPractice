# π的计算

import random
import math

spots = 5000000
point = 0

for i in range(1,spots):
    x,y = random.uniform(0, 1), random.uniform(0, 1)
    dist = math.sqrt(x*x + y*y)
    if dist <= 1:
        point += 1

pi = 4 * point/spots
print(pi)