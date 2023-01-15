def forbidden_character(file, *args):
	file = open(file)
	count = 0

	for line in file:
		
		word_arr = line.split()
		word = word_arr[0]

		for char in args:
			if char in word:
				count+=1

	return count

print(forbidden_character('words.txt', 'a', 'b', 'c', 'd'))
