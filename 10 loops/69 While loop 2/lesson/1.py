#
p1 = 1

while p1 < 10:
	if p1 % 2 == 1:
		print("{0} squared: {1}".format(p1, p1**2))
	p1 += 1
print('--------------')

#
p2 = 1
p3_odd = 0
p3_even = 0

while p2 < 20:
	if p2 % 2 == 0:
		p3_even+=p2
		print("{0} squared: {1}".format(p2, p2**2))

	if p2 % 2 == 1:
		p3_odd+=p2
		print("{0} squared: {1}".format(p2, p2**2))
	p2 += 1

print("total odd: {0}".format(p3_odd))
print("total even: {0}".format(p3_even))