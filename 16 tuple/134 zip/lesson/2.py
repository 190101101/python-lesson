import string

p1 = list(string.ascii_lowercase)
p2 = range(1, 27)
p3 = zip(p1, p2)

for i in p3:
	print(i)