p1 = {i:
	[x for x in range(2, i+1) if i % x == 0]
	for i in range(2, 21)
}

print(p1)