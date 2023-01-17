# read
with open('../../../00 bin/docs/pantry/lorem.txt', mode='r', encoding='utf') as file:
	content = file.read(50)
	print(content)

#
with open('../../../00 bin/docs/pantry/lorem.txt') as file:
	content = file.readline()
	print(content)

#
with open('../../../00 bin/docs/pantry/lorem.txt') as file:
	for line in file:
		print(line)
