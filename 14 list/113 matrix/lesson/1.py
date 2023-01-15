p1 = [
	[1,2,3],
	[4,5,6],
	[7,8,9],
]

p2 = [
	[10,20,30],
	[40,50,60],
	[70,80,90],
]

p3 = p1 + p2

for i in range(len(p1)):
	for q in range(len(p2)):
		p3[i][q] = p1[i][q] + p2[i][q]


print(p3)