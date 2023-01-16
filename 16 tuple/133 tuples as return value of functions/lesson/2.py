p1 = divmod(23, 4)

p2, p3 = p1

print(p2, p3)

def add_and_mult(*args):
	
	sum_total = sum(args)
	mult_total = 1

	for arg in args:
		mult_total *= arg

	return (sum_total, mult_total)

p1, p2 = add_and_mult(12,3,4, 13, 11)
print(p1, p2)