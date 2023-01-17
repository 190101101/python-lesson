import os

file = 'lorem.txt'
rename = 'lorem2.txt'

try:
	os.rename(file, rename)
except:
	print('file not found')

#
file = 'files/lorem.txt'
rename = 'files/lorem2.txt'

try:
	os.rename(file, rename)
except:
	print('file not found')