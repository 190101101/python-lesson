p1 = [1,2,3]
p2 = ['a', 'b', 'c']
p3 = []

for letter in p2:
	for num in p1:
		p3.append((letter, num))

print(p3)