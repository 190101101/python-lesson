p1 = [
	('Monday'),
	('Tuesday'),
	('Wednesday'),
	('Thursday'),
	('Friday'),
	('Saturday'),
	('Sunday'),
]
p2 = range(1, 8)

p3 = zip(p1, p2)

for key, value in p3:
	print(f"{key}: {value}")