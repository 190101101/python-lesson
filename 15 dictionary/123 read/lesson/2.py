p1 = {
	'bir': 'one',
	'iki': 'two',
	'uc': 'three',
	'dord': 'four',
	'besh': 'five',
	'alti': 'six',
	'yeddi': 'seven',
	'sekkiz': 'eight',
	'doqquz': 'nine',
	'on': 'ten',
}

print(p1)
print(p1.keys())
print(p1.values())
print(p1.items())

for key, value in p1.items():
	print("in anahtarda {0}: {1} degeri var".format(key, value))