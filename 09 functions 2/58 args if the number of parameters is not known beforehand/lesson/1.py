def total(*args):
	return sum(args)

print(total(10, 5))
print(total(12, 5, 11))

def parameters(*args):
	for p1 in args:
		print(p1)

parameters(10, 11, True, 'python')