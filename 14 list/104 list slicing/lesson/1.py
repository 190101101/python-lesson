p1 = ['a','b','c','d','e','f']

print(p1[1:5])
print(p1[1:4])
print(p1[2:4])
print(p1[0:3])
print(p1[:3])
print(p1[:])

p1[1:4] = [10, 20, 30]
print(p1)


print(id(p1))