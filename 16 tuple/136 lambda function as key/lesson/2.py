def lam(p1):
	return len(p1)

p1 = ['vw', 'bmw', 'audi', 'porshe', 'mercedes']
p2 = list(p1)
p2.sort(key = lam)
print(p2)
