p1 = ['a','b','c']

def add_upper_letter(p1):
	p2 = ['A','B','C']
	p1.extend(p2)

add_upper_letter(p1)

print(p1)