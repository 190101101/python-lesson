p1 = [1,2,3]
p2 = ['a', 'b', 'c']

p3 = [(letter, num)
	for  letter in p2
	for  num in p1
]

print(p3)