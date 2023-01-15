def down_write(p1, p2):
	if p2 == p1:
		print(p2)
		return
	else:
		print(p2)
		down_write(p1, p2 - 1)

down_write(5, 10)