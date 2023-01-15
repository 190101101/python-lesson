text = 'hello my name is cookie'

def count_character(text, p1):
	p2 = 0

	for i in text:
		if i == p1:
			p2 += 1

	return p2


print(count_character(text, 'e'))
print(count_character(text, 'm'))