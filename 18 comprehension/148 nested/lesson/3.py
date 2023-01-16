p1 = {}

for i in range(1, 11):
	for x in range(1, i + 1):
		if not i in p1:
			p1[i] = [x]
		else:
			p1[i].append(x)

print(p1)