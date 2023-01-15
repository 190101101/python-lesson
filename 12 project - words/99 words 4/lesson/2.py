#1
def uses_only_presents(text, character):
	
	for char in text:
		if char.isalpha() and not char in character:
			return False
	else:
		return True

#2
def uses_all(text, letters):

	p1 = True

	for letter in letters:
		if not letter in text:
			p1 = False

	return p1

#3
def uses_all_lorem(letters):
	file = open('words.txt')

	for line in file:
		word_arr = line.split()
		word = word_arr[0]

		if uses_all(word, letters):
			print(word)

uses_all_lorem('aei')
print('---')

#4
def uses_only_all(letters):
	file = open('words.txt')

	for line in file:
		word_arr = line.split()
		word = word_arr[0]
		if uses_only_presents(word, letters) and\
 		uses_all(word, letters):
			print(word)

uses_only_all('ae')

#5
def correct_word(word):
	
	p1 = word[0]

	for letter in word:
		if letter < p1:
			return False

		p1 = letter

	return True

print(correct_word('qar'))
print(correct_word('abcdef'))

#6
def correct_word_lorem():
	file = open('words.txt')

	for line in file:
		word_arr = line.split()
		word = word_arr[0]

		if correct_word(word):
			print(word)

print('---')
correct_word_lorem();