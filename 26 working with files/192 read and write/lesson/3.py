#
# with open('../../../00 bin/docs/pantry/lorem2.txt', mode='a') as file:
	# file.write('new line 2\n')

#
with open('../../../00 bin/docs/pantry/lorem2.txt', mode='a') as file:
	added_lines = ['new line 1\n', 'new line 2\n', 'new line 3\n']
	file.writelines(added_lines)
