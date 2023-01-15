#1
def forbidden_letters(text, char):

	for word in text:

		if char in word:
			return True
		else:
			return False

print(forbidden_letters('cookie the cat', 'a'))

#2
def letters_with_permission(text, character):
	
	for char in text:
		if char.isalpha() and not char in character:
			return False
	else:
		return True


print(letters_with_permission('cookie the cat', 'a'))

print(set('cookie the cat'))