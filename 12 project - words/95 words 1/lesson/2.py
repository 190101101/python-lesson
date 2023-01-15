file = open('words.txt')

for index, line in enumerate(file):
	if index <= 20:
		word_arr = line.split()
		print(word_arr)
	else:
		break