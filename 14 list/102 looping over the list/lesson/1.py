p1 = ['red', 'black', 'white']

#
for i in p1:
	print(i)

#
for index, key in enumerate(p1):
	print(f"{index}: {key}")


p2 = [1,2,3,4,5]

#
for i in p2:
	num = i * 10
	print(num)

#
for index, i in enumerate(p2):
	num = i * 10
	p2[index] = num

print(p2)