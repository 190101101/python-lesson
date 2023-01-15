print(not True)
print(not False)

p1 = 4
p2 = 5
p3 = 3

print(not p1 == 5)
print(not p1 == 4)

if p1 == p2:
	print('p1 == p2')
else:
	if p1 > p2:
		print('p1 > p2')
	elif p1 < p3:
		print('p1 < p2')
	else:
		print('what the f...?')
