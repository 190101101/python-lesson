#
with open('../../../00 bin/docs/pantry/lorem.txt') as file:
	for line in file:
		word_arr = line.split()
		print(word_arr)
		
