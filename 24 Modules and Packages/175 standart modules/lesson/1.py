import math
import random

print(math.pi)
print(random.random())
print(random.randint(10, 50))

p1 = [1,2,3,4]
p2 = random.choice(p1)
print(p2)

p3 = random.sample(p1, 3)
print(p3)