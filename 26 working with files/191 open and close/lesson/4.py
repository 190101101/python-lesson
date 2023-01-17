try:
	with open('../../../00 bin/docs/pantry/word.txt', 'r', encoding='utf') as file:
		content = file.read()
		print(content)
except:
	print('file not found')
else:
	file.close()
