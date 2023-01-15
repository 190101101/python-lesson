p1 = 10
p2 = 11
p3 = 13

print(p1 == p2)
print(p1 != p2)
print(p1 >= p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 < p2)

print(p1 == p2 & p1 < p3)
print(p1 == p2 or p1 < p3)

print("{0} == {1} & {2} < {3}".format(p1, p2, p1, p3))

print((True and False) or (False or True))