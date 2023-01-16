
def lam(p1):
	return len(p1)

p1 = ['vw', 'bmw', 'audi', 'porshe', 'mercedes']
p2 = list(p1)

p1.sort(key = lambda x:len(x))
sorted(p2, key = lambda x:len(x))
p1.sort(key = lam)


print(p1)
print(p1)
print(p2)