def cube(p1):
	return p1 **3

print(cube(10))

q = cube
print(type(q))
print(type(cube))
print(q(5))