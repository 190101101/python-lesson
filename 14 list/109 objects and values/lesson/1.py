p1 = 'cookie'
p2 = 'cookie'

print(id(p1))
print(id(p2))
print(p1 == p2)
print(id(p1) == id(p2))

p2 = 'cookies'
print(p2)
print(p1)

print(p1 == p2)

print(id(p1) == id(p2))