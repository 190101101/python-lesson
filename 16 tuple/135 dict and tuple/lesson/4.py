user = {
	('cookie', 'cat'): 'aa',
	('caiser', 'dog'): 'dc',
	('apsi', 'cat'): 'ff',
	('ketty', 'cat'): 'fd',
}

print(user)

p1 = ['cookie', 'cat', 'apsi', 'ketty']
p2 = ['cat', 'dog', 'cat', 'cat']
p3 = ['aa', 'dc', 'ff', 'fd']
p4 = {}

for p1,p2,p3 in zip(p1, p2, p3):
	print(f"{p1}, {p2}: {p3}")
	p4[(p1, p2)] = p3

print(p4)