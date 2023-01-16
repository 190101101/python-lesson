def get_entry(text='something'):
	return input("[+] write {0}: ".format(text))

def get_string():
	return get_entry()

def get_integer():

	while True:
		try:
			number = int(get_entry(text='integer'))
		except ValueError:
			continue
		else:
			return number

#
def get_integer_decade():

	while True:
		try:
			number = float(get_entry(text='decade'))
		except ValueError:
			continue
		else:
			return number