# read
with open('../../../00 bin/docs/pantry/word.txt', mode='rt', encoding='utf') as file:
	content = file.read()
	print(content)

# binary read
with open('../../../00 bin/docs/pantry/image.jpg', mode='rb') as file:
	content = file.read()
	print(content)
