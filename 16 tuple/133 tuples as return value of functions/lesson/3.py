import statistics

def simp_static(p1):
	minimum = min(p1)
	maximum = max(p1)
	avg = statistics.mean(p1)

	return (minimum, maximum, avg)

arr = range(1, 100)
p1, p2, p3 = simp_static(arr)
print(p1, p2, p3)