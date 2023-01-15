#
def letter_count(text):
	
	letters = dict()

	for letter in text:
		if letter.isalpha():
			if letter in letters.keys():
				letters[letter] += 1
			else:
				letters[letter] = 1
	return letters	

#
def rever_search(vocabulary, value):

	for key in vocabulary:
		if vocabulary[key] == value:
			return key
	else:
		return False

#
def list_letter(text):
	
	dictionary = letter_count(text)
	letters = dict()

	for key in dictionary:
		value = dictionary[key]
		if value not in letters:
			letters[value] = [key]
		else:
			letters[value].append(key)
	
	return letters

text = 'Hello my name is Cookie i am a web developer'	

letters = list_letter(text)
print(letters)