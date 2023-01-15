import math


def cube(p1):
	"""
		hello world
	"""
	p2 = p1 ** 3
	return p2

print(cube(10))

help(cube)
print(cube.__doc__)

print(math.pow.__doc__)
print(help(math.pow))

print(cube.__module__)
print(cube.__name__)