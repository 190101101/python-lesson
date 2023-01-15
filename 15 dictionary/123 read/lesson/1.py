p1 = {
	'one': 'bir',
	'two': 'iki',
	'three': 'uc',
	'four': 'dord',
	'five': 'besh',
	'six': 'alti',
	'seven': 'yeddi',
	'eight': 'sekkiz',
	'nine': 'doqquz',
	'ten': 'on',
}

print(p1)
print(p1.keys())
print(p1.values())
print(p1.items())

for key, value in p1.items():
	print("in key {0}: have {1} value".format(key, value))