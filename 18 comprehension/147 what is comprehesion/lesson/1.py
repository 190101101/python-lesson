p1 = []

for i in range(1, 11):
	p1.append(i ** 2)

print(p1)

p2 = [i ** 2 for i in range(1, 11)]
print(p2)