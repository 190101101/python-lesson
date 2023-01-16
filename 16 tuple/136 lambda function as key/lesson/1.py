def lam(p1):
	return len(p1)

p1 = ('vw', 'bmw', 'audi', 'porshe', 'mercedes')
p2 = list(p1)
# p2.sort(p3 = lam)

print(sorted(p1, key = lambda x:len(x)))
print(p2.sort(key = lambda x:len(x)))