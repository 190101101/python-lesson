file = open('../../../00 bin/docs/pantry/word.txt')

lorem = ''
lorem += file.readline()
lorem += file.readline()
lorem += file.readline()
lorem += file.readline()
file.close()

print(lorem)
