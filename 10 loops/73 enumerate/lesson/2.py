p1 = range(10, 101, 5)
p2 = 0
for index, i in enumerate(p1):
	p2 += i
	print("{0}: {1} - {1}".format(index, i, p2))

