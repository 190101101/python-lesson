p1 = {
	'A': ord('A'),
	'B': ord('B'),
	'C': ord('C'),
	'a': ord('a'),
	'b': ord('b'),
	'c': ord('c'),
}

print(p1)
print(p1.items())

for key, value in p1.items():
	print(key, value)