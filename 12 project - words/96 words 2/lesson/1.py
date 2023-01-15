file1 = open('words.txt')

#1
for index, line in enumerate(file1):
	if index <= 20:
		word_arr = line.split()
		print(word_arr)
	else:
		break

print('--------')
#2

file2 = open('words.txt')
for index, line in enumerate(file2):
	
	word_arr = line.split()
	word = word_arr[0]

	if len(word) > 10:
		print(word)

print('--------')

#3
file3 = open('words.txt')
for line in file3:

	word_arr = line.split()
	word = word_arr[0]

	if not 'a' in word and \
	not 'e' in word and \
	not 'i' in word and \
	not 'o' in word and \
	not 'u' in word:
		print(word)

print('--------')

#4
file4 = open('words.txt')
for line in file4:

	word_arr = line.split()
	word = word_arr[0]

	if 'ae' in word:
		print(word)

