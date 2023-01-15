#
def mult(p1):
	return lambda p2: p2 * p1

p1 = mult(10)
print(type(p1))

print(p1(10))

#
p2x = mult(2)
p4x = mult(4)
p8x = mult(8)

print(p2x(10))
print(p4x(10))
print(p8x(10))