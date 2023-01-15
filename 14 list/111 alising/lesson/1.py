p1 = 10
p2 = p1

print(p1 == p2)
print(p1 is p2)

p3 = [1,2,3,4,5]
p4 = p3

print(p3 == p4)
print(p3 is p4)

p3[0] = 'a'

print(p3)
print(p4)