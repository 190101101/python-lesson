p1 = {}

for i in range(1, 10):
	for x in range(2, i +1):
		if i % x == 0:
			if not i in p1:
				p1[i] = [x]
			else:
				p1[i].append(x)

print(p1)				