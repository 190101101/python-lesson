#1
def letters_with_permission(text, character):
	
	for char in text:
		if char.isalpha() and not char in character:
			return False
	else:
		return True

#2
def only_letters_with_permission(letter):
	file = open('words.txt')

	for line in file:
		word_arr = line.split()
		word = word_arr[0]

		if letters_with_permission(word, letter):
			print(word)

only_letters_with_permission('ens')

#3
def uses_all(text, letters):

	p1 = True

	for letter in letters:
		if not letter in text:
			p1 = False

	return p1

print(uses_all('hello my name is cookie', 'ct'))
print(uses_all('hello my name is cookie', 'ki'))