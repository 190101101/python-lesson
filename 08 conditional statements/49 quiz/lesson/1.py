#1
def is_odd_or_even(p1):
	if p1 % 2 == 0:
		print(f"{p1} is even")
	elif p1 % 2 == 1:
		print(f"{p1} is odd")

is_odd_or_even(10)
is_odd_or_even(9)

#2
def noise_character(p1):
	if p1 == 'a' or p1 == 'o' or p1 == 'u' or p1 == 'i':
		print('detected')
	else:
		print('not detected')

noise_character('a')
noise_character('z')

#3
def figure(p1):
	if p1 == 3:
		print('triangle')
	elif p1 == 4:
		print('square')
	elif p1 == 5:
		print('pentagon')
	else:
		print('unknown')

figure(3)

#4
def months_day(p1):
	if p1 == 'january' or p1 == 'march' or p1 == 'may' or\
 		p1 == 'july' or p1 == 'august' or\
		p1 == 'october' or p1 == 'december':
		print(f"{p1} is 31")
	elif p1 == 'February' or p1 == 'april' or p1 == 'june' or\
		p1 == 'september' or p1 == 'november':
		print(f"{p1} is not 31")
	else:
		print("what?")

months_day('january')


#5
def triangle_name(p1, p2, p3):
	if p1 == p2 and p2 == p3:
		print("equilateral triangle");
	elif p1 == p2 or p1 == p3 or p2 == p3:
		print("isosceles triangle");
	else:
		print("length side triangle");

triangle_name(10, 10, 11)
triangle_name(11, 10, 11)
triangle_name(1, 10, 2)

#6
def fruits(p1):
	if p1 == 'summer':
		print('banana, orange ,berry')
	elif p1 == 'winter':
		print('apple, mandarin, pear')
	else:
		print('oops')

fruits('summer')

#9
def odd_even_total(p1, p2):

	if (p1 % 2 == 1 and p2 % 2 == 0) or\
	(p1 % 2 == 0 and p2 % 2 == 1):
		print("total: odd")
	else:
		print("total: even")

odd_even_total(10, 11)

#10
def double_count_back(p1, p2):

	small = 0
	big = 0

	if p1 <= p2:
		small = p1
		big = p2
	else:
		small = p2
		big = p1

	print(f"small {small}")
	print(f"big {big}")


double_count_back(10, 11)
double_count_back(12, 10)