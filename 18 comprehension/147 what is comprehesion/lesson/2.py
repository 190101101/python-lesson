p1 = [1,2,3]
p2 = ['php', 'java', 'python']

#1
for key, value in zip(p1, p2):
	print(f"{key}: {value}")

#2
p3 = {num:prog for num, prog in zip(p1, p2)}
print(p3)