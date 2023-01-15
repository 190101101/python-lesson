#
def count_down(p1):
	if p1 <= 0:
		print('done')
	else:
		print(p1)
		count_down(p1-1)

count_down(10)

#
def text_write(text, p1):
	if p1 <= 0:
		return
	else:
		print(text)
		text_write(text, p1 - 1)

text_write('hello', 3)

#
def counter(p1):
	if p1 == 100:
		print('done')
	else:
		print(p1)
		counter(p1 + 1)

counter(90)

