def rever_search(vocabulary, value):

	for key in vocabulary:
		if vocabulary[key] == value:
			return key
	else:
		return False

p1 = {
	'a':2,
	'b':1,
	'c':4,
	'd':3,
	'e':2,
}

value = 7
print(rever_search(p1, value))