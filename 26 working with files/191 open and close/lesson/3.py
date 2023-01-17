try:
	file = open('../../../00 bin/docs/pantry/words.txt', encoding='utf')
	print(file.read())
except:
	print('file not found')
else:
	file.close()