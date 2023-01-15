#1
def letter_count(text):
	
	letters = dict()

	for letter in text:
		if letter.isalpha():
			if letter in letters.keys():
				letters[letter] += 1
			else:
				letters[letter] = 1
	return letters			

p1 = 'hello my name is cookie i am web developer'
print(letter_count(p1))

letter_word = letter_count(p1)
print(letter_count(p1).get('a'))

print(letter_word.get('o'))
print(letter_word.get('c'))

#2
def letter_count2(text):

	letters = dict()

	for letter in text:
		if letter.isalpha():
			letters[letter] = letters.get(letter, 0) + 1

	return letters			

p2 = letter_count2(p1)
print(p2)
print(p2.get('m'))

